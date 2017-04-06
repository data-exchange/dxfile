#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: dump_dxfile.py
   :platform: Unix
   :synopsis: Print an hdf5 file Group/Data dataset list.

"""

from __future__ import print_function

import h5py
import dxchange.reader as dxreader


def print_hdf5_file_structure(file_name) :
    """Prints the HDF5 file structure"""
    filee = h5py.File(file_name, 'r') # open read-only
    item = filee #["/Configure:0000/Run:0000"]
    print_hdf5_item_structure(item)
    filee.close()
 
def print_hdf5_item_structure(g, offset='    ') :
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
            print (g.name, '=', dxreader.read_hdf5(fname,  g.name))
 
    elif isinstance(g, h5py.Group) :
        print ('Group:', g.name)
 
    else :
        print ('WORNING: UNKNOWN ITEM IN HDF5 FILE', g.name)
        sys.exit ( "EXECUTION IS TERMINATED" )
 
    if isinstance(g, h5py.File) or isinstance(g, h5py.Group) :
        for key,val in dict(g).iteritems() :
            subg = val
            #print (offset, key )#,"   ", subg.name #, val, subg.len(), type(subg),
            print_hdf5_item_structure(subg, offset + '    ')
 
if __name__ == "__main__" :
        
    # Set path to the micro-CT data.
    fname = '/tomobank/tomo_00001/tomo_00001.h5'
    print_hdf5_file_structure(fname)

