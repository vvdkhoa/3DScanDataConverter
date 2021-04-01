# Read setting
import json
with open('settings.json') as json_file:
    json_str = json_file.read()
    my_settings = json.loads(json_str)[0]
if my_settings['input_path'] == '':
    my_settings['input_path'] = 'CAD_DATA/InputFile'
if my_settings['output_path'] == '':
    my_settings['output_path'] = 'CAD_DATA/OutputFile'
if my_settings['processing_path'] == '':
    my_settings['processing_path'] = 'CAD_DATA/ProcessingFile'

# Meshlab
# https://github.com/cnr-isti-vclab/PyMeshLab
# https://pymeshlab.readthedocs.io/en/latest/filter_list.html#apply-filter-parameters
import pymeshlab

# FreeCad
# FREECADPATH = 'D:/Program Files/FreeCAD 0.18/bin/'
import sys
sys.path.append(my_settings['FreeCAD_path'])
import FreeCAD
import Mesh
import Part


# Mesh Data Filter using Meshlab
def mesh_filter(my_settings):

    print_devide('Mesh Data Processing')

    ms = pymeshlab.MeshSet()
    ms.load_new_mesh("{}\\input.stl".format(my_settings['input_path']))


    ms.merge_close_vertices(threshold=1)

    for i in range(my_settings['hc_laplacian_smooth_time']):
        ms.hc_laplacian_smooth()

    ms.surface_reconstruction_screened_poisson(
        visiblelayer=False, depth=10, fulldepth=5, cgdepth=0, scale=1.1, samplespernode=1.5, pointweight=4,
        iters=my_settings['poisson_iters'],
        confidence=False, preclean=True)     # preclean= False
    ms.simplification_quadric_edge_collapse_decimation(targetfacenum=my_settings['targetfacenum'])

    ms.save_current_mesh("{}\\filtered_mesh.stl".format(my_settings['processing_path']))


# Convert data from stl to iges using freeCad
def convert_stl_iges(my_settings):

    print_devide('Convert SLT to IGES')

    Mesh.open(u"D:/OneDrive/Programing/CAD/3DScan/filtered_mesh.stl")
    App.setActiveDocument("Unnamed") #
    App.ActiveDocument=App.getDocument("Unnamed") #

    # makeShape
    FreeCAD.getDocument("Unnamed").addObject("Part::Feature","filtered_mesh001")
    __shape__=Part.Shape()
    __shape__.makeShapeFromMesh(FreeCAD.getDocument("Unnamed").getObject("filtered_mesh").Mesh.Topology,0.100000)
    FreeCAD.getDocument("Unnamed").getObject("filtered_mesh001").Shape=__shape__
    #
    FreeCAD.getDocument("Unnamed").getObject("filtered_mesh001").purgeTouched()  # Marks the object as unchanged
    # del __shape__

    # To solid
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

    # Export file
    save_path = "{}\\sample.iges".format(my_settings['output_path'])
    Part.export(__objs__,u"{}".format(save_path))


def print_devide(text):
    print('''
++++++++++++++++++++++++++++++++++
+++++ {} ++++++++++++
++++++++++++++++++++++++++++++++++
          '''.format(text))

if __name__ == '__main__':

    print_devide('SETTINGS')
    print_devide(my_settings)

    mesh_filter(my_settings)

    convert_stl_iges(my_settings)

    print_devide('FINISH')


# https://github.com/cnr-isti-vclab/PyMeshLab
# PyMeshLab
# All rights reserved.

# VCGLib  http://www.vcglib.net                                     o o
# Visual and Computer Graphics Library                            o     o
#                                                               _   O  _
# Paolo Cignoni                                                    \/)\/
# Visual Computing Lab  http://vcg.isti.cnr.it                    /\/|
# ISTI - Italian National Research Council                           |
# Copyright(C) 2020


