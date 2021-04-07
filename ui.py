import tkinter as tk
import tkinter.font as tkFont

# Read setting
import json
with open('settings.json') as json_file:
    json_str = json_file.read()
    my_settings = json.loads(json_str)#[0]


##############################################
class App:
    
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=392
        height=249
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_804=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "left"
        GLabel_804["text"] = "SETTINGS: "
        GLabel_804.place(x=10,y=0,width=120,height=25)

        GLabel_426=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "left"
        GLabel_426["text"] = "FreeCAD Path"
        GLabel_426.place(x=10,y=150,width=120,height=30)

        GLabel_101=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_101["font"] = ft
        GLabel_101["fg"] = "#333333"
        GLabel_101["justify"] = "left"
        GLabel_101["text"] = "HC Smooth"
        GLabel_101.place(x=10,y=30,width=120,height=30)

        GLabel_902=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_902["font"] = ft
        GLabel_902["fg"] = "#333333"
        GLabel_902["justify"] = "left"
        GLabel_902["text"] = "Poisson Iters"
        GLabel_902.place(x=10,y=60,width=120,height=30)

        GLabel_618=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_618["font"] = ft
        GLabel_618["fg"] = "#333333"
        GLabel_618["justify"] = "left"
        GLabel_618["text"] = "Target Facenum"
        GLabel_618.place(x=10,y=90,width=120,height=30)

        GLabel_903=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_903["font"] = ft
        GLabel_903["fg"] = "#333333"
        GLabel_903["justify"] = "left"
        GLabel_903["text"] = "Shape Tolerance"
        GLabel_903.place(x=10,y=120,width=120,height=30)

        GButton_878=tk.Button(root)
        GButton_878["activebackground"] = "#999999"
        GButton_878["activeforeground"] = "#000000"
        GButton_878["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_878["font"] = ft
        GButton_878["fg"] = "#000000"
        GButton_878["justify"] = "center"
        GButton_878["text"] = "Data Converter"
        GButton_878["relief"] = "raised"
        GButton_878.place(x=240,y=210,width=145,height=30)
        GButton_878["command"] = self.GButton_878_command

        ########################################################
        #self.GMessage_707=tk.Message(root)
        self.GMessage_707=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GMessage_707["font"] = ft
        self.GMessage_707["fg"] = "#333333"
        self.GMessage_707["justify"] = "left"
        self.GMessage_707["text"] = "Message"
        self.GMessage_707["relief"] = "ridge"
        self.GMessage_707.place(x=240,y=30,width=145,height=136)
        ########################################################

        GCheckBox_402=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_402["font"] = ft
        GCheckBox_402["fg"] = "#333333"
        GCheckBox_402["justify"] = "center"
        GCheckBox_402["text"] = "IGES"
        GCheckBox_402.place(x=310,y=170,width=58,height=30)
        GCheckBox_402["offvalue"] = "0"
        GCheckBox_402["onvalue"] = "1"
        GCheckBox_402["command"] = self.GCheckBox_402_command

        GCheckBox_75=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_75["font"] = ft
        GCheckBox_75["fg"] = "#333333"
        GCheckBox_75["justify"] = "center"
        GCheckBox_75["text"] = "STEP"
        GCheckBox_75.place(x=240,y=170,width=58,height=31)
        GCheckBox_75["offvalue"] = "0"
        GCheckBox_75["onvalue"] = "1"
        GCheckBox_75["command"] = self.GCheckBox_75_command

        GLabel_601=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_601["font"] = ft
        GLabel_601["fg"] = "#333333"
        GLabel_601["justify"] = "left"
        GLabel_601["text"] = "Input Folder"
        GLabel_601.place(x=10,y=180,width=120,height=30)

        GLabel_348=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_348["font"] = ft
        GLabel_348["fg"] = "#333333"
        GLabel_348["justify"] = "left"
        GLabel_348["text"] = "Save As"
        GLabel_348.place(x=10,y=210,width=120,height=30)

        ######################################################################
        self.GLineEdit_253=tk.Entry(root)
        self.GLineEdit_253["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_253["font"] = ft
        self.GLineEdit_253["fg"] = "#333333"
        self.GLineEdit_253["justify"] = "left"
        self.GLineEdit_253["text"] = ""
        self.GLineEdit_253.place(x=130,y=30,width=95,height=25)
        #self.GLineEdit_253["show"] = "222"
        self.GLineEdit_253["invalidcommand"] = "Command1"
        self.GLineEdit_253["validatecommand"] = "Command2"
        self.GLineEdit_253.insert(0, my_settings['hc_laplacian_smooth_time'])
        ######################################################################

        self.GLineEdit_770=tk.Entry(root)
        self.GLineEdit_770["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_770["font"] = ft
        self.GLineEdit_770["fg"] = "#333333"
        self.GLineEdit_770["justify"] = "left"
        self.GLineEdit_770["text"] = ""
        self.GLineEdit_770.place(x=130,y=60,width=95,height=25)
        self.GLineEdit_770.insert(0, my_settings['poisson_iters'])

        self.GLineEdit_472=tk.Entry(root)
        self.GLineEdit_472["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_472["font"] = ft
        self.GLineEdit_472["fg"] = "#333333"
        self.GLineEdit_472["justify"] = "left"
        self.GLineEdit_472["text"] = ""
        self.GLineEdit_472.place(x=130,y=90,width=95,height=25)
        self.GLineEdit_472.insert(0, my_settings['targetfacenum'])

        self.GLineEdit_658=tk.Entry(root)
        self.GLineEdit_658["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_658["font"] = ft
        self.GLineEdit_658["fg"] = "#333333"
        self.GLineEdit_658["justify"] = "left"
        self.GLineEdit_658["text"] = ""
        self.GLineEdit_658.place(x=130,y=120,width=95,height=25)
        self.GLineEdit_658.insert(0, my_settings['shape_tolerance'])

        self.GLineEdit_533=tk.Entry(root)
        self.GLineEdit_533["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_533["font"] = ft
        self.GLineEdit_533["fg"] = "#333333"
        self.GLineEdit_533["justify"] = "left"
        self.GLineEdit_533["text"] = ""
        self.GLineEdit_533.place(x=130,y=150,width=95,height=25)
        self.GLineEdit_533.insert(0, my_settings['FreeCAD_path'])

        self.GLineEdit_664=tk.Entry(root)
        self.GLineEdit_664["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_664["font"] = ft
        self.GLineEdit_664["fg"] = "#333333"
        self.GLineEdit_664["justify"] = "left"
        self.GLineEdit_664["text"] = ""
        self.GLineEdit_664.place(x=130,y=180,width=95,height=25)
        self.GLineEdit_664.insert(0, my_settings['input_path'])

        self.GLineEdit_517=tk.Entry(root)
        self.GLineEdit_517["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_517["font"] = ft
        self.GLineEdit_517["fg"] = "#333333"
        self.GLineEdit_517["justify"] = "left"
        self.GLineEdit_517["text"] = ""
        self.GLineEdit_517.place(x=130,y=210,width=95,height=25)
        self.GLineEdit_517.insert(0, my_settings['output_path'])

    def GButton_878_command(self, *args):
        print("Data Convert")
        
        hc_laplacian_smooth_time = int(self.GLineEdit_253.get())
        poisson_iters = int()
        


    def GCheckBox_402_command(self):
        print("Iges selected")


    def GCheckBox_75_command(self):
        print("Step selected")


    def Command1(self):
        print("Entry 1")
        
    def Command2(self):
        print("Entry 2")

    def GLineEdit_253_get(self):
        print('aaaaa')


##############################################
def json_edit(json_path, key, value):

    # Read
    a_file = open(json_path, "r")
    json_object = json.load(a_file)
    a_file.close()
    print(json_object)

    # Update
    json_object[key] = value
    a_file = open("settings.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


##############################################
if __name__ == "__main__":
    
    root = tk.Tk()
    app = App(root)
    root.mainloop()
