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

Top level (root)
================

This node represents the top level of the HDF5 file and holds some
general information about the file.


+---------------+----------------+-----------------------------------------+
|    Member     |      Type      |              Example                    |
+===============+================+=========================================+
|**implements** | string dataset | **exchange**:*measurement*:*provenance* |
+---------------+----------------+-----------------------------------------+
|**exchange**   |    group       |                                         |
+---------------+----------------+-----------------------------------------+
|*measurement*  |    group       |                                         |
+---------------+----------------+-----------------------------------------+
| *provenance*  |    group       |                                         |
+---------------+----------------+-----------------------------------------+

implements
    | 
    | A colon separated list that shows which components are present in
      the file. The only **mandatory** component is **exchange**. A more
      general Data Exchange file also contains *measurement* and
      *provenance* information, if so these will be declared in **implements**
      as **exchange**:*measurement*:*provenance*

exchange or exchange_N
    | 
    | The data taken from measurements or processing. Dimension
      descriptors within the group may also serve to describe
      “positioner” values involved in a scan. 

measurement or measurement_N
    | 
    | Description of the sample and instrument as configured for the
      measurement. This group is appropriate for relatively static
      metadata. For measurements where there are many “positioner”
      values (aka a “scan”), it is more sensible to add dimension(s) to
      the exchange dataset, and describe the “positioner” values as
      dimension scales rather than record the data via multiple matching
      *measurement* and **exchange** groups. This is a judgement left to
      the user.

provenance
    | 
    | The Provenance group describes all process steps that have been
      applied to the data.
      
**exchange**
============

In X-ray tomography, the 3D arrays representing the most basic version
of the data include projections, dark, and white fields. It is
**mandatory** that there is at least one dataset named **data** in each
exchange group. Most data analysis and plotting programs will primarily
focus in this group.

+------------------+---------------------------------------------------------+-----------------------------+
|     Member       |      Type                                               |     Example/Attributes      |
+==================+=========================================================+=============================+
|    *title*       |      string dataset                                     |  "raw absorption tomo"      |
+------------------+---------------------------------------------------------+-----------------------------+
|    **data**      |      3D dataset                                         |  axes: *theta:y:x*          |
+------------------+---------------------------------------------------------+-----------------------------+
|   *theta*        |      1D dataset                                         |  units: "deg"               |
+------------------+---------------------------------------------------------+-----------------------------+
|  *data_dark*     |      3D dataset                                         |  axes: *theta_dark:y:x*     |
+------------------+---------------------------------------------------------+-----------------------------+
|  *theta_dark*    |      1D dataset                                         |  units: "deg"               |
+------------------+---------------------------------------------------------+-----------------------------+
|  *data_white*    |      3D dataset                                         |  axes: *theta_white:y:x*    |
+------------------+---------------------------------------------------------+-----------------------------+
|  *theta_white*   |      dimension scale 0                                  |  units: "deg"               |
+------------------+---------------------------------------------------------+-----------------------------+
|   *data_shift_x* |      relative x shift of data at each angular position  |                             |
+------------------+---------------------------------------------------------+-----------------------------+
|   *data_shift_y* |      relative y shift of data at each angular position  |                             |
+------------------+---------------------------------------------------------+-----------------------------+

Table: Exchange Group Members for Tomography

title
    | 
    | This is the data title.

data
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
      
data_dark, data_white
    | 
    | The dark field and white fields must have the same dimensions as
      the projection images and can be collected at any time before,
      during, or after the projection data collection. To specify where
      dark and white images were taken, specify the axes attribute with
      “theta_dark:y:x” and “theta_white:y:x” and provide *theta_dark*
      and *theta_white* vector datasets that specify the rotation angles
      where they were collected.
      
theta, theta dark, theta_white
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

Attribute
---------

Description and units can be added as attribute to any data, both array or values,
inside a data exchange file. If units is omitted default is SI.

+---------------+------------------------+------------------------+
|    Member     |      Type              |    Example             |
+===============+========================+========================+
| *description* |   string attribute     | “transmission”         |
+---------------+------------------------+------------------------+
|    *units*    |   string attribute     |      *counts*          |
+---------------+------------------------+------------------------+

Table: data attributes

*measurement*
=============

This group holds sample and instrument information. These groups are
designed to hold relatively static data about the sample and instrument
configuration at the time of the measurement. Rapidly changing
*positioner* values (aka scan) are better represented in the exchange
group dataset.

+---------------+----------------------+------------------------+
|    Member     |      Type            |     Example            |
+===============+======================+========================+
|  instrument_  |      group           |                        |
+---------------+----------------------+------------------------+
|    sample_    |      group           |                        |
+---------------+----------------------+------------------------+

Table: Measurement Group Members

instrument
    | 
    | The instrument used to collect this data.

sample
    | 
    | The sample measured.


.. _instrument:

*instrument*
------------

The instrument group stores all relevant beamline components status at
the beginning of a measurement. While all these fields are optional, if
you do intend to include them they should appear within this parentage
of groups.


+---------------------------------------------+-------------------------+-------------------------+
|                    Member                   |           Type          |         Example         |
+=============================================+=========================+=========================+
|                  *name*                     |       string dataset    | "XSD/32-ID/TXM"         |
+---------------------------------------------+-------------------------+-------------------------+
|                  *description*              |       string dataset    | "X-ray Microscope"      |
+---------------------------------------------+-------------------------+-------------------------+
|                   source_                   |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   shutter_                  |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   attenuator_               |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   monochromator_            |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   mirror_                   |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   crl_                      |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   beam_monitor_             |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   diffuser_                 |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   beam_stop_                |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   condenser_                |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   pin_hole_                 |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   zone_plate_               |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   bertrand_lens_            |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   flight_tube_              |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   interferometer_           |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   detector_                 |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   acquisition_              |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+
|                   setup_                    |          group          |                         |
+---------------------------------------------+-------------------------+-------------------------+

