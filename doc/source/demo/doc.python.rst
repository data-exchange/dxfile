Utility
=======

This section contains links to python code examples to generate a :download:`simple.py <../../../doc/demo/simple.py>`
and a :download:`full.py <../../../doc/demo/full.py>` data-exchange file using the DXfile class.

:download:`dump_dxfile.py <../../../doc/demo/dump_dxfile.py>` allows to print the list of Groups/Datasets names 
and values contained in a DataExchange hdf file. Using > is possible to save this script output to a text file. 
The script has also an option to convert a DataExchange file into a stack of tiff files.

Usage: ::

	python dump_dxfile.py -h
	usage: dump_dxfile.py [-h] [--tiff] fname

	
	positional arguments:
  		fname       directory containing multiple dxfiles or a single DataExchange
                    file: /data/ or /data/sample.h5

	optional arguments:
  		-h, --help  	show this help message and exit
  		--tiff          convert a single DataExchange file to a stack of tiff files

Example: ::

    python /local/user2bmb/dxfile/doc/demo/dump_dxfile.py test01/ | grep "start_date"

        test01/001_test.h5 /process/acquisition/start_date = ['May 29, 2019 19:20:21']
        test01/002_test.h5 /process/acquisition/start_date = ['May 29, 2019 19:23:26']
        test01/003_test.h5 /process/acquisition/start_date = ['May 29, 2019 19:26:51']
        test01/004_test.h5 /process/acquisition/start_date = ['May 29, 2019 19:30:17']
        test01/005_test.h5 /process/acquisition/start_date = ['May 29, 2019 19:33:42']
        test01/006_test.h5 /process/acquisition/start_date = ['May 29, 2019 19:37:07']
        ...


    python /local/user2bmb/dxfile/doc/demo/dump_dxfile.py test01/ | grep "data array"
        data array test01/001_test.h5 /exchange/data (1500, 2048, 2448)
        data array test01/002_test.h5 /exchange/data (1500, 2048, 2448)
        data array test01/003_test.h5 /exchange/data (1500, 2048, 2448)
        data array test01/004_test.h5 /exchange/data (1500, 2048, 2448)
        data array test01/005_test.h5 /exchange/data (1500, 2048, 2448)
        data array test01/006_test.h5 /exchange/data (1500, 2048, 2448)
        ...

	python dump_dxfile.py /tomobank/tomo_00001.h5 > experiment_log.txt
	python dump_dxfile.py /tomobank/tomo_00001.h5 --tiff
