.. role:: math(raw)
   :format: html latex
..

================
X-ray Tomography
================

This section describes extensions and additions to the core Data
Exchange format for X-ray Tomography. We begin with the extensions to
the exchange and instrument groups, and then describe the tomography
process groups.

Data Structure
============== 

A tomographic data set consists of a series of projections, dark and white field images. The dark and white fields must have the same
projection image dimensions and can be collected at any time before, after or during the projection data collection. The angular position of
the tomographic rotation axis, theta, can be used to keep track of when the dark and white images are collected. 
These examples show projection, dark, and white images saved in three 3D arrays as shown in Figures :ref:`MinimalTomo0` and :ref:`MinimalTomo1` using, by default, the natural HDF5 order of the a multidimensional array (rotation axis, ccd y, ccd x), i.e. with the fastest changing dimension being the last dimension, and the slowest changing dimension being the first dimension. If using the default dimension order, the axes attribute *theta:y:x* can be
omitted. The attribute is **mandatory** if the 3D arrays use a different axes order. This could be the case when, for example, the arrays are
optimized for sinogram read *y:theta:x*. As no units are specified the data is assumed to be in *counts" with the axes (x, y) in pixels. If the positions of the rotation axis for each projection, dark, and white images are not specified via theta dimension scale datasets, it is assumed that the raw projections are taken at equally spaced angular intervals between 0 and 180 degree, with white and dark field collected at the same time before or after the projection data collection.

.. _MinimalTomo0:

.. figure:: figures/dx_MinimalTomo0.png
   :align: center
   :alt: Diagram of a minimal Data Exchange file for a single tomographic data set including raw projections, dark, and white fields.
   :width: 50.0%

   Diagram of a minimal Data Exchange file for a single tomographic data set including raw projections, dark, and white fields 

.. _MinimalTomo1:

.. figure:: figures/dx_MinimalTomo1.png
   :align: center
   :alt: Diagram of a single tomographic data set including raw projections, dark and white fields. In this case, there are additional dimension descriptor datasets theta, theta_dark, and theta_white that contain the positions of the rotation axis for each projection, dark, and white image. The lefthand example shows this as it would appear using the HDF5 H5DSattach_scale function. The righthand example shows this as it would appear by manually adding an axes attribute (for cases where H5DSattach_scale is unavailable). 
   :width: 80.0%

   Diagram of a single tomographic data set including raw projections,
   dark and white fields. In this case, there are additional dimension
   descriptor datasets theta, theta_dark, and theta_white that contain
   the positions of the rotation axis for each projection, dark, and
   white image. The lefthand example shows this as it would appear using
   the HDF5 H5DSattach_scale function. The righthand example shows this
   as it would appear by manually adding an axes attribute (for cases
   where H5DSattach_scale is unavailable)


Series
------

A series of tomographic measurements, when relevant, can be stored in
the same file appending _N to the measurement tag. 
A series of tomographic data sets are typically collected changing the
instrument status (energy, detector or optics position); changing the
sample status (position, environment etc.). Figure :ref:`MinimalTomo2`,
:ref:`MinimalTomo3` and :ref:`MinimalTomo4` show the content of files
changing the sample temperature, the X-ray source energy and
detector-sample distance.
In nano tomography experiments, for example, the detector field of view is 
often smaller than the sample. To collect a complete tomographic data set, 
it is necessary to raster the sample across the field of view moving its x
and y location. Figure :ref:`NanoTomo1` shows a file from a nano
tomography experiment when the sample rasters through the field of view.

There are limits to this approach, as one clearly does not want to have
hundreds of measurement groups in a file (or multiple files) where most
of the metadata is the same. For measurements where there are many
“positioner” values (aka a “scan”), it is more sensible to add
dimension(s) to the exchange dataset, and describe the “positioner”
values as dimension scales. This is a judgement left to the user.

Temperature
~~~~~~~~~~~

.. _MinimalTomo2:

.. figure:: figures/dx_MinimalTomo2.png
   :align: center
   :alt: Diagram of two tomographic data sets taken at two different sample temperatures (100 and 200 Celsius).
   :width: 100.0%

   Diagram of two tomographic data sets taken at two different sample
   temperatures (100 and 200 Celsius)

