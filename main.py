import time
from textwrap import wrap

import keyboard
from numpy import true_divide
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import socket
import colorama
from colorama import Fore
import random
import Elements
import threading
from tkinter import *
import multiprocessing
import pymysql
from tkinter import messagebox,filedialog
from PIL import ImageTk


FLAG=0  #this is the flag for authentication

def submitdb():
    global con, mycursor, FLAG
    # host = hostval.get()  ### localhost
    # user = userval.get()  #### root
    # password = passwordval.get()  ###Ritik@123
    host = 'localhost'  ### localhost
    user = "root"  #### root
    password = "Ritik@123"  ###Ritik@123

    try:
        con = pymysql.connect(host=host, user=user, password=password)
        mycursor = con.cursor()
        FLAG=1

    except:
        messagebox.showerror('Alert', 'Data is incorrect, please try again', parent=dbroot)

    try:
        strr = 'create database userqueries' #projectrecordkeeper2
        mycursor.execute(strr)
        strr = 'use userqueries' #projectsdata
        mycursor.execute(strr)
        strr = 'create table userquery(querynumber int AUTO_INCREMENT PRIMARY KEY,query varchar(90),executed Boolean)'
        mycursor.execute(strr)
        # strr = 'alter table userquery modify column querynumber int not null'
        # mycursor.execute(strr)
        # strr = 'alter table userquery modify column querynumber int primary key'
        # mycursor.execute(strr)
        messagebox.showinfo('Notification', 'DataBase Created ! Now you are connected to the DataBase...',
                            parent=dbroot)



    except:
        strr = 'use userqueries'
        mycursor.execute(strr)
        messagebox.showinfo('Notification', 'Now you are connected to the DataBase...', parent=dbroot)
    dbroot.destroy()


dbroot = Tk()
dbroot.grab_set()

dbroot.geometry('470x250+800+230')
dbroot.overrideredirect(True)
# dbroot.iconbitmap('ICON.ico')
dbroot.wm_attributes("-topmost", True)
dbroot.attributes('-alpha',0.7)
# dbroot.wm_attributes("-transparentcolor", "#171717")

dbroot.resizable(False, False)
dbroot.config(bg='#171717')
# .......................#Connect DB labels

hostlabel = Label(dbroot, text="Enter Host : ", bg='black',foreground="white", font=('Courier', 15, 'bold'), relief=GROOVE,
                  borderwidth=3, width=18, anchor='w')
hostlabel.place(x=10, y=10)
hostlabel.config(bd=0)

userlabel = Label(dbroot, text="Enter User : ", bg='black',foreground="white", font=('Courier', 15, 'bold'), relief=GROOVE,
                  borderwidth=3, width=18, anchor='w')
userlabel.place(x=10, y=70)
userlabel.config(bd=0)

passwordlabel = Label(dbroot, text="Enter Password : ", bg='black',foreground="white", font=('Courier', 15, 'bold'), relief=GROOVE,
                      borderwidth=3, width=18, anchor='w')
passwordlabel.place(x=10, y=130)
passwordlabel.config(bd=0)

# .......................#Connect DB input Boxes

hostval = StringVar()
hostentry = Entry(dbroot, font=('Courier', 15, 'bold'), bd=5,width=15, textvariable=hostval,highlightthickness=1)
hostentry.config(bd=0,highlightbackground = "cyan", highlightcolor= "White",background="black",foreground="chartreuse")
hostentry.place(x=250, y=10)

userval = StringVar()

userentry = Entry(dbroot, font=('Courier', 15, 'bold'), bd=5,width=15, textvariable=userval,highlightthickness=1)
userentry.config(bd=0,highlightbackground = "cyan", highlightcolor= "White",background="black",foreground="chartreuse")
userentry.place(x=250, y=70)

passwordval = StringVar()
passwordentry = Entry(dbroot, font=('Courier', 15, 'bold'), bd=5,width=15, textvariable=passwordval,highlightthickness=1)
passwordentry.config(bd=0,highlightbackground = "cyan", highlightcolor= "White",background="black", foreground="chartreuse")
passwordentry.place(x=250, y=130)

# .......................#Connect (submit) Button

exitbutton = Button(dbroot, text='Submit', bd=0, bg='#171717',foreground="white", font=('Biting My Nails', 15, 'bold'), width=10,
                      activebackground="#171717", activeforeground='white', command=submitdb)
