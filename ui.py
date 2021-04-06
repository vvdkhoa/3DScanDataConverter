import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=374
        height=254
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_804=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "left"
        GLabel_804["text"] = "SETTINGS: "
        GLabel_804.place(x=10,y=0,width=70,height=25)

        GLabel_426=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "left"
        GLabel_426["text"] = "FreeCAD Path"
        GLabel_426.place(x=10,y=150,width=100,height=30)

        GLabel_101=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_101["font"] = ft
        GLabel_101["fg"] = "#333333"
        GLabel_101["justify"] = "left"
        GLabel_101["text"] = "HC Smooth"
        GLabel_101.place(x=10,y=30,width=100,height=30)

        GLabel_902=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_902["font"] = ft
        GLabel_902["fg"] = "#333333"
        GLabel_902["justify"] = "left"
        GLabel_902["text"] = "Poisson Iters"
        GLabel_902.place(x=10,y=60,width=100,height=30)

        GLabel_618=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_618["font"] = ft
        GLabel_618["fg"] = "#333333"
        GLabel_618["justify"] = "left"
        GLabel_618["text"] = "Target Facenum"
        GLabel_618.place(x=10,y=90,width=100,height=30)

        GLabel_903=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_903["font"] = ft
        GLabel_903["fg"] = "#333333"
        GLabel_903["justify"] = "left"
        GLabel_903["text"] = "Shape Tolerance"
        GLabel_903.place(x=10,y=120,width=100,height=30)

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
        GButton_878.place(x=220,y=210,width=145,height=30)
        GButton_878["command"] = self.GButton_878_command

        GMessage_707=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_707["font"] = ft
        GMessage_707["fg"] = "#333333"
        GMessage_707["justify"] = "left"
        GMessage_707["text"] = "Message"
        GMessage_707["relief"] = "ridge"
        GMessage_707.place(x=210,y=30,width=159,height=137)

        GCheckBox_402=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_402["font"] = ft
        GCheckBox_402["fg"] = "#333333"
        GCheckBox_402["justify"] = "center"
        GCheckBox_402["text"] = "IGES"
        GCheckBox_402.place(x=300,y=170,width=58,height=30)
        GCheckBox_402["offvalue"] = "0"
        GCheckBox_402["onvalue"] = "1"
        GCheckBox_402["command"] = self.GCheckBox_402_command

        GCheckBox_75=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_75["font"] = ft
        GCheckBox_75["fg"] = "#333333"
        GCheckBox_75["justify"] = "center"
        GCheckBox_75["text"] = "STEP"
        GCheckBox_75.place(x=220,y=170,width=58,height=31)
        GCheckBox_75["offvalue"] = "0"
        GCheckBox_75["onvalue"] = "1"
        GCheckBox_75["command"] = self.GCheckBox_75_command

        GLabel_601=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_601["font"] = ft
        GLabel_601["fg"] = "#333333"
        GLabel_601["justify"] = "left"
        GLabel_601["text"] = "Save As"
        GLabel_601.place(x=10,y=180,width=100,height=30)

        GLabel_348=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_348["font"] = ft
        GLabel_348["fg"] = "#333333"
        GLabel_348["justify"] = "left"
        GLabel_348["text"] = "Input Folder"
        GLabel_348.place(x=10,y=210,width=100,height=30)

        GLineEdit_253=tk.Entry(root)
        GLineEdit_253["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_253["font"] = ft
        GLineEdit_253["fg"] = "#333333"
        GLineEdit_253["justify"] = "left"
        GLineEdit_253["text"] = ""
        GLineEdit_253.place(x=110,y=30,width=95,height=25)
        GLineEdit_253["show"] = "222"
        GLineEdit_253["invalidcommand"] = "Command1"
        GLineEdit_253["validatecommand"] = "Command2"
        GLineEdit_253.insert(0, '2222')

        GLineEdit_770=tk.Entry(root)
        GLineEdit_770["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_770["font"] = ft
        GLineEdit_770["fg"] = "#333333"
        GLineEdit_770["justify"] = "left"
        GLineEdit_770["text"] = ""
        GLineEdit_770.place(x=110,y=60,width=95,height=25)

        GLineEdit_472=tk.Entry(root)
        GLineEdit_472["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_472["font"] = ft
        GLineEdit_472["fg"] = "#333333"
        GLineEdit_472["justify"] = "left"
        GLineEdit_472["text"] = ""
        GLineEdit_472.place(x=110,y=90,width=95,height=25)

        GLineEdit_658=tk.Entry(root)
        GLineEdit_658["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_658["font"] = ft
        GLineEdit_658["fg"] = "#333333"
        GLineEdit_658["justify"] = "left"
        GLineEdit_658["text"] = ""
        GLineEdit_658.place(x=110,y=120,width=95,height=25)

        GLineEdit_533=tk.Entry(root)
        GLineEdit_533["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_533["font"] = ft
        GLineEdit_533["fg"] = "#333333"
        GLineEdit_533["justify"] = "left"
        GLineEdit_533["text"] = ""
        GLineEdit_533.place(x=110,y=150,width=95,height=25)

        GLineEdit_664=tk.Entry(root)
        GLineEdit_664["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_664["font"] = ft
        GLineEdit_664["fg"] = "#333333"
        GLineEdit_664["justify"] = "left"
        GLineEdit_664["text"] = ""
        GLineEdit_664.place(x=110,y=180,width=95,height=25)

        GLineEdit_517=tk.Entry(root)
        GLineEdit_517["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_517["font"] = ft
        GLineEdit_517["fg"] = "#333333"
        GLineEdit_517["justify"] = "left"
        GLineEdit_517["text"] = ""
        GLineEdit_517.place(x=110,y=210,width=95,height=25)

    def GButton_878_command(self):
        print("command")
        print()


    def GCheckBox_402_command(self):
        print("command")


    def GCheckBox_75_command(self):
        print("command")


    def Command1(self):
        print("invalidcommand")

    def Command2(self):
        print("validatecommand")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