Table: Instrument Group for Tomography

name
    | 
    | Name of the instrument.

source
    | 
    | The source used by the instrument.

shutter
    | 
    | The shutter(s) used by the instrument.

attenuator
    | 
    | The attenuators that are part of the instrument.

monochromator
    | 
    | The monochromator used by the instrument.

detector
    | 
    | The detectors that compose the instrument.

acquisition
    | 
    | acquisition setup parameters (static setup values)


.. _source:

*source*
~~~~~~~~

Class describing the light source being used.

+-----------------------------+--------------------------------+---------------------------+
| Member                      |     Type                       |     Example               |
+=============================+================================+===========================+
|*name*                       |     string dataset             |     “APS”                 |
+-----------------------------+--------------------------------+---------------------------+
|*description*                |     float dataset              |     "optional"            |
+-----------------------------+--------------------------------+---------------------------+
|*datetime*                   |     string dataset (ISO 8601)  |     “2011-07-15T15:10Z”   |
+-----------------------------+--------------------------------+---------------------------+
|*beamline*                   |     string dataset             |     “2-BM”                |
+-----------------------------+--------------------------------+---------------------------+
|*current*                    |     float dataset              |     0.094                 |
+-----------------------------+--------------------------------+---------------------------+
|*energy*                     |     float dataset              |     4.807e-15             |
+-----------------------------+--------------------------------+---------------------------+
|*pulse_energy*               |     float dataset              |     1.602e-15             |
+-----------------------------+--------------------------------+---------------------------+
|*pulse_width*                |     float dataset              |     15e-11                |
+-----------------------------+--------------------------------+---------------------------+
|*mode*                       |     string dataset             |     “TOPUP”               |
+-----------------------------+--------------------------------+---------------------------+
|*beam_intensity_incident*    |     float dataset              |     55.93                 |
+-----------------------------+--------------------------------+---------------------------+
|*beam_intensity_transmitted* |     float dataset              |     100.0                 |
+-----------------------------+--------------------------------+---------------------------+
| geometry_                   |     group                      |                           |
+-----------------------------+--------------------------------+---------------------------+
| setup_                      |     group                      |                           |
+-----------------------------+--------------------------------+---------------------------+

Table: table_source


name
    | 
    | Name.

description
    | 
    | Description.
    
datetime
    | 
    | Date and time source was measured.
    
beamline
    | 
    | Name of the beamline.
    
current
    | 
    | Electron beam current (A).
    
energy
    | 
    | Characteristic photon energy of the source (J). For an APS bending
    | magnet this is 30 keV or 4.807e-15 J.
      
pulse_energy
    | 
    | Sum of the energy of all the photons in the pulse (J). pulse_width
    | Duration of the pulse (s).
    
mode
    | 
    | Beam mode: TOP-UP.
    
beam_intensity_incident
    | 
    | Incident beam intensity in (photons per s).
    
beam_intensity_transmitted
    | 
    | Transmitted beam intensity (photons per s).

.. _shutter:

*shutter*
~~~~~~~~~

Class describing the shutter being used.

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Front End Shutter 1"     |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|     *status*       |     string dataset      |     “OPEN”                    |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Shutter Group Members

name
    | 
    | Name.

description
    | 
    | Description.

status
    | 
    | “OPEN” or “CLOSED”

.. _attenuator:

*attenuator*
~~~~~~~~~~~~

This class describes the beamline attenuator(s) used during data
collection. If more than one attenuators are used they will be named as
attenuator_1, attenuator_2 etc.

+---------------------------+-------------------------+-------------------------------+
|      Member               |           Type          |         Example               |
+===========================+=========================+===============================+
| *name*                    |     string dataset      |     “Filter Set 1"            |
+---------------------------+-------------------------+-------------------------------+
| *description*             |     string dataset      |     “Al"                      |
+---------------------------+-------------------------+-------------------------------+
| *thickness*               |     float dataset       |     1e-3                      |
+---------------------------+-------------------------+-------------------------------+
| *transmission*            |     float dataset       |     unit-less                 |
+---------------------------+-------------------------+-------------------------------+
| geometry_                 |     group               |                               |
+---------------------------+-------------------------+-------------------------------+
| setup_                    |     group               |                               |
+---------------------------+-------------------------+-------------------------------+

Table: Attenuator Group Members


name
    | 
    | Name.

description
    | 
    | Description.

thickness 
    | 
    | Thickness of attenuator along beam direction.
    
attenuator_transmission
    | 
    | The nominal amount of the beam that gets through (transmitted
    |  intensity)/(incident intensity).
    
description
    | 
    | Type or composition of attenuator.

.. _monochromator:

*monochromator*
~~~~~~~~~~~~~~~

Define the monochromator used in the instrument.

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
| *name*             |     string dataset      |     “Mono 1”                  |
+--------------------+-------------------------+-------------------------------+
| *description*      |     string dataset      |     “Multilayer”              |
+--------------------+-------------------------+-------------------------------+
| *energy*           |     float dataset       |     1.602e-15                 |
+--------------------+-------------------------+-------------------------------+
| *energy_error*     |     float dataset       |     1.602e-17                 |
+--------------------+-------------------------+-------------------------------+
| *mono_stripe*      |     string dataset      |     “Ru/C”                    |
+--------------------+-------------------------+-------------------------------+
| geometry_          |     group               |                               |
+--------------------+-------------------------+-------------------------------+
| setup_             |     group               |                               |
+--------------------+-------------------------+-------------------------------+

