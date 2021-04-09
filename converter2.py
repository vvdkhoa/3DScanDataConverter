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
