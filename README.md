## 3D Scan Data Converters
#### This tool uses MeshLab and freecad to convert stl scanned data into steps or iges.
#### Note: Use only with each stl file one by one

### User Requirements
1. Windowns 10 64 bit
2. FreeCAD install

### Using
1. Download packet
2. Crease shortcut:
#### Way 1: Create desktop shortcut and using
Run Create_Desktop_Shortcut_EN.vbs or<br/>
Run Create_Desktop_Shortcut_JA.vbs
#### Way 2:
Run Scripts\ScanDataConverter.bat
#### Way 3: (CMD Debug)
cd \3DScanDataConverter\Scripts
run_ui<br/>
run_converter1  (check meshlap import)<br/>
run_converter2  (check freeCAD import)

### Settings
settings.json (Setting can save from tkinter UI)
1. FreeCAD_path, example:
"FreeCAD_path": "C:/Program Files/FreeCAD 0.18/bin"

### Develope Requirements
1. Python 3.6.6 for FreeCAD
2. Python 3.9.4 for pymeshlab (To avoid errors Load DLL faild on windowns)

### Lib
1. pymeshlab==0.2
2. numpy==1.19.5

## Refer Document
https://github.com/cnr-isti-vclab/PyMeshLab<br/>
https://pymeshlab.readthedocs.io/en/latest/filter_list.html#apply-filter-parameters<br/>
https://wiki.freecadweb.org/FreeCAD_API
