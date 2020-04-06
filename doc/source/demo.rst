========
Examples
========

Tomographic data files
======================

For a repository of experimental and simulated data sets using the
the Data Exchange file format (`DXfile <http://dxfile.readthedocs.org/>`_) 
:cite:`DeCarlo:14a`, please check 
`TomoBank <http://tomobank.readthedocs.io/>`_ :cite:`DeCarlo:17`.

For reading tomography files formatted in different ways, please 
go check the `DXchange <http://dxchange.readthedocs.io>`_ package. There
are various examples and demonstration scripts about how to load your datasets. 

Area Detector
=============

At synchrotron facilities using the EPICS :cite:`EPICS:01` software for area 
detectors :cite:`AD:01` with the NDFileHDF5 plugin :cite:`AD:02`, is possible 
to directly save `DXfile <http://dxfile.readthedocs.org/>`_ by properly configure 
the detector and the HDF schema attribute files. Below are examples on how 
this has been implemented at various facilities.

.. toctree::

   demo/doc.areadetector

Python
======

This section contains python code examples on how to generate and access the meta-data
of a `DXfile <http://dxfile.readthedocs.org/>`_.

.. toctree::

   demo/doc.python