Table: Monochromator Group Members

name
    | 
    | Name.

description
    | 
    | Description.
    
energy
    | 
    | Peak of the spectrum that the monochromator selects. Since units
    |  is not defined this field is in J and corresponds to 10 keV.
    
energy_error
    | 
    | Standard deviation of the spectrum that the monochromator selects.
    |  Since units is not defined this field is in J.
    
mono_stripe
    | 
    | Type of multilayer coating or crystal.


.. _mirror:

*mirror*
~~~~~~~~

Class describing the mirror being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “M1"                      |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Mirror Group Members


.. _crl:

crl
~~~

Class describing the compound refractive lenses being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “CRL"                     |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: CRL Group Members


.. _beam_monitor:

*beam_monitor*
~~~~~~~~~~~~~~

Class describing the beam monitor being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Beam Monitor"            |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Beam Monitor Group Members


.. _diffuser:

*diffuser*
~~~~~~~~~~

Class describing the diffuser being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Diffuser"                |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Diffuser Group Members


.. _beam_stop:

*beam_stop*
~~~~~~~~~~~

Class describing the beam stop being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Beam Stop"               |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Beam Stop Group Members


.. _condenser:

*condenser*
~~~~~~~~~~~

Class describing the condenser being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Condenser"               |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Condenser Group Members


.. _pin_hole:

*pin_hole*
~~~~~~~~~~

Class describing the pin hole being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Pin Hole"                |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Pin Hole Group Members


.. _zone_plate:

*zone_plate*
~~~~~~~~~~~~

Class describing the zone plate being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Zone Plate"              |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Zone Plate Group Members


.. _bertrand_lens:

*bertrand_lens*
~~~~~~~~~~~~~~~

Class describing the Bertrand lens being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Bertrand Lens"           |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Bertrand Lens Group Members


.. _flight_tube:

*flight_tube*
~~~~~~~~~~~~~

Class describing the flight tube being used, if there is more than one append _##

+--------------------+-------------------------+-------------------------------+
|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|      *name*        |     string dataset      |     “Flight Tube"             |
+--------------------+-------------------------+-------------------------------+
|  *description*     |     string dataset      |     “optional”                |
+--------------------+-------------------------+-------------------------------+
|       geometry_    |        group            |                               |
+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |
+--------------------+-------------------------+-------------------------------+

Table: Flight Tube Group Members


.. _interferometer: 

*interferometer*
~~~~~~~~~~~~~~~~

This group stores the interferometer parameters.

+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|    *name*                                    |     string dataset               |     “Inter 1”                    |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *description*                             |     string dataset               |     “description”                |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *grid_start*                              |      float                       |      1.8                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *grid_end*                                |      float                       |      3.51                        | 
+----------------------------------------------+----------------------------------+----------------------------------+
|    *number_of_grid_periods*                  |      int                         |      1                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *number_of_grid_steps*                    |      int                         |      6                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|         geometry_                            |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|         setup_                               |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+

Table: Interferometer Group Members

name
    | 
    | Name.

description
    | 
    | Description.

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

*detector*
~~~~~~~~~~

This class holds information about the detector used during the
experiment. If more than one detector are used they will be all listed
as detector_N. In full field imaging the detector consists of
a CCD camera, microscope objective and a scintillator screen. Raw data
recorded by a detector as well as its position and geometry should be
stored in this class.

+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|   *name*                                     | string dataset                   |      "DIMAX 1"                   |   
+----------------------------------------------+----------------------------------+----------------------------------+
|   *description*                              | string dataset                   |      "description"               |   
+----------------------------------------------+----------------------------------+----------------------------------+
|   *manufacturer*                             | string dataset                   |      "CooKe Corporation"         |   
+----------------------------------------------+----------------------------------+----------------------------------+
|   *model*                                    | string dataset                   |       "pco dimax"                |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *serial_number*                            | string dataset                   |       "1234XW2"                  |  
+----------------------------------------------+----------------------------------+----------------------------------+
|   *firmware_version*                         | string dataset                   |       "3.7.9"                    |  
+----------------------------------------------+----------------------------------+----------------------------------+
|   *software_version*                         | string dataset                   |       "1.3.14"                   |  
+----------------------------------------------+----------------------------------+----------------------------------+
|   *bit_depth*                                |      integer                     |      12                          |     
+----------------------------------------------+----------------------------------+----------------------------------+
|   *pixel_size_x*                             |      float                       |      6.7e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *pixel_size_y*                             |      float                       |      6.7e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *actual_pixel_size_x*                      |      float                       |      1.2e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *actual_pixel_size_y*                      |      float                       |      1.2e-6                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *dimension_x*                              |      integer                     |      2048                        |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *dimension_y*                              |      integer                     |      2048                        |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *binning_x*                                |      integer                     |      1                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *binning_y*                                |      integer                     |      1                           |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *operating_temperature*                    |      float                       |       270                        |     
+----------------------------------------------+----------------------------------+----------------------------------+
|   *exposure_time*                            |      float                       |      1.7e-3                      |   
+----------------------------------------------+----------------------------------+----------------------------------+
|   *delay_time*                               |      float                       |      1.7e-3                      |   
+----------------------------------------------+----------------------------------+----------------------------------+
|   *stabilization_time*                       |      float                       |      1.7e-3                      |   
+----------------------------------------------+----------------------------------+----------------------------------+
|   *frame_rate*                               |      integer                     |       2                          |
+----------------------------------------------+----------------------------------+----------------------------------+
|   *output_data*                              | string dataset                   |      "/exchange"                 |
+----------------------------------------------+----------------------------------+----------------------------------+
|    roi_                                      |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|    objective_                                |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|    scintillator_                             |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *counts_per_joule*                        |      float                       |      unitless                    | 
+----------------------------------------------+----------------------------------+----------------------------------+
|    *basis_vectors*                           |      float array                 |      length                      | 
+----------------------------------------------+----------------------------------+----------------------------------+
|    *corner_position*                         |      3 floats                    |      length                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|         geometry_                            |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+
|         setup_                               |      group                       |                                  |
+----------------------------------------------+----------------------------------+----------------------------------+


