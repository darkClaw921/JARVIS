from simple_bot import Bot
from longpoll_bot import LongPollBot


# создание и запуск обычного бота
bot = Bot()
    
# отправка тестового сообщения
bot.send_message()

long_poll_bot = LongPollBot()
long_poll_bot.run_long_poll()
  
# отправка сообщения с заданными параметрами
#bot.send_message(receiver_user_id="59125947", message_text="Привет, это сообщение отправлено автоматически")
