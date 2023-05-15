import time
import telebot


TOKEN = '' # @BotFather
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command_handelr(message):
	text = 'Send Your File'
	bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['audio'])
def audio_handler(message):
	print(message)
	file_info = bot.get_file(message.audio.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	bot.send_voice(message.chat.id, downloaded_file)


if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
		except Exception as e:
			print(e)
			time.sleep(30)





