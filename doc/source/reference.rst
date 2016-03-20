.. role:: math(raw)   :format: html latex..

==============Core Reference==============Top level (root)================This node represents the top level of the HDF5 file and holds somegeneral information about the file.+---------------+----------------+-----------------------------------------+|    Member     |      Type      |              Example                    |
+===============+================+=========================================+|**implements** | string dataset | **exchange**:*measurement*:*provenance* |+---------------+----------------+-----------------------------------------+|**exchange**   |    group       |                                         |
+---------------+----------------+-----------------------------------------+|*measurement*  |    group       |                                         |+---------------+----------------+-----------------------------------------+| *provenance*  |    group       |                                         |+---------------+----------------+-----------------------------------------+implements    |     | A colon separated list that shows which components are present in      the file. The only **mandatory** component is **exchange**. A more      general Data Exchange file also contains *measurement* and      *provenance* information, if so these will be declared in **implements**      as **exchange**:*measurement*:*provenance*exchange or exchange_N
    |     | The data taken from measurements or processing. Dimension      descriptors within the group may also serve to describe      “positioner” values involved in a scan. 

measurement or measurement_N    |     | Description of the sample and instrument as configured for the      measurement. This group is appropriate for relatively static      metadata. For measurements where there are many “positioner”      values (aka a “scan”), it is more sensible to add dimension(s) to      the exchange dataset, and describe the “positioner” values as      dimension scales rather than record the data via multiple matching      *measurement* and **exchange** groups. This is a judgement left to      the user.

provenance    |     | The Provenance group describes all process steps that have been      applied to the data.**exchange**============The exchange group is where scientific datasets reside. This groupcontains one or more array datasets containing n-dimensional data andoptional descriptions of the axes (dimension scale datasets). Exactlyhow this group is used is dependent on the application, however thegeneral idea is that one exchange group contains one cohesive dataset.If, for example, the dataset is processed into some other form, thenanother exchange group is used to store the derived data.Multiple exchange groups are numbered consecutively as**exchange_N**. At a minimum, each exchange group should have aprimary dataset named **data**. The *title* is optional.
+---------------+----------------+-----------------------------------------+|     Member    |      Type      |            Example                      |
+===============+================+=========================================+|    *title*    | string dataset |       “absorption_tomography”           |+---------------+----------------+-----------------------------------------+|   **data**    | array dataset  |        n-dimensional dataset            |
+---------------+----------------+-----------------------------------------+Table: Exchange Group Members

title    |     | Descriptive *title* for **data** dataset. Current types include:      absorption_tomography, phase_tomography, dpc_tomography data    |     | The primary scientific dataset. Additional related datasets may      have any arbitrary name. Each dataset should have a units and      description attribute. Discussion of dimension descriptors and      optional axes attribute is covered in Section [sec:multidims].Attribute
---------

Description and units can be added as attribute to any data, both array or values,
inside a data exchange file. If units is omitted default is SI.
+---------------+------------------------+------------------------+|    Member     |      Type              |    Example             |
+===============+========================+========================+| *description* |   string attribute     | “transmission”         |
+---------------+------------------------+------------------------+|    *units*    |   string attribute     |      *counts*          |+---------------+------------------------+------------------------+Table: data attributes*measurement*=============This group holds sample and instrument information. These groups aredesigned to hold relatively static data about the sample and instrumentconfiguration at the time of the measurement. Rapidly changing*positioner* values (aka scan) are better represented in the exchangegroup dataset.+---------------+----------------------+------------------------+|    Member     |      Type            |     Example            |
+===============+======================+========================+|   instrument_ |      group           |                        |+---------------+----------------------+------------------------+|    sample_    |      group           |                        |
+---------------+----------------------+------------------------+Table: Measurement Group Members

instrument    |     | The instrument used to collect this data.

sample    |     | The sample measured.

.. _instrument:

*instrument*------------The instrument group stores all relevant beamline components status atthe beginning of a measurement. While all these fields are optional, ifyou do intend to include them they should appear within this parentageof groups.

+---------------------------------------------+-------------------------+-------------------------+|                    Member                   |           Type          |         Example         |
+=============================================+=========================+=========================+
|                   *name*                    |       string dataset    | "XSD/2-BM"              |+---------------------------------------------+-------------------------+-------------------------+|                   component_1_              |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                  *component_2*              |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                  *component_n*              |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+|                   setup_                    |          group          |                         |+---------------------------------------------+-------------------------+-------------------------+

Table: Instrument

name    |     | Name of the instrument.

component    |     | List of components part of the instrument. Replace *component* with the actual item name, *source*, *mirror*, etc.

detector    |     | The detectors that compose the instrument.

.. _component_1:

