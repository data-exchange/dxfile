.. role:: math(raw)
============

Root Level Structure

---------------+----------------+-----------------------------------------+
+===============+================+=========================================+
---------------+----------------+-----------------------------------------+
+---------------+----------------+-----------------------------------------+
---------------+----------------+-----------------------------------------+
---------------+----------------+-----------------------------------------+
      the **implements** string would be: **exchange**:*measurement*:*provenance*.

Definitions
===========


All the diagrams in this section follow the color conventions shown in

.. _DiagramColorCode:
   :alt: AExplanation of the color code used in the diagrams
Multidimensional data
While UDUNITS is a software package, it contains simple XML files that 
describe units strings and acceptable aliases.

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

Imaging
The examples in this section show how one can store data for imaging

.. figure:: figures/dx_Minimal1.png
   :alt: Diagram of a minimal Data Exchange file for a single image.
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
