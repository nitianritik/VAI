import socket
import webbrowser
import speedtest
import pyttsx3
import os
import time
import keyboard
import requests
import json
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(" , "+audio)
    print(audio)
    # engine.runAndWait()


question_elements = {"where", "how", "when", "how", "what"}
start_elements = {"start", "turn on", "open", "run"}
stop_elements = {"stop", "close", "off", "turn off", "band", "terminate"}

####---- DIFFERENT FUNCTIONS STARTS HERE -----####

'''
 _____________________________________________

 Function to check INTERNET CONNECTION
 _____________________________________________

'''

REMOTE_SERVER = "one.one.one.one"


def is_connected(hostname):
    #Assuming we are offline here
    i=False
    j=False
    k=False

    ''' FIRST CHECK '''
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        i = True  # Stores True if first check is online
    except:
        pass
    ''' SECOND CHECK '''
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        j = True  # Stores True if first check is online
    except:
        pass
    ''' THIRD CHECK '''
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        j = True  # Stores True if first check is online
    except:
        pass


    return (i or j or k)


# __________________________________________

'''
 _____________________________________________

 Function to GOOGLE.COM
 _____________________________________________

'''


def open_google():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', webbrowser.BackgroundBrowser(chrome_path), 1)
    webbrowser.open_new_tab("www.google.com")


'''
 _____________________________________________

 Function to OPEN YOUTUBE.COM
 _____________________________________________

'''


def open_youtube():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', webbrowser.BackgroundBrowser(chrome_path), 1)
    webbrowser.open_new_tab("www.youtube.com")


'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''


def check_speed():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', webbrowser.BackgroundBrowser(chrome_path), 1)
    webbrowser.open_new_tab("www.fast.com")


'''
 _____________________________________________

 Function to CHECK INTERNET SPEED
 _____________________________________________

'''
from tkinter import *

def check_internet_speed():
    t = Toplevel()



    test = speedtest.Speedtest()
    print("SERVER LIST ...")

    test.get_servers()  # ---->>> gets list of servers
    print("BEST SERVER IS ... ")

    best = test.get_best_server()  # --->>> chooses best servers
    print(f"Found Server : {best['host']} ||  Location : {best['country']}")

    print("Performing download test...")
    download_result = test.download()

    print("Performing upload test...")
    upload_result = test.upload()

    ping_result = test.results.ping

    print(download_result)
    print(upload_result)

    t.mainloop()

# check_internet_speed()

'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''

def checkk():
    import keyboard

    keyboard.press_and_release('windows')
    time.sleep(1)
    keyboard.write('cmd')
    time.sleep(1)
    keyboard.press_and_release('Enter')
    time.sleep(1)
    keyboard.write('speedtest')
    time.sleep(1)
    keyboard.press_and_release('Enter')


    return

'''
 _____________________________________________

 Function to OPEN Chrome
 _____________________________________________

'''
def open_chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', webbrowser.BackgroundBrowser(chrome_path), 1)
    os.startfile(chrome_path)

'''
 _____________________________________________

 Function to SWITCH WINDOW
 _____________________________________________

'''

def switch_window():
    keyboard.press_and_release('alt+tab')

'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''

def search(query):
    # query = query.replace('search', '', 1)
    # query = query.replace('for ', '', 1)
    # query = query.replace(' ', '+')
    # query = query.strip()
    query = query.replace(' ', '+')
    query = query.strip()
    query = "https://www.google.com/search?q=" + query
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', webbrowser.BackgroundBrowser(chrome_path), 1)
    webbrowser.open_new_tab(query)

def search_youtube(query):
    # query = query.replace('search', '', 1)
    # query = query.replace('for ', '', 1)
    # query = query.replace(' ', '+')
    # query = query.strip()
    query = query.replace(' ', '+')
    query = query.strip()
    #https://www.youtube.com/results?search_query=Support+Vector+Machine+Algorithm
    query = "https://www.youtube.com/results?search_query=" + query
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', webbrowser.BackgroundBrowser(chrome_path), 1)
    webbrowser.open_new_tab(query)





'''
 _____________________________________________

 Function to OPEN CODE
 _____________________________________________
 


'''

def open_code():
    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