*component*~~~~~~~~~~~Class describing the component being used. 
+-----------------------------+--------------------------------+---------------------------+| Member                      |     Type                       |     Example               |+=============================+================================+===========================+
| *name*                      |     string dataset             |     “APS”                 |+-----------------------------+--------------------------------+---------------------------+| *description*               |     string dataset             |     “APS”                 |+-----------------------------+--------------------------------+---------------------------+| *arbitrary_label_1*         |     string dataset             |     “what ever”           |+-----------------------------+--------------------------------+---------------------------+| *arbitrary_label_2*         |     string dataset             |     “what ever”           |+-----------------------------+--------------------------------+---------------------------+| *arbitrary_label_n*         |     string dataset             |     “what ever”           |+-----------------------------+--------------------------------+---------------------------+| setup_                      |     group                      |                           |+-----------------------------+--------------------------------+---------------------------+| geometry_                   |     group                      |                           |+-----------------------------+--------------------------------+---------------------------+Table: Component Description

name    |     | Name.
    
arbitrary_label(s)    |     | Date and time source was measured.
    

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
+----------------------------------------------+----------------------------------+----------------------------------+|     Member                                   |      Type                        |            Example               |
+==============================================+==================================+==================================+|    *positioner_x*                            |      float                       |      -10.107                     |+----------------------------------------------+----------------------------------+----------------------------------+|    *positioner_y*                            |      float                       |       -17.900                    |+----------------------------------------------+----------------------------------+----------------------------------+|    *positioner_z*                            |      float                       |      -5.950                      |+----------------------------------------------+----------------------------------+----------------------------------+Table: Setup Group Members


.. _geometry:

*geometry*^^^^^^^^^^

The geometry group is common to many of the subgroups undermeasurement. The intent is to describe the translation and rotation(orientation) of the sample or instrument component relative to somecoordinate system. Since we believe it is not possible to determine allpossible uses at this time, we leave the precise definition of geometryup to the technique. We do encourage the use of separate translation andorientation subgroups within geometry. As such, we do not describegeometry further here. This class holds the general position and 
orientation of a component. 

+---------------+------------------------+------------------------+|    Member     |      Type              |    Example             |
+===============+========================+========================+| *translation* |     group              |                        |+---------------+------------------------+------------------------+| *orientation* |     group              |                        |
+---------------+------------------------+------------------------+translation    |     | The position of the object with respect to the origin of your      coordinate system.orientation    |     | The rotation of the object with respect to your coordinate system.

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


.. _sample:

*sample*--------This group holds basic information about the sample, its geometry,properties, the sample owner (user) and sample proposal information.While all these fields are optional, if you do intend to include themthey should appear within this parentage of groups.


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
*experiment*~~~~~~~~~~~~This provides references to facility ids for the proposal, scheduledactivity, and safety form.+---------------+-------------------------+----------------------+|   Member      |            Type         |       Example        | +===============+=========================+======================+
| *proposal*    |     string dataset      |        “1234”        |+---------------+-------------------------+----------------------+| *activity*    |     string dataset      |        “9876”        |+---------------+-------------------------+----------------------+| *safety*      |     string dataset      |        “9876”        |+---------------+-------------------------+----------------------+Table: Experiment Group Members

proposal    |     | Proposal reference number. For the APS this is the General User    | Proposal number.
      
activity    |     | Proposal scheduler id. For the APS this is the beamline scheduler      activity id.

safety    |     | Safety reference document. For the APS this is the Experiment    | Safety Approval Form number.*experimenter*~~~~~~~~~~~~~~Description of a single experimenter. Multiple experimenters can berepresented through numbered entries such as experimenter_1,experimenter_2.+--------------------+-------------------------+--------------------------------------------+|      Member        |           Type          |         Example                            |
+====================+=========================+============================================+
|       *name*       |     string dataset      |     “John Doe”                             |+--------------------+-------------------------+--------------------------------------------+|       *role*       |     string dataset      |     “Project PI”                           |+--------------------+-------------------------+--------------------------------------------+|    *affiliation*   |     string dataset      |     “University of California, Berkeley”   |+--------------------+-------------------------+--------------------------------------------+|      *address*     |     string dataset      |     “EPS UC Berkeley CA 94720 4767 USA”    |+--------------------+-------------------------+--------------------------------------------+|       *phone*      |     string dataset      |     “+1 123 456 0000”                      |+--------------------+-------------------------+--------------------------------------------+|       *email*      |     string dataset      |     “johndoe@berkeley.edu”                 |+--------------------+-------------------------+--------------------------------------------+| *facility_user_id* |     string dataset      |     “a123456”                              |+--------------------+-------------------------+--------------------------------------------+Table: Experimenter Group Members    name: User name.    role: User role.    affiliation: User affiliation.    address: User address.    phoen: User phone number.    email: User e-mail address    facility_user_id: User badge number