Energy
~~~~~~
.. _MinimalTomo3:

.. figure:: figures/dx_MinimalTomo3.png
   :align: center
   :alt: Diagram of two tomographic data sets taken at two different energy (10 and 20 keV).
   :width: 80.0%

   Diagram of two tomographic data sets taken at two different energy
   (10 and 20 keV)

Detector-sample
~~~~~~~~~~~~~~~

.. _MinimalTomo4:

.. figure:: figures/dx_MinimalTomo4.png
   :align: center
   :alt: Diagram of two tomographic data sets collected with two different detector-sample distances (5 and 9 mm). Note the use of output_data dataset to associate the detector with the exchange group generated from the acquisition.
   :width: 80.0%

   Diagram of two tomographic data sets collected with two different
   detector-sample distances (5 and 9 mm). Note the use of output_data
   dataset to associate the detector with the exchange group generated
   from the acquisition

Raster
~~~~~~

.. _NanoTomo1:

.. figure:: figures/dx_NanoTomo1.png
   :align: center
   :alt: Diagram of a file with 4 tomographic data sets from a nano tomography experiment.
   :width: 90.0%

   Diagram of a file with 4 tomographic data sets from a nano tomography
   experiment

Groups
======

Exchange
--------

In X-ray tomography, the 3D arrays representing the most basic version
of the data include projections, dark, and white fields. It is
**mandatory** that there is at least one dataset named **data** in each
exchange group. Most data analysis and plotting programs will primarily
focus in this group.

+------------------+---------------------------------------------------------+-----------------------------+
|     Member       |      Type                                               |     Example/Attributes      |
+==================+=========================================================+=============================+
|    title         |      string dataset                                     |  "raw absorption tomo"      |
+------------------+---------------------------------------------------------+-----------------------------+
|    **data**      |      3D dataset                                         |  axes: *theta:y:x*          |
+------------------+---------------------------------------------------------+-----------------------------+
|    x             |      dimension scale 2                                  |                             |
+------------------+---------------------------------------------------------+-----------------------------+
|    y             |      dimension scale 1                                  |                             |
+------------------+---------------------------------------------------------+-----------------------------+
|    theta         |      dimension scale 0                                  |  units: "deg"               |
+------------------+---------------------------------------------------------+-----------------------------+
|  *data_dark*     |      3D dataset                                         |  axes: *theta_dark:y:x*     |
+------------------+---------------------------------------------------------+-----------------------------+
|  *theta_dark*    |      dimension scale 0                                  |  units: "deg"               |
+------------------+---------------------------------------------------------+-----------------------------+
|  *data_white*    |      3D dataset                                         |  axes: *theta_white:y:x*    |
+------------------+---------------------------------------------------------+-----------------------------+
|  *theta_white*   |      dimension scale 0                                  |  units: "deg"               |
+------------------+---------------------------------------------------------+-----------------------------+
|    data_shift_x  |      relative x shift of data at each angular position  |                             |
+------------------+---------------------------------------------------------+-----------------------------+
|    data_shift_y  |      relative y shift of data at each angular position  |                             |
+------------------+---------------------------------------------------------+-----------------------------+

Table: Exchange Group Members for Tomography

title
    | 
    | This is the data title.

**data**
    | 
    | A tomographic data set consists of a series of projections (**data**),
      dark field (*data_dark*), and white field (*data_white*) images. The
      dark and white fields must have the same projection image
      dimensions and can be collected at any time before, after or
      during the projection data collection. The angular position of the
      tomographic rotation axis, theta, can be used to keep track of
      when the dark and white images are collected. These datasets are
      saved in 3D arrays using, by default, the natural HDF5 order of a
      multidimensional array (rotation axis, ccd y, ccd x), i.e. with
      the fastest changing dimension being the last dimension, and the
      slowest changing dimension being the first dimension. If using the
      default dimension order, the axes attribute *theta:y:x* can be
      omitted. The attribute is **mandatory** if the 3D arrays use a
      different axes order. This could be the case when, for example,
      the arrays are optimized for sinogram read ( = *y:theta:x*). As no
      units are specified the data is assumed to be in *counts* with the
      axes (x, y) in pixels.
      
