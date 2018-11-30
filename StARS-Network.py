from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter.font import *
import pywifi
from pywifi import const
import time
 
root = Tk()
root.title("StARS WiFi Gate")
root.configure(bg='snow')

# Methods for the Widgets

def changecol1():
    lab2.config(image=img2, bg='snow')
                
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)
    assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = Password

    #iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(30)
    assert iface.status() == const.IFACE_CONNECTED
  
# Add a grid #Main Window

mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 50, padx = 50)
mainframe.configure(bg='snow')


#images

img1 = PhotoImage(file="C:/Users/Abdullah.H/Desktop/python/pics/closed gate.png")
img2 = PhotoImage(file="C:/Users/Abdullah.H/Desktop/python/pics/open gate.png")
img3 = PhotoImage(file="C:/Users/Abdullah.H/Desktop/python/pics/connect.png")
img4 = PhotoImage(file="C:/Users/Abdullah.H/Desktop/python/StARS Logo Transparent1.png")

#Labels

lab2 = Label (mainframe, image=img4, bg='snow')
lab2.grid(row = 2, column =4, sticky='')

lab3 = Label(mainframe, image=img1, bg='snow')
lab3.grid(row = 3, column =4, sticky='')




# Create a Tkinter variable

tkvar = StringVar(root)
tkvar1 = StringVar(root)
tkvar2 = StringVar(root)
tkvar3 = StringVar(root)


# Dictionary with options

choice1 = "Essaf"
choice2 = "Maadi"
choice15 = "HUB"
popupMenu = OptionMenu(mainframe, tkvar, choice1, choice2, choice15)

# on change dropdown value
    
def change_dropdown(*args):
        print( tkvar.get() )
        if tkvar.get()== choice1:
            choice3 = "StARS__MGT2"
            choice4 = "StARS__MGT"
            choice5 = "StARS-RLAP"
            choice6 = "StARS-PS"
            choice7 = "StARS_GildHall"
            choice8 = "StARS_ARC"
            choice9 = "StARS_Caravan"
            popupMenu1 = OptionMenu(mainframe, tkvar1, choice3, choice4, choice5, choice6,
                                choice7, choice8, choice9)
            
    # on change dropdown value
            
            def change_dropdown(*args):
                print( tkvar1.get() )
                if tkvar1.get()== choice3:
                    ssid = tkvar1.get()
                    password = 'Sep@pass@2018'
                elif tkvar1.get()== choice4:
                    ssid = tkvar1.get()
                    password = 'Sep@pass@201'
                elif tkvar1.get()== choice5:
                    ssid = tkvar1.get()
                    password = 'ITpass@stars@2018'
                elif tkvar1.get()== choice6:
                    ssid = tkvar1.get()
                    password = 'ITpass@stars@2018'
                elif tkvar1.get()== choice7:
                    ssid = tkvar1.get()
                    password = 'ITpass@stars@2018'
                elif tkvar1.get()== choice8:
                    ssid = tkvar1.get()
                    password = 'ITpass@stars@2018'
                elif tkvar1.get()== choice9:
                    ssid = tkvar1.get()
                    password = 'ITpass@stars@2018'
                
    # link function to change dropdown
            
            tkvar1.trace('w', change_dropdown)
    
            Label(mainframe, text="Choose a Network", bg='snow').grid(row = 6, column = 4, sticky='')
            popupMenu1.grid(row = 7, column =4, sticky='')


        elif tkvar.get()== choice2:
            choice10 = "StARS_Maadi 2"
            choice11 = "StARS Maadi 3"
            choice12 = "Maadi_Teachers_Room"
            choice13 = "Maadi_School"
            choice14 = "Maadi-Rooftop"
            popupMenu2 = OptionMenu(mainframe, tkvar1 ,choice10, choice11, choice12,
                                    choice13, choice14)
# on change dropdown value
            
            def change_dropdown(*args):
                print( tkvar1.get() )
                if tkvar1.get()== choice10:
                        ssid = tkvar1.get()
                        password = 'ITpass@stars@2018'
                elif tkvar1.get()== choice11:
                        ssid = tkvar1.get()
                        password = 'ITpass@stars@2018' 
                        
                elif tkvar1.get()== choice12:
                        ssid = tkvar1.get()
                        password = 'ITpass@stars@2018' 
                        
                elif tkvar1.get()== choice13:
                        ssid = tkvar1.get()
                        password = 'ITpass@stars@2018' 
                        
                elif tkvar1.get()== choice14:
                        ssid = tkvar1.get()
                        password = 'ITpass@stars@2018' 
                        
                
    # link function to change dropdown
            
            tkvar1.trace('w', change_dropdown)
            Label(mainframe, text="Choose a Network", bg='snow').grid(row = 6, column = 4,sticky='')
            popupMenu2.grid(row = 7, column =4, sticky='')



# link function to change dropdown

tkvar.trace('w', change_dropdown)

Label(mainframe, text="Choose a Site", bg='snow').grid(row = 4, column = 4,sticky='')
popupMenu.grid(row = 5, column =4, sticky='')



#Buttons

butt = Button(mainframe, image=img3, text="Sign in", bg='snow')
butt.grid(row = 8, column =4, sticky='')

root.mainloop()
