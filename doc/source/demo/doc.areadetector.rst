Advanced Photon Source
======================

At synchrotron facilities using the EPICS :cite:`EPICS:01` software for area detectors :cite:`AD:01` with the
NDFileHDF5 plugin :cite:`AD:02`, is possible to save Data Exchange files by properly configure
the detector and the HDF schema attribute files to obtain `txm.h5 <https://drive.google.com/open?id=0B78bW1AwveI_UmVvcHVTUzVBVXM>`_

Here are the templates in use at the  Advanced Photon Source:


- 2-BM
    - Fast Micro Tomography Instrument: :download:`A_station_hdf_schema.xml <../../../doc/demo/areadetector/2-BM/flir2bmaLayout.xml>` and :download:`A_station_detector_attributes.xml <../../../doc/demo/areadetector/2-BM/flir2bmaDetectorAttributes.xml>`
    - Dynamic Tomography Instrument: :download:`dyna_hdf_schema.xml <../../../doc/demo/areadetector/2-BM/PCOLayout.xml>` and :download:`dyna_detector_attributes.xml <../../../doc/demo/areadetector/2-BM/PCODetectorAttributes.xml>`
    - MONA project: :download:`mona_hdf_schema.xml <../../../doc/demo/areadetector/2-BM/monaLayout.xml>` and :download:`mona_detector_attributes.xml <../../../doc/demo/areadetector/2-BM/monaDetectorAttributes.xml>`

- 6-BM
    - Micro Tomography Instrument: :download:`TomoScanLayout.xml <../../../doc/demo/areadetector/6-BM/pg6bmTomoScanLayout.xml>` and :download:`TomoScanDetectorAttributes.xml <../../../doc/demo/areadetector/6-BM/pg6bmTomoScanDetectorAttributes.xml>`

- 7-BM
    - Fast Micro Tomography Instrument: :download:`mct.xml <../../../doc/demo/areadetector/7-BM/mct3.xml>` and :download:`mct_attributes.xml <../../../doc/demo/areadetector/7-BM/mctDetectorAttributes1.xml>`

- 13-BM
    - Micro-tomography system at 13-BM-D using PG cameras: :download:`tomoLayout.xml <../../../doc/demo/areadetector/13-BM/tomoLayout.xml>` and :download:`tomoDetectorAttributes.xml <../../../doc/demo/areadetector/13-BM/tomoDetectorAttributes.xml>`

- 32-ID 
    - Transmission X-Ray Microscope: :download:`txm_hdf_schema.xml <../../../doc/demo/areadetector/32-ID/nct.xml>` and :download:`txm_detector_attribute.xml <../../../doc/demo/areadetector/32-ID/nctDetectorAttributes.xml>` and the generated HDF5 file: `txm.h5 <https://drive.google.com/open?id=0B78bW1AwveI_UmVvcHVTUzVBVXM>`_ .
    - Micro Tomography Instrument: :download:`mct_hdf_schema.xml <../../../doc/demo/areadetector/32-ID/mct.xml>` and :download:`mct_detector_attribute.xml <../../../doc/demo/areadetector/32-ID/mctDetectorAttributes.xml>`. 


XML
---

To check that the areadetector attributes and layout XML contain a set of matching names run:

::

   $ bash
   usertxm@txmtwo$ grep -oP 'name=\"\K[^\"]+' TomoScanDetectorAttributes.xml | while read -r line ; do echo -n "$line " ; grep -q "$line" TomoScanLayout.xml && echo true || echo false ; done | grep false
   usertxm@txmtwo$ grep -oP 'ndattribute=\"\K[^\"]+' TomoScanLayout.xml | while read -r line; do echo -n "$line "; grep -q "$line" TomoScanDetectorAttributes.xml && echo true || echo false ; done |grep false
