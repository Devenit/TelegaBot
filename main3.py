import asyncio
import logging
import json
import requests

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5965185798:AAFnH0qBYM1OrmDhaKJLCJVlstytBWhVJn4"

router = Router()
# reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать')]], resize_keyboard=True)
start_text = '''Привет, {full_name}. Я бот, который может искать товары по категориям в WildBerries!
Используйте команды на клавиатуре для дальнейшей работы!'''
help_text = '''Нажмите на Категория, чтобы узнать, в каких категориях вы можете посмотреть товары.
Затем выберите ту категорию, которая вам нужна.'''
planshets = '''{index}: Модель: {model}, цена: {sell}, цена со скидкой: {sell2}.
Ссылка на товар: https://www.wildberries.ru/catalog/0/search.aspx?search={url}'''
categories = '''Существующие категории: планшеты, смартфоны, ноутбуки.'''


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"{start_text.format(full_name=message.from_user.full_name)}",
                         reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Помощь')], [KeyboardButton(text='Категории')]], resize_keyboard=True))


@router.message(Text('Помощь'))
async def help_handler(message: Message) -> None:
    await message.answer(f'{help_text}', reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Категории')]], resize_keyboard=True))


@router.message(Text('Категории'))
async def categories_handler(message: Message) -> None:
    await message.answer_photo('https://nn.wadoo.ru/upload/iblock/74b/74bb0f62f3efffbc3135d8178490c533.jpg', caption='Планшеты')
    await message.answer_photo('https://a.allegroimg.com/original/112d56/ff8ef69e4f908b70046f1f79455b/Smartfon-LG-V40-ThinQ-6-4-6-128GB-NFC-SNAP-845-Marka-telefonu-LG', caption='Смартфоны')
    await message.answer_photo('https://i5.walmartimages.com/asr/f66ea803-bece-4b07-967b-52c6f06b3ecb.4bc3bce99350e8322483d49fb7d454bf.jpeg',
                               caption='Ноутбуки',
                               reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Планшеты')], [KeyboardButton(text='Смартфоны')], [KeyboardButton(text='Ноутбуки')]], resize_keyboard=True))


@router.message()
async def echo_handler(message: Message) -> None:
    with open('res.json', 'r') as file:
        data = json.load(file)
    with open('res2.json', 'r') as file:
        data2 = json.load(file)
    with open('res3.json', 'r') as file:
        data3 = json.load(file)
    print(data)
    print(data2)
    print(data3)
    if 'планшеты' in message.text.lower():
        for i in data:
            await message.answer(f'{planshets.format(index=i, model=data[i][0], sell=data[i][1], sell2=data[i][2], url=data[i][3])}')
    elif 'смартфоны' in message.text.lower():
        for i in data2:
            await message.answer(f'{planshets.format(index=i, model=data2[i][0], sell=data2[i][1], sell2=data2[i][2], url=data2[i][3])}')

    elif 'ноутбуки' in message.text.lower():
        for i in data3:
            await message.answer(f'{planshets.format(index=i, model=data3[i][0], sell=data3[i][1], sell2=data3[i][2], url=data3[i][3])}')
    else:
        await message.answer('Я вас не понимаю. Используйте доступные вам команды на клавиатуре!',
                             reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Помощь')], [KeyboardButton(text='Категории')]], resize_keyboard=True))


def get_data():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=popular&page=1&discount=50',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.2.806 Yowser/2.5 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        'https://catalog.wb.ru/catalog/electronic22/catalog?appType=1&curr=rub&dest=-1257786&discount=50&page=1&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&sort=popular&spp=0&subject=515',
        headers=headers,
    ).json()
    headers1 = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/promotions/vesennyaya-rasprodazha-huawei?sort=sale&page=1&xsubject=517',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.895 Yowser/2.5 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response1 = requests.get(
        'https://search.wb.ru/promo/bucket_28/catalog?appType=1&curr=rub&dest=-1257786&page=1&preset=158657&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&sort=sale&spp=0&xsubject=517',
        headers=headers1,
    ).json()

    headers3 = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki?sort=popular&page=1&discount=30',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.2.806 Yowser/2.5 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response3 = requests.get(
        'https://catalog.wb.ru/catalog/electronic15/catalog?appType=1&curr=rub&dest=-1257786&discount=30&page=1&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&sort=popular&spp=0&subject=2290',
        headers=headers3,
    ).json()

    product_id = response1.get('data').get('products')
    product_id2 = response.get('data').get('products')
    product_id3 = response3.get('data').get('products')

    with open('product.json', 'w') as file:
        json.dump(product_id, file, indent=4, ensure_ascii=False)
    s = {}
    for i in product_id:
        s[i['name']] = i['brand'], str(i['priceU'])[:5], str(i['salePriceU'])[:5], i['id']
    with open('res.json', 'w') as file:
        json.dump(s, file, indent=4, ensure_ascii=False)
    with open('product2.json', 'w') as file:
        json.dump(product_id2, file, indent=4, ensure_ascii=False)
    s = {}
    for i in product_id2:
        s[i['name']] = i['brand'], str(i['priceU'])[:5], str(i['salePriceU'])[:5], i['id']
    with open('res2.json', 'w') as file:
        json.dump(s, file, indent=4, ensure_ascii=False)
    with open('product3.json', 'w') as file:
        json.dump(product_id3, file, indent=4, ensure_ascii=False)
    s = {}
    for i in product_id3:
        s[i['name']] = i['brand'], str(i['priceU'])[:5], str(i['salePriceU'])[:5], i['id']
    with open('res3.json', 'w') as file:
        json.dump(s, file, indent=4, ensure_ascii=False)


async def main() -> None:
    get_data()
    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())