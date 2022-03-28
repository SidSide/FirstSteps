from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('29e734735d9b67bb4bb704ad69ae2358')
mgr = owm.weather_manager()

place=input("Город: ")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
temp = w.temperature('celsius') ["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура: " + str(temp))

if temp<0:
	print("Дубак")
elif temp>0:
	print("Весна пришла")
else:
	print("ХЗ")