*data_dark*, *data_white*
    | 
    | The dark field and white fields must have the same dimensions as
      the projection images and can be collected at any time before,
      during, or after the projection data collection. To specify where
      dark and white images were taken, specify the axes attribute with
      “theta_dark:y:x” and “theta_white:y:x” and provide *theta_dark*
      and *theta_white* vector datasets that specify the rotation angles
      where they were collected.
x, y
    | 
    | X and y are vectors storing the dimension scale for the second and
      third data array dimension. If x, y are not defined, the second
      and third dimensions of the data array are assumed to be in
      pixels.
      
theta, theta dark, *theta_white*
    | 
    | Theta is a vector dataset storing the projection angular
      positions. If theta is not defined the projections are assumed to
      be collected at equally spaced angular interval between 0 and 180
      degree. The dark field and white fields can be collected at any
      time before, during, or after the projection data. *theta_dark*,
      and *theta_white* store the position of the tomographic rotation
      axis when the corresponding dark and white images are collected.
      If *theta_dark* and *theta_white* are missing the corresponding
      *data_dark* and *data_white* are assumed to be collected all at the
      beginning or at the end of the projection data collection.
      
data_shift_x, data_shift_y
    | 
    | Data_shift_x and data_shift_y are the vectors storing at each
      projection angular positions the image relative shift in x and y.
      These vectors are used in high resolution CT when at each angular
      position the sample x and y are moved to keep the sample in the
      field of view based on a pre-calibration of rotary stage runout.
      If the unit is not defined are assumed to be in pixels.

.. _instrument:

Instrument
----------

The instrument group for X-ray tomography introduces an extended
detector group definition adding definitions for and . The extended
instrument group is as shown in Table.

+----------------------------------------------+----------------------+-------------------------------+
|                   Member                     |      Type            |            Example            |
+==============================================+======================+===============================+
|                   name                       |       string dataset | "XSD/2-BM"                    |
+----------------------------------------------+----------------------+-------------------------------+
|                   source                     |       group          | same as core                  |
+----------------------------------------------+----------------------+-------------------------------+
|                   shutter_N                  |       group          | same as core                  |
+----------------------------------------------+----------------------+-------------------------------+
|                   attenuator_N               |       group          | same as core                  |
+----------------------------------------------+----------------------+-------------------------------+
|                   monochromator              |       group          | same as core                  |
+----------------------------------------------+----------------------+-------------------------------+
|                  acquisition_                |       group          | new                           |
+----------------------------------------------+----------------------+-------------------------------+
|                  detector_                   |       group          | extended from core            |
+----------------------------------------------+----------------------+-------------------------------+
|                  setup_                      |       group          | new                           |
+----------------------------------------------+----------------------+-------------------------------+

Table: Instrument Group for Tomography

.. _setup:

Setup
~~~~~

Logging instrument and beamline component setup parameters (static setup values) 
is not defined by Data Exchange because is specific and different for each instrument
and beamline. To capture this information Data Exchange requires to set a *setup* 
group under each beamline component and leaves each facility free to store what 
is relevant for each component (list of motor positions etc.). 
Ideally each component in the instrument list (source, shutter, attenuator etc.) should have
included its setup group. For setup values not associated with a specific beamline component
a  *setup* group in the instrument group should be created.

+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|     motor_x                                  |      float                       |       -10.107                    |
+----------------------------------------------+----------------------------------+----------------------------------+
|     motor_y                                  |      float                       |       -17.900                    |
+----------------------------------------------+----------------------------------+----------------------------------+
|     motor_z                                  |      float                       |        -5.950                    |
+----------------------------------------------+----------------------------------+----------------------------------+
|     motor_xx                                 |      float                       |        -1.559                    |
+----------------------------------------------+----------------------------------+----------------------------------+
|     motor_zz                                 |      float                       |         1.307                    |
+----------------------------------------------+----------------------------------+----------------------------------+

