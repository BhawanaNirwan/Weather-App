import tkinter as tk
from tkinter import messagebox
import requests

# Your OpenWeatherMap API Key
API_KEY = 'fcc8de7015bbb202209bbf0261babf4c'  # Replace this with your own API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Function to get weather
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        # Request weather data from OpenWeatherMap API
        response = requests.get(f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric')
        data = response.json()

        # Check if the city is found
        if data['cod'] == 200:
            city_name = data['name']
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            icon_code = data['weather'][0]['icon']

            # Update the UI with the weather information
            result_label.config(text=f"Weather in {city_name}")
            temperature_label.config(text=f"Temperature: {temp}°C")
            description_label.config(text=f"Description: {weather_desc.capitalize()}")
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            icon_img = tk.PhotoImage(file=icon_url)  # You may need to download the icon image
            icon_label.config(image=icon_img)
            icon_label.image = icon_img  # Keep a reference to the image
        else:
            messagebox.showerror("Error", f"City '{city}' not found.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")

# Set up the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#f0f8ff")

# City input field
city_label = tk.Label(root, text="Enter City Name", font=("Arial", 14), bg="#f0f8ff")
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

# Get Weather button
get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather)
get_weather_button.pack(pady=10)

# Labels to display weather results
result_label = tk.Label(root, text="Weather Info", font=("Arial", 18, "bold"), bg="#f0f8ff")
result_label.pack(pady=20)

temperature_label = tk.Label(root, text="Temperature: ", font=("Arial", 14), bg="#f0f8ff")
temperature_label.pack(pady=5)

description_label = tk.Label(root, text="Description: ", font=("Arial", 14), bg="#f0f8ff")
description_label.pack(pady=5)

icon_label = tk.Label(root, bg="#f0f8ff")
icon_label.pack(pady=10)

# Start the main event loop
root.mainloop()
