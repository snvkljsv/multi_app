import customtkinter as ctk
import os
from tkinter import *
from pytube import YouTube
from tkinter import PhotoImage
from PIL import ImageTk,Image
import random
import sqlite3
from tkinter import messagebox
import speech_recognition as sr
from translate import Translator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import googletrans
from translate import Translator
from tkinter import filedialog
import assemblyai as aai
import moviepy.editor
from time import *
def update():
    time_string=strftime("%m-%d-%Y %H:%M%p")
    time_lable.config(text=time_string)
    time_lable.after(1000,update)

m_cntr=0
def insert_sql():
    z=name_sing.get()
    v=password_sing.get()
    n=email_sing.get()
    p=[z,v,n]
    o=sqlite3.connect("C:\\Users\\PC\\customer.db")
    e=o.cursor()
    e.execute ("INSERT INTO customer (uname,password,email) VALUES(?,?,?)",p)
    o.commit()
   
def sing_check():
    m=name_sing.get()
    v=password_sing.get()
    c=scur_sing.get()
    if m!="" and v!="" and c==str(pk) :
        insert_sql()
    else:
        Label(frame,text="It is incorrect",background="#ff8080",fg="#b30000").place(x=180,y=284)
def notification():
    global pk
    pk=random.randint(1000000,10000000)
    numb=email_sing.get()
    print(" your code:",pk)
    messagebox.showinfo("check your terminal"," I sent an authentication code to your terminal, check it")
    
def find_error_for_sing():
    n=name_sing.get()
    p=password_sing.get()
    e=email_sing.get()
    g=0
    if n=="" :
        Label(frame,text="You must fill in the username",background="#ff8080",fg="#b30000").place(x=180,y=95)
        messagebox.showerror("The information i","All the mentioned items must be filled and are necessary")
        g=g+1
    if p=="":
        Label(frame,text="You must fill in the password",background="#ff8080",fg="#b30000").place(x=180,y=160)
        if g==0:
            messagebox.showerror("The information i","All the mentioned items must be filled and are necessary")
            g=g+1
    if e=="":
        Label(frame,text="You must fill in the email",background="#ff8080",fg="#b30000").place(x=180,y=225)
    else:
        notification()
def create_accont():
    global top,frame
    top=Toplevel()
    top.title("sing up")
    top.resizable(False,False)
    top.geometry("700x700")
    top.config(background="#7a98b4")
    frame=LabelFrame(top,text="Sing up:",width=500,height=400,background="#E1e5e7",font=("Helvetica",15))
    frame.place(x=100,y=100)
    global name_sing
    Label(frame,text="User name :",font=("NORMAL",12),bg="#E1e5e7").place(x=50,y=67)
    name_sing=Entry(frame,border=2,font=("Microsoft YaHei UI Light",11,"bold"),bg="#FFE4C4")
    name_sing.place(x=180,y=66,width=200,height=30)
    Label(frame,text="Password :",font=("NORMAL",12),bg="#E1e5e7").place(x=56,y=130)
    global password_sing
    password_sing=Entry(frame,border=2,font=("Microsoft YaHei UI Light",11,"bold"),bg="#FFE4C4")
    password_sing.place(x=180,y=128,width=200,height=30)
    Label(frame,text="Email :",font=("NORMAL",12),bg="#E1e5e7").place(x=84,y=193)
    global email_sing
    email_sing=Entry(frame,border=2,font=("Microsoft YaHei UI Light",11,"bold"),bg="#FFE4C4")
    email_sing.place(x=180,y=193,width=200,height=30)
    Label(frame,text="identification :",font=("NORMAL",12),bg="#E1e5e7").place(x=40,y=256)
    global scur_sing
    scur_sing=Entry(frame,border=2,font=("Microsoft YaHei UI Light",11,"bold"),bg="#FFE4C4")
    scur_sing.place(x=180,y=253,width=100,height=30)
    email_send=Button(frame,text="Code",font=("bold",9,"bold"),cursor="hand2",bg="yellow",fg="green",command=find_error_for_sing)
    email_send.place(x=284,y=252,height=33)
    sub_button=Button(frame,text=" Submit ",command=sing_check,background="#FC9E5F",foreground="#05d7ff",activebackground="#65e7ff",activeforeground="gray",highlightthickness=2,highlightbackground="#05d7ff",highlightcolor="WHITE",width=7,height=1,border=0,cursor="hand2",font=("arial",16,"bold"))
    sub_button.place(x=290,y=300)
