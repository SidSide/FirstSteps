import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('29e734735d9b67bb4bb704ad69ae2358')
mgr = owm.weather_manager()

bot = telebot.TeleBot("5279023735:AAHQeJlIMI14loAjcXzUtQ3BUepKVGKAC8g")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius') ["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n\n"
	answer += "Температура: " + str(temp) + "\n\n"

	if temp<0:
		answer +="Погодка совсем не такая жаркая, как ты. Одевайся потеплее! И хорошего тебе дня!"
	elif temp<10:
		answer +="Весна робко входит в свои права, но лучше не выходить расстёгнутой! Хорошего дня!"
	elif temp<15:
		answer +="За окном уже совсем весна!"
	else:
		answer +="Погода супер, совсем как ты!"
	#bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)