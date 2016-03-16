.. role:: math(raw)   :format: html latex..
=========Reference=========Top level (root)================This node represents the top level of the HDF5 file and holds somegeneral information about the file.+---------------+----------------+-----------------------------------------+|    Member     |      Type      |              Example                    |
+===============+================+=========================================+|**implements** | string dataset | **exchange**:*measurement*:*provenance* |+---------------+----------------+-----------------------------------------+|**exchange_N** |    group       |                                         |
+---------------+----------------+-----------------------------------------+|*measurement_N*|    group       |                                         |+---------------+----------------+-----------------------------------------+| *provenance*  |    group       |                                         |+---------------+----------------+-----------------------------------------+**implements**    |     | A colon separated list that shows which components are present in      the file. The only **mandatory** component is **exchange**. A more      general Data Exchange file also contains *measurement* and      *provenance* information, if so these will be declared in **implements**      as **exchange**:*measurement*:*provenance***exchange_N**    |     | The data taken from measurements or processing. Dimension      descriptors within the group may also serve to describe      “positioner” values involved in a scan. 

*measurement_N*    |     | Description of the sample and instrument as configured for the      measurement. This group is appropriate for relatively static      metadata. For measurements where there are many “positioner”      values (aka a “scan”), it is more sensible to add dimension(s) to      the exchange dataset, and describe the “positioner” values as      dimension scales rather than record the data via multiple matching      *measurement_N* and **exchange_N** groups. This is a judgement left to      the user.

*provenance*    |     | The Provenance group describes all process steps that have been      applied to the data.Exchange========The exchange group is where scientific datasets reside. This groupcontains one or more array datasets containing n-dimensional data andoptional descriptions of the axes (dimension scale datasets). Exactlyhow this group is used is dependent on the application, however thegeneral idea is that one exchange group contains one cohesive dataset.If, for example, the dataset is processed into some other form, thenanother exchange group is used to store the derived data.Multiple exchange groups are numbered consecutively as**exchange_N**. At a minimum, each exchange group should have aprimary dataset named **data**. The *title* is optional.
+---------------+----------------+-----------------------------------------+|     Member    |      Type      |            Example                      |
+===============+================+=========================================+|    *title*    | string dataset |       “absorption_tomography”           |+---------------+----------------+-----------------------------------------+|   **data**    | array dataset  |        n-dimensional dataset            |
+---------------+----------------+-----------------------------------------+Table: Exchange Group Members

*title*    |     | Descriptive *title* for **data** dataset. Current types include:      absorption_tomography, phase_tomography, dpc_tomography **data**    |     | The primary scientific dataset. Additional related datasets may      have any arbitrary name. Each dataset should have a units and      description attribute. Discussion of dimension descriptors and      optional axes attribute is covered in Section [sec:multidims].+---------------+------------------------+------------------------+|    Member     |      Type              |    Example             |
+===============+========================+========================+|  description  |   string attribute     | “transmission”         |
+---------------+------------------------+------------------------+|     units     |   string attribute     |      *counts*          |+---------------+------------------------+------------------------+Table: data attributesMultidimensional dataset~~~~~~~~~~~~~~~~~~~~~~~~A multidimensional dataset should be described as fully as possible,with units for the dataset as well as dimension descriptors (that alsohave units defined). There are also additional descriptive fieldsavailable such as *title* and description. The order of dimensions in thedataset should put the slowest changing dimension first, and the fastestchanging dimension last.It is strongly encouraged that all datasets have a units attribute. Thestring value for units should preferably be an SI unit, however wellunderstood non-SI units are acceptable, in particular *degree*. Theunits strings should conform to those defined by UDUNITS :cite:`UNIDATA:01`. 
While UDUNITS is a software package, it contains simple XML files 
that describe units strings and acceptable aliases.The axes of a multidimensional dataset are described through the use ofadditional one-dimensional datasets (dimension descriptors), one foreach axis in the main dataset. Take for example a 3-dimensional cube ofimages, with axes of x, y, and z where z represents the angle of thesample when each image was taken. There should be 3 additionalone-dimensional datasets called x, y, and z where x and y contain aninteger sequence, and z contains a list of angles. X and y have units of*counts* and z has units of *degree*. To simplify, it is acceptable toomit x and y, since the default interpretation will always be an integersequence.The dimension descriptors (x, y, z) can be associated with the maindataset through two mechanisms. The HDF5 libraries contain a functioncall to *attach* a dimension descriptor dataset to a given dimension ofthe main dataset. HDF5 takes care of entering several attributes in thefile that serve to keep track of this association. If the particularprogramming language you work in does not support this HDF5 function,then you can instead add a string attribute to your main dataset calledaxes. The axes attribute is simply a colon separated string naming thedimension descriptor datasets in order, so *z:y:x* in this case.Measurement===========This group holds sample and instrument information. These groups aredesigned to hold relatively static data about the sample and instrumentconfiguration at the time of the measurement. Rapidly changing*positioner* values (aka scan) are better represented in the exchangegroup dataset.There is a geometry group common to many of the subgroups undermeasurement. The intent is to describe the translation and rotation(orientation) of the sample or instrument component relative to somecoordinate system. Since we believe it is not possible to determine allpossible uses at this time, we leave the precise definition of geometryup to the technique. We do encourage the use of separate translation andorientation subgroups within geometry. As such, we do not describegeometry further here.+---------------+----------------------+------------------------+|    Member     |      Type            |     Example            |
+===============+======================+========================+|   instrument  |      group           |                        |+---------------+----------------------+------------------------+|    sample     |      group           |                        |
+---------------+----------------------+------------------------+|  description  |   string attribute   | "Tomography of a rock” |
+---------------+----------------------+------------------------+Table: Measurement Group Members

