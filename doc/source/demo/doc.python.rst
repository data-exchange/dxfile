Python
======

This section contains links to python code examples to generate a :download:`simple.py <../../../doc/demo/simple.py>`
and a :download:`full.py <../../../doc/demo/full.py>` data-exchange file using the DXfile class.

We also provide a  :download:`dump_dxfile.py <../../../doc/demo/dump_dxfile.py>` to print the list of Groups/Datasets names 
and values contained in an hdf file. Using > is possible to save this script output to a text file. The script has also an
option to convert the HDF5 file into a stack of tiff files.

Usage: ::

	python dump_dxfile.py -h
	usage: dump_dxfile.py [-h] [--tiff] fname

	
	positional arguments:
  		fname       DataExchange file name: /data/sample.h5

	optional arguments:
  		-h, --help  	show this help message and exit
  		--tiff      	Convert HDF5 to a stack of tiff files

Example: ::

	python dump_dxfile.py /tomobank/tomo_00001.h5 > experiment_log.txt
	python dump_dxfile.py /tomobank/tomo_00001.h5 --tiff




