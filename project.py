from tkinter import messagebox
import requests
import tkinter

# Link to open weather details
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b5e9675885ea680bf8ccb296a620f50f'


# Function to get weather details
def get_weather(city):
    result = requests.get(url.format(city))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = float("{:.2f}".format(temp_kelvin - 273.15))
        weather1 = json['weather'][0]['description']
        final = [city, country, temp_kelvin,
                 temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")


# Function to search about city
def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + " Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


# Creating App Window
weather_app = tkinter.Tk()
weather_app.title("Weather App ☔☀️🌦️☁️")
weather_app.geometry("400x300")
weather_app.configure(background='#00BFFF')

# Adding entry field
city_text = tkinter.StringVar()
city_entry = tkinter.Entry(weather_app, textvariable=city_text, width=16, font={'bold'}, background='#ADD8E6')
city_entry.pack()
line_break = tkinter.Label(weather_app, text="\n", background='#00BFFF')
line_break.pack()

# Adding button
Search_btn = tkinter.Button(weather_app, text="Search Weather", command=search, width=15, padx=20, pady=10,
                            font={'bold'}, background='#ADD8E6', foreground='green')
Search_btn.pack()
line_break = tkinter.Label(weather_app, text="\n", background='#00BFFF')
line_break.pack()

location_lbl = tkinter.Label(weather_app, text="Location", font={'bold'}, background='#00BFFF')
location_lbl.pack()
temperature_label = tkinter.Label(weather_app, text="", background='#00BFFF')
temperature_label.pack()
weather_l = tkinter.Label(weather_app, text="", background='#00BFFF')
weather_l.pack()
weather_app.mainloop()
