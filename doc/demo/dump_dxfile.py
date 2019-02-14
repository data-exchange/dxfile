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
import dxchange.reader as dxreader


def dump_hdf5_file_structure(file_name) :
    """Prints the HDF5 file structure"""
    filee = h5py.File(file_name, 'r') # open read-only
    item = filee #["/Configure:0000/Run:0000"]
    dump_hdf5_item_structure(item, file_name)
    filee.close()
 
def dump_hdf5_item_structure(g, file_name, offset='    ') :
    """Prints the input file/group/dataset (g) name and begin iterations on its content"""

    if   isinstance(g, h5py.File) :
        print (g.file, 'File:', g.name)
 
    elif isinstance(g, h5py.Dataset) :
        #print ('Dataset: ', g.name) #, g.dtype
        if g.name == '/exchange/theta':
            print('theta array')
        elif g.name == '/exchange/data':
            print('data array')
        elif g.name == '/exchange/data_white':
            print('data white')
        elif g.name == '/exchange/data_dark' :
            print('data dark')
        else:
            print (g.name, '=', dxreader.read_hdf5(file_name,  g.name))
 
    elif isinstance(g, h5py.Group) :
        print ('Group:', g.name)
 
    else :
        print ('WORNING: UNKNOWN ITEM IN HDF5 FILE', g.name)
        sys.exit ( "EXECUTION IS TERMINATED" )
 
    if isinstance(g, h5py.File) or isinstance(g, h5py.Group) :
        # for key,val in dict(g).iteritems() :
        for key,val in dict(g).items() :
            subg = val
            #print (offset, key )#,"   ", subg.name #, val, subg.len(), type(subg),
            dump_hdf5_item_structure(subg, file_name, offset + '    ')
 

def main(arg):

    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="DataExchange file name: /data/sample.h5")
    parser.add_argument("--tiff",action="store_true", help="Convert HDF5 to a stack of tiff files")

    args = parser.parse_args()

    # Set path to the micro-CT data to reconstruct.
    fname = args.fname
    tiff = args.tiff
    if os.path.isfile(fname): 
        dump_hdf5_file_structure(fname)
        if tiff:   
            # Read APS 32-BM raw data.
            print("Reading HDF5 file: ", fname)
            proj, flat, dark, theta = dxchange.read_aps_32id(fname)
            print("Converting ....")
            top_out = os.path.join(os.path.dirname(fname), os.path.splitext(os.path.basename(fname))[0])
            flats_out = os.path.join(top_out, "flats", "image")
            darks_out = os.path.join(top_out, "darks", "image")
            radios_out = os.path.join(top_out, "radios", "image")
            print("flats: ", flat.shape)
            dxchange.write_tiff_stack(flat, fname=flats_out)
            print("darks: ", dark.shape)
            dxchange.write_tiff_stack(dark, fname=darks_out)
            print("projections: ", proj.shape)
            dxchange.write_tiff_stack(proj, fname=radios_out)
            print ("Converted data: ", top_out)
            print ("Done!")

if __name__ == "__main__":
    main(sys.argv[1:])
