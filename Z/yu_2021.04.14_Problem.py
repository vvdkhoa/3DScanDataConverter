# Meshlab
import pymeshlab
import pymeshlab    # Import 2 times to avoid exception

import ntpath

# Import HELP function
from my_help import my_print, read_my_settings


##################################
# Mesh Data Filter Using Meshlab
def mesh_filter(file_path):

    my_print('Mesh Data Processing')

    my_settings = read_my_settings()

    # Create a new MeshSet
    ms = pymeshlab.MeshSet()

    # Load a new mesh
    ms.load_new_mesh(file_path)

    # Close vertices
    ms.merge_close_vertices(threshold=my_settings['merge_close_vertices_threshold'])

    #ms.remove_unreferenced_vertices()

    # HC Smooth
    for i in range(my_settings['hc_laplacian_smooth_time']):
        ms.hc_laplacian_smooth()

    # Filling holes poisson
    try:
        print('Try surface_reconstruction_screened_poisson with preclean=False')
        ms.surface_reconstruction_screened_poisson( visiblelayer=False,
            depth=my_settings['poisson_depth'], fulldepth=5, cgdepth=0, scale=1.1, samplespernode=1.5,
            pointweight=4, iters=8, confidence=False, preclean=False)
    except:
        print('Surface_reconstruction_screened_poisson preclean=True')
        ms.surface_reconstruction_screened_poisson( visiblelayer=False,
            depth=my_settings['poisson_depth'], fulldepth=5, cgdepth=0, scale=1.1, samplespernode=1.5,
            pointweight=4, iters=8, confidence=False, preclean=True)

    # Reduce face numble
    ms.simplification_quadric_edge_collapse_decimation(
        targetfacenum=my_settings['targetfacenum'], targetperc=0, qualitythr=0.3,
        preserveboundary=False, boundaryweight=1, preservenormal=False, preservetopology=False,
        optimalplacement=True, planarquadric=False, planarweight=0.001, qualityweight=False,
        autoclean=True, selected =False)

    # Save project
    input_file_name = ntpath.basename(file_path).split('.')[0]
    
    save_path = "{}\\{}_Converted.stl".format(my_settings['processing_path'], input_file_name)
    ms.save_current_mesh(save_path)

    return save_path

##################################
if __name__ == '__main__':
    pass

#   PyMeshLab
#   All rights reserved.
#
#   VCGLib  http://www.vcglib.net                                     o o
#   Visual and Computer Graphics Library                            o     o
#                                                                  _   O  _
#   Paolo Cignoni                                                    \/)\/
#   Visual Computing Lab  http://vcg.isti.cnr.it                    /\/|
#   ISTI - Italian National Research Council                           |
#   Copyright(C) 2020       





import os
import sys
import shutil
import ntpath

# Root Path Setting #####################
root_path = os.getcwd()
sys.path.insert(1, root_path)

# Import HELP function
from my_help import my_print, read_my_settings, absoluteFilePaths

# Import FreeCad Library
my_settings = read_my_settings()
sys.path.append(my_settings['FreeCAD_path'])
import FreeCAD
import Mesh
import Part


#########################################
# FreeCad: STL => IGES, STEP
def convert_stl_iges(file_path):

    my_print('Convert Data')

    my_settings = read_my_settings()

    # Create temporary file
    tem_file_path = "{}\\FreeCadTemporary\\filtered_mesh.stl".format(my_settings['processing_path'])
    shutil.copyfile(file_path, tem_file_path)

    # Read STL
    Mesh.open(u"{}".format(tem_file_path))
    App.setActiveDocument("Unnamed")
    App.ActiveDocument=App.getDocument("Unnamed")

    # MakeShape
    FreeCAD.getDocument("Unnamed").addObject("Part::Feature","filtered_mesh001")
    __shape__=Part.Shape()
    __shape__.makeShapeFromMesh(FreeCAD.getDocument("Unnamed").getObject("filtered_mesh").Mesh.Topology,my_settings['shape_tolerance'])
    FreeCAD.getDocument("Unnamed").getObject("filtered_mesh001").Shape=__shape__
    FreeCAD.getDocument("Unnamed").getObject("filtered_mesh001").purgeTouched()  # Marks the object as unchanged
    # del __shape__

    # Convert To solid
    __s__=App.ActiveDocument.filtered_mesh001.Shape
    __s__=Part.Solid(__s__)
    __o__=App.ActiveDocument.addObject("Part::Feature","filtered_mesh001_solid")
    __o__.Label="filtered_mesh001 (Solid)"
    __o__.Shape=__s__
    # del __s__, __o_

    # STL To IGES
    __objs__=[]
    if FreeCAD.getDocument("Unnamed").getObject("filtered_mesh001_solid"):
        __objs__.append(FreeCAD.getDocument("Unnamed").getObject("filtered_mesh001_solid"))    # If solid available
    else:
        __objs__.append(FreeCAD.getDocument("Unnamed").getObject("filtered_mesh001"))  # If only surface available

    # Export
    input_file_name = ntpath.basename(file_path).split('.')[0]

    for file_type in my_settings['export_file_type']:
        save_path = "{}\\{}.{}".format(my_settings['output_path'], input_file_name, file_type)
        my_print("Export {} File :\br{}".format(file_type, save_path))

        Part.export(__objs__,u"{}".format(save_path))


