import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("6399845740:AAE3comDFyRcr0keIGCLj_gKNMTfr-euic0",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "Привет"  # Можно менять текст
text_button_1 = "о любви"  # Можно менять текст
text_button_2 = "о друге"  # Можно менять текст
text_button_3 = "о проблеме"  # Можно менять текст

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет! может познакомимся?',  # Можно менять текст
        reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id, 'Какое ваше _имя_?')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)



@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id, 'Хорошее имя) А сколько _лет_ моему читателю? ')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.age, message.chat.id)


@bot.message_handler(state=PollState.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    bot.send_message(message.chat.id, 'Рад знакомсву. Предлагаю окунуться в мир стихотворений',
                     reply_markup=menu_keyboard)  # Можно менять текст
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, """Ты у меня в голове гуляешь,
И зашла в глубины моего сознания
И пусть между нами расстояние
У меня одно сокровенное желание
 
Никакие подарки мне не нужны, 
Кроме одной, падающий звезды
На которую я просто взгляну и загадаю, 
Лишь бы ты была счастливая рядом. 
 
Твоя улыбка дороже всего на свете
Хотел бы её видеть в любые моменты, 
Хоть сейчас мы с тобой не вместе, 
Но я запомню твою улыбку в сердце. 
 
Не важно, что происходит за спиной, 
Все мои здравые мысли долой. 
Мне кажется, что нашел свое призвание,
Когда ты сразила своим очарованием
 
Я хочу делать тебя счастливой, 
Даже если нужно рисковать жизнью, 
Все в мире будет только для тебя
Если возьмешь в свою жизнь, меня"""
, reply_markup=menu_keyboard)  # Можно менять текст \ \


@ bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, """Вот ты сидишь на перроне, 
В ожидании чего-то хорошего, 
Хочешь затушить свое горе, 
Но нет друга надёжного. 
 
Поезда приходят и уходят,
Подобно друзьям вокруг. 
И вот он, единственный,приходит
И потом понимаешь, что он не самый верный друг.
 
Когда ты считаешь, что это он,
Тот самый, которого долго ждал,
То тебе приходиться возвращаться домой,
Понимая, что билет потерял...
 
И вот, когда встретишь его,
То ты понимаешь с кем хочешь жизнь провести,
В ненастье, счастье и горе,
Ты в свою душу ему путь укажи"""
, reply_markup=menu_keyboard)  # Можно менять текст \ \


@ bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, """Я словно камень брошенный,
Живу один под своей звездой.
И часто так бывает,
Что душу свою никому не открываю. 
 
И спокойно жизнь ты проводишь,
Встречая перед собой преграды -
И спокойно ты их решаешь,
Или же совсем про все забываешь.
 
Конечно же, есть у меня цель, быть может, 
Которая скорее всего не понятна.
Может кто-то мне в будущем в этом поможет,
Возможно я просто отложу все, как всегда, на завтра.
 
И когда я это осознаю, возможно,
Тогда решу все делать сразу. 
Но это лишь тот промежуток времени,
Когда я уже выгоню эту заразу.
Когда ты вдруг понимаешь,
Что словно нет смысла в жизни,
Что в жизни ты не кому не нужен,
И будешь до конца стоять, как на полке старая книжка"""
, reply_markup=menu_keyboard)  # Можно менять текст


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()