L=sqlite3.connect("C:\\Users\\PC\\customer.db")
h=L.cursor()
Uname=h.execute ("SELECT uname FROM customer")
Uname=Uname.fetchall()
Uname_list1=[]
for name in Uname:
    Uname_list1.append(name[0])

def message_error():
    messagebox.showerror("Error in identification","Apparently, you entered your information incorrectly, please correct it carefully")
def empty_error():
    messagebox.showerror("Incomplete information","The requested items are necessary, you must fill them")
def wrong_detection():

    p=L.cursor()
    fname=p.execute ("SELECT password FROM customer")
    fname=fname.fetchall()
    fname_list=[]
    messageboxx=0
    for pas in fname:
        fname_list.append(pas[0])
    
    u_name=name_entry.get()
    U_password=password_entry.get()
    securty1=scur_entry.get()
    Variabl=var.get()
    my_name=[u_name,427,103,"Your username is incorrect"]
    my_pass=[U_password,427,189,"Your password is incorrect"]
    my_security=[securty1,280,218,"The security code is incorrect"]
    if my_name[0] not in Uname_list1:
        error_lable=Label(log_data,text=f"**{my_name[3]}**",background="#ff8080",fg="#b30000")
        error_lable.place(x=my_name[1],y=my_name[2]) 
        messageboxx=messageboxx+1

    if my_pass[0] not in fname_list:
        error_lable1=Label(log_data,text=f"**{my_pass[3]}**",background="#ff8080",fg="#b30000")
        error_lable1.place(x=my_pass[1],y=my_pass[2])   
        messageboxx=messageboxx+1   
    if my_security[0]!=str(a):
        error_lable2=Label(log_data,text=f"**{my_security[3]}**",background="#ff8080",fg="#b30000")
        error_lable2.place(x=my_security[1],y=my_security[2])
        messageboxx=messageboxx+1      
    if str(Variabl)=="0":
        error_lable3=Label(log_data,text=f"**clik checkbox**",background="#ff8080",fg="#b30000")
        error_lable3.place(x=410,y=285)
        messageboxx=messageboxx+1
    if messageboxx==0:
        pass
    else:
        message_error()

def Error_Detection():
    u_name=name_entry.get()
    U_password=password_entry.get()
    securty=scur_entry.get()
    d_human=var.get()

    my_list=[(u_name,427,103),(U_password,427,189),(securty,280,218)]
    cntr=0
    for w,x,y in my_list:
        
        if w=="":
            error_lable=Label(log_data,text="**You did not fill this item**",background="#ff8080",fg="#b30000")
            error_lable.place(x=x,y=y)
            cntr=cntr+1
    if cntr!=0:
        empty_error()
        
def log_in():
    global m_cntr
    m_cntr=0
    dicitonary={} 
    L=sqlite3.connect("C:\\Users\\PC\\customer.db")
    h=L.cursor()
    Uname_list=h.execute ("SELECT uname,password FROM customer")
    Uname_list=Uname_list.fetchall()
    for man,key in Uname_list:
        dicitonary[man]=key
    print(dicitonary)
    Uname=name_entry.get()
    password=password_entry.get()
    scurity=scur_entry.get()
    human=var.get()
    if Uname in Uname_list1 and dicitonary[Uname]==password and scurity==str(a) and human==1 :
         m_cntr=m_cntr+1
         root.destroy()
        
    if Uname=="" or password=="" or scurity=="":
        Error_Detection()
    else:
        wrong_detection()

def on_enter(e):
    name_entry.delete(0,'end')

def ps_enter(e):
    password_entry.delete(0,'end')

def sec_enter(e):
    scur_entry.delete(0,'end')
