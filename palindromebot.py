import telebot

bot = telebot.TeleBot("5116644969:AAFKTn0ulRnrVOVlqvaaQi9RXflhRWyby8Q")


@bot.message_handler(content_types=["text"])
def check_pali(message):
    message.text = message.text.lower()
    counts = {}
    for letter in message.text:
        if letter in counts.keys():
            counts[letter] += 1
        elif ord(letter) >= 1072 and ord(letter) <= 1103:
            counts[letter] = 1
    middle = ""
    answer = ""
    reversed_string = ""
    s = message.text.replace(" ", "")
    for i in range(len(s), 0, -1):
        reversed_string += s[i - 1]
    if s == reversed_string:
        answer = "Строка является палиндромом"
    else:
        # answer = "неа"
        for letter in counts:
            if middle and counts[letter] % 2 == 1:
                answer = "Строка не является палиндромом.\n"
                answer += "Из неё невозможно составить палиндром"
            elif counts[letter] % 2 == 1:
                middle = letter
                new_pali = ""
                if middle:
                    new_pali = middle * counts[middle]
                for letter in counts:
                    if letter != middle:
                        new_pali = letter * int(counts[letter] / 2) + new_pali + letter * int(counts[letter] / 2)
                        answer = "Строка не является палиндромом.\n"
                        answer += "Однако из неё возможно составить палиндром.\n"
                        answer += "Вот его возможный вариант:\n"
                        answer += new_pali
            elif counts[letter] % 2 == 0:
                new_pali = ""
                if middle:
                    new_pali = middle * counts[middle]
                for letter in counts:
                    if letter != middle:
                        new_pali = letter * int(counts[letter] / 2) + new_pali + letter * int(counts[letter] / 2)
                        answer = "Строка не является палиндромом.\n"
                        answer += "Однако из неё возможно составить палиндром.\n"
                        answer += "Вот его возможный вариант:\n"
                        answer += new_pali
        # return True
    # our_string = message.text
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)

# print(check_pali(our_string))