instrument    |     | The instrument used to collect this data.

sample    |     | The sample measured.

description    |     | Measurement description.
Instrument~~~~~~~~~~The instrument group stores all relevant beamline components status atthe beginning of a measurement. While all these fields are optional, ifyou do intend to include them they should appear within this parentageof groups.

+---------------------------------------------+-------------------------+-------------------------+|                    Member                   |           Type          |         Example         |
+=============================================+=========================+=========================+
|                   name                      |       string dataset    | "XSD/2-BM"              |+---------------------------------------------+-------------------------+-------------------------+|                   source_                   |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   shutter_N_                |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   attenuator_N_             |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   monochromator_            |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   capacitive_sensors_       |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   amplifier_                |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   detector_N_               |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+
|                   setup_                    |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+

Table: Instrument

name    |     | Name of the instrument.
source    |     | The source used by the instrument.
shutter_N    |     | The shutter(s) used by the instrument.
attenuator    |     | The attenuators that are part of the instrument.
monochromator    |     | The monochromator used by the instrument.
capacitive_sensor    |     | The capacitive_sensors used to monitor for example the sample      position during data collection.
amplifier    |     | The amplifier used by the instrument.
detector_N    |     | The detectors that compose the instrument.
.. _setup:

.. _source:

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
+==============================================+==================================+==================================+|    sample_x                                  |      float                       |      -10.107                     |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_y                                  |      float                       |       -17.900                    |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_z                                  |      float                       |      -5.950                      |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_xx                                 |      float                       |      -1.559                      |+----------------------------------------------+----------------------------------+----------------------------------+|    sample_zz                                 |      float                       |      1.307                       |+----------------------------------------------+----------------------------------+----------------------------------+Table: Setup Group Members

Source^^^^^^Class describing the light source being used.
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

.. _shutter_N:

Shutter^^^^^^^
Class describing the shutter being used.+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
|       name         |     string dataset      |     “Front End Shutter 1      |+--------------------+-------------------------+-------------------------------+|      status        |     string dataset      |     “OPEN”                    |+--------------------+-------------------------+-------------------------------+|       geometry_    |        group            |                               |+--------------------+-------------------------+-------------------------------+
|       setup_       |        group            |                               |+--------------------+-------------------------+-------------------------------+
Table: Shutter Group Members

name
    |     | Shutter name.status
    |     | “OPEN” or “CLOSED”

.. _attenuator_N:
Attenuator^^^^^^^^^^This class describes the beamline attenuator(s) used during datacollection. If more than one attenuators are used they will be named asattenuator_1, attenuator_2 etc.

+---------------------------+-------------------------+-------------------------------+|      Member               |           Type          |         Example               |
+===========================+=========================+===============================+
| thickness                 |     float dataset       |     1e-3                      |+---------------------------+-------------------------+-------------------------------+| attenuator_transmission   |     float dataset       |     unit-less                 |+---------------------------+-------------------------+-------------------------------+| type                      |     string dataset      |     “Al”                      |+---------------------------+-------------------------+-------------------------------+| geometry_                 |     group               |                               |+---------------------------+-------------------------+-------------------------------+| setup_                    |     group               |                               |+---------------------------+-------------------------+-------------------------------+Table: Attenuator Group Members


