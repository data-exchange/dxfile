.. role:: math(raw)
   :format: html latex
..

================
X-ray Tomography
================

This section describes extensions and additions to the core Data
Exchange format for X-ray Tomography. We begin with the extensions to
the exchange and instrument groups, and then describe the possible 
tomography data collection schemes and corresponding data structures.

Top level (root)================This node represents the top level of the HDF5 file and holds somegeneral information about the file.+---------------+----------------+-----------------------------------------+|    Member     |      Type      |              Example                    |
+===============+================+=========================================+|**implements** | string dataset | **exchange**:*measurement*:*provenance* |+---------------+----------------+-----------------------------------------+|**exchange**   |    group       |                                         |
+---------------+----------------+-----------------------------------------+|*measurement*  |    group       |                                         |+---------------+----------------+-----------------------------------------+| *provenance*  |    group       |                                         |+---------------+----------------+-----------------------------------------+**implements**    |     | A colon separated list that shows which components are present in      the file. The only **mandatory** component is **exchange**. A more      general Data Exchange file also contains *measurement* and      *provenance* information, if so these will be declared in **implements**      as **exchange**:*measurement*:*provenance***exchange** or **exchange_N**    |     | The data taken from measurements or processing. Dimension      descriptors within the group may also serve to describe      “positioner” values involved in a scan. 

*measurement* or *measurement_N*    |     | Description of the sample and instrument as configured for the      measurement. This group is appropriate for relatively static      metadata. For measurements where there are many “positioner”      values (aka a “scan”), it is more sensible to add dimension(s) to      the exchange dataset, and describe the “positioner” values as      dimension scales rather than record the data via multiple matching      *measurement* and **exchange** groups. This is a judgement left to      the user.

*provenance*    |     | The Provenance group describes all process steps that have been      applied to the data.
      
Exchange
========

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

Measurement===========

This group holds sample and instrument information. These groups aredesigned to hold relatively static data about the sample and instrumentconfiguration at the time of the measurement. Rapidly changing*positioner* values (aka scan) are better represented in the exchangegroup dataset.+---------------+----------------------+------------------------+|    Member     |      Type            |     Example            |
+===============+======================+========================+|   instrument  |      group           |                        |+---------------+----------------------+------------------------+|    sample     |      group           |                        |
+---------------+----------------------+------------------------+|  description  |   string attribute   | "Tomography of a rock” |
+---------------+----------------------+------------------------+Table: Measurement Group Members

instrument    |     | The instrument used to collect this data.

sample    |     | The sample measured.

description    |     | Measurement description.

Instrument----------The instrument group stores all relevant beamline components status atthe beginning of a measurement. While all these fields are optional, ifyou do intend to include them they should appear within this parentageof groups.

+---------------------------------------------+-------------------------+-------------------------+|                    Member                   |           Type          |         Example         |
+=============================================+=========================+=========================+
|                   name                      |       string dataset    | "XSD/2-BM"              |+---------------------------------------------+-------------------------+-------------------------+|                   source_                   |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   shutter_                  |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   attenuator_               |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   monochromator_            |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   capacitive_sensors_       |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   detector_                 |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+
|                   set-up_                   |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+

Table: Instrument Group for Tomography

name    |     | Name of the instrument.

source    |     | The source used by the instrument.

shutter    |     | The shutter(s) used by the instrument.

attenuator    |     | The attenuators that are part of the instrument.

monochromator    |     | The monochromator used by the instrument.

capacitive_sensor    |     | The capacitive_sensors used to monitor for example the sample      position during data collection.

detector    |     | The detectors that compose the instrument.
.. _set-up:

Setup
~~~~~

Logging instrument and beamline component setup parameters (static setup values) 
is not defined by Data Exchange because is specific and different for each instrument
and beamline. To capture this information Data Exchange requires to set a *setup* 
group under each beamline component and leaves each facility free to store what 
is relevant for each component (list of motor positions etc.). 
Ideally each component in the instrument list (source, shutter, attenuator etc.) should have
included its setup group. For setup values not associated with a specific beamline component
a  *setup* group in the instrument group should be created. For tomography we also recommend
to log acquisition setup parameters (static setup values) under the instrument/setup tag.


