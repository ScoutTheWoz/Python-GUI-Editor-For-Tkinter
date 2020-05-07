from tkinter import *
import pyperclip

#Starts up the window
root = Tk()
root.geometry('350x400')
root.resizable(width=False, height=False)
#Sets up the second window, will be used for global variables such as root name
root2 = Tk()
root2.geometry('500x200')
root2.resizable(width=False, height=True)
#List of available widgets to chose from
tkvar = StringVar(root)
layOutChoice = {'Button','Label', 'Entry'}
tkvar.set('Button')

code = ""

rootName = "root"

#The Class that allows for adding widgets
class NewButtton():
    previousWidget = ""
    #creates items that need to be called
    ChoiceOfModules = OptionMenu(root,tkvar,*layOutChoice)
    enteryX = Entry(root)
    enteryY = Entry(root)
    enteryName = Entry(root)
    codeButtonName = Entry(root)

    fullcode = ""
    def __init__(self):
        #spawns buttons that don't need to be called
        btnSpawn = Button(root, text="Spawn Button",command=self.newButton)
        btnSpawn.place(x=130,y=0)
        #places items made from top of class
        self.enteryX.place(x=0, y=0)
        self.enteryY.place(x=225, y=0)
        self.enteryName.place(x=0,y=30)
        self.codeButtonName.place(x=225, y=30)
        self.ChoiceOfModules.place(x=131.5,y=20)
        
    #Creates a new Label or Button
    def newButton(self):
        #Sets variables needed for the widgets to spawn
        newBX = self.enteryX.get()
        newBY = str(int(self.enteryY.get()) + 75)
        newBtext = self.enteryName.get()
        newButtonCodeName = self.codeButtonName.get()
        newButton = displayButton()
        newButton.place(newBtext,newBX,newBY)
        #Creates a label or button for preview by seeing what is selected in the selection box
        print(tkvar.get())
        #Creates new code for the new widget and then adds that to the fullcode variable
        ButtonCode = newButtonCodeName +" = " + str(tkvar.get()) + "(root,text=" + "'" + newBtext + "'" +")\n" + newButtonCodeName + ".place(x=" + newBX + ", y=" + str(int(newBY) - 75) + ")\n"
        print(ButtonCode)
        self.fullcode = self.fullcode + ButtonCode
        print(self.fullcode)
        code = self.fullcode
    
    #prints the code to the command line
    #CHANGE: Make it print to a text file or copy it the clipboard

    
class OtherOptions():
    CodeLabel = Label(root2,text="")
    def __init__(self):
        updateRootButton = Button(root2,text="Update",command=self.update)
        updateRootButton.grid(row=1,column=0)
        copyCodeButton = Button(root2,text="Copy The Code",command=self.copyCode)
        copyCodeButton.grid(row=1,column=1)
        self.CodeLabel.grid(row=0,column=0)
        undoButton = Button(root2,text="Undo",command=self.undoPreviousWidget)
        undoButton.grid(row=1,column=2)
    
    def update(self):
        self.CodeLabel['text'] = WidgetCreater.fullcode
    
    def copyCode(self):
        pyperclip.copy(WidgetCreater.fullcode)
    
    def undoPreviousWidget(self):
        WidgetCreater.previousWidget.destroy()
        
class displayButton():
    
    
    def place(self, textvalue, xvalue, yvalue):
        selfButton = Button(root,text="test")
        selfButton['text'] = textvalue
        selfButton['command'] = self.removeButton
        selfButton.place(x=xvalue,y=yvalue)
        self.button = selfButton

    def __delete__(self):
        print("removed")

    def removeButton(self):
        self.button.destroy()
        




#Creates The Widget Creater
WidgetCreater = NewButtton()
OptionsMenu = OtherOptions()
#mainloop for tkinter
root.mainloop()
root2.mainloop()
