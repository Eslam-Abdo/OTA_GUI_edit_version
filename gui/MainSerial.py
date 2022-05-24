'''
referance: https://programming.vip/docs/python-serial-communication-applet-gui-interface.html
'''
import tkinter
from tkinter import ttk
from SerialClass import SerialAchieve   # Import serial communication class
from urllib.request import urlopen

class MainSerial:
    def __init__(self):
        # Define serial port variables
        self.port = None
        self.band = None
        self.check = None
        self.data = None
        self.stop = None
        self.myserial = None

        self.hex_code = None

        # Initialize the GUI
        self.mainwin = tkinter.Tk()
        self.mainwin.title("FOTA tool")
        self.mainwin.geometry("700x290")

        # Label
        self.label1 = tkinter.Label(self.mainwin,text = "Serial Port:",font = ("Song Dynasty",15))
        self.label1.place(x = 5,y = 25)
        self.label2 = tkinter.Label(self.mainwin, text="Baud Rate:", font=("Song Dynasty", 15))
        self.label2.place(x=5, y=65)

        # Text display, clear send data
        self.label3 = tkinter.Label(self.mainwin, text="screen", font=("Song Dynasty", 20))
        self.label3.place(x=420, y=3)

        # used steps
        self.label4 = tkinter.Label(self.mainwin, text="Steps : 1- Select PORT & Baud Rate", font=("Song Dynasty", 11))
        self.label4.place(x=200, y=200)
        
        # Note Label
        self.label5 = tkinter.Label(self.mainwin, text="2- Open PORT & Check for Update", font=("Song Dynasty", 11))
        self.label5.place(x=250, y=220)
        
        # Note Label
        self.label6 = tkinter.Label(self.mainwin, text="3- Reset stm then click update now!", font=("Song Dynasty", 11))
        self.label6.place(x=250, y=240)

        self.label7 = tkinter.Label(self.mainwin, text="4- Close PORT & Exit program", font=("Song Dynasty", 11))
        self.label7.place(x=250, y=260)

        # serial port number
        self.com1value = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_port = ttk.Combobox(self.mainwin, textvariable=self.com1value,
                                          width = 10,font = ("Song Dynasty",13))
        # Enter selection
        self.combobox_port["value"] = [""]  # Select first here

        self.combobox_port.place(x = 125,y = 25)  # show

        # baud rate
        self.bandvalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_band = ttk.Combobox(self.mainwin, textvariable=self.bandvalue, width=10, font=("Song Dynasty", 13))
        # Enter selection
        self.combobox_band["value"] = ["4800","9600","14400","19200","38400","57600","115200"]  # Select first here
        self.combobox_band.current(6)  # The 0th is selected by default
        self.combobox_band.place(x=125, y=65)  # show
        self.combobox_band.bind('<<ComboboxSelected>>', func=self.band_update_change)


        # check update button
        self.button_Send = tkinter.Button(self.mainwin, text="check update",  # show text
                                            command=self.button_check_click, font=("Song Dynasty", 13),
                                            width=13, height=1)
        self.button_Send.place(x=50, y=100)  # show button

        # update now button
        self.button_Send = tkinter.Button(self.mainwin, text="update now",  # show text
                                          command=self.button_update_click, font=("Song Dynasty", 13),
                                          width=13, height=1)
        self.button_Send.place(x=50, y=140)  # show button


        # open serial port button
        self.button_OK = tkinter.Button(self.mainwin, text="Open serial port",
                                        command=self.button_OK_click, font = ("Song Dynasty",13),
                                        width = 13,height = 1)
        self.button_OK.place(x = 50,y = 190)  # show button 
        # close serial port button
        self.button_Cancel = tkinter.Button(self.mainwin, text="close serial port",  # show text
                                 command=self.button_Cancel_click, font = ("Song Dynasty",13),
                                 width=13, height=1)
        self.button_Cancel.place(x = 50,y = 230)  # show button

        # clear send data button
        self.button_Cancel = tkinter.Button(self.mainwin, text="clear screen",  # show text
                                            command=self.button_clcScreen_click, font=("Song Dynasty", 13),
                                            width=10, height=1)
        self.button_Cancel.place(x=555, y=200)  # show button

         # Exit button
        self.button_Cancel = tkinter.Button(self.mainwin, text="Exit!",  # show text
                                            command=self.mainwin.quit, font=("Song Dynasty", 13),
                                            width=6, height=1)
        self.button_Cancel.place(x=590, y=240)  # show button

        # show box
        # A functional component that implements Notepad
        self.scrollbar = tkinter.Scrollbar(self.mainwin)
        self.ScreenDataView = tkinter.Text(self.mainwin,width = 44,height = 8,
                                         font = ("Song Dynasty",13), yscrollcommand = self.scrollbar.set)  # text is actually a text editor
        self.ScreenDataView.place(x = 260,y = 37)  # show
        self.scrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )
        self.scrollbar.config(command=self.ScreenDataView.yview)
        # Get the parameters of the interface
        self.band = self.combobox_band.get()

        print("Baud rate:" , self.band)
        self.myserial = SerialAchieve(band=int(self.band))

        # Handling serial port values
        self.port_list = self.myserial.get_port()
        port_str_list = []  # Used to store the cut serial port
        for i in range(len(self.port_list)):
            # Cut out the serial port
            lines = str(self.port_list[i])
            str_list = lines.split(" ")
            port_str_list.append(str_list[0])
        self.combobox_port["value"] = port_str_list
        self.combobox_port.current(0)  # The 0th is selected by default

    def show(self):
        self.mainwin.mainloop()

    def band_update_change(self, *args):
            self.band = self.combobox_band.get()
            print("Baud rate:" , self.band)
            self.myserial.bandRate = self.band

    def button_OK_click(self):
        '''
        @ serial port open function
        :return: 
        '''
        if self.port == None or self.port.isOpen() == False:
            # Get the parameters of the interface
            self.myserial.open_port(self.combobox_port.get())
            self.print_screen("Open serial port successfully\n")
        else:
            pass

    def button_Cancel_click(self):
        self.myserial.delete_port()
        self.print_screen("Close the serial port successfully\n")

    def button_clcScreen_click(self):
        self.ScreenDataView.delete("1.0","end")

    def button_check_click(self):
        try:
            self.hex_code = self.get_hex_code()
            if self.hex_code == None:
                check = "No Update Found now!\n"
            else:
                check = "Update Found!\n"
            self.print_screen(check)
        except:
            self.print_screen("Failed to check update\n")

    def button_update_click(self):
        try:
            if self.myserial.port.isOpen() == True:
                self.print_screen("Start Updating\n")
                # print("start")
                count = 0
                for index,line in enumerate(self.hex_code):
                    self.myserial.Write_data(line)
                    # print(line)
                    check = self.myserial.Read_data()
                    # print(check)
                    while (check != 'ok'):
                        check = self.myserial.Read_data()
                        print(check)
                    count = count + 1
                    if index % 10 == 0:
                        self.print_screen('.')

                # print(count-len(self.hex_code))
                if (len(self.hex_code) - count) == 0:
                    self.print_screen("\nDone Update!\n")
                else:
                    self.print_screen("Faild Update!,please Try again later!\n")
            else:
                self.print_screen("Serial port is not open\n")
        except:
            self.print_screen("Update Failed, please check Update First!\n")


    def get_hex_code(self):
        url = "http://iot-arm.freevar.com/start_flash.php?config=allfile"
        page = urlopen(url)

        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        hex_list = html[1:-1].split('%')
        # if no file found
        if len(hex_list) < 2: 
            return None
        # hex_list.remove('')
        return hex_list

    def print_screen(self,data):
        print(data)
        self.ScreenDataView.insert(tkinter.INSERT, data)

if __name__ == '__main__':
    my_ser1 = MainSerial()
    my_ser1.show()