thickness     |     | Thickness of attenuator along beam direction.
attenuator_transmission    |     | The nominal amount of the beam that gets through (transmitted      intensity)/(incident intensity).
type    |     | Type or composition of attenuator.

.. _monochromator:
Monochromator^^^^^^^^^^^^^
Define the monochromator used in the instrument.+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
| type               |     string dataset      |     “Multilayer”              |+--------------------+-------------------------+-------------------------------+| energy             |     float dataset       |     1.602e-15                 |+--------------------+-------------------------+-------------------------------+| energy_error       |     float dataset       |     1.602e-17                 |+--------------------+-------------------------+-------------------------------+| mono_stripe        |     string dataset      |     “Ru/C”                    |+--------------------+-------------------------+-------------------------------+| geometry_          |     group               |                               |+--------------------+-------------------------+-------------------------------+| setup_             |     group               |                               |+--------------------+-------------------------+-------------------------------+Table: Monochromator Group Members

type    |     | Multilayer type.
energy    |     | Peak of the spectrum that the monochromator selects. Since units      is not defined this field is in J and corresponds to 10 keV.
energy_error    |     | Standard deviation of the spectrum that the monochromator selects.      Since units is not defined this field is in J.
mono_stripe    |     | Type of multilayer coating or crystal.
.. _capacitive_sensors:

Capacitive Sensors^^^^^^^^^^^^^^^^^^Define the capacitive sensors used in the instrument.+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
| name               |     string dataset      |     “Capacitive Sensors”      |+--------------------+-------------------------+-------------------------------+| gain               |     float dataset       |     1.602e-15                 |+--------------------+-------------------------+-------------------------------+| shift_x            |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+| shift_y            |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+| shift_z            |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+
| geometry_          |     group               |                               |+--------------------+-------------------------+-------------------------------+
| setup_             |     group               |                               |+--------------------+-------------------------+-------------------------------+
Table: Capacitive Sensors Group Membersname
    |     | Capacitive Sensors name.

gain    |     | Capacitive Sensors gain in V/m.
    
shift_x, shift_y, shift_z    |     | vectors containing for each scan point the position monitored by      the capacitive sensor... _amplifier:

Amplifier^^^^^^^^^Define the aplifier used in the instrument.

+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
| name               |     string dataset      |     “Amplifier”               |+--------------------+-------------------------+-------------------------------+| gain               |     float dataset       |     1.602e-15                 |+--------------------+-------------------------+-------------------------------+| current            |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+
| setup_             |     float dataset       |     vector of float           |+--------------------+-------------------------+-------------------------------+
Table: Amplifier Group Members


name    |     | Amplifier name.
    
gain    |     | Amplifier gain.
    
current    |     | vectors containing for each scan point the current recorded by the amplifier.

.. _detector_N:
Detector^^^^^^^^This class holds information about the detector used during theexperiment. If more than one detector are used they will be all listedas detector_N.+--------------------+-------------------------+-------------------------------+|      Member        |           Type          |         Example               |
+====================+=========================+===============================+
| manufacturer       |     string dataset      |     “CooKe Corporation”       |+--------------------+-------------------------+-------------------------------+| model              |     string dataset      |     “pco dimax”               |+--------------------+-------------------------+-------------------------------+| serial_number      |     string dataset      |     “1234XW2”                 |+--------------------+-------------------------+-------------------------------+|   geometry_        |          group          |                               |+--------------------+-------------------------+-------------------------------+|   setup_           |          group          |                               |+--------------------+-------------------------+-------------------------------+| output_data        |     string dataset      |     “/exchange”               |+--------------------+-------------------------+-------------------------------+

Table: Detector Group Members

manufacturer    |
    | The detector manufacturer.

model    |    | The detector model.

serial_number    |
    | The detector serial number.output_data
    |    | String HDF5 path to the exchange group where the detector output data is located.

Sample~~~~~~This group holds basic information about the sample, its geometry,properties, the sample owner (user) and sample proposal information.While all these fields are optional, if you do intend to include themthey should appear within this parentage of groups.

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
Experiment^^^^^^^^^^This provides references to facility ids for the proposal, scheduledactivity, and safety form.+---------------+-------------------------+----------------------+|   Member      |            Type         |       Example        | +===============+=========================+======================+
| proposal      |     string dataset      |        “1234”        |+---------------+-------------------------+----------------------+| activity      |     string dataset      |        “9876”        |+---------------+-------------------------+----------------------+| safety        |     string dataset      |        “9876”        |+---------------+-------------------------+----------------------+Table: Experiment Group Members

proposal    |     | Proposal reference number. For the APS this is the General User    | Proposal number.
      