+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|     acquisition_                             |       group                      |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
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

Table: Instrument Acquisition Group for Tomography


.. _source:

Source~~~~~~Class describing the light source being used.
+-----------------------------+--------------------------------+---------------------------+| Member                      |     Type                       |     Example               |+=============================+================================+===========================+
| name                        |     string dataset             |     “APS”                 |+-----------------------------+--------------------------------+---------------------------+| datetime                    |     string dataset (ISO 8601)  |     “2011-07-15T15:10Z”   |+-----------------------------+--------------------------------+---------------------------+| beamline                    |     string dataset             |     “2-BM”                |+-----------------------------+--------------------------------+---------------------------+| current                     |     float dataset              |     0.094                 |+-----------------------------+--------------------------------+---------------------------+| energy                      |     float dataset              |     4.807e-15             |+-----------------------------+--------------------------------+---------------------------+| pulse_energy                |     float dataset              |     1.602e-15             |+-----------------------------+--------------------------------+---------------------------+| pulse_width                 |     float dataset              |     15e-11                |+-----------------------------+--------------------------------+---------------------------+| mode                        |     string dataset             |     “TOPUP”               |+-----------------------------+--------------------------------+---------------------------+| beam_intensity_incident     |     float dataset              |     55.93                 |+-----------------------------+--------------------------------+---------------------------+| beam_intensity_transmitted  |     float dataset              |     100.0                 |+-----------------------------+--------------------------------+---------------------------+| geometry_                   |     group                      |                           |+-----------------------------+--------------------------------+---------------------------+| setup_                      |     group                      |                           |+-----------------------------+--------------------------------+---------------------------+Table: table_source


name    |     | Name of the facility.
datetime    |     | Date and time source was measured.
beamline    |     | Name of the beamline.
current    |     | Electron beam current (A).
energy    |     | Characteristic photon energy of the source (J). For an APS bending      magnet this is 30 keV or 4.807e-15 J.
pulse_energy    |     | Sum of the energy of all the photons in the pulse (J).
pulse_width    |     | Duration of the pulse (s).
mode    |     | Beam mode: TOP-UP.
beam_intensity_incident    |     | Incident beam intensity in (photons per s).
beam_intensity_transmitted    |     | Transmitted beam intensity (photons per s).

.. _shutter:

Shutter~~~~~~~
Class describing the shutter being used.+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|       name         |     string dataset      |     “Front End Shutter 1      |+--------------------+-------------------------+-------------------------------+|      status        |     string dataset      |     “OPEN”                    |+--------------------+-------------------------+-------------------------------+|       geometry_    |        group            |                               |+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |+--------------------+-------------------------+-------------------------------+
Table: Shutter Group Members

name
    |     | Shutter name.status
    |     | “OPEN” or “CLOSED”

.. _attenuator:
Attenuator~~~~~~~~~~This class describes the beamline attenuator(s) used during datacollection. If more than one attenuators are used they will be named asattenuator_1, attenuator_2 etc.

+---------------------------+-------------------------+-------------------------------+|      Member               |           Type          |         Example               |
+===========================+=========================+===============================+
| thickness                 |     float dataset       |     1e-3                      |+---------------------------+-------------------------+-------------------------------+| attenuator_transmission   |     float dataset       |     unit-less                 |+---------------------------+-------------------------+-------------------------------+| type                      |     string dataset      |     “Al”                      |+---------------------------+-------------------------+-------------------------------+| geometry_                 |     group               |                               |+---------------------------+-------------------------+-------------------------------+| setup_                    |     group               |                               |+---------------------------+-------------------------+-------------------------------+Table: Attenuator Group Members


