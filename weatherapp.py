import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Input Error", "Please enter a city name")
        return

    # OpenWeatherMap API URL with the API key
    api_key = "c7073cd8cd9ce53a6348f67dea39d5f5"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    # Make a request to the API
    try:
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found. Please try again.")
        else:
            main_data = data["main"]
            weather_data = data["weather"][0]
            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            description = weather_data["description"]

            # Display weather data
            weather_info.config(text=f"Temperature: {temperature}°C\n"
                                    f"Pressure: {pressure} hPa\n"
                                    f"Humidity: {humidity}%\n"
                                    f"Description: {description.capitalize()}")
    except Exception as e:
        messagebox.showerror("Connection Error", "Failed to connect to the weather service.")

# Set up the GUI
root = tk.Tk()
root.title("Weather App")

# Set window size
root.geometry("400x400")

# Add a label for the city input
city_label = tk.Label(root, text="Enter City Name:", font=('normal', 14))
city_label.pack(pady=10)

# Add an entry widget for the city name
city_entry = tk.Entry(root, font=('normal', 14))
city_entry.pack(pady=10)

# Add a button to get weather data
get_weather_button = tk.Button(root, text="Get Weather", font=('normal', 14), command=get_weather)
get_weather_button.pack(pady=10)

# Label to display weather info
weather_info = tk.Label(root, text="", font=('normal', 14), justify=tk.LEFT)
weather_info.pack(pady=20)

# Run the app
root.mainloop()