root=ctk.CTk()
root.title("my app")
root.geometry("1050x700")
image = Image.open("C:\\Users\\PC\\OneDrive\\Pictures\\back.jpg")
op_image=Image.open("C:\\Users\\PC\\OneDrive\\Pictures\\glas.jpg")
resize_image = image.resize((1360, 1000))
img = ImageTk.PhotoImage(resize_image)
img_glass = ImageTk.PhotoImage(op_image)
bg_image=Label(root,image=img)
bg_image.place(x=0,y=0)
logintxt=Label(root,text="Welcome !",font=("Helvetica",30),bg="#93aec9",fg="white").place(x=565,y=130)
log_data=LabelFrame(root,text="Login:",width=800,height=450,background="#E1e5e7",font=("Helvetica",15))
log_data.place(x=270,y=270)
user_name=Label(log_data,image=img_glass).place(x=-250,y=-250)
Label(log_data,text="Login !",font=("Helvetica",20),bg="#7a98b4").place(x=360,y=1)
Label(log_data,text="User name :",font=("NORMAL",15),bg="#7a98b4").place(x=60,y=69)
name_entry=Entry(log_data,border=2,font=("Microsoft YaHei UI Light",11,"bold"),bg="#FFE4C4")
name_entry.place(x=280,y=68,width=300,height=35)
name_entry.insert(0,'Your Username')
name_entry.bind('<FocusIn>',on_enter)
Label(log_data,text="Password :",font=("NORMAL",15),bg="#7a98b4").place(x=60,y=154)
password_entry=Entry(log_data,border=2,font=("Microsoft YaHei UI Light",11,"bold"),show="*",bg="#FFE4C4")
password_entry.place(x=280,y=153,width=300,height=35)
password_entry.insert(0,'Your Password')
password_entry.bind('<FocusIn>',ps_enter)
Label(log_data,text="security :",font=("NORMAL",15),bg="#7a98b4").place(x=60,y=240)
a=random.randint(1000000,10000000)
Label(log_data,text=a,font=("NORMAL",20),bg="blue").place(x=480,y=240)
scur_entry=Entry(log_data,border=2,font=("Microsoft YaHei UI Light",11,"bold"),bg="#FFE4C4")
scur_entry.place(x=280,y=240,width=180,height=35)
scur_entry.insert(0,'write number')
scur_entry.bind('<FocusIn>',sec_enter)
var =IntVar()
checkbutton =Checkbutton(log_data, text="I AM HUMAN", variable=var, onvalue=1, offvalue=0,justify=LEFT,font=("NORMAL",13),bg="#FFE4C4")
checkbutton.place(x=280,y=280)
sub_button=Button(log_data,text=" Submit ",command=log_in,background="#020f12",foreground="#05d7ff",activebackground="#65e7ff",activeforeground="BLACK",highlightthickness=2,highlightbackground="#05d7ff",highlightcolor="WHITE",width=7,height=1,border=0,cursor="hand2",font=("arial",16,"bold"))
sub_button.place(x=510,y=310)
Label(log_data,text="Don't have account?").place(x=280,y=320)
sing_up=Button(log_data,text="sign up",command=create_accont,cursor="hand2",fg="yellow",font=("bold",8,"bold"),bg="black")
sing_up.place(x=400,y=319)
time_lable=Label(root,font=("Arial",20),fg="#00FF00",bg="black")
time_lable.place(x=0,y=0)
update()
root.resizable(False,False)
root.mainloop()



if m_cntr!=1:
    exit()   

def serch():
    def voice():
        r = sr.Recognizer()
        with sr.Microphone() as src:
                    r.adjust_for_ambient_noise(src, duration=0.2)
                    audio = r.listen(src)
                
                    text = r.recognize_google(audio)
                    text = text.lower()
                    search_entry.insert(0,f'{text}')
                    go()
    def go():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        try:
    # Open Google's homepage
            driver.get("https://www.google.com")

    # Find the search box element (by name attribute)
            search_box = driver.find_element("name", "q")

    # Enter the search word (e.g., "Selenium")
            search_word = search_entry.get()
            search_box.send_keys(search_word)

    # Submit the search form
            search_box.send_keys(Keys.RETURN)

    # Wait for the results to load and display the title
            driver.implicitly_wait(10)  # seconds
            print(driver.title)
            
        
        finally:
    # Close the browser window
            while True:
                a=input("go? ")
                if a=="y":
                    break
            driver.quit()
    root3=Tk()
    root3.geometry("400x400")
    root3.title("Search")
    root3.resizable(False,False)
    root3.config(background="#F0F8FF")
    Label(root3,text="Search somthing!",bg="green",fg="white",font=("Helvetica",15)).place(x=0,y=3,width=400,height=100)
    search_entry=Entry(root3)
    search_entry.place(x=70,y=130,height=50,width=250)
    go_btn=Button(root3,text="go",command=go,font=("Helvetica",19),bg="yellow")
    go_btn.place(x=270,y=130)
    Button(root3,text="mic",command=voice).place(x=235,y=180)


    root3.mainloop()    