thickness     |     | Thickness of attenuator along beam direction.
attenuator_transmission    |     | The nominal amount of the beam that gets through (transmitted      intensity)/(incident intensity).
type    |     | Type or composition of attenuator.

.. _monochromator:
Monochromator~~~~~~~~~~~~~
Define the monochromator used in the instrument.+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
| type               |     string dataset      |     “Multilayer”              |+--------------------+-------------------------+-------------------------------+| energy             |     float dataset       |     1.602e-15                 |+--------------------+-------------------------+-------------------------------+| energy_error       |     float dataset       |     1.602e-17                 |+--------------------+-------------------------+-------------------------------+| mono_stripe        |     string dataset      |     “Ru/C”                    |+--------------------+-------------------------+-------------------------------+| geometry_          |     group               |                               |+--------------------+-------------------------+-------------------------------+| setup_             |     group               |                               |+--------------------+-------------------------+-------------------------------+Table: Monochromator Group Members

type    |     | Multilayer type.
energy    |     | Peak of the spectrum that the monochromator selects. Since units      is not defined this field is in J and corresponds to 10 keV.
energy_error    |     | Standard deviation of the spectrum that the monochromator selects.      Since units is not defined this field is in J.
mono_stripe    |     | Type of multilayer coating or crystal.
.. _capacitive_sensors:

Capacitive Sensors~~~~~~~~~~~~~~~~~~Define the capacitive sensors used in the instrument.+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
| name               |     string dataset      |     “Capacitive Sensors”      |+--------------------+-------------------------+-------------------------------+| gain               |     float dataset       |     1.602e-15                 |+--------------------+-------------------------+-------------------------------+| shift_x            |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+| shift_y            |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+| shift_z            |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+
| geometry_          |     group               |                               |+--------------------+-------------------------+-------------------------------+
| setup_             |     group               |                               |+--------------------+-------------------------+-------------------------------+
Table: Capacitive Sensors Group Membersname
    |     | Capacitive Sensors name.

gain    |     | Capacitive Sensors gain in V/m.
    
shift_x, shift_y, shift_z    |     | vectors containing for each scan point the position monitored by      the capacitive sensor.
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
|    firmware_version                          | string dataset                   |       "3.7.9"                    |  
+----------------------------------------------+----------------------------------+----------------------------------+
|    software_version                          | string dataset                   |       "1.3.14"                   |  
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
|   min_x        | integer        |      256        |   
+----------------+----------------+-----------------+
|  size_x        | integer        |      256        |
+----------------+----------------+-----------------+
|   min_y        | integer        |      1792       |
+----------------+----------------+-----------------+
|  size_y        | integer        |      1792       |
+----------------+----------------+-----------------+

Table: ROI Group Members

min_x, min_y
    | 
    | Top Left pixel x and y position.

size_x, size_y
    | 
    | x and y image size.



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


.. _setup:

Setup
^^^^^

Logging instrument and beamline component setup parameters (static setup values) 
is not defined by Data Exchange because is specific and different for each instrument
and beamline. To capture this information Data Exchange requires to set a *setup* 
group under each beamline component and leaves each facility free to store what 
is relevant for each component (list of motor positions etc.). 
Ideally each component in the instrument list (source, shutter, attenuator etc.) should have
included its setup group. For setup values not associated with a specific beamline component
a  *setup* group in the instrument group should be created.

+----------------------------------------------+----------------------------------+----------------------------------+|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+|    sample_x                                  |      float                       |      -10.107                     |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_y                                  |      float                       |       -17.900                    |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_z                                  |      float                       |      -5.950                      |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_xx                                 |      float                       |      -1.559                      |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_zz                                 |      float                       |      1.307                       |+----------------------------------------------+----------------------------------+----------------------------------+

Sample------This group holds basic information about the sample, its geometry,properties, the sample owner (user) and sample proposal information.While all these fields are optional, if you do intend to include themthey should appear within this parentage of groups.

