Area Detector
=============

At synchrotron facilities using the EPICS :cite:`EPICS:01` software for area detectors :cite:`AD:01` with the
NDFileHDF5 plugin :cite:`AD:02`, is possible to save Data Exchange files by properly configure
the detector and the HDF schema attribute files .  

Here are the templates in use at the  Advanced Photon Source:


- 2-BM
    - Micro Tomography Instrument: :download:`A_station_hdf_schema.xml <../../../doc/demo/areadetector/2-BM/AlocalPG1Layout.xml>` and :download:`A_station_detector_attributes.xml <../../../doc/demo/areadetector/2-BM/AlocalPG1DetectorAttributes.xml>`
    - Micro Tomography Instrument: :download:`B_station_hdf_schema.xml <../../../doc/demo/areadetector/2-BM/BlocalPG1Layout.xml>` and :download:`B_station_detector_attributes.xml <../../../doc/demo/areadetector/2-BM/BlocalPG1DetectorAttributes.xml>`
    - Dynamic Tomography Instrument: :download:`dyna_hdf_schema.xml <../../../doc/demo/areadetector/2-BM/DynaMCTHDFLayout.xml>` and :download:`dyna_detector_attributes.xml <../../../doc/demo/areadetector/2-BM/DynaMCTDetectorAttributes.xml>`
    
- 32-ID 
    - Transmission X-Ray Microscope: :download:`txm_hdf_schema.xml <../../../doc/demo/areadetector/32-ID/nct.xml>` and :download:`txm_detector_attribute.xml <../../../doc/demo/areadetector/32-ID/nctDetectorAttributes.xml>` and the generated HDF5 file: `txm.h5 <https://drive.google.com/open?id=0B78bW1AwveI_UmVvcHVTUzVBVXM>`_ .
    - Micro Tomography Instrument: :download:`mct_hdf_schema.xml <../../../doc/demo/areadetector/32-ID/mct.xml>` and :download:`mct_detector_attribute.xml <../../../doc/demo/areadetector/32-ID/mctDetectorAttributes.xml>`. 
