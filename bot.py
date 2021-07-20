import logging, schedule, time
from datetime import datetime


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1194976667:AAGrxoVyWVWjvVJL4EA2bvjxdglaVwTmytM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

users = []

@dp.message_handler(commands=['start', 'help'])
async def bemVindo(message: types.Message):
    
    await message.reply("Olá, seja bem vindo ao BOT do Guardiões da saúde!")

@dp.message_handler(commands='entrar')
async def cadastroLembrete(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    texto = (
        ('SIM!', 'sim'),
        ('NÃO!', 'nao'),
    )

    rbotao = (types.InlineKeyboardButton(tex, callback_data=dat)
              for tex, dat in texto)

    keyboard_markup.row(*rbotao)

    await message.reply("Deseja ser lembrado pelo BOT?", reply_markup=keyboard_markup)

@dp.callback_query_handler(text='sim')
@dp.callback_query_handler(text='nao')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'sim':
        users.append(query.from_user.id)

    print (users)

    await bot.send_message(query.from_user.id, "Bacana =)\n Irei te lembrar sempre!!")


@dp.message_handler(commands='sair')
async def removerLembrete(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    texto = (
        ('SIM!', 'desejo'),
        ('NÃO!', 'nao desejo'),
    )

    rbotao = (types.InlineKeyboardButton(tex, callback_data=dat)
              for tex, dat in texto)

    keyboard_markup.row(*rbotao)

    await message.reply("Deseja sair da lista de lembrete?", reply_markup=keyboard_markup)

@dp.callback_query_handler(text='desejo')
@dp.callback_query_handler(text='nao desejo')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'desejo':
        val_remove = query.from_user.id
        users.remove(val_remove)

    print (users)

    await bot.send_message(query.from_user.id, "Certo... Obrigado por me usar =)!")

def mandarMensagem():
    print("MENSAGEM")

schedule.every().day.at("23:52").do(mandarMensagem)

while 1:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)