def translate_b():
# Initialize the recognizer
    def translators():
        out_fild.delete(1.0,END)
        try:

            for key,valeus in list_languege.items():
                if (valeus==original.get()):
                    form_key_languege=key
            for ke1,valeu1 in list_languege.items():
                if (valeu1==target.get()):
                    target_key_languege=ke1
            ip=input_fild.get(1.0,END)
            print(ip)
            print(form_key_languege)
            print(target_key_languege)
            translator=Translator(from_lang=form_key_languege,to_lang=target_key_languege)
            translation=translator.translate(ip)
            out_fild.insert(1.0,translation)
            
            
            
            
            
        except Exception as e:
            messagebox.showerror("Translator",e)
    def clear():
        input_fild.delete(1.0,END)
        out_fild.delete(1.0,END)


    r = sr.Recognizer()
    window =Tk()
    window.geometry("800x800")
    window.resizable(False,False)

    list_languege=googletrans.LANGUAGES
    window.title("Translate")
    input_frame=Frame(window,bg="#D3D3D3")
    input_frame.place(x=50,y=200,width=350,height=400)
    input_fild=Text(input_frame,bg="#E6E6FA")
    input_fild.place(x=25,y=40,width=300,height=320)
    Label(input_frame,text="Input",font=("Helvetica",15)).place(x=150,y=10)
    out_frame=Frame(window,bg="#87CEFA")
    Label(out_frame,text="Output",font=("Helvetica",15)).place(x=150,y=10)
    out_frame.place(x=400,y=200,width=350,height=400)    
    out_fild=Text(out_frame,bg="#E0FFFF")
    out_fild.place(x=25,y=40,width=300,height=320)
    Label(window,text="Translate app",font=("Helvetica",15),bg="pink").place(x=0,y=0,width=800,height=100)
    Label(window,text="Input",font=("Helvetica",15),bg="lightgreen").place(x=50,y=100,width=350,height=100)
    Label(window,text="Output",font=("Helvetica",15),bg="yellow").place(x=400,y=100,width=350,height=100)
    Button(window,text="Translate",font=("Helvetica",20),bg="orange",command=translators).place(x=325,y=125)
    langueges=list(list_languege.values())
    original=ctk.CTkComboBox(window,width=120,values=langueges)
    original.place(x=110,y=103)
    target=ctk.CTkComboBox(window,width=120,values=langueges)
    target.place(x=400,y=103)
    Button(window,text="Reset",font=("Helvetica",15),fg="white",bg="black",command=clear).place(x=363,y=600)

    global counter
    counter = 2


    

    def show_text(text):
        global counter
        lbl_name = f"lbl_{counter}"
        lbl_name =Label(window,text=text)
        lbl_name.config(font=("aviny", 22, "bold"))
        lbl_name.grid(row=counter, column=0)
        counter += 1


    def get_voice():
            try:
                with sr.Microphone() as src:
                    r.adjust_for_ambient_noise(src, duration=0.2)
                    audio = r.listen(src)
                
                    text = r.recognize_google(audio)
                    text = text.lower()
                    translator = Translator(to_lang="fa")
                    translation = translator.translate(text)
    
                    show_text(translation)
                

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            
            except sr.UnknownValueError:
                show_text("Sorry try again")


    
    window.mainloop()

def youtube():
    def dowonload():
        url=entry_url.get()
        resolution1=resolution_var.get()
        progress.pack(pady=10)
        progress_bar.pack(pady=1)
        status_lable.pack(pady=10)
        try:
            yt=YouTube(url,on_progress_callback=on_progrss)
            stream=yt.streams.filter(res=resolution1).first()
            os.path.join("C:\\Users\\PC\\Videos\\",f"{yt.title}.mp4")
            stream.download(output_path="downloded!")
            ctk.CTkLabel(content_frame,text="downloded !",fg_color="green").pack(pady=10)
        
        except Exception as e :
            status_lable.configure(text=f"Error {str(e)}",text_color="black",fg_color="red")
            print(e)

    def on_progrss(stream,chunk,bytes_remaining):
        total_size=stream.filesize
        bytes_downloaded=total_size-bytes_remaining
        percentage_completed=int((bytes_downloaded/total_size)*100)
        progress.configure(text=f"{str(percentage_completed)}"+"%")
        progress.update()
        progress_bar.set(float(percentage_completed)/100)
    
    root=ctk.CTk()
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    root.title("Youtube Downloder!")
    root.geometry("720x480")
    root.minsize(720,480)
    root.maxsize(1080,720)
    content_frame=ctk.CTkFrame(root)
    content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
    url_lable=ctk.CTkLabel(content_frame,text="Enter the youtube url here :")
    entry_url=ctk.CTkEntry(content_frame,width=400,height=40)
    url_lable.pack(pady=10)
    entry_url.pack(pady=7)
    download_button=ctk.CTkButton(content_frame,text="Download",command=dowonload)
    download_button.pack(pady=10)
    resolution=["720p","360p","240p"]
    resolution_var=ctk.StringVar()
    resolution_combobox=ctk.CTkComboBox(content_frame,values=resolution,variable=resolution_var)
    resolution_combobox.pack(pady=10)
    resolution_combobox.set("720p")
    progress=ctk.CTkLabel(content_frame,text="0%")
    progress_bar=ctk.CTkProgressBar(content_frame,width=400)
    progress_bar.set(0.01)
    status_lable=ctk.CTkLabel(content_frame,text="")
    root.mainloop()


    

