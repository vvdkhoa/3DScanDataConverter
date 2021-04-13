# Meshlab
import pymeshlab
# import pymeshlab    # Import 2 times to avoid exception

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
    ms.merge_close_vertices(threshold=1)

    # HC Smooth
    for i in range(my_settings['hc_laplacian_smooth_time']):
        ms.hc_laplacian_smooth()

    # Filling holes poisson
    ms.surface_reconstruction_screened_poisson(
        visiblelayer=False, depth=10, fulldepth=5, cgdepth=0, scale=1.1, samplespernode=1.5, pointweight=4,
        iters=my_settings['poisson_iters'],
        confidence=False, preclean=True)     # preclean= False
    
    # Reduce face numble
    ms.simplification_quadric_edge_collapse_decimation(targetfacenum=my_settings['targetfacenum'])

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






import json
import os
from pathlib import Path

root_path = os.getcwd()
cad_path = Path(root_path).parent

##############################
def read_my_settings():
    
    with open('settings.json') as json_file:
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







import ntpath
import tkinter as tk
from tkinter.constants import END
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk

from time import sleep
import json
import sys
import os

# For run .bat file
from subprocess import Popen

# Get root path
root_path = os.getcwd()

# Add the root path to the environment
sys.path.insert(1, root_path)


# Meshlab function
from converter1 import mesh_filter

# Import HELP function
from my_help import my_print, read_my_settings, absoluteFilePaths, clear_folder, read_translate

# Read json settings
my_settings = read_my_settings()


'''
LANGUAGE SETTINGS

'''
language = my_settings['language']
language_index = {
    'JA': 0,
    'EN': 1,
    }
# Read translate json
TEXT = read_translate()


# Font setting
#my_font='Times'
my_font='Helvetica'