Table: Detector Group Members for Tomography

name
    | 
    | Name.

description
    | 
    | Description.

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

*roi*
^^^^^

Group describing the region of interest (ROI) of the image actually
collected, if smaller than the full CCD.

+----------------+----------------+-----------------+
|     Member     |      Type      |      Example    |
+================+================+=================+
|   *name*       | string dataset | "ROI 04"        | 
+----------------+----------------+-----------------+
| *description*  | string dataset | "center third"  | 
+----------------+----------------+-----------------+
|  *min_x*       | integer        |      256        |   
+----------------+----------------+-----------------+
|  *size_x*      | integer        |      256        |
+----------------+----------------+-----------------+
|  *min_y*       | integer        |      1792       |
+----------------+----------------+-----------------+
|  *size_y*      | integer        |      1792       |
+----------------+----------------+-----------------+

Table: ROI Group Members

name
    | 
    | Name.

description
    | 
    | Description.

min_x, min_y
    | 
    | Top Left pixel x and y position.

size_x, size_y
    | 
    | x and y image size.



.. _objective:

*objective*
^^^^^^^^^^^

Group describing the microscope objective lenses used.

+------------------------------------+----------------+-----------------+
|     Member                         |      Type      |      Example    |
+====================================+================+=================+
| *name*                             | string dataset |      "Lens 01"  |
+------------------------------------+----------------+-----------------+
| *description*                      | string dataset |      "ZeissAx"  |
+------------------------------------+----------------+-----------------+
| *manufacturer*                     | string dataset |      "Zeiss"    |
+------------------------------------+----------------+-----------------+
| *model*                            | string dataset |      "Axioplan" |
+------------------------------------+----------------+-----------------+
| *magnification*                    | float dataset  |      5          | 
+------------------------------------+----------------+-----------------+
| *numerical_aperture*               | float dataset  |      0.8        |
+------------------------------------+----------------+-----------------+
| geometry_                          | group          |                 |
+------------------------------------+----------------+-----------------+
| setup_                             | group          |                 |
+------------------------------------+----------------+-----------------+

Table: Objective Group Members

name
    | 
    | Name.

description
    | 
    | Description.

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

*scintillator*
^^^^^^^^^^^^^^

Group describing the visible light scintillator coupled to the CCD
camera objective lens.

+------------------------------------+----------------+-----------------+
|     Member                         |      Type      |      Example    |
+====================================+================+=================+
|   *name*                           | string dataset |  "Yag polished" | 
+------------------------------------+----------------+-----------------+
|   *description*                    | string dataset |  "Yag on Yag"   |  
+------------------------------------+----------------+-----------------+
|   *manufacturer*                   | string dataset |  "Crytur"       |
+------------------------------------+----------------+-----------------+
|   *serial_number*                  | string dataset |    "12"         |   
+------------------------------------+----------------+-----------------+
|   *scintillating_thickness*        | float dataset  |       5e-6      |  
+------------------------------------+----------------+-----------------+
|   *substrate_thickness*            | float dataset  |        1e-4     |  
+------------------------------------+----------------+-----------------+
|       geometry_                    | group          |                 |
+------------------------------------+----------------+-----------------+
|       setup_                       | group          |                 |
+------------------------------------+----------------+-----------------+

Table: Scintillator Group Members

name
    | 
    | Scintillator name.
    
description
    | 
    | Scintillator description.

manufacturer
    | 
    | Scintillator Manufacturer.

serial_number
    | 
    | Scintillator serial number.
    
scintillating_thickness
    | 
    | Scintillator thickness.

substrate_thickness
    | 
    | Scintillator substrate thickness.


.. _setup:

*setup*
~~~~~~~

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
|    *sample_x*                                |      float                       |      -10.107                     |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *sample_y*                                |      float                       |       -17.900                    |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *sample_z*                                |      float                       |      -5.950                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *sample_xx*                               |      float                       |      -1.559                      |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *sample_zz*                               |      float                       |      1.307                       |
+----------------------------------------------+----------------------------------+----------------------------------+

.. _sample:

*sample*
--------

This group holds basic information about the sample, its geometry,
properties, the sample owner (user) and sample proposal information.
While all these fields are optional, if you do intend to include them
they should appear within this parentage of groups.

