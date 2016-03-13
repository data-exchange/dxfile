# -*- coding: utf-8 -*-
"""
.. module:: demo.py
   :platform: Unix
   :synopsis: Generate test files in data exchange.

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15
"""

import dxfile.dxtomo as dx
import numpy as np
import datetime
import os
import time 
def main():

    fname = './demo.h5'

    experimenter_name="Francesco De Carlo"
    experimenter_affiliation="Argonne National Laboratory" 
    experimenter_email="decarlo@aps.anl.gov"
    instrument_comment="32-ID TXM"  
    sample_name = 'sample_name'

    size  = 180

    theta = range(0, 180, 180/size)
    

    if (fname != None):
        if os.path.isfile(fname):
            print "Data Exchange file already exists: ", fname
        else:
            # Create new folder.
            dirPath = os.path.dirname(fname)
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            # Open DataExchange file
            f = dx.File(fname, mode='w') 

            # Write the Data Exchange HDF5 file.
            f.add_entry(dx.Entry.experimenter(name={'value':experimenter_name}))
            f.add_entry(dx.Entry.experimenter(affiliation={'value':experimenter_affiliation}))
            f.add_entry(dx.Entry.experimenter(email={'value':experimenter_email}))
            f.add_entry(dx.Entry.instrument(comment={'value': instrument_comment}))
            f.add_entry(dx.Entry.sample( name={'value':sample_name}))

            f.add_entry(dx.Entry.data(theta={'value': theta, 'units':'degrees'}))

            f.close()
 
    else:
           print "Nothing to do ..."

if __name__ == "__main__":
    main()