#########################################
class UIApp:

    def __init__(self, root):
        #setting title
        root.title(TEXT['Scan_Data_Converter'][language])
        #setting icon
        root.iconbitmap(os.path.join(root_path, 'Icons\\icon.ico'))
        #setting window size
        width=500
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_804=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "left"
        GLabel_804["anchor"] = 'w' # For justify left
        GLabel_804["text"] = TEXT['Settings'][language]
        GLabel_804.place(x=10,y=0,width=150,height=30)

        GLabel_426=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "left"
        GLabel_426["anchor"] = 'w'
        GLabel_426["text"] = TEXT['FreeCAD_Path'][language]
        GLabel_426.place(x=10,y=190,width=150,height=40)

        GLabel_101=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_101["font"] = ft
        GLabel_101["fg"] = "#333333"
        GLabel_101["justify"] = "left"
        GLabel_101["anchor"] = 'w'
        GLabel_101["text"] = TEXT["HC_Laplacian_Smooth"][language]
        GLabel_101.place(x=10,y=30,width=170,height=40)

        GLabel_902=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_902["font"] = ft
        GLabel_902["fg"] = "#333333"
        GLabel_902["justify"] = "left"
        GLabel_902["text"] = TEXT["Reconstruction_Depth"][language]
        GLabel_902["anchor"] = 'w'
        GLabel_902.place(x=10,y=70,width=170,height=40)

        GLabel_618=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_618["font"] = ft
        GLabel_618["fg"] = "#333333"
        GLabel_618["justify"] = "left"
        GLabel_618["anchor"] = 'w'
        GLabel_618["text"] = TEXT["Target_Facenum"][language]
        GLabel_618.place(x=10,y=110,width=175,height=40)

        GLabel_903=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_903["font"] = ft
        GLabel_903["fg"] = "#333333"
        GLabel_903["justify"] = "left"
        GLabel_903["text"] = TEXT["Shape_Tolerance"][language]
        GLabel_903["anchor"] = 'w'
        GLabel_903.place(x=10,y=150,width=150,height=40)

        GLabel_980=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_980["font"] = ft
        GLabel_980["fg"] = "#333333"
        GLabel_980["justify"] = "left"
        GLabel_980["text"] = TEXT["Input_File_List"][language]
        GLabel_980["anchor"] = 'w'
        GLabel_980.place(x=270,y=0,width=180,height=30)

        GButton_878=tk.Button(root)
        GButton_878["activebackground"] = "#999999"
        GButton_878["activeforeground"] = "#000000"
        GButton_878["bg"] = "#efefef"
        ft = tkFont.Font(family=my_font,size=13)
        GButton_878["font"] = ft
        GButton_878["fg"] = "#000000"
        GButton_878["justify"] = "center"
        GButton_878["text"] = TEXT["Data_Converter"][language]
        GButton_878["relief"] = "raised"
        GButton_878.place(x=336,y=350,width=154,height=40)
        GButton_878["command"] = self.GButton_878_command

        # Message
        global GLabel_819
        GLabel_819=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=11)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "left"
        GLabel_819["text"] = TEXT["Message"][language]
        GLabel_819["anchor"] = 'w'
        GLabel_819.place(x=10,y=320,width=310,height=25)

        # Input file list
        global GListBox_56
        GListBox_56=tk.Listbox(root)
        GListBox_56["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        GListBox_56["font"] = ft
        GListBox_56["fg"] = "#333333"
        GListBox_56["justify"] = "left"
        GListBox_56["relief"] = "ridge"
        GListBox_56.place(x=270,y=30,width=220,height=150)

        # IGES check box #################################
        # Default Value
        if 'iges' in my_settings['export_file_type']:
            self.GCheckBox_402_Var = tk.IntVar(value=1)
        else:
            self.GCheckBox_402_Var = tk.IntVar(value=0)
        self.GCheckBox_402=tk.Checkbutton(root)
        ft = tkFont.Font(family=my_font,size=13)
        self.GCheckBox_402["font"] = ft
        self.GCheckBox_402["fg"] = "#333333"
        self.GCheckBox_402["justify"] = "center"
        self.GCheckBox_402["text"] = "IGES"
        self.GCheckBox_402.place(x=425,y=315,width=65,height=35)
        self.GCheckBox_402["variable"] = self.GCheckBox_402_Var
        self.GCheckBox_402["command"] = self.GCheckBox_402_command

        # STEP check box #################################
        # Default Value
        if 'step' in my_settings['export_file_type']:
            self.GCheckBox_75_Var = tk.IntVar(value=1)
        else:
            self.GCheckBox_75_Var = tk.IntVar(value=0)
        self.GCheckBox_75=tk.Checkbutton(root)
        ft = tkFont.Font(family=my_font,size=13)
        self.GCheckBox_75["font"] = ft
        self.GCheckBox_75["fg"] = "#333333"
        self.GCheckBox_75["justify"] = "center"
        self.GCheckBox_75["text"] = "STEP"
        self.GCheckBox_75.place(x=350,y=315,width=65,height=35)
        self.GCheckBox_75["variable"] = self.GCheckBox_75_Var
        self.GCheckBox_75["command"] = self.GCheckBox_75_command

        # Language Select box #################################
        # Language list
        self.language_choices = list(language_index.keys())
        self.language_variable = tk.StringVar()
        self.language_variable.set('')

        self.GLabel_Language=ttk.Combobox(root)
        ft = tkFont.Font(family=my_font,size=9)
        self.GLabel_Language["font"] = ft
        self.GLabel_Language["values"] = self.language_choices
        self.GLabel_Language["textvariable"] = self.language_variable
        self.GLabel_Language["state"] = 'readonly'
        self.GLabel_Language.current(language_index[language])
        self.GLabel_Language.place(x=450, y=5, width=40, height=20)
        

        GLabel_601=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_601["font"] = ft
        GLabel_601["fg"] = "#333333"
        GLabel_601["justify"] = "left"
        GLabel_601["anchor"] = 'w'
        GLabel_601["text"] = TEXT["Input_Folder"][language]
        GLabel_601.place(x=10,y=230,width=150,height=40)

        GLabel_348=tk.Label(root)
        ft = tkFont.Font(family=my_font,size=13)
        GLabel_348["font"] = ft
        GLabel_348["fg"] = "#333333"
        GLabel_348["justify"] = "left"
        GLabel_348["anchor"] = 'w'
        GLabel_348["text"] = TEXT["Save_As"][language]
        GLabel_348.place(x=10,y=270,width=150,height=40)

        ######################################################################
        self.GLineEdit_253=tk.Entry(root)
        self.GLineEdit_253["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        self.GLineEdit_253["font"] = ft
        self.GLineEdit_253["fg"] = "#333333"
        self.GLineEdit_253["justify"] = "left"
        self.GLineEdit_253["text"] = ""
        self.GLineEdit_253.place(x=185,y=30,width=70,height=35)
        #self.GLineEdit_253["invalidcommand"] = "Command1"
        #self.GLineEdit_253["validatecommand"] = "Command2"
        self.GLineEdit_253.insert(0, my_settings['hc_laplacian_smooth_time'])
        ######################################################################

        self.GLineEdit_770=tk.Entry(root)
        self.GLineEdit_770["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        self.GLineEdit_770["font"] = ft
        self.GLineEdit_770["fg"] = "#333333"
        self.GLineEdit_770["justify"] = "left"
        self.GLineEdit_770["text"] = ""
        self.GLineEdit_770.place(x=185,y=70,width=70,height=35)
        self.GLineEdit_770.insert(0, my_settings['poisson_iters'])

        self.GLineEdit_472=tk.Entry(root)
        self.GLineEdit_472["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        self.GLineEdit_472["font"] = ft
        self.GLineEdit_472["fg"] = "#333333"
        self.GLineEdit_472["justify"] = "left"
        self.GLineEdit_472["text"] = ""
        self.GLineEdit_472.place(x=185,y=110,width=70,height=35)
        self.GLineEdit_472.insert(0, my_settings['targetfacenum'])

        self.GLineEdit_658=tk.Entry(root)
        self.GLineEdit_658["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        self.GLineEdit_658["font"] = ft
        self.GLineEdit_658["fg"] = "#333333"
        self.GLineEdit_658["justify"] = "left"
        self.GLineEdit_658["text"] = ""
        self.GLineEdit_658.place(x=185,y=150,width=70,height=35)
        self.GLineEdit_658.insert(0, my_settings['shape_tolerance'])

        self.GLineEdit_533=tk.Entry(root)
        self.GLineEdit_533["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        self.GLineEdit_533["font"] = ft
        self.GLineEdit_533["fg"] = "#333333"
        self.GLineEdit_533["justify"] = "left"
        self.GLineEdit_533["text"] = ""
        self.GLineEdit_533.place(x=185,y=190,width=305,height=35)
        self.GLineEdit_533.insert(0, my_settings['FreeCAD_path'])

        self.GLineEdit_664=tk.Entry(root)
        self.GLineEdit_664["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        self.GLineEdit_664["font"] = ft
        self.GLineEdit_664["fg"] = "#333333"
        self.GLineEdit_664["justify"] = "left"
        self.GLineEdit_664["text"] = ""
        self.GLineEdit_664.place(x=185,y=230,width=305,height=35)
        self.GLineEdit_664.insert(0, my_settings['input_path'])

        self.GLineEdit_517=tk.Entry(root)
        self.GLineEdit_517["borderwidth"] = "1px"
        ft = tkFont.Font(family=my_font,size=13)
        self.GLineEdit_517["font"] = ft
        self.GLineEdit_517["fg"] = "#333333"
        self.GLineEdit_517["justify"] = "left"
        self.GLineEdit_517["text"] = ""
        self.GLineEdit_517.place(x=185,y=270,width=305,height=35)
        self.GLineEdit_517.insert(0, my_settings['output_path'])

        # Save Settings Button
        GButton_657=tk.Button(root)
        GButton_657["bg"] = "#efefef"
        ft = tkFont.Font(family=my_font,size=13)
        GButton_657["font"] = ft
        GButton_657["fg"] = "#000000"
        GButton_657["justify"] = "center"
        GButton_657["text"] = TEXT["Save_Settings"][language]
        GButton_657.place(x=10,y=350,width=154,height=40)
        GButton_657["command"] = self.GButton_657_command

        # Clear All Button
        GButton_290=tk.Button(root)
        GButton_290["bg"] = "#efefef"
        ft = tkFont.Font(family=my_font,size=13)
        GButton_290["font"] = ft
        GButton_290["fg"] = "#000000"
        GButton_290["justify"] = "center"
        GButton_290["text"] = TEXT["Clear_All"][language]
        GButton_290.place(x=173,y=350,width=154,height=40)
        GButton_290["command"] = self.GButton_290_command

    # IGES add or remove
    def GCheckBox_402_command(self):
        export_file_type = my_settings['export_file_type']
        if self.GCheckBox_402_Var.get() == 1:
            if 'iges' not in export_file_type:
                export_file_type.append('iges')
                print('Add IGES')
        else:
            if 'iges' in export_file_type:
                export_file_type.remove('iges')
                print('Remove IGES')
        json_edit('settings.json', 'export_file_type', export_file_type)


    # Step add or remove
    def GCheckBox_75_command(self):
        export_file_type = my_settings['export_file_type']
        if self.GCheckBox_75_Var.get() == 1:
            if 'step' not in export_file_type:
                export_file_type.append('step')
                print('Add STEP')
        else:
            if 'step' in export_file_type:
                export_file_type.remove('step')
                print('Remove STEP')
        json_edit('settings.json', 'export_file_type', export_file_type)


    # Save Setting Button Click
    def GButton_657_command(self):
        print("Save Setting")

        # Get enter data from UI
        hc_laplacian_smooth_time = int(self.GLineEdit_253.get())
        poisson_iters = int(self.GLineEdit_770.get())
        targetfacenum = int(self.GLineEdit_472.get())
        shape_tolerance = float(self.GLineEdit_658.get())
        FreeCAD_path = self.GLineEdit_533.get()
        input_path = self.GLineEdit_664.get()
        output_path = self.GLineEdit_517.get()
        new_language = self.language_variable.get()

        # Save Setting Data to Json
        json_edit('settings.json', 'hc_laplacian_smooth_time', hc_laplacian_smooth_time)
        json_edit('settings.json', 'poisson_iters', poisson_iters)
        json_edit('settings.json', 'targetfacenum', targetfacenum)
        json_edit('settings.json', 'shape_tolerance', shape_tolerance)
        json_edit('settings.json', 'FreeCAD_path', FreeCAD_path)
        json_edit('settings.json', 'input_path', input_path)
        json_edit('settings.json', 'output_path', output_path)

        if language != new_language:
            json_edit('settings.json', 'language', new_language)
            MsgBox = tk.messagebox.showinfo(TEXT['Language_Setting'][language], TEXT['Please_restart_the_application_to_apply_a_new_language'][language],icon = 'warning')

        # Send message
        GLabel_819["text"] = TEXT['Message_Save_New_Setting'][language]

    #######################################
    # Clear Input Button Click
    def GButton_290_command(self):

        MsgBox = tk.messagebox.askquestion (TEXT['Delete_Confirm'][language], TEXT['Delete_All_Files?'][language],icon = 'warning')
        if MsgBox == 'yes':
            my_settings = read_my_settings()

            error = []
            error += clear_folder(my_settings['input_path'])
            error += clear_folder(my_settings['output_path'])
            if error:
                GLabel_819["text"] = TEXT['Message_Some_files_could_not_be_deleted'][language]
            else:
                GLabel_819["text"] = TEXT['Message_Input_and_output_files_has_been_deleted'][language]
        else:
            pass


    #######################################
    # Data Converter Button Click
    def GButton_878_command(self, *args):

        # Save setting
        self.GButton_657_command()

        # Get Input Files List
        input_files = get_input_file()
        
        # Meshlab
        GLabel_819["text"] = TEXT['Message_Start_converting_data_Meshlab'][language]
        for file_path in input_files:
            
            mesh_filter(file_path)

            # Freecad Convert: Call run bat file because FreeCAD App conflict with Tkinter
            GLabel_819["text"] = TEXT['Message_Start_converting_data_FreeCAD'][language]
            p = Popen("run_converter2.bat", cwd=r"{}".format(root_path))
            stdout, stderr = p.communicate()

            # Clear temporary file
            my_settings = read_my_settings()
            clear_folder(my_settings['processing_path'])
            clear_folder("{}\\FreeCadTemporary".format(my_settings['processing_path']))

        # Send message
        GLabel_819["text"] = TEXT['Message_Complete_data_conversion'][language]
        MsgBox = tk.messagebox.showinfo(TEXT['Data_Conversion_Completed'][language], TEXT['Data_Conversion_Is_Complete'][language])


##############################################
# Return list input file (full path)
def get_input_file():

    # Read Input path
    my_settings = read_my_settings()
    input_path = my_settings['input_path']

    all_files = absoluteFilePaths(input_path)

    input_files = []
    for file in all_files:
        #file_type = os.path.splitext(file)[1]
        if os.path.splitext(file)[1] in ['.3ds', '.ply', '.stl', '.obj', '.qobj', '.off', '.ptx']:
            input_files.append(file)
    return input_files

##############################################
# Return list input file (file name)
def get_input_file_name():

    # Read Input path
    my_settings = read_my_settings()
    input_path = my_settings['input_path']

    all_files = absoluteFilePaths(input_path)

    input_files = []
    for file in all_files:
        if os.path.splitext(file)[1] in ['.3ds', '.ply', '.stl', '.obj', '.qobj', '.off', '.ptx']:
            file_name = ntpath.basename(file)
            if len(file_name) > 20:
                file_name = file_name[0:9] + '...' + file_name[-8:len(file_name)]
            input_files.append(file_name)
    return input_files

    #input_file_name = ntpath.basename(file).split('.')[0]

##############################################
def json_edit(json_path, key, value):

    # Read
    a_file = open(json_path, "r")
    json_object = json.load(a_file)
    a_file.close()

    # Update
    json_object[key] = value
    a_file = open(json_path, "w")
    json.dump(json_object, a_file)
    a_file.close()

##############################################
# Refresher UI every 1 second...
def Refresher():

    # Update file list
    global GListBox_56
    GListBox_56.delete(0, END)          # Clear list box
    show_list = get_input_file_name()   # Get list file
    GListBox_56.insert(0, *show_list)   # Show
    root.after(2000, Refresher)         # Refresher every 1s

##############################################
if __name__ == "__main__":

    # # Show settings
    # my_print('MY SETTINGS')
    # for key in my_settings:
    #     print('++++++++++++++++++++++++++++++++++++++')
        # print("{}: {}".format(key, my_settings[key]))

    # Run UI
    root = tk.Tk()
    app = UIApp(root)
    Refresher()
    root.mainloop()