##############################################
# Get data which fillted by Meshlap
def get_processing_file():

    # Read Input path
    my_settings = read_my_settings()
    input_path = my_settings['processing_path']

    all_files = absoluteFilePaths(input_path)

    input_files = []
    for file in all_files:
        file_type = os.path.splitext(file)[1]
        if os.path.splitext(file)[1] in ['.stl']:
            input_files.append(file)
    return input_files


#########################################
if __name__ == '__main__':

    # Get data which fillted by Meshlap
    processing_files = get_processing_file()

    for file_path in processing_files:
        convert_stl_iges(file_path)

    my_print('Convert STL To IGES, STEP completed.')





import json
import os
from pathlib import Path
from time import sleep
import sys

root_path = os.getcwd()
#root_path = 'C:\\Users\\Y32840\\Desktop\\3DScanDataConverter\\Scripts'
#sys.path.insert(1, root_path)

cad_path = Path(root_path).parent

##############################
def read_my_settings():

    with open('C:\\Users\\Y32840\\Desktop\\3DScanDataConverter\\Scripts\\settings.json') as json_file:
    #with open('settings.json') as json_file:
        json_str = json_file.read()
        my_settings = json.loads(json_str)

    # Default CAD Directory Setting #########
    if my_settings['input_path'] == '':
        my_settings['input_path'] = str(os.path.join(cad_path, 'CAD_DATA\\InputFile'))
    if my_settings['output_path'] == '':
        my_settings['output_path'] = str(os.path.join(cad_path, 'CAD_DATA\\OutputFile'))
    if my_settings['processing_path'] == '':
        my_settings['processing_path'] = str(os.path.join(cad_path, 'CAD_DATA\\ProcessingFile'))
        
    return my_settings

 ##############################
def read_translate():

    try:
        with open('translate.json') as json_file:
            json_str = json_file.read()
            translate = json.loads(json_str)
    except:
        with open('translate.json', encoding="utf8", errors='ignore') as json_file:
            json_str = json_file.read()
            translate = json.loads(json_str)
        
    return translate

##############################
# Get absolute paths of all files in a directory
def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


##############################
def clear_folder(folder_path):
    filelist = [ f for f in os.listdir(folder_path) if not f.endswith(".py") ]
    error = []
    if filelist:
        for f in filelist:
            try:
                os.remove(os.path.join(folder_path, f))
            except PermissionError:
                print("Can not remove: {}".format(f))
                error.append(f)
    return error

##############################
def my_print(text):
    print('''
++++++++++++++++++++++++++++++++++
+ {}
++++++++++++++++++++++++++++++++++
          '''.format(text))

##############################
if __name__ == '__main__':
    pass



{"FreeCAD_path": "C:\\Program Files\\FreeCAD 0.18\\bin", "hc_laplacian_smooth_time": 1, "poisson_depth": 7, "targetfacenum": 10000, "shape_tolerance": 0.1, "merge_close_vertices_threshold": 0.1, "export_file_type": ["step", "iges"], "input_path": "C:\\Users\\Y32840\\Desktop\\CAD_IN", "output_path": "C:\\Users\\Y32840\\Desktop\\CAD_OUT", "processing_path": "", "language": "JA"}