def subtittle():
    def click(value):
        global lang
        lang=value
    def file_search():
        global filepath
        filepath=filedialog.askopenfilename()
        input_entry.insert(0,filepath)
    def subing():
        a=input_entry.get()
        b=input_save.get()
        print(a)
        if lang==1:
            cvt_video=moviepy.editor.AudioFileClip(a)
            cvt_video.write_audiofile(f"{b}.mp3")
            aai.settings.api_key = "dd5cfec64df443b9b31c09940601fb0a" 
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(f"C:\\Users\\PC\\python project\\tkinter\\{b}.mp3" )
            subtitel=transcript.export_subtitles_srt()
            f=open(F"{b}","a")
            f.write(subtitel)
            f.close()
    sub=ctk.CTk()
    sub.geometry("800x600")
    Label(sub,text="Take a subtittle!",font=("Helvetica",25),bg="green",fg="white").place(x=0,y=0,width=1000,height=100)
    input_frame=Frame(sub,background="#6495ED")
    Label(input_frame,text="input your video:",bg="#6495ED",font=("Helvetica",15)).place(x=20,y=50)
    input_frame.place(x=180,y=200,width=650,height=400)
    input_entry=Entry(input_frame,font=("Helvetica",25),width=30)
    input_entry.place(x=50,y=100)
    Label(input_frame,text="save name:").place(x=250,y=150)
    input_save=Entry(input_frame,font=("Helvetica",25),width=10)
    input_save.place(x=330,y=140)
    var_s=IntVar()
    eng=Radiobutton(input_frame,text="english",variable=var_s,value=1,command=lambda:click(1))
    eng.place(x=53,y=160)
    farsi=Radiobutton(input_frame,text="farsi",variable=var_s,value=2,command=lambda:click(2))
    farsi.place(x=53,y=200)
    submit_button=Button(input_frame,text="Submit",bg="yellow",font=("Helvetica",15),command=subing)
    submit_button.place(x=150,y=160,width=80,height=80)
    file_button=Button(input_frame,text="search",font=("Helvetica",15),bg="lightblue",command=file_search)
    file_button.place(x=518,y=140)
    sub.mainloop()
def update1():
    time_string1=strftime("%m-%d-%Y %H:%M%p")
    time_lable1.config(text=time_string1)
    time_lable1.after(1000,update)
root1=ctk.CTk()
root1.title("my app")
root1.geometry("1050x700")
image = Image.open("C:\\Users\\PC\\OneDrive\\Pictures\\oly.jpg")
resize_image = image.resize((1360, 1000))
img = ImageTk.PhotoImage(resize_image)
bg_image=Label(root1,image=img)
bg_image.place(x=-30,y=-80)
logintxt=Label(root1,text="Welcome !",font=("Helvetica",30),bg="#E7E7E7",fg="white").place(x=565,y=80)
you_tube_btn=Button(root1,text="YouTube Downdoder",font=("Helvetica",10),bg=("red"),command=youtube)
you_tube_btn.place(x=880,y=310,width=200,height=200)
subtittle_btn=Button(root1,text="Subtittle Maker",font=("Helvetica",10),bg=("black"),fg="white",command=subtittle)
subtittle_btn.place(x=540,y=310,width=200,height=200)
wether_btn=Button(root1,text="Wether",font=("Helvetica",10),bg=("blue"))
wether_btn.place(x=200,y=310,width=200,height=200)
search_btn=Button(root1,text="Search",font=("Helvetica",10),bg=("green"),command=serch)
search_btn.place(x=700,y=510,width=200,height=200)
translate_btn=Button(root1,text="Translate",font=("Helvetica",10),bg=("yellow"),command=translate_b)
translate_btn.place(x=400,y=510,width=200,height=200)
time_lable1=Label(root1,font=("Arial",20),fg="#00FF00",bg="black")
time_lable1.place(x=0,y=0)
update1()
root1.mainloop()