+-------------------------------------+------------------------------------+-----------------------------+|    Member                           |                 Type               |          Example            |
+=====================================+====================================+=============================+
|         name                        |     string dataset                 |      "cells sample 1"       |    +-------------------------------------+------------------------------------+-----------------------------+|     description                     |     string dataset                 |      "malaria cells"        |   +-------------------------------------+------------------------------------+-----------------------------+|    preparation_date                 |  string dataset (ISO 8601)         |  "2012-07-31T21:15:22+0600" |    +-------------------------------------+------------------------------------+-----------------------------+|    chemical_formula                 | string dataset (abbr. CIF format)  |     "(Cd 2+)3,  2(H2 O)"    |   +-------------------------------------+------------------------------------+-----------------------------+|          mass                       |     float dataset                  |              0.25           |+-------------------------------------+------------------------------------+-----------------------------+|    concentration                    |     float dataset                  |              0.4            |+-------------------------------------+------------------------------------+-----------------------------+|    environment                      |     string dataset                 |             "air"           |  +-------------------------------------+------------------------------------+-----------------------------+|    temperature                      |     float dataset                  |             25.4            |+-------------------------------------+------------------------------------+-----------------------------+|    temperature_set                  |     float dataset                  |             26.0            |+-------------------------------------+------------------------------------+-----------------------------+|    pressure                         |     float dataset                  |           101325            | +-------------------------------------+------------------------------------+-----------------------------+|    thickness                        |     float dataset                  |            0.001            |+-------------------------------------+------------------------------------+-----------------------------+|    position                         |     string dataset                 |  "2D"  APS robot coord.     |+-------------------------------------+------------------------------------+-----------------------------+|    geometry_                        |            group                   |                             |+-------------------------------------+------------------------------------+-----------------------------+|    setup_                           |            group                   |                             |+-------------------------------------+------------------------------------+-----------------------------+|    experiment_                      |            group                   |                             |+-------------------------------------+------------------------------------+-----------------------------+|    experimenter_                    |            group                   |                             |+-------------------------------------+------------------------------------+-----------------------------+Table: Sample Group Members

name    |     | Descriptive name of the sample.

description    |     | Description of the sample.preparation_date
    |     | Date and time the sample was prepared.

chemical_formula    |     | Sample chemical formula using the CIF format.

mass    |     | Mass of the sample.concentration
    |     | Mass/volume.environment 
    |     | Sample environment.temperature 
    |     | Sample temperature.temperature_set
    |     | Sample temperature set point.pressure
    |     | Sample pressure.

thickness    |     | Sample thickness.position 
    |     | Sample position in the sample changer/robot.

geometry    |     | Sample center of mass position and orientation.experiment
    |     | Facility experiment identifiers.experimenter
    |     | Experimenter identifiers.
Experiment~~~~~~~~~~This provides references to facility ids for the proposal, scheduledactivity, and safety form.+---------------+-------------------------+----------------------+|   Member      |            Type         |       Example        | +===============+=========================+======================+
| proposal      |     string dataset      |        “1234”        |+---------------+-------------------------+----------------------+| activity      |     string dataset      |        “9876”        |+---------------+-------------------------+----------------------+| safety        |     string dataset      |        “9876”        |+---------------+-------------------------+----------------------+Table: Experiment Group Members

proposal    |     | Proposal reference number. For the APS this is the General User    | Proposal number.
      
activity    |     | Proposal scheduler id. For the APS this is the beamline scheduler      activity id.

