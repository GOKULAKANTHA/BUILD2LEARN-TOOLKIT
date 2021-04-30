import PySimpleGUI as sg
import tkinter
from pygame import mixer
from tkinter import *
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import random 
import random as r
import calendar
from gtts import gTTS
sg.theme("DarkBlack")

layout = [
    [sg.Text("TOOLS",font=("Arial",40))],
    [sg.Button("YoutubeVideo",font=("Arial",30)),sg.Button("MusicPlayer",font=("Arial",30))],
    [sg.Button("Calculator",font=("Arial",30)),sg.Button("CurrencyConverter",font=("Arial",30))],
    [sg.Button("ImageViewer",font=("Arial",30)),sg.Button("TextToAudio",font=("Arial",30))],
    [sg.Button("NotePad",font=("Arial",30))],
    [sg.Text("GAMES",font=("Arial",40))],
    [sg.Button("TicTacToe",font=("Arial",30)),sg.Button("ColourGame",font=("Arial",30))],
    [sg.Text("                                    **Build2LearnProject**",font=("Arial",15))]
]    

current_volume = float(0.5)

colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown']
score  = 0

time = 30


window =sg.Window("TOOL APP",layout)
while True:
    event, values = window.Read()
    if event =="NotePad":
        root = Tk()
        root.geometry("350x250")
        root.title("Notes")
        root.minsize(height=250, width=350)
        root.maxsize(height=250, width=350)

        scrollbar = Scrollbar(root)

        scrollbar.pack(side=RIGHT,
                                fill=Y)


        text_info = Text(root,
                                        yscrollcommand=scrollbar.set)
        text_info.pack(fill=BOTH)

        scrollbar.config(command=text_info.yview)

        root.mainloop()


    elif event =="CurrencyConverter":
        converter = Tk()
        converter.title("Unit Converter")
        converter.geometry("600x400")

        OPTIONS = {
            "Australian Dollar":49.10,
            "Brazilian Real":17.30,
            "British Pound":90.92,
            "Chinese Yuan":10.29,
            "Euro":77.85,
            "HongKong Dollar":8.83,
            "Indonesian Rupiah":0.004864,
            "Japanese Yen":0.628,
            "Pakistani Rupee":0.49,
            "SriLankan Rupee":0.39,
            "Swiss Franc":69.62,
            "Us Dollar":69.32
                }

        def ok():
            price = rupees.get()
            answer = variable1.get()
            DICT = OPTIONS.get(answer,None)
            converted = float(DICT)*float(price)
            result.delete(1.0,END)
            result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ",INSERT,converted)
        appName = Label(converter,text="Currency Converter",font=("arial",25,"bold","underline"),fg="dark red")
        appName.place(x=150, y=10)

        result = Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
        result.place(x=125, y=60)

        india = Label(converter,text="Value in indian Rupees:",font=("arial",10,"bold"),fg="red")
        india.place(x=30, y=165)

        rupees = Entry(converter,font=("arial",20))
        rupees.place(x=200, y=160)

        choice = Label(converter,text="Choice:",font=("arial",10,"bold"),fg="red")
        choice.place(x=30, y=220)

        variable1 = StringVar(converter)
        variable1.set(None)
        option = OptionMenu(converter,variable1,*OPTIONS)
        option.place(x=100 , y=210,width=100, height=40)

        button = Button(converter,text="Convert",fg="green",font=("arial",20),bg="powder blue",command=ok)
        button.place(x=200, y=210,height=40,width=150)

        converter.mainloop()
        root.mainloop()


    elif event =="ImageViewer":
        import io
        import os
        import PySimpleGUI as sg
        from PIL import Image
        file_types = [("JPEG (*.jpg)", "*.jpg"),
                      ("All files (*.*)", "*.*")]
        def main():
            layout = [
                [sg.Image(key="-IMAGE-")],
                [
                    sg.Text("Image File"),
                    sg.Input(size=(25, 1), key="-FILE-"),
                    sg.FileBrowse(file_types=file_types),
                    sg.Button("Load Image"),
                ],
            ]
            window = sg.Window("Image Viewer", layout)
            while True:
                event, values = window.read()
                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                if event == "Load Image":
                    filename = values["-FILE-"]
                    if os.path.exists(filename):
                        image = Image.open(values["-FILE-"])
                        image.thumbnail((400, 400))
                        bio = io.BytesIO()
                        image.save(bio, format="PNG")
                        window["-IMAGE-"].update(data=bio.getvalue())
            window.close()
        if __name__ == "__main__":
            main()
                

    elif event =="Calculator":
        class Calculator:            
            def __init__(self, master):
                self.master = master
                master.title("Python Calculator")
                self.equation=Entry(master, width=36, borderwidth=5)
                self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
                self.createButton()

            def createButton(self):
                b0 = self.addButton(0)
                b1 = self.addButton(1)
                b2 = self.addButton(2)
                b3 = self.addButton(3)
                b4 = self.addButton(4)
                b5 = self.addButton(5)
                b6 = self.addButton(6)
                b7 = self.addButton(7)
                b8 = self.addButton(8)
                b9 =  self.addButton(9)
                b_add = self.addButton('+')
                b_sub = self.addButton('-')
                b_mult = self.addButton('*')
                b_div = self.addButton('/')
                b_clear = self.addButton('c')
                b_equal = self.addButton('=')

                row1=[b7,b8,b9,b_add]
                row2=[b4,b5,b6,b_sub]
                row3=[b1,b2,b3,b_mult]
                row4=[b_clear,b0,b_equal,b_div]

                r=1
                for row in [row1, row2, row3, row4]:
                    c=0
                    for buttn in row:
                        buttn.grid(row=r, column=c, columnspan=1)
                        c+=1
                    r+=1

            def addButton(self,value):

                    return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))

            def clickButton(self, value):

                current_equation=str(self.equation.get())

                if value == 'c':
                    self.equation.delete(-1, END)

                elif value == '=':
                    answer = str(eval(current_equation))
                    self.equation.delete(-1, END)
                    self.equation.insert(0, answer)

                else:
                    self.equation.delete(0, END)
                    self.equation.insert(-1, current_equation+value)

        if __name__=='__main__':

            root = Tk()
            
            my_gui = Calculator(root)

            root.mainloop()
                            
    elif event =="MusicPlayer":
        def play_song():            
            filename = filedialog.askopenfilename(initialdir="C:/",title="Please select a file")
            current_song = filename
            song_title   = filename.split("/")
            song_title   = song_title[-1]
            
            try:
                mixer.init()
                mixer.music.load(current_song)
                mixer.music.set_volume(current_volume)
                mixer.music.play()
                song_title_label.config(fg="green",text="Now playing : " + str(song_title))
                volume_label.config(fg="green",text="Volume : " + str(current_volume))
            except Exception as e:
                print(e)
                song_title_label.config(fg="red", text="Error playing track")

        def reduce_volume():
            try:
                global current_volume
                if current_volume <=0:
                    volume_label.config(fg="red", text="Volume : Muted")
                    return
                current_volume = current_volume - float(0.1) 
                current_volume = round(current_volume,1)
                mixer.music.set_volume(current_volume)
                volume_label.config(fg="green", text="Volume : "+str(current_volume))
            except Exception as e:
                print(e)
                song_title_label.config(fg="red",text="Track hasn't been selected yet")

        def increase_volume():
            try:
                global current_volume
                if current_volume >=1:
                    volume_label.config(fg="green", text="Volume : Max")
                    return
                current_volume = current_volume + float(0.1) 
                current_volume = round(current_volume,1)
                mixer.music.set_volume(current_volume)
                volume_label.config(fg="green", text="Volume : "+str(current_volume))
            except Exception as e:
                print(e)
                song_title_label.config(fg="red",text="Track hasn't been selected yet")
        def pause():
            try:
                mixer.music.pause()
            except Exception as e:
                print(e)
                song_title_label.config(fg="red",text="Track hasn't been selected yet")
        def resume():
            try:
                mixer.music.unpause()
            except Exception as e:
                print(e)
                song_title_label.config(fg="red",text="Track hasn't been selected yet")

        master = Tk()
        master.title("Music Player")

        Label(master,text="Custom Music Player",font=("Calibri",15),fg="red").grid(sticky="N",row=0,padx=120)
        Label(master,text="Please select a music track you would like to play",font=("Calibri",12),fg="blue").grid(sticky="N",row=1)
        Label(master,text="Volume",font=("Calibri",12),fg="red").grid(sticky="N",row=4)
        song_title_label = Label(master,font=("Calibri",12))
        song_title_label.grid(stick="N",row=3)
        volume_label = Label(master,font=("Calibri",12))
        volume_label.grid(sticky="N",row=5)

        Button(master, text="Select Song", font=("Calibri",12),command=play_song).grid(row=2,sticky="N")
        Button(master, text="Pause",font=("Calibri",12),command=pause).grid(row=3,sticky="E")
        Button(master, text="Resume",font=("Calibri",12),command=resume).grid(row=3,sticky="W")
        Button(master, text="-",font=("Calibri",12),width=5,command=reduce_volume).grid(row=5,sticky="W")
        Button(master, text="+",font=("Calibri",12),width=5,command=increase_volume).grid(row=5,sticky="E")

        master.mainloop()
                
    elif event == "TicTacToe":
        def button(frame):          
            b=Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
            return b
        def change_a():             
            global a
            for i in ['O','X']:
                if not(i==a):
                    a=i
                    break
        def reset():                
            global a
            for i in range(3):
                for j in range(3):
                        b[i][j]["text"]=" "
                        b[i][j]["state"]=NORMAL
            a=r.choice(['O','X'])
        def check():                
            for i in range(3):
                    if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                            messagebox.showinfo("Congrats!!","'"+a+"' has won")
                            reset()
            if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
                messagebox.showinfo("Congrats!!","'"+a+"' has won")
                reset()   
            elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
                messagebox.showinfo("Tied!!","The match ended in a draw")
                reset()
        def click(row,col):
                b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
                check()
                change_a()
                label.config(text=a+"'s Chance")
        root=Tk()               
        root.title("Tic-Tac-Toe")   
        a=r.choice(['O','X'])       
        colour={'O':"deep sky blue",'X':"lawn green"}
        b=[[],[],[]]
        for i in range(3):
                for j in range(3):
                        b[i].append(button(root))
                        b[i][j].config(command= lambda row=i,col=j:click(row,col))
                        b[i][j].grid(row=i,column=j)
        label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
        label.grid(row=3,column=0,columnspan=3)
        root.mainloop()

    elif event == "ColourGame":
        def startGame(event):

            if time==30:
                countdown()
            nextcolor()

        def nextcolor():
            global score
            global time
            if time > 0:
                colour_entry.focus_set()
                if colour_entry.get().lower() == colours[1].lower():
                    score += 1
                colour_entry.delete(0, END)
                random.shuffle(colours) 
                colour.config(fg= str(colours[1]) , text = str(colours[0]))
                scoreLabel.config(text = "Score: " + str(score))
                
        def countdown():
            global time
            if time > 0 :
                time -= 1
                timeLabel.config(text = "Time left: "+ str(time)) 
                timeLabel.after(1000, countdown)

        if __name__=='__main__':
            root = Tk() 
            root.title('Color Game') 
            root.geometry('375x200') 
            instructions = Label(root, text = 'Type in the colour of the words, and not the word text!', font = ('Helvetica', 12)) 
            instructions.pack()
            scoreLabel = Label(root, text = 'Score :'+str(score), font=('Helvetica' , 12))
            scoreLabel.pack()
            timeLabel = Label(root, text = 'Time Left : '+str(time), font=('Helvetica' , 12))
            timeLabel.pack()
            colour = Label(root, font=('Helevetica',12))
            colour.pack()
            colour_entry = Entry(root)
            colour_entry.focus_set()
            root.bind('<Return>',startGame)
            colour_entry.pack()
            
            root.mainloop()
            
    elif event == "TextToAudio":
        from tkinter import *
        from gtts import gTTS
        import os
        root = Tk()

        frame1 = Frame(root,
                                bg = "lightPink",
                                height = "150")
        frame1.pack(fill = X)


        frame2 = Frame(root,
                                bg = "lightgreen",
                                height = "750")
        frame2.pack(fill=X)

        label = Label(frame1, text = "Text to Speech",
                                font = "bold, 30",
                                bg = "lightpink")

        label.place(x = 180, y = 70)

        entry = Entry(frame2, width = 45,
                                bd = 4, font = 14)

        entry.place(x = 130, y = 52)
        entry.insert(0, "")

        def play():

                language = "en"

                myobj = gTTS(text = entry.get(),
                                        lang = language,
                                        slow = False)

                myobj.save("convert.wav")
                os.system("convert.wav")

        btn = Button(frame2, text = "SUBMIT",
                                width = "15", pady = 10,
                                font = "bold, 15",
                                command = play, bg='yellow')

        btn.place(x = 250,
                        y = 130)

        root.title("text_to_speech_convertor")

        root.geometry("650x550+350+200")
        root.mainloop()

    elif event == "YoutubeVideo":
        from tkinter import *
        from tkinter import ttk
        from tkinter import filedialog
        from pytube import YouTube 

        Folder_Name = ""

        def openLocation():
            global Folder_Name
            Folder_Name = filedialog.askdirectory()
            if(len(Folder_Name) > 1):
                locationError.config(text=Folder_Name,fg="green")

            else:
                locationError.config(text="Please Choose Folder!!",fg="red")

 
        def DownloadVideo():
            choice = ytdchoices.get()
            url = ytdEntry.get()

            if(len(url)>1):
                ytdError.config(text="")
                yt = YouTube(url)

                if(choice == choices[0]):
                    select = yt.streams.filter(progressive=True).first()

                elif(choice == choices[1]):
                    select = yt.streams.filter(progressive=True,file_extension='mp4').last()

                elif(choice == choices[2]):
                    select = yt.streams.filter(only_audio=True).first()

                else:
                    ytdError.config(text="Paste Link again!!",fg="red")



            select.download(Folder_Name)
            ytdError.config(text="Download Completed!!")



        root = Tk()
        root.title("YTD Downloader")
        root.geometry("350x400") 
        root.columnconfigure(0,weight=1)

        ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
        ytdLabel.grid()

        ytdEntryVar = StringVar()
        ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
        ytdEntry.grid()

        ytdError = Label(root,text="Error Msg",fg="red",font=("jost",10))
        ytdError.grid()

        saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
        saveLabel.grid()

        saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
        saveEntry.grid()

        locationError = Label(root,text="Error Msg of Path",fg="red",font=("jost",10))
        locationError.grid()

        ytdQuality = Label(root,text="Select Quality",font=("jost",15))
        ytdQuality.grid()

        choices = ["720p","144p","Only Audio"]
        ytdchoices = ttk.Combobox(root,values=choices)
        ytdchoices.grid()

        downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
        downloadbtn.grid()

        developerlabel = Label(root,text="",font=("jost",15))
        developerlabel.grid()
        root.mainloop()