+-------------------------------------+------------------------------------+-----------------------------+
|    Member                           |                 Type               |          Example            |
+=====================================+====================================+=============================+
|        *name*                       |     string dataset                 |      "cells sample 1"       |    
+-------------------------------------+------------------------------------+-----------------------------+
|    *description*                    |     string dataset                 |      "malaria cells"        |   
+-------------------------------------+------------------------------------+-----------------------------+
|    *preparation_date*               |  string dataset (ISO 8601)         |  "2012-07-31T21:15:22+0600" |    
+-------------------------------------+------------------------------------+-----------------------------+
|    *chemical_formula*               | string dataset (abbr. CIF format)  |     "(Cd 2+)3,  2(H2 O)"    |   
+-------------------------------------+------------------------------------+-----------------------------+
|          *mass*                     |     float dataset                  |              0.25           |
+-------------------------------------+------------------------------------+-----------------------------+
|    *concentration*                  |     float dataset                  |              0.4            |
+-------------------------------------+------------------------------------+-----------------------------+
|    *environment*                    |     string dataset                 |             "air"           |  
+-------------------------------------+------------------------------------+-----------------------------+
|    *temperature*                    |     float dataset                  |             25.4            |
+-------------------------------------+------------------------------------+-----------------------------+
|    *temperature_set*                |     float dataset                  |             26.0            |
+-------------------------------------+------------------------------------+-----------------------------+
|    *pressure*                       |     float dataset                  |           101325            | 
+-------------------------------------+------------------------------------+-----------------------------+
|    *thickness*                      |     float dataset                  |            0.001            |
+-------------------------------------+------------------------------------+-----------------------------+
|    *position*                       |     string dataset                 |  "2D"  APS robot coord.     |
+-------------------------------------+------------------------------------+-----------------------------+
|    geometry_                        |            group                   |                             |
+-------------------------------------+------------------------------------+-----------------------------+
|    setup_                           |            group                   |                             |
+-------------------------------------+------------------------------------+-----------------------------+
|    experiment_                      |            group                   |                             |
+-------------------------------------+------------------------------------+-----------------------------+
|    experimenter_                    |            group                   |                             |
+-------------------------------------+------------------------------------+-----------------------------+

Table: Sample Group Members

name
    | 
    | Descriptive name of the sample.

description
    | 
    | Description of the sample.

preparation_date
    | 
    | Date and time the sample was prepared.

chemical_formula
    | 
    | Sample chemical formula using the CIF format.

mass
    | 
    | Mass of the sample.

concentration
    | 
    | Mass/volume.

environment 
    | 
    | Sample environment.

temperature 
    | 
    | Sample temperature.

temperature_set
    | 
    | Sample temperature set point.

pressure
    | 
    | Sample pressure.

thickness
    | 
    | Sample thickness.

position 
    | 
    | Sample position in the sample changer/robot.

geometry
    | 
    | Sample center of mass position and orientation.

experiment
    | 
    | Facility experiment identifiers.

experimenter
    | 
    | Experimenter identifiers.

*experiment*
~~~~~~~~~~~~

This provides references to facility ids for the proposal, scheduled
activity, and safety form.

+---------------+-------------------------+----------------------+
|   Member      |            Type         |       Example        | 
+===============+=========================+======================+
| *proposal*    |     string dataset      |        “1234”        |
+---------------+-------------------------+----------------------+
| *activity*    |     string dataset      |        “9876”        |
+---------------+-------------------------+----------------------+
| *safety*      |     string dataset      |        “9876”        |
+---------------+-------------------------+----------------------+

Table: Experiment Group Members

proposal
    | 
    | Proposal reference number. For the APS this is the General User
    | Proposal number.
      
activity
    | 
    | Proposal scheduler id. For the APS this is the beamline scheduler
      activity id.

safety
    | 
    | Safety reference document. For the APS this is the Experiment
    | Safety Approval Form number.

*experimenter*
~~~~~~~~~~~~~~

Description of a single experimenter. Multiple experimenters can be
represented through numbered entries such as experimenter_1,
experimenter_2.

+--------------------+-------------------------+--------------------------------------------+
|      Member        |           Type          |         Example                            |
+====================+=========================+============================================+
|      *name*        |     string dataset      |     “John Doe”                             |
+--------------------+-------------------------+--------------------------------------------+
|      *role*        |     string dataset      |     “Project PI”                           |
+--------------------+-------------------------+--------------------------------------------+
|   *affiliation*    |     string dataset      |     “University of California, Berkeley”   |
+--------------------+-------------------------+--------------------------------------------+
|     *address*      |     string dataset      |     “EPS UC Berkeley CA 94720 4767 USA”    |
+--------------------+-------------------------+--------------------------------------------+
|      *phone*       |     string dataset      |     “+1 123 456 0000”                      |
+--------------------+-------------------------+--------------------------------------------+
|      *email*       |     string dataset      |     “johndoe@berkeley.edu”                 |
+--------------------+-------------------------+--------------------------------------------+
| *facility_user_id* |     string dataset      |     “a123456”                              |
+--------------------+-------------------------+--------------------------------------------+

Table: Experimenter Group Members

    name: User name.

    role: User role.

    affiliation: User affiliation.

    address: User address.

    phoen: User phone number.

    email: User e-mail address

    facility_user_id: User badge number


.. _geometry:

*geometry*
^^^^^^^^^^

The geometry group is common to many of the subgroups under
measurement. The intent is to describe the translation and rotation
(orientation) of the sample or instrument component relative to some
coordinate system. Since we believe it is not possible to determine all
possible uses at this time, we leave the precise definition of geometry
up to the technique. We do encourage the use of separate translation and
orientation subgroups within geometry. As such, we do not describe
geometry further here. This class holds the general position and 
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