'''
 _____________________________________________

 Function to Crack Joke
 _____________________________________________

'''




def crack_jokes():
    ##### 1 st api ####
    f = "https://geek-jokes.sameerkumar.website/api?format=json"
    data = requests.get(f)
    joke = json.loads(data.text)
    return joke["joke"]
    ##### JOKE LIBRARY 02

    # using get_joke() to generate a single joke
    # language is english
    # category is neutral


    ##### 2 nd api ####
    joke = pyjokes.get_joke(language="en", category="neutral")
    return joke



def get_random_quote():
	try:
		## making the get request
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']

			## getting the quote from the data
			return data[0]['quoteText']
		else:
			print("Error while getting quote")
	except:
		return "Sorry sir..."
'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''

def start_study():
    path=["D:\STUDY"
          , "E:\🏆 MCA Semester 4"
          , "https://www.indiabix.com/interview/#"
          , "https://drive.google.com/drive/u/4/my-drive"
          , "https://leetcode.com/nitianritik/"
         ]

    for i in path:
        try:
            webbrowser.open(i)
        except:
            pass

'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''

def switch_tab(query):
    if ('1st' in query or 'first' in query):
        keyboard.press_and_release('ctrl + 1')
    elif ('2nd' in query or 'second' in query):
        keyboard.press_and_release('ctrl + 2')
    elif ('3rd' in query or 'third' in query):
        keyboard.press_and_release('ctrl + 3')
    elif ('4th' in query or 'fourth' in query):
        keyboard.press_and_release('ctrl + 4')
    elif ('5th' in query or 'fifth' in query):
        keyboard.press_and_release('ctrl + 5')
    elif ('6th' in query or 'sixth' in query):
        keyboard.press_and_release('ctrl + 6')
    elif ('7th' in query or 'seventh' in query):
        keyboard.press_and_release('ctrl + 7')
    elif ('8th' in query or 'eighth' in query):
        keyboard.press_and_release('ctrl + 8')
    elif ('9th' in query or 'nineth' in query):
        keyboard.press_and_release('ctrl + 9')
    # if ('10th' or 'tenth' in query):
    #     keyboard.press_and_release('ctrl + 10')
    # if ('11th' or 'eleventh' in query):
    #     keyboard.press_and_release('ctrl + 11')
    # if ('12th' or 'twelth' in query):
    #     keyboard.press_and_release('ctrl + 11')

'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''

def weather_report():
  api_key = "6568cf3ecfd4eba82131100bd3793971"  # Enter the API key you got from the OpenWeatherMap website
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  try:
      city_name = "bhopal"
      complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
      response = requests.get(complete_url)
      x = response.json()
      print("\n\n\n")
      print("\n\n\n")

      if x["cod"] != "404":
          y = x["main"]
          i = x["wind"]
          current_temperature = res = "{:.2f}".format(y["temp"] - 273.15)
          current_pressure = y["pressure"]
          current_humidity = y["humidity"]
          z = x["weather"]
          windspeed = "{:.2f}".format(i["speed"] * 3.6)
          weather_description = z[0]["description"]

          data = {"Temprature": str(current_temperature),
                  "Atmospheric pressure": str(current_pressure) + "Hectopascal",
                  "Humidity": str(current_humidity) + " Precentage",
                  "Description": str(weather_description) + " is visible",
                  "windspeed": str(windspeed)}

          showdata = "Temp: " + str(current_temperature) + " °C" + " | Desc: " + str(
              weather_description) + " | Wind speed: " + str(windspeed) + " km\h" + " | Humidity: " + str(
              current_humidity) + " %" + " | AP: " + str(current_pressure) + " hPa"

          speakdata = "Temprature is " + str(current_temperature) + " °Celsius. " + str(
              weather_description) + " is visible. "+ " Wind speed is " + str(
              windspeed) + " kilometer per hour. " + " Humidity level is " + str(
              current_humidity) + " percentage in the air. " + " and the atmospheric pressure is " + str(
              current_pressure) + " hectopascal"

          finaldata = [showdata, speakdata]
          return finaldata


      else:
          print(" City Not Found ")
  except:
      pass


'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''

'''
 _____________________________________________

 Function to OPEN PROGRAMS
 _____________________________________________

'''


