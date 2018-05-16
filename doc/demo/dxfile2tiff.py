#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: dump_dxfile.py
   :platform: Unix
   :synopsis: Print an hdf5 file Group/Data dataset list.

"""

from __future__ import print_function

import os
import h5py
import sys
import argparse
import dxchange



def main(arg):

    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="DataExchange file name: /data/sample.h5")
    parser.add_argument("--logfile",action="store_true")

    args = parser.parse_args()

    # Set path to the micro-CT data to reconstruct.
    fname = args.fname
    print("logFile:", args.logfile)
    
    if os.path.isfile(fname): 
        print(fname)   
        # Read APS 32-BM raw data.
        proj, flat, dark, theta = dxchange.read_aps_32id(fname)

        print(proj.shape)
        top_out = os.path.join(os.path.dirname(fname), os.path.splitext(os.path.basename(fname))[0])
        flats_out = os.path.join(top_out, "flats", "image") + "image"
        darks_out = os.path.join(top_out, "darks", "image") + "image"
        radios_out = os.path.join(top_out, "radios", "image") + "image"
        print (top_out)
        dxchange.write_tiff_stack(flat, fname=flats_out)
        #dxchange.write_tiff_stack(dark, fname=darks_out)
        #dxchange.write_tiff_stack(proj, fname=radios_out)

if __name__ == "__main__":
    main(sys.argv[1:])
