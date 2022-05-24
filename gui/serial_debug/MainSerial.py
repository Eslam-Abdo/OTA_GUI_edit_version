'''
referance: https://programming.vip/docs/python-serial-communication-applet-gui-interface.html
'''
import tkinter
from tkinter import ttk
from SerialClass import SerialAchieve   # Import serial communication class

class MainSerial:
    def __init__(self):
        # Define serial port variables
        self.port = None
        self.band = None
        self.check = None
        self.data = None
        self.stop = None
        self.myserial = None

        # Initialize the GUI
        self.mainwin = tkinter.Tk()
        self.mainwin.title("Serial debugging tool")
        self.mainwin.geometry("700x400")

        # Label
        self.label1 = tkinter.Label(self.mainwin,text = "Serial Port:",font = ("Song Dynasty",15))
        self.label1.place(x = 5,y = 5)
        self.label2 = tkinter.Label(self.mainwin, text="baud rate:", font=("Song Dynasty", 15))
        self.label2.place(x=5, y=45)
        self.label3 = tkinter.Label(self.mainwin, text="check bit:", font=("Song Dynasty", 15))
        self.label3.place(x=5, y=85)
        self.label4 = tkinter.Label(self.mainwin, text="data bits:", font=("Song Dynasty", 15))
        self.label4.place(x=5, y=125)
        self.label5 = tkinter.Label(self.mainwin,text = "stop bit:",font = ("Song Dynasty",15))
        self.label5.place(x = 5,y = 165)

        # Text display, clear send data
        self.label6 = tkinter.Label(self.mainwin, text="send data:", font=("Song Dynasty", 15))
        self.label6.place(x=260, y=5)

        self.label7 = tkinter.Label(self.mainwin, text="Receive data:", font=("Song Dynasty", 15))
        self.label7.place(x=260, y=200)

        # serial port number
        self.com1value = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_port = ttk.Combobox(self.mainwin, textvariable=self.com1value,
                                          width = 10,font = ("Song Dynasty",13))
        # Enter selection
        self.combobox_port["value"] = [""]  # Select first here

        self.combobox_port.place(x = 125,y = 5)  # show

        # baud rate
        self.bandvalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_band = ttk.Combobox(self.mainwin, textvariable=self.bandvalue, width=10, font=("Song Dynasty", 13))
        # Enter selection
        self.combobox_band["value"] = ["4800","9600","14400","19200","38400","57600","115200"]  # Select first here
        self.combobox_band.current(6)  # The 0th is selected by default
        self.combobox_band.place(x=125, y=45)  # show

        # Check bit
        self.checkvalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_check = ttk.Combobox(self.mainwin, textvariable=self.checkvalue, width=10, font=("Song Dynasty", 13))
        # Enter selection
        self.combobox_check["value"] = ["No"]  # Select first here
        self.combobox_check.current(0)  # The 0th is selected by default
        self.combobox_check.place(x=125, y=85)  # show

        # data bits
        self.datavalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_data = ttk.Combobox(self.mainwin, textvariable=self.datavalue, width=10, font=("Song Dynasty", 13) )
        # Enter selection
        self.combobox_data["value"] = ["8", "9", "0"]  # Select first here
        self.combobox_data.current(0)  # The 0th is selected by default
        self.combobox_data.place(x=125, y=125)  # show

        # stop bit
        self.stopvalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_stop = ttk.Combobox(self.mainwin, textvariable=self.stopvalue, width=10, font=("Song Dynasty", 13))
        # Enter selection
        self.combobox_stop["value"] = ["1", "0"]  # Select first here
        self.combobox_stop.current(0)  # The 0th is selected by default
        self.combobox_stop.place(x=125, y=165)  # show

        # Press the show button to open the serial port
        self.button_OK = tkinter.Button(self.mainwin, text="Open serial port",
                                        command=self.button_OK_click, font = ("Song Dynasty",13),
                                        width = 13,height = 1)
        self.button_OK.place(x = 5,y = 210)  # show button 
        # close serial port
        self.button_Cancel = tkinter.Button(self.mainwin, text="close serial port",  # show text
                                 command=self.button_Cancel_click, font = ("Song Dynasty",13),
                                 width=13, height=1)
        self.button_Cancel.place(x = 5,y = 255)  # show button

        # clear send data
        self.button_Cancel = tkinter.Button(self.mainwin, text="clear send data",  # show text
                                            command=self.button_clcSend_click, font=("Song Dynasty", 13),
                                            width=13, height=1)
        self.button_Cancel.place(x=500, y=2)  # show button

        # Clear receive data
        self.button_Cancel = tkinter.Button(self.mainwin, text="Clear receive data",  # show text
                                            command=self.button_clcRece_click, font=("Song Dynasty", 13),
                                            width=13, height=1)
        self.button_Cancel.place(x=500, y=197)  # show button

        # send button
        self.button_Send = tkinter.Button(self.mainwin, text="send",  # show text
                                            command=self.button_Send_click, font=("Song Dynasty", 13),
                                            width=6, height=1)
        self.button_Send.place(x=5, y=310)  # show button

        # receive button
        self.button_Send = tkinter.Button(self.mainwin, text="receive",  # show text
                                          command=self.button_Rece_click, font=("Song Dynasty", 13),
                                          width=6, height=1)
        self.button_Send.place(x=5, y=355)  # show button

        # show box
        # A functional component that implements Notepad
        self.SendDataView = tkinter.Text(self.mainwin,width = 38,height = 7,
                                         font = ("Song Dynasty",13))  # text is actually a text editor
        self.SendDataView.place(x = 260,y = 37)  # show

        self.ReceDataView = tkinter.Text(self.mainwin, width=38, height=7,
                                         font=("Song Dynasty", 13))  # text is actually a text editor
        self.ReceDataView.place(x=260, y=232)  # show

        # sent content
        test_str = tkinter.StringVar(value="Hello")
        self.entrySend = tkinter.Entry(self.mainwin, width=10,textvariable = test_str,font = ("Song Dynasty",15))
        self.entrySend.place(x = 115,y = 315)  # show

        # Get the parameters of the interface
        self.band = self.combobox_band.get()
        self.check = self.combobox_check.get()
        self.data = self.combobox_data.get()
        self.stop = self.combobox_stop.get()
        print("Baud rate:"+self.band)
        self.myserial = SerialAchieve(int(self.band),self.check,self.data,self.stop)

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

    def button_OK_click(self):
        '''
        @ serial port open function
        :return: 
        '''
        if self.port == None or self.port.isOpen() == False:
            self.myserial.open_port(self.combobox_port.get())
            print("Open serial port successfully")
        else:
            pass

    def button_Cancel_click(self):
        self.myserial.delete_port()
        print("Close the serial port successfully")

    def button_clcSend_click(self):
        self.SendDataView.delete("1.0","end")

    def button_clcRece_click(self):
        self.ReceDataView.delete("1.0", "end")

    def button_Send_click(self):
        try:
            if self.myserial.port.isOpen() == True:
                print("start sending data")
                send_str1 = self.entrySend.get()
                self.myserial.Write_data(send_str1)
                self.SendDataView.insert(tkinter.INSERT, send_str1+" ")
                print("Send data successfully")
            else:
                print("Serial port is not open")
        except:
            print("Failed to send")
    def button_Rece_click(self):
        try:
            readstr = self.myserial.Read_data()
            self.ReceDataView.insert(tkinter.INSERT, readstr + " ")
        except:
            print("read failed")
if __name__ == '__main__':
    my_ser1 = MainSerial()
    my_ser1.show()
