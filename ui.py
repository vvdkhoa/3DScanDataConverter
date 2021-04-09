import tkinter as tk
import tkinter.font as tkFont
from time import sleep

# For run .bat file
from subprocess import Popen

# Read json settings
import json
with open('settings.json') as json_file:
    json_str = json_file.read()
    my_settings = json.loads(json_str)#[0]

# Root Path Setting #####################
import os
root_path = os.getcwd()
#print('Root Path: ' + str(root_path))
import sys
sys.path.insert(1, root_path)

# Default CAD Directory Setting #########
if my_settings['input_path'] == '':
    my_settings['input_path'] = str(os.path.join(root_path, 'CAD_DATA\\InputFile'))
if my_settings['output_path'] == '':
    my_settings['output_path'] = str(os.path.join(root_path, 'CAD_DATA\\OutputFile'))
if my_settings['processing_path'] == '':
    my_settings['processing_path'] = str(os.path.join(root_path, 'CAD_DATA\\ProcessingFile'))

# Meshlab function
from converter1 import mesh_filter

# Import HELP function
from my_help import my_print, read_my_settings, absoluteFilePaths


#########################################
class UIApp:

    def __init__(self, root):
        #setting title
        root.title("Scan Data Converter")
        #setting icon
        root.iconbitmap(os.path.join(root_path, 'Icons\\icon.ico'))
        #setting window size
        width=420
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_804=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "left"
        GLabel_804["anchor"] = 'w' # For justify left
        GLabel_804["text"] = "SETTINGS: "
        GLabel_804.place(x=10,y=0,width=150,height=30)

        GLabel_426=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "left"
        GLabel_426["anchor"] = 'w'
        GLabel_426["text"] = "FreeCAD Path"
        GLabel_426.place(x=10,y=190,width=150,height=40)

        GLabel_101=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_101["font"] = ft
        GLabel_101["fg"] = "#333333"
        GLabel_101["justify"] = "left"
        GLabel_101["anchor"] = 'w'
        GLabel_101["text"] = "HC Smooth"
        GLabel_101.place(x=10,y=30,width=150,height=40)

        GLabel_902=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_902["font"] = ft
        GLabel_902["fg"] = "#333333"
        GLabel_902["justify"] = "left"
        GLabel_902["text"] = "Poisson Iters"
        GLabel_902["anchor"] = 'w'
        GLabel_902.place(x=10,y=70,width=150,height=40)

        GLabel_618=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_618["font"] = ft
        GLabel_618["fg"] = "#333333"
        GLabel_618["justify"] = "left"
        GLabel_618["anchor"] = 'w'
        GLabel_618["text"] = "Target Facenum"
        GLabel_618.place(x=10,y=110,width=150,height=40)

        GLabel_903=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_903["font"] = ft
        GLabel_903["fg"] = "#333333"
        GLabel_903["justify"] = "left"
        GLabel_903["text"] = "Shape Tolerance"
        GLabel_903["anchor"] = 'w'
        GLabel_903.place(x=10,y=150,width=150,height=40)

        GButton_878=tk.Button(root)
        GButton_878["activebackground"] = "#999999"
        GButton_878["activeforeground"] = "#000000"
        GButton_878["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        GButton_878["font"] = ft
        GButton_878["fg"] = "#000000"
        GButton_878["justify"] = "center"
        GButton_878["text"] = "Data Converter"
        GButton_878["relief"] = "raised"
        GButton_878.place(x=280,y=350,width=130,height=40)
        GButton_878["command"] = self.GButton_878_command

        # Message #######################################
        self.GMessage_707_Var = tk.StringVar()
        self.GMessage_707_Var.set('Message')
        self.GMessage_707=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.GMessage_707["font"] = ft
        self.GMessage_707["fg"] = "#333333"
        self.GMessage_707["justify"] = "left"
        self.GMessage_707["text"] = "Message"
        self.GMessage_707["relief"] = "ridge"
        self.GMessage_707.place(x=270,y=30,width=140,height=150)
        self.GMessage_707['textvariable'] = self.GMessage_707_Var

        # IGES check box #################################
        # Default Value
        if 'iges' in my_settings['export_file_type']:
            self.GCheckBox_402_Var = tk.IntVar(value=1)
        else:
            self.GCheckBox_402_Var = tk.IntVar(value=0)
        self.GCheckBox_402=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=14)
        self.GCheckBox_402["font"] = ft
        self.GCheckBox_402["fg"] = "#333333"
        self.GCheckBox_402["justify"] = "center"
        self.GCheckBox_402["text"] = "IGES"
        self.GCheckBox_402.place(x=345,y=315,width=65,height=35)
        self.GCheckBox_402["variable"] = self.GCheckBox_402_Var
        self.GCheckBox_402["command"] = self.GCheckBox_402_command

        # STEP check box #################################
        # Default Value
        if 'step' in my_settings['export_file_type']:
            self.GCheckBox_75_Var = tk.IntVar(value=1)
        else:
            self.GCheckBox_75_Var = tk.IntVar(value=0)
        self.GCheckBox_75=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=14)
        self.GCheckBox_75["font"] = ft
        self.GCheckBox_75["fg"] = "#333333"
        self.GCheckBox_75["justify"] = "center"
        self.GCheckBox_75["text"] = "STEP"
        self.GCheckBox_75.place(x=275,y=315,width=65,height=35)
        self.GCheckBox_75["variable"] = self.GCheckBox_75_Var
        self.GCheckBox_75["command"] = self.GCheckBox_75_command

        GLabel_601=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_601["font"] = ft
        GLabel_601["fg"] = "#333333"
        GLabel_601["justify"] = "left"
        GLabel_601["anchor"] = 'w'
        GLabel_601["text"] = "Input Folder"
        GLabel_601.place(x=10,y=230,width=150,height=40)

        GLabel_348=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_348["font"] = ft
        GLabel_348["fg"] = "#333333"
        GLabel_348["justify"] = "left"
        GLabel_348["anchor"] = 'w'
        GLabel_348["text"] = "Save As"
        GLabel_348.place(x=10,y=270,width=150,height=40)

        ######################################################################
        self.GLineEdit_253=tk.Entry(root)
        self.GLineEdit_253["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_253["font"] = ft
        self.GLineEdit_253["fg"] = "#333333"
        self.GLineEdit_253["justify"] = "left"
        self.GLineEdit_253["text"] = ""
        self.GLineEdit_253.place(x=160,y=30,width=95,height=35)
        #self.GLineEdit_253["invalidcommand"] = "Command1"
        #self.GLineEdit_253["validatecommand"] = "Command2"
        self.GLineEdit_253.insert(0, my_settings['hc_laplacian_smooth_time'])
        ######################################################################

        self.GLineEdit_770=tk.Entry(root)
        self.GLineEdit_770["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_770["font"] = ft
        self.GLineEdit_770["fg"] = "#333333"
        self.GLineEdit_770["justify"] = "left"
        self.GLineEdit_770["text"] = ""
        self.GLineEdit_770.place(x=160,y=70,width=95,height=35)
        self.GLineEdit_770.insert(0, my_settings['poisson_iters'])

        self.GLineEdit_472=tk.Entry(root)
        self.GLineEdit_472["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_472["font"] = ft
        self.GLineEdit_472["fg"] = "#333333"
        self.GLineEdit_472["justify"] = "left"
        self.GLineEdit_472["text"] = ""
        self.GLineEdit_472.place(x=160,y=110,width=95,height=35)
        self.GLineEdit_472.insert(0, my_settings['targetfacenum'])

        self.GLineEdit_658=tk.Entry(root)
        self.GLineEdit_658["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_658["font"] = ft
        self.GLineEdit_658["fg"] = "#333333"
        self.GLineEdit_658["justify"] = "left"
        self.GLineEdit_658["text"] = ""
        self.GLineEdit_658.place(x=160,y=150,width=95,height=35)
        self.GLineEdit_658.insert(0, my_settings['shape_tolerance'])

        self.GLineEdit_533=tk.Entry(root)
        self.GLineEdit_533["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_533["font"] = ft
        self.GLineEdit_533["fg"] = "#333333"
        self.GLineEdit_533["justify"] = "left"
        self.GLineEdit_533["text"] = ""
        self.GLineEdit_533.place(x=160,y=190,width=250,height=35)
        self.GLineEdit_533.insert(0, my_settings['FreeCAD_path'])

        self.GLineEdit_664=tk.Entry(root)
        self.GLineEdit_664["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_664["font"] = ft
        self.GLineEdit_664["fg"] = "#333333"
        self.GLineEdit_664["justify"] = "left"
        self.GLineEdit_664["text"] = ""
        self.GLineEdit_664.place(x=160,y=230,width=250,height=35)
        self.GLineEdit_664.insert(0, my_settings['input_path'])

        self.GLineEdit_517=tk.Entry(root)
        self.GLineEdit_517["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_517["font"] = ft
        self.GLineEdit_517["fg"] = "#333333"
        self.GLineEdit_517["justify"] = "left"
        self.GLineEdit_517["text"] = ""
        self.GLineEdit_517.place(x=160,y=270,width=250,height=35)
        self.GLineEdit_517.insert(0, my_settings['output_path'])

        # Save Settings Button
        GButton_657=tk.Button(root)
        GButton_657["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        GButton_657["font"] = ft
        GButton_657["fg"] = "#000000"
        GButton_657["justify"] = "center"
        GButton_657["text"] = "Save Settings"
        GButton_657.place(x=10,y=350,width=130,height=40)
        GButton_657["command"] = self.GButton_657_command

        # Clear Input Button
        GButton_290=tk.Button(root)
        GButton_290["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        GButton_290["font"] = ft
        GButton_290["fg"] = "#000000"
        GButton_290["justify"] = "center"
        GButton_290["text"] = "Clear Input"
        GButton_290.place(x=145,y=350,width=130,height=40)
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

        # Save Setting Data to Json
        json_edit('settings.json', 'hc_laplacian_smooth_time', hc_laplacian_smooth_time)
        json_edit('settings.json', 'poisson_iters', poisson_iters)
        json_edit('settings.json', 'targetfacenum', targetfacenum)
        json_edit('settings.json', 'shape_tolerance', shape_tolerance)
        json_edit('settings.json', 'FreeCAD_path', FreeCAD_path)
        json_edit('settings.json', 'input_path', input_path)
        json_edit('settings.json', 'output_path', output_path)

    #######################################
    # Clear Input Button Click
    def GButton_290_command(self):
        print("Clear Input")
        
        input_files = get_input_file()
        print(input_files)

    # Data Converter Button Click
    def GButton_878_command(self, *args):

        # Save setting
        self.GButton_657_command()

        # Get Input Files List
        input_files = get_input_file()
        
        # Meshlab
        self.GMessage_707_Var.set('Meshlap\nProcessing')
        for file_path in input_files:
            
            mesh_filter(file_path)

        # Freecad Convert: Call run bat file because FreeCAD App conflict with Tkinter
        self.GMessage_707_Var.set('FreeCAD\nProcessing')
        p = Popen("run_converter2.bat", cwd=r"{}".format(root_path))
        stdout, stderr = p.communicate()

        # Send message
        self.GMessage_707_Var.set('Completed')


##############################################  
def get_input_file():

    # Read Input path
    my_settings = read_my_settings()
    input_path = my_settings['input_path']

    all_files = absoluteFilePaths(input_path)

    input_files = []
    for file in all_files:
        file_type = os.path.splitext(file)[1]
        if os.path.splitext(file)[1] in ['.3ds', '.ply', '.stl', '.obj', '.qobj', '.off', '.ptx']:
            input_files.append(file)
    return input_files


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
if __name__ == "__main__":

    # Show settings
    my_print('MY SETTINGS')
    for key in my_settings:
        print('++++++++++++++++++++++++++++++++++++++')
        print("{}: {}".format(key, my_settings[key]))

    # Run UI
    root = tk.Tk()
    app = UIApp(root)
    root.mainloop()
