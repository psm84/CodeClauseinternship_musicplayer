# you can import this module
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer

mixer.init()

class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        self.root.title('music_player')
        self.root.geometry()
        self.root.configure(background='black')

    
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()


        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='file',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='Exit',command=self.root.destroy)

        def About():
            tkinter.messagebox.showinfo('About Us','Muisc Player Created By Prajwal Mohite')

        self.submenu2=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Help',menu=self.submenu2)
        self.submenu2.add_command(label='About',command=About)

        
        self.label=Label(text='select and play',bg='white',font=22).place(x=70,y=30)
        

        self.L_photo=ImageTk.PhotoImage(file='left_side.png')
        L_photo=Label(self.root,image=self.L_photo,bg='black').place(x=15,y=60, width=1000, height=500)


        self.photo=ImageTk.PhotoImage(file='bg.png')
        photo=Label(self.root,image=self.photo,bg='black').place(x=5,y=60,width=500,height=300)

        self.label1=Label(self.root,text='Lets play it.',fg='black',font=10)
        self.label1.pack(side=BOTTOM,fill=X)

        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']='music_playing..'
                except:
                    tkinter.messagebox.showerror('Error','file could not found please select song')
            else:
                mixer.music.unpause()
                self.label1['text']='Music_unpaused'

        self.photo_b1=ImageTk.PhotoImage(file='play.png')
        photo_b1=Button(self.root,image=self.photo_b1,bd=0,command=playmusic).place(x=80,y=350,width=30,height=25)




        def pausemusic():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label1['text']='music_pause..'
        
        self.photo_b2=ImageTk.PhotoImage(file='pause.png')
        photo_b2=Button(self.root,image=self.photo_b2,bd=0,command=pausemusic).place(x=160,y=350,width=30,height=25)

       
       
       
        def stopmusic():
            mixer.music.stop()
            self.label1['text']='music_stoped..'

        self.photo_b3=ImageTk.PhotoImage(file='stop.png')
        photo_b3=Button(self.root,image=self.photo_b3,bd=0,command=stopmusic).place(x=240,y=350,width=30,height=25)

        def mute():
            self.scale.set(0)
            self.mute=ImageTk.PhotoImage(file='mute.png')
            mute=Button(self.root,image=self.mute,command=unmute).place(x=320,y=350,width=30,height=25)
            self.label1['text']='Music_mute...'

        def unmute():
            self.scale.set(25)
            self.volimg=ImageTk.PhotoImage(file='volume.png')
            volimg=Button(self.root,image=self.volimg,command=mute).place(x=320,y=350,width=30,height=25)
            self.label1['text']='Music_unmute...'





        self.volimg=ImageTk.PhotoImage(file='volume.png')
        volimg=Button(self.root,image=self.volimg,command=mute).place(x=320,y=350,width=30,height=25)

        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)



        self.scale=Scale(self.root,from_=0,to=100,bg='cyan',orient=HORIZONTAL,length=120,command=volume)
        self.scale.set(25)
        self.scale.place(x=370.,y=350,height=30)

         


root=Tk()
obj=musicplayer(root)
root.mainloop()