Table: Setup Group Members

.. _acquisition:

Acquisition
^^^^^^^^^^^

Logging acquisition setup parameters (static setup values) is not defined by Data Exchange 
because is specific and different for each instrument and beamline.
In the table below we present the implementation adopted by the Swiss Light Source and
Advanced Photon Source.


+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|    rotation_start_angle                      |      float                       |      0.0                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    rotation_end_angle                        |      float                       |      180.0                       |
+----------------------------------------------+----------------------------------+----------------------------------+
|    angular_step                              |      float                       |      0.125                       |
+----------------------------------------------+----------------------------------+----------------------------------+
|    number_of_projections                     |      integer                     |      1441                        |
+----------------------------------------------+----------------------------------+----------------------------------+
|    number_of_flats                           |      integer                     |      100                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    number_of_darks                           |      integer                     |      32                          |
+----------------------------------------------+----------------------------------+----------------------------------+
|    start_date                                | string dataset (ISO 8601)        |      "2012-07-31T21:15:22+0600"  |    
+----------------------------------------------+----------------------------------+----------------------------------+
|    end_date                                  | string dataset (ISO 8601)        |      "2012-07-31T23:10:20+0600"  |    
+----------------------------------------------+----------------------------------+----------------------------------+
|    sample_in                                 |      float                       |      0.0                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    sample_out                                |      float                       |      4.0                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    type                                      | string                           |      dpc_tomography              |
+----------------------------------------------+----------------------------------+----------------------------------+
|    setup_                                    | string                           |      dpc_tomography              |
+----------------------------------------------+----------------------------------+----------------------------------+

Table: Instrument Acquisition Group for Tomography


.. _interferometer: 

Interferometer
~~~~~~~~~~~~~~

This group stores the interferometer parameters.

+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|    grid_start                                |      float                       |      1.8                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    grid_end                                  |      float                       |      3.51                        | 
+----------------------------------------------+----------------------------------+----------------------------------+
|    number_of_grid_periods                    |      int                         |      1                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|    number_of_grid_steps                      |      int                         |      6                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|         geometry_                            |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|         setup_                               |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+

Table: Interferometer Group Members

start_angle
    | 
    | Interferometer start angle.

grid_start
    | 
    | Interferometer grid start angle.

grid_end
    | 
    | Interferometer grid end angle.

grid_position_for_scan
    | 
    | Interferometer grid position for scan.   

number_of_grid_steps
    | 
    | Number of grid steps.

.. _detector:

Detector
~~~~~~~~

This class holds information about the detector used during the
experiment. If more than one detector are used they will be all listed
as detector_N. In full field imaging the detector consists of
a CCD camera, microscope objective and a scintillator screen. Raw data
recorded by a detector as well as its position and geometry should be
stored in this class.

+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|    manufacturer                              | string dataset                   |      "CooKe Corporation"         |   
+----------------------------------------------+----------------------------------+----------------------------------+
|    model                                     | string dataset                   |       "pco dimax"                |
+----------------------------------------------+----------------------------------+----------------------------------+
|    serial_number                             | string dataset                   |       "1234XW2"                  |  
+----------------------------------------------+----------------------------------+----------------------------------+
|    bit_depth                                 |      integer                     |      12                          |     
+----------------------------------------------+----------------------------------+----------------------------------+
|    pixel_size_x                              |      float                       |      6.7e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|    pixel_size_y                              |      float                       |      6.7e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|    actual_pixel_size_x                       |      float                       |      1.2e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|    actual_pixel_size_y                       |      float                       |      1.2e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|    dimension_x                               |      integer                     |      2048                        |
+----------------------------------------------+----------------------------------+----------------------------------+
|    dimension_y                               |      integer                     |      2048                        |
+----------------------------------------------+----------------------------------+----------------------------------+
|    binning_x                                 |      integer                     |      1                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|    binning_y                                 |      integer                     |      1                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|    operating_temperature                     |      float                       |       270                        |     
+----------------------------------------------+----------------------------------+----------------------------------+
|    exposure_time                             |      float                       |      1.7e-3                      |   
+----------------------------------------------+----------------------------------+----------------------------------+
|    delay_time                                |      float                       |      1.7e-3                      |   
+----------------------------------------------+----------------------------------+----------------------------------+
|    stabilization_time                        |      float                       |      1.7e-3                      |   
+----------------------------------------------+----------------------------------+----------------------------------+
|    frame_rate                                |      integer                     |       2                          |
+----------------------------------------------+----------------------------------+----------------------------------+
|    output_data                               | string dataset                   |      "/exchange"                 |
+----------------------------------------------+----------------------------------+----------------------------------+
|    roi_                                      |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|    objective_                                |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|    scintillator_                             |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|    counts_per_joule                          |      float                       |      unitless                    | 
+----------------------------------------------+----------------------------------+----------------------------------+
|    basis_vectors                             |      float array                 |      length                      | 
+----------------------------------------------+----------------------------------+----------------------------------+
|    corner_position                           |      3 floats                    |      length                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|         geometry_                            |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|         setup_                               |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+