safety    |     | Safety reference document. For the APS this is the Experiment    | Safety Approval Form number.Experimenter~~~~~~~~~~~~Description of a single experimenter. Multiple experimenters can berepresented through numbered entries such as experimenter_1,experimenter_2.+--------------------+-------------------------+--------------------------------------------+|      Member        |           Type          |         Example                            |
+====================+=========================+============================================+
|       name         |     string dataset      |     “John Doe”                             |+--------------------+-------------------------+--------------------------------------------+|       role         |     string dataset      |     “Project PI”                           |+--------------------+-------------------------+--------------------------------------------+|    affiliation     |     string dataset      |     “University of California, Berkeley”   |+--------------------+-------------------------+--------------------------------------------+|      address       |     string dataset      |     “EPS UC Berkeley CA 94720 4767 USA”    |+--------------------+-------------------------+--------------------------------------------+|       phone        |     string dataset      |     “+1 123 456 0000”                      |+--------------------+-------------------------+--------------------------------------------+|       email        |     string dataset      |     “johndoe@berkeley.edu”                 |+--------------------+-------------------------+--------------------------------------------+| facility_user_id   |     string dataset      |     “a123456”                              |+--------------------+-------------------------+--------------------------------------------+Table: Experimenter Group Members    name: User name.    role: User role.    affiliation: User affiliation.    address: User address.    phoen: User phone number.    email: User e-mail address    facility_user_id: User badge number


.. _geometry:

Geometry
^^^^^^^^

The geometry group is common to many of the subgroups undermeasurement. The intent is to describe the translation and rotation(orientation) of the sample or instrument component relative to somecoordinate system. Since we believe it is not possible to determine allpossible uses at this time, we leave the precise definition of geometryup to the technique. We do encourage the use of separate translation andorientation subgroups within geometry. As such, we do not describegeometry further here. This class holds the general position and 
orientation of a component.

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
```````````

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
```````````

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

Provenance==========Data provenance is the documentation of all transformations, analysesand interpretations of data performed by a sequence of process functionsor actorts.Maintaining this history allows for reproducible data. The Data Exchangeformat tracks provenance by allowing each actor to append provenanceinformation to a process table. The provenance process table tracks theexecution order of a series of processes by appending sequential entriesin the process table.Scientific users will not generally be expected to maintain data in thisgroup. The expectation is that analysis pipeline tools willautomatically record process steps using this group. In addition, it ispossible to re-run an analysis using the information provided here.+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+|   actor   |    start_time     |    end_time       |     status    |     message          |          reference       |     description                     |+===========+===================+===================+===============+======================+==========================+=====================================+
| gridftp   |     21:15:22      |     21:15:23      |     FAILED    |     auth. error      |     /provenance/griftp   |     transfer detector to cluster    |+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| gridftp   |     21:15:26      |     21:15:27      |     FAILED    |     auth. error      |     /provenance/griftp   |     transfer detector to cluster    |   +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| gridftp   |     21:17:28      |     22:15:22      |     SUCCESS   |         OK           |     /provenance/griftp   |     transfer detector to cluster    |    +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| norm      |     22:15:23      |     22:30:22      |     SUCCESS   |         OK           |     /provenance/norm     |     normalize the raw data          |+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| rec       |     22:30:23      |     22:50:22      |     SUCCESS   |         OK           |     /provenance/rec      |     reconstruct the norm. data      |  +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| convert   |     22:50:23      |                   |     RUNNING   |         OK           |     /provenance/export   |     convert reconstructed data      |  +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| gridftp   |                   |       QUEUED      |               |                      |     /provenance/griftp_2 |     transfer data to user           | +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+Table: Process table to log actors activity

actor    |     | Name of the process in the pipeline stage that is executed at this      step.*start_time*    |     | Time the process started.*end_time*    |     | TIme the process ended.*status*    |     | Current process status. May be one of the following: QUEUED,      RUNNING, FAILED, or SUCCESS.*message*    |     | A process specific message generated by the process. It may be a      confirmation that the process was successful, or a detailed error      message, for example.*reference*    |     | Path to a process description group. The process description group      contains all metadata to perform the specific process. This      reference is simply the HDF5 path within this file of the      technique specific process description group. The process      description group should contain all parameters necessary to run      the process, including the name and version of any external      analysis tool used to process the data. It should also contain      input and output references that point to the      **exchange_N** groups that contain the input and output      datasets of the process.*description*    |     | Process description.
