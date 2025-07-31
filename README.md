#Weather Application (Command-Line Project)

This is a simple command-line Python application that allows users to check the current weather of any city using the OpenWeatherMap API. It helps beginners learn how to use APIs, handle JSON data, and structure code using functions.

---

#Features

- User can enter a city name to get:
  - City name
  - Temperature (in Celsius)
  - Weather condition (e.g., clear, cloudy, rain)
  - Humidity level
  - Wind speed
- Uses the `requests` library to call a public weather API
- Handles errors like:
  - Invalid city name
  - Network/API issues

---

#Requirements

- Python 3.x
- `requests` library

#Install the requests library:

```bash
pip install requests
```

---

#How to Run the App

1. Get a free API key from [https://openweathermap.org/api](https://openweathermap.org/api).
2. Create a file named `weather_app.py` and paste the Python code.
3. Inside the code, add your API key in this line:

```python
API_KEY = "your_api_key_here"
```

4. Open your terminal or VS Code terminal.
5. Navigate to the folder where the file is saved.
6. Run the app using:

```bash
python weather_app.py
```

7. Enter a city name when prompted.

---

#Example Output

```
== Weather App ==
Enter city name: Chennai

 Weather Info:
City: Chennai
Temperature: 31.5°C
Condition: Clear sky
Humidity: 60%
Wind Speed: 4.3 m/s
```

---

#Learning Objectives

- How to use third-party APIs
- How to parse and handle JSON data in Python
- How to organize Python code using functions
- Basic error handling
- Command-line interaction

---

#Author

This project was created as a beginner-friendly task to improve Python skills with real-world API usage.