Table: Detector Group Members for Tomography

manufacturer
    | 
    | The detector manufacturer.

model
    | 
    | The detector model.

serial_number
    | 
    | The detector serial number .
     
bit_depth
    | 
    | The detector bit depth.

pixel_size_x, pixel_size_y
    | 
    | Physical detector pixel size (m).

dimension_x, dimension_y
    | 
    | The detector horiz./vertical dimension.

actual_pixel_size_x, actual_pixel_size_y
    | 
    | Actual pixel size on the sample plane.

binning_x, binning_y
    | 
    | If the data are collected binning the detector binning_x and binning_y store the binning factor.

operating_temperature
    | 
    | The detector operating temperature (K).

exposure_time
    | 
    | The detector exposure time (s).

delay_time
    | 
    | Delay time between projections when using a mechanical shutter to reduce radiation damage of the sample (s).

stabilization_time
    | 
    | Time required by the sample to stabilize (s).

frame_rate
    | 
    | The detector frame rate (fps). This parameter is set for fly scan.

roi
    | 
    | The detector selected Region Of Interest (ROI).

objective_N
    | 
    | List of the visible light objectives mounted between the detector and the scintillator screen.

counts_per_joule
    | 
    | Number of counts recorded per each joule of energy received by the detector. The number of incident photons can then be calculated by:

basis_vectors
    | 
    | A matrix with the basis vectors of the detector data.

corner_position
    | 
    | The x, y and z coordinates of the corner of the first data element.

geometry
    | 
    | Position and orientation of the center of mass of the detector. This should only be specified for non pixel detectors. For pixel detectors use basis_vectors and corner_position.

.. _roi:

ROI
^^^

Group describing the region of interest (ROI) of the image actually
collected, if smaller than the full CCD.


+----------------+----------------+-----------------+
|     Member     |      Type      |      Example    |
+================+================+=================+
|    name        | string dataset | "center third"  | 
+----------------+----------------+-----------------+
|    x1          | integer        |      256        |   
+----------------+----------------+-----------------+
|    y1          | integer        |      256        |
+----------------+----------------+-----------------+
|    x2          | integer        |      1792       |
+----------------+----------------+-----------------+
|    y2          | integer        |      1792       |
+----------------+----------------+-----------------+

Table: ROI Group Members

x1
    | 
    | Left pixel position.

y1
    | 
    | Top pixel position.

x2
    | 
    | Right pixel position.

y2
    | 
    | Bottom pixel position.

.. _objective:

Objective
^^^^^^^^^

Group describing the microscope objective lenses used.

+------------------------------------+----------------+-----------------+
|     Member                         |      Type      |      Example    |
+====================================+================+=================+
| manufacturer                       | string dataset |      "Zeiss"    |
+------------------------------------+----------------+-----------------+
| model                              | string dataset |      "Axioplan" |
+------------------------------------+----------------+-----------------+
| magnification                      | float dataset  |      5          | 
+------------------------------------+----------------+-----------------+
| numerical_aperture                 | float dataset  |      0.8        |
+------------------------------------+----------------+-----------------+
| geometry_                          | group          |                 |
+------------------------------------+----------------+-----------------+
| setup_                             | group          |                 |
+------------------------------------+----------------+-----------------+

