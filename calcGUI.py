# Written by siembra1978
from tkinter import *
import calculator
import otherGUI
import internet
import config

# Sets Local Variable Corresponding to config.py (May change to a YAML or JSON File Type)
currentStatus = config.status

# Sets Up Entry GUI Class
class entryGUI:

    def __init__(self, master):

        # Sets master to itself
        self.master = master

        # Sets Window Title and Size
        master.title('Calvin the Calculator')
        #master.geometry('380x195')
        master.configure(bg='gray1')
        master.iconbitmap('Diamond Pickaxe.ico')

        # Create and Set master frame
        self.window = Frame(master,
                            # height=240,
                            # width=320,
                            bg='white',
                            cursor='dot'
                            )
        self.window.pack()  # Pack frame into window

        # Create and Set Listbox object for entries
        self.entries = Listbox(self.window, width=52, height=13, font='Courier 11', bg='gray9', fg='white')
        self.entries.pack(side=TOP)  # Pack listbox into frame at top

        # Create and Set Entry
        self.entry = Entry(self.window, width=52, bg='gray9', fg='white', font= 'Courier 11')
        self.entry.pack(side=BOTTOM)

        # Set Binds for Program Functionality
        self.entry.bind('<Return>', self.devEntry)  # Press Enter/Return to send an entry into the calculator

        self.entry.bind('<Tab>', self.openYVars)  # [EXPERIMENTAL]

        self.entry.focus_set()  # Sets GUI focus on the entry bar

        # Creates and Sets top bar for menu
        self.bar = Menu(self.master)
        self.master.config(menu=self.bar)

        # Adds cascades to the bar, corresponding with config.py
        #self.graph = Menu(self.bar)
        #self.bar.add_cascade(label=currentStatus, menu=self.graph)

    # Function to put the solution into the list box
    def giveAnswer(self, answer):
        self.entries.insert(END, 'CAL> ' + str(answer))
        self.entries.yview(END)
        #self.bar.entryconfig(1, label='Idle')

    # Function to be performed when 'Enter' is pressed
    def devEntry(self, event):
        print('Pressed Enter')  # Debug Test

        value = self.entry.get()  # Grabs the entry from the entry bar
        strvalue = str(value)  # Turn the entry into a String variable type

        self.entry.delete(0, END)  # Deletes the contents of the Entry bar
        self.entries.insert(END, 'USR> ' + value)  # Inserts the previous content of the Entry bar into the Listbox
        self.entries.yview(END)  # Takes the GUI to the bottom of the Listbox

        # Checks for an internet connection
        if internet.is_connected(internet.REMOTE_SERVER):
            print('Internet Connection Detected. Using WolfRamAlpha.')  # Use WolfRamAlpha if an Internet Connection is available

            #self.bar.entryconfig(1, label="Loading...")
            #print("Loading...")

            answer = calculator.wolframCalc.answer(strvalue)  # Contacts the calculator with the entry using WolfRamAlpha
            self.giveAnswer(answer)  # Returns the solution to the giveAnswer() function

            '''
            try:
                answer = calculator.wolframCalc.answer(strvalue)  # Contacts the calculator with the entry using WolfRamAlpha
                self.giveAnswer(answer)  # Returns the solution to the giveAnswer() function
            except:
                self.giveAnswer('(WiFi: On) ERROR: INVALID EXPRESSION')  # If WolfRamAlpha is unable to give an answer
            '''

        elif not internet.is_connected(internet.REMOTE_SERVER):
            print(
                'No Internet Connection Detected. Using Offline Calculator.')  # Using eval() in the lack of an
            # internet connection
            
            try:
                answer = calculator.calculate(strvalue)  # Contacts Calculator with the entry uding eval()
                self.giveAnswer(answer)  # Returns the solution to the giveAnswer() function
            except:
                self.giveAnswer('(WiFi: Off) ERROR: INVALID EXPRESSION')  # If eval() is unable to give an answer

    def openYVars(self, event):
        print('Pressed')
        otherGUI.startY()


print('Calculator GUI Imported')


# Creates a Tk object using an instance of the EntryGUI Class
def startGUI():
    root = Tk()
    primaryGUI = entryGUI(root)
    root.mainloop()
