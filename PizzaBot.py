from telebot import *
import csv
bot = TeleBot('1600511033:AAFrVE1PILYh_koEvBym_RiUsM832V4lmEU')
inline = types.InlineKeyboardMarkup()
in_yes = types.InlineKeyboardButton(text='Да!', callback_data='yes')
in_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
inline.add(in_yes,in_no)
inline2 = types.InlineKeyboardMarkup()
in_da = types.InlineKeyboardButton(text='Давай', callback_data='da')
in_net = types.InlineKeyboardButton(text='Не', callback_data='net')
inline2.add(in_da, in_net)
inline3 = types.InlineKeyboardMarkup()
in_buyN = types.InlineKeyboardButton(text='6 кусков(30000)',callback_data='buy')
in_menu = types.InlineKeyboardButton(text='Меню',callback_data='menu')
inline3.add(in_buyN,in_menu)
inline4 = types.InlineKeyboardMarkup()
in_buyM = types.InlineKeyboardButton(text='6 кусков(35000)',callback_data='buy')
inline4.add(in_buyM,in_menu)
inline5 = types.InlineKeyboardMarkup()
in_buyC = types.InlineKeyboardButton(text='6 кусков(32000)',callback_data='buy')
inline5.add(in_buyC,in_menu)
inlineMox = types.InlineKeyboardMarkup()
in_buyMo = types.InlineKeyboardButton(text="Заказать(15000)",callback_data='buy')
inlineMox.add(in_buyMo,in_menu)
reply1 = types.ReplyKeyboardMarkup(True,True)
opt11 = types.KeyboardButton('Заказать')
opt21 = types.KeyboardButton('Помощь')
reply1.add(opt11, opt21)
reply2 = types.ReplyKeyboardMarkup(True,True)
opt12 = types.KeyboardButton('Пицца')
opt32 = types.KeyboardButton('Десерты')
opt42 = types.KeyboardButton('Напитки')
opt52 = types.KeyboardButton('Назад')
reply2.add(opt12,opt32,opt42,opt52)
replyPizza=types.ReplyKeyboardMarkup(True,True)
opt13=types.KeyboardButton('Моцарелла')
opt23=types.KeyboardButton('Пепперони')
opt33=types.KeyboardButton('Пепперони-микс')
opt43 = types.KeyboardButton('Курица-барбекю')
opt53 = types.KeyboardButton('Чизбургер-пицца')
opt63 = types.KeyboardButton('Чили-пицца')
opt73 = types.KeyboardButton('Вегетарианская')
opt83 = types.KeyboardButton('Меню')
replyPizza.add(opt13,opt23,opt33,opt43,opt53,opt63,opt73,opt83)
replyDeserts = types.ReplyKeyboardMarkup(True,True)
opt15 = types.KeyboardButton('Наполеон')
opt25 = types.KeyboardButton('Медовик')
opt35 = types.KeyboardButton('Синнабоны')
opt45 = types.KeyboardButton('Меню')
replyDeserts.add(opt15,opt25,opt35,opt45)
replyDrinks = types.ReplyKeyboardMarkup(True,True)
opt16 = types.KeyboardButton('Coca-cola 0.5')
opt26 = types.KeyboardButton('Coca-cola 1.0')
opt36 = types.KeyboardButton('Coca-cola 1.5')
opt46 = types.KeyboardButton('Мохито PizzaOn')
opt56 = types.KeyboardButton('Меню')
replyDrinks.add(opt16,opt26,opt36,opt46,opt56)
replySize = types.ReplyKeyboardMarkup(True,True)
opt17 = types.KeyboardButton('Маленькая(16000)')
opt27 = types.KeyboardButton('Средняя(25000)')
opt37 = types.KeyboardButton('Большая(34000)')
opt47 = types.KeyboardButton('Мега(45000)')
opt57 = types.KeyboardButton('Не хочу эту пиццу')
replySize.add(opt17,opt27,opt37,opt47,opt57)
replySize2 = types.ReplyKeyboardMarkup(True,True)
optPS = types.KeyboardButton('Маленькая(19000)')
optPM = types.KeyboardButton('Средняя(23000)')
optPB = types.KeyboardButton('Большая(35000)')
optPME = types.KeyboardButton('Мега(51000)')
replySize2.add(optPS,optPM,optPB,optPME,opt57)
replySize3 = types.ReplyKeyboardMarkup(True,True)
optMS = types.KeyboardButton('Маленькая(22000)')
optMM = types.KeyboardButton('Средняя(31000)')
optMB = types.KeyboardButton('Большая(43000)')
optMME = types.KeyboardButton('Мега(58000)')
replySize3.add(optMS,optMM,optMB,optMME,opt57)
replySize4 = types.ReplyKeyboardMarkup(True,True)
optBS = types.KeyboardButton('Маленькая(25000)')
optBM = types.KeyboardButton('Средняя(33000)')
optBB = types.KeyboardButton('Большая(41000)')
optBME = types.KeyboardButton('Мега(57000)')
replySize4.add(optBS,optBM,optBB,optBME,opt57)
replySize5 = types.ReplyKeyboardMarkup(True,True)
optCS = types.KeyboardButton('Маленькая(26000)')
optCM = types.KeyboardButton('Средняя(35000)')
optCB = types.KeyboardButton('Большая(46000)')
optCME = types.KeyboardButton('Мега(60000)')
replySize5.add(optCS,optCM,optCB,optCME,opt57)
replySize6 = types.ReplyKeyboardMarkup(True,True)
optCHS = types.KeyboardButton('Маленькая(31000)')
optCHM = types.KeyboardButton('Средняя(50000)')
optCHB = types.KeyboardButton('Большая(74000)')
optCHME = types.KeyboardButton('Мега(112000)')
replySize6.add(optCHS,optCHM,optCHB,optCHME,opt57)
replySize7 = types.ReplyKeyboardMarkup(True,True)
optVS = types.KeyboardButton('Маленькая(15000)')
optVM = types.KeyboardButton('Средняя(21000)')
optVB = types.KeyboardButton('Большая(35000)')
optVME = types.KeyboardButton('Мега(40000)')
replySize7.add(optVS,optVM,optVB,optVME,opt57)
replyLocation = types.ReplyKeyboardMarkup(True,True)
loc = types.KeyboardButton(text="Отправить свою локацию",request_location=True)
replyLocation.add(loc,opt56)
replyPhone = types.ReplyKeyboardMarkup(True,True)
ph = types.KeyboardButton(text="Поделиться номером",request_contact=True)
replyPhone.add(ph,opt56)
@bot.message_handler(commands=['start','help'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,"Добро пожаловать в PizzaOn!\nЛюбите пиццу с итальянским привкусом?)",reply_markup=inline)
    elif message.text == '/help':
        bot.send_message(message.chat.id,'Это бот пиццерии "PizzaOn". Совершайте заказы и получите бесплатную доставку по Самарканду')
@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id,"Круто!",reply_markup=reply1)
    elif call.data == 'no':
        reply3 = types.ReplyKeyboardMarkup(True,True)
        reply3.add(opt32,opt42,opt52)
        bot.send_message(call.message.chat.id,'Тогда меню без пиццы:',reply_markup=reply3)
    elif call.data == 'da':
        bot.send_message(call.message.chat.id,'Отправьте нам свой адрес:',reply_markup=replyLocation)
    elif call.data == 'net':
        bot.send_message(call.message.chat.id,'Наш ассортимент:',reply_markup=reply2)
    elif call.data == 'buy':
        bot.send_message(call.message.chat.id,'Отправьте нам свой адрес:',reply_markup=replyLocation)
    elif call.data == 'menu':
        bot.send_message(call.message.chat.id,'Меню:',reply_markup=reply2)
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Заказать':
        bot.send_message(message.chat.id, "Наш ассортимент:", reply_markup=reply2)
    elif message.text == 'Помощь':
        bot.send_message(message.chat.id,'Это бот пиццерии "PizzaOn". Совершайте заказы и получайте бесплатную доставку по Самарканду')
    elif message.text == 'Пицца':
        bot.send_message(message.chat.id,"Выбирай по душе:",reply_markup=replyPizza)
    elif message.text == 'Десерты':
        bot.send_message(message.chat.id,"Десерты:",reply_markup=replyDeserts)
    elif message.text == 'Напитки':
        bot.send_message(message.chat.id,"Дринки:",reply_markup=replyDrinks)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id,"Ну ок",reply_markup=reply1)
    elif message.text == 'Моцарелла':
        bot.send_photo(message.chat.id,'https://imbt.ga/MnFEdMnT3C',reply_markup=replySize)
    elif message.text == 'Пепперони':
        bot.send_photo(message.chat.id,'https://imbt.ga/8SncR7QX5T', reply_markup=replySize2)
    elif message.text == 'Пепперони-микс':
        bot.send_photo(message.chat.id, 'https://imbt.ga/JdSQLdBQeZ', reply_markup=replySize3)
    elif message.text == 'Курица-барбекю':
        bot.send_photo(message.chat.id, 'https://imbt.ga/oskPfzu8kn', reply_markup=replySize4)
    elif message.text == 'Чизбургер-пицца':
        bot.send_photo(message.chat.id, 'https://imbt.ga/6sZzEh28dD', reply_markup=replySize5)
    elif message.text == 'Чили-пицца':
        bot.send_photo(message.chat.id, 'https://imbt.ga/z67f42T00A', reply_markup=replySize6)
    elif message.text == 'Вегетарианская':
        bot.send_photo(message.chat.id, 'https://imbt.ga/aNJDDaDxCO', reply_markup=replySize7)
    elif message.text == 'Меню':
        bot.send_message(message.chat.id,'Меню',reply_markup=reply2)
    elif message.text == 'Маленькая(16000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 16000 сум', reply_markup=inline2)
    elif message.text == 'Средняя(25000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 25000 сум',
                         reply_markup=inline2)
    elif message.text == 'Большая(34000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 34000 сум',
                         reply_markup=inline2)
    elif message.text == 'Мега(45000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 45000 сум',
                         reply_markup=inline2)
    elif message.text == 'Маленькая(19000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 19000 сум',
                         reply_markup=inline2)
    elif message.text == 'Средняя(23000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 23000 сум',
                         reply_markup=inline2)
    elif message.text == 'Большая(35000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 35000 сум',
                         reply_markup=inline2)
    elif message.text == 'Мега(51000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 51000 сум',
                         reply_markup=inline2)
    elif message.text == 'Маленькая(22000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 22000 сум',
                         reply_markup=inline2)
    elif message.text == 'Средняя(31000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 31000 сум',
                         reply_markup=inline2)
    elif message.text == 'Большая(43000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 43000 сум',
                         reply_markup=inline2)
    elif message.text == 'Мега(58000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 58000 сум',
                         reply_markup=inline2)
    elif message.text == 'Маленькая(25000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 25000 сум',
                         reply_markup=inline2)
    elif message.text == 'Средняя(33000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 33000 сум',
                         reply_markup=inline2)
    elif message.text == 'Большая(41000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 41000 сум',
                         reply_markup=inline2)
    elif message.text == 'Мега(57000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 57000 сум',
                         reply_markup=inline2)
    elif message.text == 'Маленькая(26000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 26000 сум',
                         reply_markup=inline2)
    elif message.text == 'Средняя(35000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 35000 сум',
                         reply_markup=inline2)
    elif message.text == 'Большая(46000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 46000 сум',
                         reply_markup=inline2)
    elif message.text == 'Мега(60000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 60000 сум',
                         reply_markup=inline2)
    elif message.text == 'Маленькая(31000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 31000 сум',
                         reply_markup=inline2)
    elif message.text == 'Средняя(50000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 50000 сум',
                         reply_markup=inline2)
    elif message.text == 'Большая(74000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 74000 сум',
                         reply_markup=inline2)
    elif message.text == 'Мега(112000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 112000 сум',
                         reply_markup=inline2)
    elif message.text == 'Маленькая(15000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 15000 сум',
                         reply_markup=inline2)
    elif message.text == 'Средняя(21000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 21000 сум',
                         reply_markup=inline2)
    elif message.text == 'Большая(35000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 35000 сум',
                         reply_markup=inline2)
    elif message.text == 'Мега(40000)':
        bot.send_message(message.chat.id,'Действительно хотите приобрести пиццу? Стоимость 40000 сум',
                         reply_markup=inline2)
    elif message.text == 'Не хочу эту пиццу':
        bot.send_message(message.chat.id, 'Выберите другую:',reply_markup=replyPizza)
    elif message.text == 'Наполеон':
        bot.send_photo(message.chat.id,'https://imbt.ga/9P9b1UlyWD',reply_markup=inline3)
    elif message.text == 'Медовик':
        bot.send_photo(message.chat.id,'https://imbt.ga/Lx9EcjdyRd',reply_markup=inline4)
    elif message.text == 'Синнабоны':
        bot.send_photo(message.chat.id,'https://imbt.ga/Kx7FTC2Nyj',reply_markup=inline5)
    elif message.text == 'Coca-cola 0.5':
        bot.send_message(message.chat.id,"Заказать?(5000)",reply_markup=inline2)
    elif message.text == 'Coca-cola 1.0':
        bot.send_message(message.chat.id,"Заказать?(8000)",reply_markup=inline2)
    elif message.text == 'Coca-cola 1.5':
        bot.send_message(message.chat.id,"Заказать?(11000)",reply_markup=inline2)
    elif message.text == 'Мохито PizzaOn':
        bot.send_photo(message.chat.id,'https://imbt.ga/RJSTnYguk7',reply_markup=inlineMox)
    else:
        bot.send_message(message.chat.id,"Не говорю на человеческом")
@bot.message_handler(content_types=['location'])
def loc(message):
    print(message.location)
    if message.location:
        bot.send_message(message.chat.id,"Отправьте номер телефона:",reply_markup=replyPhone)
@bot.message_handler(content_types=['contact'])
def cont(message):
    if message.contact:
        bot.send_message(message.chat.id,"Ваш заказ принят! Наш оператор свяжется с вами в ближайшее время, чтобы уточнить детали.",reply_markup=reply1)
        bot.send_contact(message.chat.id, message.contact.phone_number, message.contact.first_name)
        bot.send_message(message.chat.id, ' заказал вегетарианку')












bot.polling()

