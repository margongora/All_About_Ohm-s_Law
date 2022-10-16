from tkinter import *


# Base class
class Window(Toplevel):
    def __init__(self, par):
        super().__init__(par)

        self.geometry('600x500')
        self.configure(background='#E5E4E2')


# Extended versions of the Window class
class VWindow(Window):
    def __init__(self, par):
        super().__init__(par)

        # Config
        self.title('Voltage')

        # Info
        Label(self, height=1, text='', bg='#E5E4E2').pack()
        Label(self, height=1, width=19, font=('Andale Mono', 40, 'bold'),
              text='Voltage', bg='#D3D3D3', fg='#D22B2B', borderwidth=5, relief='solid').pack()
        Label(self, height=1, width=28, font=('Andale Mono', 40, 'bold'),
              text='-----------------------------', bg='#E5E4E2').pack(side=TOP)

        # Main box
        text = """VOLTAGE is the change in ELECTRIC 
POTENTIAL between two points.\n
The more CURRENT you have, the more 
VOLTAGE you'll have, as long as 
RESISTANCE stays the same.

VOLTAGE is measured in VOLTS (V)!
        """
        Label(self, height=15, width=37, font=('Andale Mono', 20, 'bold'), bg='#D3D3D3',
                borderwidth=5, relief='solid', text=text).pack()
        


class IWindow(Window):
    def __init__(self, par):
        super().__init__(par)

        # Config
        self.title('Current')

        # Info
        Label(self, height=1, text='', bg='#E5E4E2').pack()
        Label(self, height=1, width=19, font=('Andale Mono', 40, 'bold'),
              text='Current', bg='#D3D3D3', fg='#1434A4', borderwidth=5, relief='solid').pack()
        Label(self, height=1, width=28, font=('Andale Mono', 40, 'bold'),
              text='-----------------------------', bg='#E5E4E2').pack(side=TOP)

        text="""CURRENT is how much 
POWER / CHARGE (electricity)
moves through a CIRCUIT.\n
The more VOLTAGE you have, the more
CURRENT you'll have, as long as
RESISTANCE stays the same.\n
CURRENT is measuered in AMPERES (A)! 
        """
        Label(self, height=15, width=37, font=('Andale Mono', 20, 'bold'), bg='#D3D3D3',
              borderwidth=5, relief='solid', text=text).pack()


class RWindow(Window):
    def __init__(self, par):
        super().__init__(par)

        # Config
        self.title('Resistance')

        # Info
        Label(self, height=1, text='', bg='#E5E4E2').pack()
        Label(self, height=1, width=19, font=('Andale Mono', 40, 'bold'),
              text='Resistance', bg='#D3D3D3', fg='#228B22', borderwidth=5, relief='solid').pack()
        Label(self, height=1, width=28, font=('Andale Mono', 40, 'bold'),
              text='-----------------------------', bg='#E5E4E2').pack(side=TOP)

        # Main box
        text="""RESISTANCE is what slows CURRENT
from moving in a CIRCUIT.\n
The more RESISTANCE you have,
the less CURRENT you'll have.
VOLTAGE may get bigger, since it
depends on both CURRENT and
RESISTANCE.\n
RESISTANCE is measured in OHMS (Ω)!
        """
        Label(self, height=15, width=37, font=('Andale Mono', 20, 'bold'), bg='#D3D3D3',
              borderwidth=5, relief='solid', text=text).pack()


class App(Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.geometry('650x500')
        self.title('All About Ohm\'s Law')
        self.configure(background='#E5E4E2')

        # Display info
        Label(self, height=1, text='', bg='#E5E4E2').pack()
        Label(self, height=1, width=19, font=('Andale Mono', 40, 'bold'), text='All About Ohm\'s Law', bg='#D3D3D3', borderwidth=5, relief='solid').pack()
        Label(self, height=1, width=28, font=('Andale Mono', 40, 'bold'), text='-----------------------------', bg='#E5E4E2').pack(side=TOP)
        Label(self, height=1, width=15, text='V = I•R', font=(
            'Andale Mono', 35, 'bold'), bg='#D3D3D3', borderwidth=5, relief='solid').pack()
        Label(self, height=1, text='', bg='#E5E4E2').pack()

        Label(self, height=1, width=19, font=('Andale Mono', 30, 'bold'), text='Click to learn more:', bg='#E5E4E2').pack()

        # Buttons
        Button(self, height=1, width=14, text='V : VOLTS', font=('Andale Mono', 30),
               relief='flat', command=lambda: self.open_window('V'), activeforeground='#D22B2B').pack()
        Label(self, height=1, text='', bg='#E5E4E2').pack()
        
        Button(self, height=1, width=14, text='I : CURRENT', font=('Andale Mono', 30), 
               relief='flat', command=lambda: self.open_window('I'), activeforeground='#1434A4').pack()
        Label(self, height=1, text='', bg='#E5E4E2').pack()

        Button(self, height=1, width=14, text='R : RESISTANCE', font=('Andale Mono', 30), 
               relief='flat', command=lambda: self.open_window('W'), activeforeground='#228B22').pack()


    # Opens windows based on certain types
    def open_window(self, type):
        print('Opening window...')
        if type == 'V':
            VWindow(self).grab_set()
        elif type == 'I':
            IWindow(self).grab_set()
        else:
            RWindow(self).grab_set()


if __name__ == '__main__':
    app = App()
    app.mainloop()
    