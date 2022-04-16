import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('29e734735d9b67bb4bb704ad69ae2358')
mgr = owm.weather_manager()

bot = telebot.TeleBot("5279023735:AAHQeJlIMI14loAjcXzUtQ3BUepKVGKAC8g")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    # daily_forecaster = mgr.forecast_at_place(message.text, 'daily')
    # tomorrow = timestamps.tomorrow()
    # wt = daily_forecaster.get_weather_at(tomorrow)
    temp = w.temperature('celsius')["temp"]
    temp_feel = w.temperature('celsius')["feels_like"]
    wind_speed = w.wind()['speed']
    try:
        wind_force = w.wind()['gust']
    except KeyError:
        wind_force = -1

    # if bool(w.wind()['gust']) == False:
    #     wind_force = -1
    # else:
    #     wind_force = w.wind()['gust']
    wind_where = w.wind()['deg']

    answer = "Населенный пункт: " + message.text + "\n\n"
    answer += "Температура сейчас: " + str(temp) + " ℃" + "\n"
    answer += "Ощущается как " + str(temp_feel) + " ℃" + "\n\n"
    answer += "На небе: " + w.detailed_status + "\n\n"
    answer += "Влажность: " + str(w.humidity) + "%" + "\n\n"
    # answer += "Ветер: " + str(wind_where) + "°" + "\n"

    if 338 <= int(wind_where) <= 360:
        answer += "Ветер: Северный" + "\n"
    elif 0 <= int(wind_where) <= 22:
        answer += "Ветер: Северный" + "\n"
    elif 23 <= int(wind_where) <= 68:
        answer += "Ветер: Северо-восточный" + "\n"
    elif 69 <= int(wind_where) <= 112:
        answer += "Ветер: Восточный" + "\n"
    elif 111 <= int(wind_where) <= 157:
        answer += "Ветер: Юго-восточный" + "\n"
    elif 156 <= int(wind_where) <= 202:
        answer += "Ветер: Южный" + "\n"
    elif 201 <= int(wind_where) <= 247:
        answer += "Ветер: Юго-западный" + "\n"
    elif 246 <= int(wind_where) <= 292:
        answer += "Ветер: Западный" + "\n"
    elif 291 <= int(wind_where) <= 337:
        answer += "Ветер: Северо-западный" + "\n"
    else:
        answer += "Направление ветра не определено" + "\n"

    answer += "Скорость ветра: " + str(wind_speed) + " м/с" + "\n"

    if 0 < int(wind_force) < 800:
        answer += "Порывы до: " + str(wind_force) + " м/с" + "\n\n"
    else:
        answer += "Данных по порывам ветра нет" + "\n\n"

    if temp < 0:
        answer += "Погодка совсем не такая жаркая, как ты. Одевайся потеплее! И хорошего тебе дня!" + "\n\n"
    elif temp < 10:
        answer += "Весна робко входит в свои права, но лучше не выходить расстёгнутой! Хорошего дня!" + "\n\n"
    elif temp < 15:
        answer += "За окном уже совсем весна!" + "\n\n"
    else:
        answer += "Погода супер, совсем как ты!" + "\n\n"

    # bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