*translation*
`````````````

This is the description for the general spatial location of a component
for tomography.

+----------------------------+------------------------+-----------------+
|     Member                 |      Type              |      Example    |
+============================+========================+=================+
|           *distances*      | 3 float array dataset  |  (0, 0.001, 0)  |
+----------------------------+------------------------+-----------------+

distances
    | 
    | The x, y and z components of the translation of the origin of the object
    | relative to the origin of the global coordinate system (the place where 
    | the X-ray beam  meets the sample when the sample is first aligned in the beam).
    | If  distances does not have the attribute units set then the units are in
    | meters.

.. _orientation:

*orientation*
`````````````

This is the description for the orientation of a component for
tomography.

+----------------------------+------------------------+-----------------+
|     Member                 |      Type              |      Example    |
+============================+========================+=================+
|      *value*               | 6 float array dataset  |                 |
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

*provenance*
============

Data provenance is the documentation of the data collection strategy
(*acquisition*) and all transformations, analyses and interpretations 
of data performed by a sequence of process functions or actorts.

Maintaining this history allows for reproducible data. The Data Exchange
format tracks provenance by allowing each actor to append provenance
information to a process table. The provenance process table tracks the
execution order of a series of processes by appending sequential entries
in the process table.

+-------------------------------------+------------------------------------+-----------------------------+
|    Member                           |                 Type               |          Example            |
+=====================================+====================================+=============================+
|        *name*                       |     string dataset                 |            "name"           |    
+-------------------------------------+------------------------------------+-----------------------------+
|    *description*                    |     string dataset                 |           "optional"        |   
+-------------------------------------+------------------------------------+-----------------------------+
|    acquisition_                     |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
|    tomo_rec_                        |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
|    transfer_                        |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
|    table_                           |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
Table: Provenance Group Members

name    |     | Descriptive provenance task.

description    |     | Description of the provenance task.
    
.. _acquisition:

*acquisition*
-------------

Logging acquisition setup parameters (static setup values) is not defined by Data Exchange 
because is specific and different for each instrument and beamline.
In the table below we present the implementation adopted by the Swiss Light Source and
Advanced Photon Source.

+----------------------------------------------+--------------------+------------------------------------------------------+
|     Member                                   |      Type          |            Example                                   |
+==============================================+====================+======================================================+
|   *name*                                     | string dataset     |      "dpc_tomography"                                |
+----------------------------------------------+--------------------+------------------------------------------------------+
|   *description*                              | string dataset     |      "step scan"                                     |
+----------------------------------------------+--------------------+------------------------------------------------------+
|   *version*                                  | string dataset     | https://github.com/data_collection_scripts/b9ad87e17 |
+----------------------------------------------+--------------------+------------------------------------------------------+
|   *output_data*                              | string dataset     |        "/exchange"                                   |+----------------------------------------------+--------------------+------------------------------------------------------+
|   set-up_                                    | group              |                                                      |
+----------------------------------------------+--------------------+------------------------------------------------------+


Table: Acquisition Group Members


.. _set-up:

*setup*
~~~~~~~

In the table below we present the implementation adopted by the Swiss Light Source and
Advanced Photon Source.

+----------------------------------------------+----------------------------------+----------------------------------+
|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+
|    *rotation_start_angle*                    |      float                       |      0.0                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *rotation_end_angle*                      |      float                       |      180.0                       |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *angular_step*                            |      float                       |      0.125                       |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *number_of_projections*                   |      integer                     |      1441                        |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *number_of_flats*                         |      integer                     |      100                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *number_of_darks*                         |      integer                     |      32                          |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *sample_in*                               |      float                       |      0.0                         |
+----------------------------------------------+----------------------------------+----------------------------------+
|    *sample_out*                              |      float                       |      4.0                         |
+----------------------------------------------+----------------------------------+----------------------------------+

Table: Setup Acquisition Group for Tomography

.. _reconstruction:

*tomo_rec*----------The Reconstruction process description group contains metadata requiredto run a tomography reconstruction. The specific algorithm is describedin a separate group under the reconstruction setup group.
Here is where to log the algorithm setup parameters. In the case of tomoPy 
this can simply be the link to the scrip used to run the reconstruction. 
+-------------------------------------+------------------------------------+---------------------------------------------+
|    Member                           |                 Type               |          Example                            |
+=====================================+====================================+=============================================+
|       *name*                        |     string dataset                 |        "test rec"                           | 
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *description*                 |     string dataset                 |        "optional"                           |
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *version*                     |     string dataset                 | https://github.com/tomopy_scripts/b9ad87e17 |
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *input_data*                  |     string dataset                 |        "/exchange"                          |+-------------------------------------+------------------------------------+---------------------------------------------+
|       *output_data*                 |     string dataset                 |        "/exchange_1"                        |+-------------------------------------+------------------------------------+---------------------------------------------+
|       set_up_                       |        group                       |                                             |
+-------------------------------------+------------------------------------+---------------------------------------------+


Table: Reconstruction Actor Group Members

name    |     | Descriptive actor task.

description    |     | Description of the actor task.
    
version    |     | Version of the actor task.
    |     | If available this can be the repository link to the actor version used
    | https://github.com/tomopy_scripts/b9ad87e17
input_data, output_data
    |     | Origin and destination of the data processed by the reconstruction task.
    
.. _set_up:

*setup*
~~~~~~~

Here is where to log the algorithms used by the reconstruction actor. 