exitbutton.place(x=70, y=190)
exitbutton.config(bd=0)

submitbutton = Button(dbroot, text='Exit', bd=0, bg='#171717',foreground="white", font=('Biting My Nails', 15, 'bold'), width=10,
                      activebackground="#171717", activeforeground='white', command=exit)
submitbutton.place(x=230, y=190)
submitbutton.config(bd=0)

dbroot.mainloop()

# strr = 'insert into userquery values(NULL,"patanahi kya hai ye",true);'
# mycursor.execute(strr)
# con.commit()

if(FLAG==0):
     exit()
################### fetching the last number

NUMBER=-1
def tryy():
   global NUMBER
   try:
    strr = 'select *from userquery order by querynumber DESC LIMIT 1;'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    for row in datas:
        NUMBER=row[0]
   except:
       NUMBER=0
tryy()
#


#---- VARIABLES TO CHANGE SOME POINTED INDEXES COLORS ON TKINTER TEXT BOX ----#

i = 1
i_float = 1.11
mylist_convert_1 = ''
mylist_convert_2 = ''
j = 1
j_float = 1.11
mylist2_convert_1 = ''
mylist2_convert_2 = ''



# __________ TKINTER - ROOT CONFIGURATION ______

root = Tk()
root.geometry('1174x700+200+150')
root.resizable(False, False)
root.config(bg='#171717')
root.title("ASSISTANT")
root.attributes('-alpha',0.8)

###### --can make tkinter window transparent form here
# root.wm_attributes("-transparentcolor", "white")

####### --can attach background image in root window fromm here
# img= PhotoImage(file='bg.png', master= root)
# img_label= Label(root,image=img)
# img_label.place(x=0, y=0)

# ____________TKINTER - FRAMES CONFIGURATION ______

#######  FRAME3 & MYLIST3 ########

Frame3 = Frame(root, bg='cyan', relief=RAISED, borderwidth=2)
Frame3.place(x=10, y=80, width=500, height=90)

scrollbar = Scrollbar(Frame3)
# scrollbar.pack(side=RIGHT, fill=BOTH) <--- if we want scrollbar
mylist3 = Text(Frame3, yscrollcommand=scrollbar.set,cursor="plus",pady=10,padx=10)
mylist3.pack(expand=True, fill=BOTH)
mylist3.configure(background="black", foreground="OliveDrab2", font=('"Courier" 13'))
scrollbar.config(command=mylist3.yview)

#######  FRAME1 & MYLIST2 ########

Frame1 = Frame(root, bg='cyan', relief=RAISED, borderwidth=2)
Frame1.place(x=10, y=200, width=500, height=480)
scrollbar = Scrollbar(Frame1)
# scrollbar.pack(side=RIGHT, fill=BOTH) <--- if we want scrollbar
mylist2 = Text(Frame1, yscrollcommand=scrollbar.set, wrap=WORD,cursor="plus",pady=10,padx=10)
mylist2.pack(expand=True, fill=BOTH)
mylist2.configure(background="black", foreground="LightCyan3", font=('"MV Boli" 13'))


scrollbar.config(command=mylist2.yview)

#######  FRAME3 & MYLIST3 ########


Frame2 = Frame(root, bg='cyan', relief=RAISED, borderwidth=2)
Frame2.place(x=520, y=80, width=640, height=600)
scrollbar = Scrollbar(Frame2)
# scrollbar.pack(side=RIGHT, fill=BOTH)  <--- if we want scrollbar
mylist = Text(Frame2, yscrollcommand=scrollbar.set, wrap=WORD,cursor="plus",pady=10,padx=10)
mylist.pack(expand=True, fill=BOTH)
mylist.configure(background="black", foreground="LightCyan3", font=('"Consolas" 13'))
scrollbar.config(command=mylist.yview)

'''---------- IMPORTING VARIABLES FROM ELEMENTS.PY ---------'''

question_elements = Elements.question_elements
start_elements = Elements.start_elements
stop_elements = Elements.stop_elements

# ________________________pyttsx3 engine________

