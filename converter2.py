# Read setting ##########################
import json
with open('settings.json') as json_file:
    json_str = json_file.read()
    my_settings = json.loads(json_str)#[0]

# Root Path Setting #####################
import os
import sys
root_path = os.getcwd()
#print('Root Path: ' + str(root_path))
sys.path.insert(1, root_path)


# Default CAD Directory Setting #########
if my_settings['output_path'] == '':
    my_settings['output_path'] = str(os.path.join(root_path, 'CAD_DATA/OutputFile'))
if my_settings['processing_path'] == '':
    my_settings['processing_path'] = str(os.path.join(root_path, 'CAD_DATA/ProcessingFile'))


# Import FreeCad Library
sys.path.append(my_settings['FreeCAD_path'])
import FreeCAD
import Mesh
import Part


# Import HELP function
from my_help import my_print


#########################################
# FreeCad: STL => IGES, STEP
def convert_stl_iges(my_settings):

    my_print('Convert Data')

    # Read STL
    input_path = "{}\\filtered_mesh.stl".format(my_settings['processing_path'])
    Mesh.open(u"{}".format(input_path))
    App.setActiveDocument("Unnamed") #
    App.ActiveDocument=App.getDocument("Unnamed") #

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
    for file_type in my_settings['export_file_type']:
        save_path = "{}\\sample.{}".format(my_settings['output_path'], file_type)
        my_print("Export {} File :\br{}".format(file_type, save_path))

        Part.export(__objs__,u"{}".format(save_path))

#########################################
if __name__ == '__main__':

    convert_stl_iges(my_settings)

    my_print('Convert STL To IGES, STEP completed.')