+-------------------------------------+------------------------------------+-----------------------------------------------+
|    Member                           |                 Type               |          Example                              |
+=====================================+====================================+===============================================+
|    *astra*                          |     string dataset                 | https://github.com/astra/b9ad87e17            | 
+-------------------------------------+------------------------------------+-----------------------------------------------+
|    *tomopy*                         |     string dataset                 | https://github.com/tomopy/c9ad87e77           |
+-------------------------------------+------------------------------------+-----------------------------------------------+
Table: Reconstruction Setup Group Members
.. _reconstruction_sls:

*tomo_rec_sls*--------------The reconstruction process description group contains metadata requiredto run a tomography reconstruction. The specific algorithm is describedin a separate group under the reconstruction setup group.
Here is where to log the algorithm setup parameters. 
+-------------------------------------+------------------------------------+---------------------------------------------+
|       Member                        |                 Type               |          Example                            |
+=====================================+====================================+=============================================+
|       *name*                        |     string dataset                 |        "sls rec"                            | 
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *description*                 |     string dataset                 |        "optional"                           |
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *version*                     |     string dataset                 | https://github.com/sls_scripts/b9ad87e17    |
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *input_data*                  |     string dataset                 |        "/exchange"                          |+-------------------------------------+------------------------------------+---------------------------------------------+
|       *output_data*                 |     string dataset                 |        "/exchange_1"                        |+-------------------------------------+------------------------------------+---------------------------------------------+
|       set_up_sls_                   |        group                       |                                             |
+-------------------------------------+------------------------------------+---------------------------------------------+


Table: Reconstruction Actor Group Members

name    |     | Descriptive actor task.

description    |     | Description of the actor task.
    
version    |     | Version of the actor task.
    |     | If available this can be the repository link to the actor version used
    | https://github.com/tomopy_scripts/b9ad87e17
input_data, output_data
    |     | Origin and destination of the data processed by the reconstruction task.
    
.. _set_up_sls:

*setup_sls*
~~~~~~~~~~~

Here is where to log the algorithms used by the reconstruction actor. 

+-------------------------------------+-----------------+----------------------------+|    Member                           | Type            |          Example           |
+=====================================+=================+============================+
|    *reconstruction_slice_start*     | int dataset     |       1000                 |+-------------------------------------+-----------------+----------------------------+|    *reconstruction_slice_end*       | int dataset     |       1030                 |+-------------------------------------+-----------------+----------------------------+|    *rotation_center*                | Float dataset   |      1048.50               |+-------------------------------------+-----------------+----------------------------+|    algorithm-sls_                   | Group           |                            |+-------------------------------------+-----------------+----------------------------+Table: Reconstruction Setup SLS Group Members

reconstruction_slice_start    |     | First reconstruction slice.reconstruction_slice_end    |     | Last reconstruction slice.rotation_center    |     | Center of rotation in pixels.algorithm    |     | Algorithm group describing reconstruction algorithm parameters.

.. _algorithm-sls:
algorithm sls (iterative)^^^^^^^^^^^^^^^^^^^^^^^^^The Algorithm group contains information required to run a tomographyreconstruction algorithm.+----------------------------------------------+-----------------+-------------------+|     Member                                   |      Type       |    Example        |+==============================================+=================+===================+|    *name*                                    | string dataset  | "SART"            |     +----------------------------------------------+-----------------+-------------------+|    *version*                                 | string dataset  | "1.0"             |+----------------------------------------------+-----------------+-------------------+|    *implementation*                          | string dataset  | "GPU"             |    +----------------------------------------------+-----------------+-------------------+|    *number_of_nodes*                         | int dataset     | 16                |+----------------------------------------------+-----------------+-------------------+|    *type*                                    | string dataset  | "Iterative"       |     +----------------------------------------------+-----------------+-------------------+|    *stop_condition*                          | string dataset  | "iteration_max"   |  +----------------------------------------------+-----------------+-------------------+|    *iteration_max*                           | int dataset     | 200               |+----------------------------------------------+-----------------+-------------------+|    *projection_threshold*                    | float dataset   |                   |  +----------------------------------------------+-----------------+-------------------+|    *difference_threshold_percent*            | float dataset   |                   |    +----------------------------------------------+-----------------+-------------------+|    *difference_threshold_value*              | float dataset   |                   |+----------------------------------------------+-----------------+-------------------+|    *regularization_type*                     | string dataset  | "total_variation" |  +----------------------------------------------+-----------------+-------------------+|    *regularization_parameter*                | float dataset   |                   |  +----------------------------------------------+-----------------+-------------------+|    *step_size*                               | float dataset   | 0.3               |+----------------------------------------------+-----------------+-------------------+|    *sampling_step_size*                      | float dataset   | 0.2               |+----------------------------------------------+-----------------+-------------------+Table: Algorithm Group Membersname    |     | Reconstruction method name: SART, EM, FBP.version    |     | Algorithm version.implementation    |     | CPU or GPU.number_of_nodes    |     | Number of nodes to use on cluster. This parameter is set when the reconstruction is parallelized and run on a cluster.type    |     | Tomography reconstruction method: iterative.stop_condition    |     | iteration_max, projection_threshold, difference_threshold_percent, difference_threshold_value.iteration_max    |     | Maximum number of iterations.projection_threshold    |     | The threshold of projection difference to stop the iterations as.. math:: | y - Ax_{\mathrm{n}}| < pdifference_threshold_percent    |     | The threshold of reconstruction difference to stop the iterations as.. math:: | x_{\mathrm{n+1}}|/ |x_{\mathrm{n}}| < pdifference_threshold_value    |     | The threshold of reconstruction difference to stop the iterations as:.. math:: | x_{\mathrm{n+1}}| - |x_{\mathrm{n}}| < pregularization_type    |     | total_variation, none.regularization_parameter    |     | step_size    |     | Step size between iterations in iterative methods sampling_step_size    |     | Step size used for forward projection calculation in iterative methods.   algorithm sls (analytic)^^^^^^^^^^^^^^^^^^^^^^^^The Algorithm group contains information required to run a tomographyreconstruction algorithm.+----------------------------------------------+-----------------+-------------------+|     Member                                   |      Type       |    Example        |+==============================================+=================+===================+|    name                                      | string dataset  | "gridrec"         |     +----------------------------------------------+-----------------+-------------------+|    version                                   | string dataset  | "1.0"             |+----------------------------------------------+-----------------+-------------------+|    implementation                            | string dataset  | "CPU"             |    +----------------------------------------------+-----------------+-------------------+|    number_of_nodes                           | int dataset     | 16                |+----------------------------------------------+-----------------+-------------------+|    type                                      | string dataset  | "analytic"        |     +----------------------------------------------+-----------------+-------------------+|    filter                                    | string dataset  | "Parzen"          |+----------------------------------------------+-----------------+-------------------+|    padding                                   | float dataset   | 0.50              |+----------------------------------------------+-----------------+-------------------+Table: Algorithm Group Membersname    |     | Reconstruction method name: GridRec.version    |     | Algorithm version.implementation    |     | CPU or GPU.number_of_nodes    |     | Number of nodes to use on cluster. This parameter is set when the reconstruction is parallelized and run on a cluster.type    |     | Tomography reconstruction method: analytic.filter    |     | Filter type.padding        