''' 
From here we can change the voices
By changing the value of the index of the voices array (should be b/w 0-2)
'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
voice_character = 0
engine.setProperty('voice', voices[voice_character].id)


# _____________SPEAK FUNCTION___________________

def speak(audio):
    global mylist_convert_1
    global mylist_convert_2
    global i
    global i_float
    print("Assistant : ", end="")
    # print("\033[1;32m Assistant  \n" + audio)
    # print(Fore.YELLOW + "Assistant : " + audio, end="")
    print("\t" + audio)
    # speak_printer(audio)
    engine.say(" . " + audio)
    a = "Assistant  --> "
    total = a + audio
    mylist.insert(END, str(total+'\n'))
    i_float = i+0.0
    # print(i_float , end="")

    mylist_convert_1 = str(i_float)
    i_float=i+0.11
    # print(i_float , end="\n")

    mylist_convert_2 = str(i_float)
    i=i+1
    mylist.tag_add("start", mylist_convert_1, mylist_convert_2)
    mylist.tag_config("start", background="black", font=('"Terminal" 13'), foreground="cyan")
    mylist.update()
    # mylist.insert(END, "\n")

    mylist.yview(END)
    engine.runAndWait()
'''_________ OVERLOADED SPEAKK FUNCTION _____________'''


def speakk(*args):
    r=random.randint(0, (len(args)-1))
    speak(args[r])
    print(len(args)-1)
    print(r)


'''---------- WISH ME FUNCTION ---------'''



def wishMe():
    hour = int(datetime.datetime.now().hour)

    # WISHING ACCORDING TO TIME
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    #----- SAYING WHO IS THE ASSISTANT

    if (voice_character == 0):
        speak("I am Jarvis. ")
    elif (voice_character == 1):
        speak("I am Cinderella.")

    elif (voice_character == 2):
        speak("I am Friday. ")
    speak("User Authenticated, initializing databases...")

    if (Elements.is_connected('www.google.com')):

        speak("We are online and ready.")
    else:
        speak("I can see we are offline sir.")


'''---------- TAKECOMMAND FUNCTION ---------'''


def takeCommand():
    global mylist2_convert_1
    global mylist2_convert_2
    global j
    global j_float
    # It takes microphone input from the user and returns string output
    print("\n")
    # mylist3.insert(END, "-------------------------")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("-> Listening...")
        try:
           mylist3.delete("1.0", END)
        except:
            pass
        mylist3.insert(END, "Listening..."+'\n')
        mylist3.yview(END)


        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("-> Recognizing...")
        mylist3.insert(END, "Recognizing..."+'\n')
        query = r.recognize_google(audio, language='en-in')
        # mylist3.insert(END, "-------------------------")
        print(f"User said : \t{query}")
        stt = "User said  --> " + query
        mylist2.insert(END, stt+"\n")
        j_float = j + 0.0
        # print(i_float , end="")

        mylist2_convert_1 = str(j_float)
        j_float = j + 0.11
        # print(i_float , end="\n")

        mylist2_convert_2 = str(j_float)
        j = j + 1

        mylist2.update()

        # mylist2.tag_add("start", "2.0", "2.10")
        # mylist2.tag_config("start", background="black", font=('"Courier" 13'), foreground="white")

        mylist2.yview(END)
        mylist3.yview(END)


    except Exception as e:
        # print(e)
        print("-> Say that again please...")
        mylist3.insert(END, "Say that again please..."+'\n')
        mylist3.yview(END)

        return "None"

    mylist2.tag_add("start", mylist2_convert_1, mylist2_convert_2)
    mylist2.tag_config("start", background="black", font=('"Terminal" 13'), foreground="yellow")

    return query


'''---------- SEND MAIL FUNCTION ---------'''


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('itikkadoleedu@gmail.com', 'golurishii')
    server.sendmail('itikkadoleedu@gmail.com', to, content)
    # server.login('youremail@gmail.com', 'your-password')
    # server.sendmail('youremail@gmail.com', to, content)
    server.close()


stop_threads = False


def main_thread():
    while True:

        query = takeCommand().lower()
        query = query.lower()

        if 'wikipedia' in query:
            try:

                query = query.replace("wikipedia", "")
                speak(f"Searching wikipedia for,  {query}")
                results = wikipedia.summary(query, sentences=2)
                try:
                    results = results.strip('\n')
                    results = results.strip('\t')
                    print("stripped")
                except error as e:
                    print(e)
                    pass
                try:
                    results = results.replace('\n', '')
                    results = results.replace('\t', '')
                    print("stripped")
                except error as e:
                    print(e)
                    pass
                print(type(results))
                speak("According to, Wikipedia")
                speak(results)

            except Exception as e:
                speakk("can you say that again please",
                       "Does not found sir,please say that again",
                       "Sorry sir, please say that again",
                       "Sorry sir, related query not found")
        elif query.find('what is') == 0:
            try:

                query = query.replace("what is", "")
                # speak(f"Searching wikip for,  {query}")
                results = wikipedia.summary(query, sentences=2)
                try:
                    results = results.strip('\n')
                    results = results.strip('\t')
                    print("stripped")
                except error as e:
                    print(e)
                    pass
                try:
                    results = results.replace('\n', '')
                    results = results.replace('\t', '')
                    print("stripped")
                except error as e:
                    print(e)
                    pass
                print(type(results))
                speak("Sir...")
                speak(results)

            except Exception as e:
                pass

        elif "search for" in query :
            print("query =" + query)
            query = query.replace('search for ', '', 1)
            # query = query.replace('for ', '', 1)
            print("query =" + query)
            Elements.search(query)
            speak(f"Searching for {query}")

        elif 'search youtube for' in query:
            query = query.replace('search youtube', '', 1)
            query = query.replace('for ', '', 1)
            Elements.search_youtube(query)
            speak(f"Searching youtube for {query}")

        elif any(item in query for item in start_elements):
              if 'google' in query :
                 try:
                    speak('opening Google...')
                    Elements.open_google()
                 except:
                     speak("Sorry sir can not open Google")
              elif 'youtube' in query :
                 try:
                     speak('opening Youtube...')
                     Elements.open_youtube()
                 except:
                     speak("Sorry sir can not open Google")
              elif 'chrome' in query :
                 try:
                     speak('opening Chrome Browser...')
                     Elements.open_chrome()
                 except:
                     speak("Sorry sir can not open chrome")
              elif 'vs code' in query or "visual studio" in query:
                 try:
                     speak('opening Visual Studio code ...')
                     Elements.open_code()
                 except:
                     speak("Sorry sir can not open Visual Studio code")
              elif 'study' in query:
                     Elements.start_study()
                     speak("Ok sir, opening available directories and web links...")
              elif 'whatsapp' in query:
                     path_whatsapp="C:\\Users\\R\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                     webbrowser.open(path_whatsapp)
                     speak("Opening whatsapp...")
                     # keyboard.press_and_release("windows + down")


        elif (('switch' in query) or ("change" in query)) and 'window' in query:
            Elements.switch_window()
            speakk("ok sir", "sure sir", "ok")
        elif (('weather report' in query) or ("weather details" in query) or ("how is the weather" in query) or ("how is weather" in query)) :
            speak("In bhopal...")

            weather_data= Elements.weather_report()
            # speak(weather_data[0])
            print(weather_data[1])

            global mylist_convert_1
            global mylist_convert_2
            global i
            global i_float
            print("Assistant : ", end="")
            # print("\033[1;32m Assistant  \n" + audio)
            # print(Fore.YELLOW + "Assistant : " + audio, end="")
            print("\t" + weather_data[0])
            # speak_printer(audio)
            engine.say(weather_data[1])
            a = "Assistant  --> "
            total = a + weather_data[0]
            mylist.insert(END, str(total + '\n'))
            i_float = i + 0.0
            # print(i_float , end="")

            mylist_convert_1 = str(i_float)
            i_float = i + 0.11
            # print(i_float , end="\n")

            mylist_convert_2 = str(i_float)
            i = i + 1
            mylist.tag_add("start", mylist_convert_1, mylist_convert_2)
            mylist.tag_config("start", background="black", font=('"Terminal" 13'), foreground="cyan")
            mylist.update()
            # mylist.insert(END, "\n")

            mylist.yview(END)
            engine.runAndWait()
            # speak(weather_data[0])
        elif (('jarvis' in query) and ("hello" in query)):
            speakk("Hello sir", "Hello", "Yes sir")

        elif (('switch' in query) and ("tab" in query)):
            Elements.switch_tab(query)

        elif 'go to sleep' in query:
            speak("as your wish sir...")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "start study" in query:
            # speak("Ok sir, opening available directories and web links...")
            Elements.start_study()
            speak("Ok sir, opening available directories and web links...")

        elif 'wake up' in query:
            keyboard.press_and_release('Enter')
            time.sleep(1)
            keyboard.press_and_release('Enter')
            time.sleep(1)


        elif ("internet" in query or "check" in query) and 'speed' in query:
            s = threading.Thread(target=Elements.check_speed(),args=())
            s.start()
            speak('Checking internet connection speed...')


        elif (('switch' in query) or ("change" in query)) and ('assistant' in query or "voice" in query):
            global voice_character
            voice_character += 1
            voice_character %= 3
            engine.setProperty('voice', voices[voice_character].id)
            wishMe()

        elif (("check" in query or "see" in query or "status" in query) and (
                "internet" in query or "connection" in query or "online" in query)):

            if (Elements.is_connected('www.google.com')):
                speak("I can see we are online sir...")
            else:
                speak("I can see we are offline sir...")


        elif (('you' in query) and ('stop' in query)):
            speak('Terminating my self,  Good bye sir..')
            root.quit()
            break
            exit()

        elif 'close browser' in query:
            os.system('TASKKILL /F /IM msedge.exe ')
        elif (any(item in query for item in stop_elements))  and ('chrome' in query):
            os.system('TASKKILL /F /IM chrome.exe ')

        # PLAYING AND STOPPING SONGS

        elif ((any(item in query for item in start_elements) or 'play' in query) and (
                'music' in query or 'song' in query)):
            music_dir = 'D:\\songs\\TO HERE'
            speak("ok sir, here you go ")
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            time.sleep(2)
            keyboard.press_and_release("windows + down")


        elif (('song' in query or 'gana' in query or 'music' in query or 'songs' in query) and (
        any(item in query for item in stop_elements))):
            os.system('TASKKILL /F /IM vlc.exe ')
            speak("done!")

        elif 'stop music' in query:
            os.system('TASKKILL /F /IM vlc.exe ')

            # This code is SUSPECIOUS | we will test this code tommorow
        elif "how are you" in query:
            if (Elements.is_connected('www.google.com')):
                speak("I am online and ready sir...")
            else:
                speak("Unfortunately I am offline sir")
        elif "who are you" in query:
           speak("I am JARVIS, means, Just anonymous Reprogrammable Virtual Intellegent System, i cannot learn myself for now.")

        elif ('you' in query) and any(item in query for item in question_elements):
            speak("Sorry, i dont know much, about myself...")

        elif ("jarvis" in query) and ("tell" in query or "crack" in query) and("joke" in query):
            try:
              speak(str(Elements.crack_jokes()))
            except:
                speak("Sorry sir...")
        elif ("jarvis" in query) and ("motivate" in query or "motivation" in query and "me" in query):
            try:
              speak(str(Elements.get_random_quote()))
            except:
                speak("Sorry sir...")

        elif 'thank' in query:
            speakk("No problem sir.", "Not a problem.", "Dont mention sir.", "Welcome sir.")
        elif any(item in query for item in question_elements)  and 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "wake up" in query or 'where are you' in query:
            speak(f"Sir, the time is {strTime}")

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "itikkadoleedu@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir i could not send this email")

        elif 'clear all' in query:
            try:
                mylist2.delete("1.0", END)
            except:
                pass

            speakk("Ok sir", "Clearing...", "Understood Sir", "Clearing Sir")
            global j
            j = 1
        elif query == "jarvis":
            speak(", Sir...")
        elif 'jarvis shutdown' in query and ('system' in query ):
            speak("Shutting down the system, good bye and, stay motivated sir...")
            os.system("shutdown /s /t 1")

        elif 'are you there' in query:
            speakk("At your service sir.", "For you, always sir.")

       # to store queries uncomment this below code
       #  else:
       #      if query == "none":
       #          continue
       #      try:
       #          strr = "insert into userquery values(NULL," + query + ",false);"
       #          mycursor.execute(strr)
       #          con.commit()
       #      except:
       #          pass
       #
       #      continue
       #  if query == "none":
       #      continue

        # query = '"' + query + '"'
        # try:
        #   strr = "insert into userquery values(NULL," + query + ",true);"
        #   mycursor.execute(strr)
        #   con.commit()
        # except:
        #     pass


t2 = threading.Thread(target=main_thread, args=())


# t2 = multiprocessing.Process(target=main_thread, args=())


def start_assistant():
    # main.quit()
    speak("Hello sir...")

    wishMe()
    t2.start()

    print("\n_______________________\n")



process = multiprocessing.Process(target=start_assistant, args=())


# process2 = multiprocessing.Process(target=mainloop(), args=())


def Exit():
    # global run
    # run= False
    engine.stop()

    root.quit()


    try:
        # process.terminate()
        engine.stop()
        # t2.terminate()
        # process2.terminate()
    except:
        pass
    try:
        # process.terminate()
        # r.__exit__()
        t2.terminate()
        # process2.terminate()
    except:
        pass
    try:
        global stop_threads
        stop_threads = True
        # process2.terminate()
    except:
        pass
    try:
        # t2.terminate()
        process.terminate()
    except:
        pass
    try:
        root.quit()
        # process2.terminate()
    except:
        pass
    # try:
    #     root.destroy()
    #     # process2.terminate()
    # except:
    #     pass

    exit()


# def Stop():
#     # try:
#         process.terminate()
#         del process

#         process = multiprocessing.Process(target=start_assistant, args=())


def main_function_starter():
    # print(type(process))

    #  mainthread = threading.Thread(target=start_assistant, args=())
    #  mainthread.start()
    # root.mainloop()

    process.start()
    # process.join()
    # process2.start()
    # t2.start()


'''_____________MAIN FUNCTION______________'''

# main = Tk()
# # main.geometry("200*190")

# scrollbar = Scrollbar(main)
# scrollbar.pack( side = RIGHT, fill = Y )

# mylist = Listbox(main, yscrollcommand = scrollbar.set )

# mylist.insert(END, str("strr"))

# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )


'''_____________MAIN FUNCTION______________'''

# def temp():
#     Frame1.update()


L = Label(root, text=" STATE ",font=('"Impact" 12' ),padx=0, pady=0, bd=0, foreground="white" , background="#ff0000" )
L.grid(row=0, sticky=W, rowspan=5,pady=0,padx=0,)
L.place(x=11, y=59)

M = Label(root, text=" USER INPUTS ",font=('"Impact" 12' ),padx=0, pady=0, bd=0, foreground="white" , background="#ff0000" )
M.grid(row=0, sticky=W, rowspan=5,pady=0,padx=0,)
M.place(x=11, y=179)

N = Label(root, text=" ASSISTANT OUTPUTS ",font=('"Impact" 12' ),padx=0, pady=0, bd=0, foreground="white" , background="#ff0000" )
N.grid(row=0, sticky=W, rowspan=5,pady=0,padx=0,)
N.place(x=521, y=59)


# b = Button(root, text="Start", command=start_assistant)

b = Button(root, text="Start" ,command=start_assistant, relief=GROOVE,font=('"Biting My Nails" 20'),foreground='white',background='#171717',activebackground='#171717',activeforeground='cyan',borderwidth=0,highlightcolor='yellow',highlightbackground='white')
b.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

# # s=Button(root,text="Stop", command=Stop)
# # s.grid(row=0,column=12,columnspan=2,padx=5,pady=5)
#
# e = Button(root, text="Exit",command=Exit, relief=GROOVE,font=('"Segoe UI Black"  16'),foreground='white',background='black',activebackground='black',activeforeground='cyan',borderwidth=0)
# e.grid(row=0, column=22, columnspan=2, padx=5, pady=5)
#
# e = Button(root, text="Exit",command=Exit, relief=GROOVE,font=('"Bauhaus 93"  20'),foreground='white',background='black',activebackground='black',activeforeground='cyan',borderwidth=0)
# e.grid(row=0, column=25, columnspan=2, padx=5, pady=5)

e = Button(root, text="Exit",command=Exit, relief=GROOVE,font=('"Biting My Nails"  20'),foreground='white',background='#171717',activebackground='#171717',activeforeground='cyan',borderwidth=0)
e.grid(row=0, column=25, columnspan=2, padx=5, pady=5)
# root.after(3000,root.update)


# root.quit()


# start_assistant()
# mainloop()





if __name__ == "__main__":




           root.mainloop()

    # main.mainloop()




