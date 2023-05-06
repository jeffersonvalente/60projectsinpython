import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()
    
    
class windows1: #tela principal
    def __init__(self,master):
        self.master = master
        self.master.title("Sistema de Gestão da Farmácia")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Username = StringVar
        self.Password = StringVar
        
        self.LableTitle = Label(self.frame, text = "   Sistema de Gestão da Farmácia   ", font= ("arial",40,"bold"),
                                bd= 10,relief = "sunken")
        self.LableTitle.grid(row = 0, column = 0, columnspan = 2, pady=20)
        
        self.LoginFrame1 = Frame(self.frame, width= 1000, height= 300, bd= 10, relief="groove")
        self.LoginFrame1.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame, width= 1000, height= 100, bd= 10, relief="groove")
        self.LoginFrame2.grid(row=2,column=0,pady = 15)
        
        self.LoginFrame3 = Frame(self.frame, width= 1000, height= 200, bd= 10, relief="groove")
        self.LoginFrame3.grid(row=6,column=0, pady= 5)
        
        self.button_reg = Button(self.LoginFrame3,text = "Tela de registro de paciente", font=("arial",15,"bold"),
                                 command= self.Registration_window)
        self.button_reg.grid(row=0, column= 0, padx= 10, pady= 10)
        
        self.button_Hosp = Button(self.LoginFrame3,text = "Tela de registro de paciente", font=("arial",15,"bold"),
                                 command= self.Hospital_window)
        self.button_Hosp.grid(row=0, column= 1, padx= 10, pady= 10)
        
        self.button_Dr_appt = Button(self.LoginFrame3,text = "Tela de registro de paciente", font=("arial",15,"bold"),
                                 command= self.Dr_Apoint_window)
        self.button_Dr_appt.grid(row=1, column= 0, padx= 10, pady= 10)
        
        self.button_med_stock = Button(self.LoginFrame3,text = "Tela de registro de paciente", font=("arial",15,"bold"),
                                 command= self.Medicine_stock)
        self.button_med_stock.grid(row=1, column= 1, padx= 10, pady= 10)
        
        #login
        self.LabelUsername = Label(self.LoginFrame1, text = "Usuario", font = ("arial",20,"bold"),bd =3)
        self.LabelUsername.grid(row=0,column=0)
        
        self.textUsername = Entry(self.LoginFrame1, font = ("arial",20,"bold"), bd = 3, textvariable= self.Username)
        self.textUsername.grid(row=0, column= 1, padx=40, pady=15)
        
        self.LabelPassword = Label(self.LoginFrame1, text = "Senha", font = ("arial",20,"bold"),bd =3)
        self.LabelPassword.grid(row=1,column=0)
        
        self.textPassword = Entry(self.LoginFrame1, font = ("arial",20,"bold"), bd = 3, textvariable= self.Password)
        self.textPassword.grid(row=1, column= 1, padx=40, pady=15)
        

        
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows2(self.newWindow)
    
    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows3(self.newWindow)
    
    def Dr_Apoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows4(self.newWindow)
    
    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)
        
    
class windows2:
    def __init__(self,master):
        self.master = master
        self.master.title("Sistema de Gestão da Paciente")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows3:
    def __init__(self,master):
        self.master = master
        self.master.title("Sistema de Gestão do Hospital")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows4:
    def __init__(self,master):
        self.master = master
        self.master.title("Sistema de Gestão do Doutor")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


class windows5:
    def __init__(self,master):
        self.master = master
        self.master.title("Sistema de Tratamento")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main__":
    main()