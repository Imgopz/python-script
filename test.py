# importing libraries
import pyowm

# loading api key
owm = pyowm.OWM('API_KEY')

# observing and getting weather details for a specified location
observation = owm.weather_at_place('Philadelphia, Pennsylvania, United States')
w = observation.get_weather()

# fetching values from the weather details
tempC = w.get_temperature('celsius')
tempF = w.get_temperature('fahrenheit')
status = w.get_detailed_status()
humidity = w.get_humidity()

# displaying values
print('\n*********Philadelphia, Pennsylvania, United States*********')
print('\nTemperature: ' + str(int(tempC['temp'])) + ' deg C | ' + str(int(tempF['temp'])) + ' deg F')
print('Humidity: ' + str(humidity) + ' %')
print('\n*************************END*******************************')