activity    |     | Proposal scheduler id. For the APS this is the beamline scheduler      activity id.

safety    |     | Safety reference document. For the APS this is the Experiment    | Safety Approval Form number.Experimenter^^^^^^^^^^^^Description of a single experimenter. Multiple experimenters can berepresented through numbered entries such as experimenter_1,experimenter_2.+--------------------+-------------------------+--------------------------------------------+|      Member        |           Type          |         Example                            |
+====================+=========================+============================================+
|       name         |     string dataset      |     “John Doe”                             |+--------------------+-------------------------+--------------------------------------------+|       role         |     string dataset      |     “Project PI”                           |+--------------------+-------------------------+--------------------------------------------+|    affiliation     |     string dataset      |     “University of California, Berkeley”   |+--------------------+-------------------------+--------------------------------------------+|      address       |     string dataset      |     “EPS UC Berkeley CA 94720 4767 USA”    |+--------------------+-------------------------+--------------------------------------------+|       phone        |     string dataset      |     “+1 123 456 0000”                      |+--------------------+-------------------------+--------------------------------------------+|       email        |     string dataset      |     “johndoe@berkeley.edu”                 |+--------------------+-------------------------+--------------------------------------------+| facility_user_id   |     string dataset      |     “a123456”                              |+--------------------+-------------------------+--------------------------------------------+Table: Experimenter Group Members    name: User name.    role: User role.    affiliation: User affiliation.    address: User address.    phoen: User phone number.    email: User e-mail address    facility_user_id: User badge number


.. _geometry:

Geometry^^^^^^^^

This class holds the general position and orientation of a component. Wedo not define this further here.

+---------------+------------------------+------------------------+|    Member     |      Type              |    Example             |
+===============+========================+========================+|  translation  |     group              |                        |+---------------+------------------------+------------------------+|  orientation  |     group              |                        |
+---------------+------------------------+------------------------+translation    |     | The position of the object with respect to the origin of your      coordinate system.orientation    |     | The rotation of the object with respect to your coordinate system.Provenance----------Data provenance is the documentation of all transformations, analysesand interpretations of data performed by a sequence of process functionsor actorts.Maintaining this history allows for reproducible data. The Data Exchangeformat tracks provenance by allowing each actor to append provenanceinformation to a process table. The provenance process table tracks theexecution order of a series of processes by appending sequential entriesin the process table.Scientific users will not generally be expected to maintain data in thisgroup. The expectation is that analysis pipeline tools willautomatically record process steps using this group. In addition, it ispossible to re-run an analysis using the information provided here.+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+|   actor   |    start_time     |    end_time       |     status    |     message          |          reference       |     description                     |+===========+===================+===================+===============+======================+==========================+=====================================+
| gridftp   |     21:15:22      |     21:15:23      |     FAILED    |     auth. error      |     /provenance/griftp   |     transfer detector to cluster    |+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| gridftp   |     21:15:26      |     21:15:27      |     FAILED    |     auth. error      |     /provenance/griftp   |     transfer detector to cluster    |   +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| gridftp   |     21:17:28      |     22:15:22      |     SUCCESS   |         OK           |     /provenance/griftp   |     transfer detector to cluster    |    +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| norm      |     22:15:23      |     22:30:22      |     SUCCESS   |         OK           |     /provenance/norm     |     normalize the raw data          |+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| rec       |     22:30:23      |     22:50:22      |     SUCCESS   |         OK           |     /provenance/rec      |     reconstruct the norm. data      |  +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| convert   |     22:50:23      |                   |     RUNNING   |         OK           |     /provenance/export   |     convert reconstructed data      |  +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| gridftp   |                   |       QUEUED      |               |                      |     /provenance/griftp_2 |     transfer data to user           | +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+Table: Process table to log actors activity

actor    |     | Name of the process in the pipeline stage that is executed at this      step.*start_time*    |     | Time the process started.*end_time*    |     | TIme the process ended.*status*    |     | Current process status. May be one of the following: QUEUED,      RUNNING, FAILED, or SUCCESS.*message*    |     | A process specific message generated by the process. It may be a      confirmation that the process was successful, or a detailed error      message, for example.*reference*    |     | Path to a process description group. The process description group      contains all metadata to perform the specific process. This      reference is simply the HDF5 path within this file of the      technique specific process description group. The process      description group should contain all parameters necessary to run      the process, including the name and version of any external      analysis tool used to process the data. It should also contain      input and output references that point to the      **exchange_N** groups that contain the input and output      datasets of the process.*description*    |     | Process description.
