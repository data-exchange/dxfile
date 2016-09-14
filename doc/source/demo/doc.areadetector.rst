Area Detector
=============

At synchrotron facilities using the EPICS :cite:`EPICS:01` software for area detectors :cite:`AD:01` with the
NDFileHDF5 plugin :cite:`AD:02`, is possible to save Data Exchange files by properly configure
the detector and the HDF schema attribute files .  

Here are the templates in use at the  Advanced Photon Source: 

   - Transmission X-Ray Microscope at beamline 32-ID: :download:`txm_hdf_schema.xml <../../../doc/demo/areadetector/32-ID/nct.xml>` and :download:`txm_detector_attribute.xml <../../../doc/demo/areadetector/32-ID/nctDetectorAttributes.xml>` and the generated HDF5 file: `txm.h5 <https://drive.google.com/open?id=0B78bW1AwveI_UmVvcHVTUzVBVXM>`_ . 

   - Micro Tomography Instrument at beamline 32-ID: :download:`mct_hdf_schema.xml <../../../doc/demo/areadetector/32-ID/mct.xml>` and :download:`mct_detector_attribute.xml <../../../doc/demo/areadetector/32-ID/mctDetectorAttributes.xml>`. 

and the data exchange file 