*provenance*
============

Data provenance is the documentation of the data collection strategy
(*acquisition*) and all transformations, analyses and interpretations 
of data performed by a sequence of process functions (*actor*).

Maintaining this history allows for reproducible data. The Data Exchange
format tracks provenance by allowing each actor to append provenance
information to a process table. The provenance process table tracks the
execution order of a series of processes by appending sequential actor 
entries in the process table.

+-------------------------------------+------------------------------------+-----------------------------+
|     Member                          |                 Type               |          Example            |
+=====================================+====================================+=============================+
|     *name*                          |     string dataset                 |            "name"           |    
+-------------------------------------+------------------------------------+-----------------------------+
|    *description*                    |     string dataset                 |           "optional"        |   
+-------------------------------------+------------------------------------+-----------------------------+
|     actor_1_                        |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
|    *actor_2*                        |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
|    *actor_n*                        |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
|    table_                           |         group                      |                             |    
+-------------------------------------+------------------------------------+-----------------------------+
Table: Provenance Group Members

name    |     | Descriptive provenance task.

description    |     | Description of the provenance task.
    
.. _actor_1:

*actor*
-------

This is the actor description group. Each entry of the process table_ will refer to the correspondent 
actor description.


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
|       set-up_                       |        group                       |                                             |
+-------------------------------------+------------------------------------+---------------------------------------------+


Table: Actor Group Members

name    |     | Descriptive actor task.

description    |     | Description of the actor task.
    
version    |     | Version of the actor task.
    |     | If available this can be the repository link to the actor version used
    | https://github.com/tomopy_scripts/b9ad87e17
input_data, output_data
    |     | Origin and destination of the data processed by the actor.

.. _set-up:


setup (actor)
~~~~~~~~~~~~~

Here is where to log the actor setup parameters (static setup values). 

+----------------------------------------------+------------------------------------+-----------------------------------------------+
|     Member                                   |      Type                          |            Example                            |
+==============================================+====================================+===============================================+
|    *parameter_name_1*                        |      float                         |      0.0                                      |
+----------------------------------------------+------------------------------------+-----------------------------------------------+
|    *parameter_name_2*                        |      string dataset                |      "Parzen"                                 |
+----------------------------------------------+------------------------------------+-----------------------------------------------+
|    *parameter_name_n*                        |      float                         |      2.0                                      |
+----------------------------------------------+------------------------------------+-----------------------------------------------+
|    *module__name_1*                          |     string dataset                 | https://github.com/astra/b9ad87e17            |
+----------------------------------------------+------------------------------------+-----------------------------------------------+
|    *module_name_2*                           |     string dataset                 | https://github.com/tomopy/c9ad87e77           |
+----------------------------------------------+------------------------------------+-----------------------------------------------+

Table: Actor Setup Group

.. table:

*table*
-------

Scientific users will not generally be expected to maintain data in this
group. The expectation is that the data collection and analysis pipeline 
tools will automatically record process steps using this group. 
In addition, it is possible to re-run an analysis using the information 
provided here.
+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+|   actor   |    start_time     |    end_time       |     status    |     message          |          reference       |     description                     |+===========+===================+===================+===============+======================+==========================+=====================================+
| actor_1   |     21:15:22      |     21:15:23      |     SUCCESS   |         OK           |     /provenance/actor_1  |     raw data collection             |+-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| actor_2   |     21:15:26      |     21:15:27      |     RUNNING   |         OK           |     /provenance/actor_2  |     reconstruct                     |   +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+| actor_n   |     21:17:28      |     22:15:22      |     QUEUED    |         OK           |     /provenance/actor_n  |     transfer data to user           |    +-----------+-------------------+-------------------+---------------+----------------------+--------------------------+-------------------------------------+Table: Process table to log actors activity

actor    |     | Name of the process in the pipeline stage that is executed at this step.*start_time*    |     | Time the process started.*end_time*    |     | TIme the process ended.*status*    |     | Current process status. May be one of the following: QUEUED,    | RUNNING, FAILED, or SUCCESS.*message*    |     | A process specific message generated by the process. It may be a    | confirmation that the process was successful, or a detailed error    | message, for example.*reference*    |     | Path to the actor description group. The process description group    | contains all metadata to perform the specific process. This    | reference is simply the HDF5 path within this file of the    | technique specific process description group. The process    | description group should contain all parameters necessary to run    | the process, including the name and version of any external    | analysis tool used to process the data. It should also contain    | input and output references that point to the    | **exchange_N** groups that contain the input and output    | datasets of the process.*description*    |     | Process description.