.. _transfer:

*transfer*----------The transfer process description group contains metadata requiredto trasfer data from source (data analysis machine) to destination
(data distribution server). 

+-------------------------------------+------------------------------------+---------------------------------------------+
|    Member                           |                 Type               |          Example                            |
+=====================================+====================================+=============================================+
|       *name*                        |     string dataset                 |        "Globus"                             | 
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *description*                 |     string dataset                 |        "data distribution to users"         |
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *version*                     |     string dataset                 | https://github.com/globus/b9ad87e17         |
+-------------------------------------+------------------------------------+---------------------------------------------+
|       *input_data*                  |     string dataset                 |        "gsiftp://host1/path"                |+-------------------------------------+------------------------------------+---------------------------------------------+
|       *output_data*                 |     string dataset                 |        "gsiftp://host2/path"                |+-------------------------------------+------------------------------------+---------------------------------------------+
|       *setup*                       |        group                       |                                             |
+-------------------------------------+------------------------------------+---------------------------------------------+


Table: Transfer Actor Group Members

name    |     | Descriptive actor task.

description    |     | Description of the actor task.
    
version    |     | Version of the actor task.
    |     | If available this can be the repository link to the actor version used
    | https://github.com/globus/b9ad87e17
    
input_data, output_data
    |     | Origin and destination of the data processed by the trasnfer task.
    setup
    |
    | Group containing the specific data transfer protocol paramenters.


.. table:

*table*
-------

Scientific users will not generally be expected to maintain data in this
group. The expectation is that analysis pipeline tools will
automatically record process steps using this group. In addition, it is
possible to re-run an analysis using the information provided here.

+---------------+-------------------+-------------------+---------------+----------------------------+-------------------------------+--------------------------+
|   actor       |    start_time     |    end_time       |     status    |     message                |          reference            |   description            |
+===============+===================+===================+===============+============================+===============================+==========================+
| acquisition   |     21:15:22      |     21:15:23      |     FAILED    |     beamline off line      |     /provenance/acquisition   |   raw data collection    |
+---------------+-------------------+-------------------+---------------+----------------------------+-------------------------------+--------------------------+
| acquisition   |     21:15:26      |     21:15:27      |     FAILED    |     beamline off line      |     /provenance/acquisition   |   raw data collection    |
+---------------+-------------------+-------------------+---------------+----------------------------+-------------------------------+--------------------------+
| acquisition   |     21:17:28      |     22:15:22      |     SUCCESS   |            OK              |     /provenance/acquisition   |   raw data collection    |
+---------------+-------------------+-------------------+---------------+----------------------------+-------------------------------+--------------------------+
| tomo_rec      |     22:30:23      |     22:50:22      |     SUCCESS   |            OK              |     /provenance/tomo_rec      |   reconstruct            |  
+---------------+-------------------+-------------------+---------------+----------------------------+-------------------------------+--------------------------+
| transfer      |                   |                   |     QUEUED    |                            |     /provenance/transfer      |   transfer data to user  | 
+---------------+-------------------+-------------------+---------------+----------------------------+-------------------------------+--------------------------+

Table: Process table to log actors activity

actor    |     | Name of the process in the pipeline stage that is executed at this step.*start_time*    |     | Time the process started.*end_time*    |     | TIme the process ended.
    *status*    |     | Current process status. May be one of the following: QUEUED,    | RUNNING, FAILED, or SUCCESS.
    *message*    |     | A process specific message generated by the process. It may be a    | confirmation that the process was successful, or a detailed error    | message, for example.
    *reference*    |     | Path to the actor description group. The process description group    | contains all metadata to perform the specific process. This    | reference is simply the HDF5 path within this file of the    | technique specific process description group. The process    | description group should contain all parameters necessary to run    | the process, including the name and version of any external    | analysis tool used to process the data. It should also contain    | input and output references that point to the    | **exchange_N** groups that contain the input and output    | datasets of the process.
    *description*    |     | Process description.
