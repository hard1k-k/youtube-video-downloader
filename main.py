import pytube
import os
import tkinter
from PIL import ImageTk, Image
import requests
from io import BytesIO
from tkinter import filedialog
from tkinter import ttk
import sv_ttk
folder=10

def select_directory():
    global folder
    folder=filedialog.askdirectory()
    showdir=tkinter.Label(window,text=f"Current folder: {folder}",font=("Georgia",10))
    showdir.place(x=170,y=60)


def start(searchquery):
    if type(folder)==str and len(folder)!=0:
        search=pytube.Search(str(searchquery.get()))
        if len(searchquery.get())!=0:
            vid1=search.results[0]
            vidtwo=search.results[1]
            vidthree=search.results[2]
            vidfour=search.results[3]
            vid1length="   "+str((vid1.length)//60)+":"+str((vid1.length)%60)
            vidtwolength="   "+str((vidtwo.length)//60)+":"+str((vidtwo.length)%60)
            vidthreelength="   "+str((vidthree.length)//60)+":"+str((vidthree.length)%60)
            vidfourlength="   "+str((vidfour.length)//60)+":"+str((vidfour.length)%60)
            buttonframe=tkinter.Frame(window,bd=5,background='#4096F3',relief='raised',width=720)

            response1 = requests.get(vid1.thumbnail_url)
            img_data1 = response1.content
            img1 = ImageTk.PhotoImage((Image.open(BytesIO(img_data1))).resize(size=(178,100),resample=0))
            label1=tkinter.Label(buttonframe,text='1. '+vid1.title+vid1length,image=img1,compound='top',wraplength=178,relief='sunken',background="#393AB0",foreground="#FFFFFF",font=("Georgia",10))
            label1.image=img1
            button1mp3=tkinter.Button(buttonframe,text="Download mp3.",relief='raised',background="#EDDEDA",command=lambda:download_audio(vid1,folder),font=("Georgia",9))
            button1mp3.grid(row=1,column=0,padx=2,pady=2)
            button1mp4=tkinter.Button(buttonframe,text="Download mp4.",relief='raised',background="#EDDEDA",command=lambda:download_video(vid1,folder),font=("Georgia",9))
            button1mp4.grid(row=1,column=1,padx=2,pady=2)
            label1.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

            
            responsetwo = requests.get(vidtwo.thumbnail_url)
            img_datatwo = responsetwo.content
            imgtwo = ImageTk.PhotoImage((Image.open(BytesIO(img_datatwo))).resize(size=(178,100),resample=0))
            labeltwo=tkinter.Label(buttonframe,text='2. '+vidtwo.title+vidtwolength,image=imgtwo,compound='top',wraplength=178,relief='sunken',background="#393AB0",foreground="#FFFFFF",font=("Georgia",10))
            labeltwo.image=imgtwo
            buttontwomp3=tkinter.Button(buttonframe,text="Download mp3.",relief='raised',background="#EDDEDA",command=lambda:download_audio(vidtwo,folder),font=("Georgia",9))
            buttontwomp3.grid(row=1,column=2,padx=2,pady=2)
            buttontwomp4=tkinter.Button(buttonframe,text="Download mp4.",relief='raised',background="#EDDEDA",command=lambda:download_video(vidtwo,folder),font=("Georgia",9))
            buttontwomp4.grid(row=1,column=3,padx=2,pady=2)
            labeltwo.grid(row=0,column=2,columnspan=2,padx=5,pady=5)

            responsethree = requests.get(vidthree.thumbnail_url)
            img_datathree = responsethree.content
            imgthree = ImageTk.PhotoImage((Image.open(BytesIO(img_datathree))).resize(size=(178,100),resample=0))
            labelthree=tkinter.Label(buttonframe,text='1. '+vidthree.title+vidthreelength,image=imgthree,compound='top',wraplength=178,relief='sunken',background="#393AB0",foreground="#FFFFFF",font=("Georgia",10))
            labelthree.image=imgthree
            buttonthreemp3=tkinter.Button(buttonframe,text="Download mp3.",relief='raised',background="#EDDEDA",command=lambda:download_audio(vidthree,folder),font=("Georgia",9))
            buttonthreemp3.grid(row=3,column=0,padx=2,pady=2)
            buttonthreemp4=tkinter.Button(buttonframe,text="Download mp4.",relief='raised',background="#EDDEDA",command=lambda:download_video(vidthree,folder),font=("Georgia",9))
            buttonthreemp4.grid(row=3,column=1,padx=2,pady=2)
            labelthree.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

            responsefour = requests.get(vidfour.thumbnail_url)
            img_datafour = responsefour.content
            imgfour = ImageTk.PhotoImage((Image.open(BytesIO(img_datafour))).resize(size=(178,100),resample=0))
            labelfour=tkinter.Label(buttonframe,text='1. '+vidfour.title+vidfourlength,image=imgfour,compound='top',wraplength=178,relief='sunken',background="#393AB0",foreground="#FFFFFF",font=("Georgia",10))
            labelfour.image=imgfour
            buttonfourmp3=tkinter.Button(buttonframe,text="Download mp3.",relief='raised',background="#EDDEDA",command=lambda:download_audio(vidfour,folder),font=("Georgia",9))
            buttonfourmp3.grid(row=3,column=2,padx=2,pady=2)
            buttonfourmp4=tkinter.Button(buttonframe,text="Download mp4.",relief='raised',background="#EDDEDA",command=lambda:download_video(vidfour,folder),font=("Georgia",9))
            buttonfourmp4.grid(row=3,column=3,padx=2,pady=2)
            labelfour.grid(row=2,column=2,columnspan=2,padx=5,pady=5)



            buttonframe.place(x=50,y=150)
        else:
            errorlabel_=tkinter.Label(window,text="Enter a valid search query.",font=("Georgia",10))
            errorlabel_.place(x=50,y=150)
    else:
        errorlabel=tkinter.Label(window,text="Select an output folder first.",font=("Georgia",10))
        errorlabel.place(x=50,y=150)
    

def download_audio(yt, output_path):
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path)
    title=yt.title
    for i in ['<', '>', ':', '"', '/', '\\', '|', '?', '*',"'"]:
        title=title.replace(i,"")
    os.rename(f'{output_path}/{title}.mp4',f'{output_path}/{title}.mp3')
    print(f"Downloaded: {yt.title} as mp3 file.")
    successlabel=tkinter.Label(window,text=f"Downloaded: {yt.title} as mp3 file.",font=("Georgia",10))
    successlabel.place(x=30,y=550)
    
def download_video(yt, output_path):
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path)
    title=yt.title
    print(f"Downloaded: {yt.title} as mp4 file.")
    successlabel=tkinter.Label(window,text=f"Downloaded: {yt.title} as mp4 file.",font=("Georgia",20))
    successlabel.place(x=30,y=550)


window=tkinter.Tk()
window.config(width=570,height=600)
window.title("Download Youtube Videos as mp3 or mp4 files.")


dirbutton=ttk.Button(window,text="Select Output Folder",command=select_directory)
dirbutton.place(x=30,y=60)

heading=tkinter.Label(window,text="Download Youtube Videos",font=("Georgia",25))
heading.place(x=50,y=10)

searchlabel=ttk.Label(window,text="Search here :",font=("Georgia",10))
searchlabel.place(x=30,y=100)

searchquery=ttk.Entry(width=45)
searchquery.place(x=30,y=120)

startbutton=ttk.Button(window,text="Search",command=lambda:start(searchquery))
startbutton.place(x=310,y=120)



sv_ttk.set_theme("dark")

window.mainloop()



'''
print('---------')
id=str(vid1)[41:-1]

response2 = requests.get(vid2.thumbnail_url)
img_data2 = response2.content
img2 = ImageTk.PhotoImage((Image.open(BytesIO(img_data2))).resize(size=(178,100),resample=0))
button2=tkinter.Button(buttonframe,text='2. '+vid2.title,image=img2,compound='top',wraplength=178,
                    command=lambda:download_window(vid2))
button2.grid(row=0,column=1)

response3 = requests.get(vid3.thumbnail_url)
img_data3 = response3.content
img3 = ImageTk.PhotoImage((Image.open(BytesIO(img_data3))).resize(size=(178,100),resample=0))
button3=tkinter.Button(buttonframe,text='3. '+vid3.title,image=img3,compound='top',wraplength=178,
                    command=lambda:download_window(vid3))
button3.grid(row=1,column=0)

response4 = requests.get(vid4.thumbnail_url)
img_data4 = response4.content
img4 = ImageTk.PhotoImage((Image.open(BytesIO(img_data4))).resize(size=(178,100),resample=0))
button4=tkinter.Button(buttonframe,text='4. '+vid4.title,image=img4,compound='top',wraplength=178,
                    command=lambda:download_window(vid2))
button4.grid(row=1,column=1)
'''
