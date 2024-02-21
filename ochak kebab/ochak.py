from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from logging import basicConfig, INFO
import sqlite3
from config import token
from datetime import datetime

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
basicConfig(level=INFO)

class OrderFoodState(StatesGroup):
    name = State()
    title = State()
    phone_number = State()
    address = State()
    
connect = sqlite3.connect('ojak_kebab_bot.db')
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        title TEXT,
        phone_number VARCHAR(100),
        address VARCHAR(100)
    );
''')
connect.commit()




start_keyboard = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('меню'),
    types.KeyboardButton('Заказать еду')
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboard)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Приветствую вас в очак кебаб {message.from_user.full_name}", reply_markup=start_button)

@dp.message_handler(text='О нас')
async def start(message:types.Message):
    await message.answer("вся информация о нас находится на нашем сайте")
    await message.answer('https://ocak.uds.app/c/about')
    
@dp.message_handler(text='Адрес')
async def start(message:types.Message):
    await message.answer("234، 246 Курманжан-Датка ул., Ош")
    await message.answer_location(40.52665878674943, 72.79530016626835)
    
    
@dp.message_handler(text='меню')
async def start(message:types.Message):
    await message.answer("раздел шашлвыков ")
    await message.answer("https://nambafood.kg/ojak-kebap") 
    
@dp.message_handler(text='Заказать еду')
async def start(message:types.Message):
    await message.answer('введите своё имя')
    await OrderFoodState.name.set()
    
@dp.message_handler(state=OrderFoodState.name)
async def ordes_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer('Что хотите заказать ')
    await OrderFoodState.next()

@dp.message_handler(state=OrderFoodState.title)
async def ordes_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await message.answer('  ведите номер телефона  ')
    await OrderFoodState.next()
    
@dp.message_handler(state=OrderFoodState.phone_number)
async def process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await message.answer("Введите свой адрес")
    await OrderFoodState.next()

    
@dp.message_handler(state=OrderFoodState.address)
async def ordes_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
        
    async with state.proxy() as data:
        name=data['name']
        title=data['title']
        phone=data['phone_number']
        address=data['address']

    cursor.execute('''
        INSERT INTO orders (name, title, phone_number, address )
        VALUES (?, ?, ?, ?)
    ''', (name, title, phone, address))
    connect.commit()

    await message.answer(" ваш заказ принять")
    await state.finish()
        
executor.start_polling(dp)