Table: Objective Group Members

manufacturer
    | 
    | Lens manufacturer.

model
    | 
    | Lens model.

magnification
    | 
    | Lens specified magnification.

numerical_aperture
    | 
    | The numerical aperture (N.A.) is a measure of the light-gathering characteristics of the lens.

.. _scintillator:

Scintillator
^^^^^^^^^^^^

Group describing the visible light scintillator coupled to the CCD
camera objective lens.

+------------------------------------+----------------+-----------------+
|     Member                         |      Type      |      Example    |
+====================================+================+=================+
|    manufacturer                    | string dataset |  "Crytur"       |
+------------------------------------+----------------+-----------------+
|    serial_number                   | string dataset |    "12"         |   
+------------------------------------+----------------+-----------------+
|    name                            | string dataset |  "Yag polished" | 
+------------------------------------+----------------+-----------------+
|    type                            | string dataset |  "Yag on Yag"   |  
+------------------------------------+----------------+-----------------+
|    scintillating_thickness         | float dataset  |       5e-6      |  
+------------------------------------+----------------+-----------------+
|    substrate_thickness             | float dataset  |        1e-4     |  
+------------------------------------+----------------+-----------------+
|       geometry_                    | group          |                 |
+------------------------------------+----------------+-----------------+
|       setup_                       | group          |                 |
+------------------------------------+----------------+-----------------+

Table: Scintillator Group Members

manufacturer
    | 
    | Scintillator Manufacturer.

serial_number
    | 
    | Scintillator serial number.

name
    | 
    | Scintillator name.

scintillating_thickness
    | 
    | Scintillator thickness.

substrate_thickness
    | 
    | Scintillator substrate thickness.

.. _geometry:

Geometry
````````

This class holds the position and orientation of a component for
tomography.

+----------------------------------------------+-----------------+----------------------------------+
|     Member                                   |      Type       |            Example               |
+==============================================+=================+==================================+
|      translation_                            |      group      |                                  |
+----------------------------------------------+-----------------+----------------------------------+
|      orientation_                            |      group      |                                  |
+----------------------------------------------+-----------------+----------------------------------+

translation
    | 
    | The position of the object with respect to the origin of your coordinate system.

orientation
    | 
    | The rotation of the object with respect to your coordinate system.

.. _translation:

Translation
'''''''''''

This is the description for the general spatial location of a component
for tomography.

+----------------------------+------------------------+-----------------+
|     Member                 |      Type              |      Example    |
+============================+========================+=================+
|           distances        | 3 float array dataset  |  (0, 0.001, 0)  |
+----------------------------+------------------------+-----------------+

distances
    | 
    | The x, y and z components of the translation of the origin of the object
    | relative to the origin of the global coordinate system (the place where 
    | the X-ray beam  meets the sample when the sample is first aligned in the beam).
    | If  distances does not have the attribute units set then the units are in
    | meters.

.. _orientation:

Orientation
'''''''''''

This is the description for the orientation of a component for
tomography.

+----------------------------+------------------------+-----------------+
|     Member                 |      Type              |      Example    |
+============================+========================+=================+
|      value                 | 6 float array dataset  |                 |
+----------------------------+------------------------+-----------------+

value
    | 
    | Dot products between the local and the global unit vectors. Unitless


The orientation information is stored as direction cosines. The
direction cosines will be between the local coordinate directions and
the global coordinate directions. The unit vectors in both the local and
global coordinates are right-handed and orthonormal.

Calling the local unit vectors (x', y',z') and the reference unit
vectors (x, y, z) the six numbers will be


.. math:: [x \cdot x, x' \cdot y, x' \cdot z, y' \cdot x, y'  \cdot y, y' \cdot z] 

where 

.. math:: `\cdot` 

is the scalar dot product (cosine of the angle between the unit vectors).

Notice that this corresponds to the first two rows of the rotation
matrix that transforms from the global orientation to the local
orientation. The third row can be recovered by using the fact that the
basis vectors are orthonormal.
