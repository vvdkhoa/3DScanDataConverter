## 3D Scan Data Converters
This tool uses MeshLab and freecad to convert stl scanned data into steps or iges...

## Requirements
1. Windowns 10 64 bit
2. MeshLab_64bit_fp v2020.12 Installed
3. FreeCAD install
4. Python 3.6.6
5. Lib numpy==1.19.5
6. Lib pymeshlab==0.2

## Settings
settings.json

1. FreeCAD_path, example:
"FreeCAD_path": "D:/Program Files/FreeCAD 0.18/bin"

### Meshlab processing
2. HC Laplacian Smooth number of uses, example:
"hc_laplacian_smooth_time": 2
3. 
"poisson_iters": 8
4. 
5. 
6. 

## Refer Document
https://github.com/cnr-isti-vclab/PyMeshLab
https://pymeshlab.readthedocs.io/en/latest/filter_list.html#apply-filter-parameters
https://wiki.freecadweb.org/FreeCAD_API


## Copyring
https://github.com/cnr-isti-vclab/PyMeshLab
PyMeshLab
All rights reserved.

VCGLib  http://www.vcglib.net                                     o o
Visual and Computer Graphics Library                            o     o
                                                              _   O  _
Paolo Cignoni                                                    \/)\/
Visual Computing Lab  http://vcg.isti.cnr.it                    /\/|
ISTI - Italian National Research Council                           |
Copyright(C) 2020
