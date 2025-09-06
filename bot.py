import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Tokenni ENV dan olish (Render uchun to‘g‘ri)
import os
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# O‘quvchilar ro‘yxati
students = [
    "1. Abduvohidova G",
    "2. Abdujalilov Y",
    "3. Absoatov F",
    "4. Bozorova B",
    "5. Eshmurodov S",
    "6. Jumayeva D",
    "7. Koʻchkinov A",
    "8. Mamayusupuv R",
    "9. Mamanazarov O",
    "10. Mengaliyev B",
    "11. Mengliboyeva D",
    "12. Qahhorov M",
    "13. Toʻxtayeva H",
    "14. Turdimurodova M",
    "15. Toshpoʻlatov A",
    "16. Xolmirzayeva F",
    "17. Xolmirzayev S",
    "18. Xudoyberdiyeva N",
    "19. Xushvaqtov J",
    "20. Oʻrazov M",
    "21. Choriyev R"
]

# Uy manzillari
addresses = [
    "1. Abduvohida G: Surxondaryo, Jarqurgon, Xalqobod MFY Novroʻz N124",
    "2. Abdujalilov Y: Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N91",
    "3. Absoatov F: Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N29",
    "4. Bozorova B: Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N57",
    "5. Eshmurodov S: Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N22",
    "6. Jumayeva D: Surxondaryo, Qumqorgon, Bobotogʻ MFY Polvonlar N28",
    "7. Koʻchkinov A: Surxondaryo, Jarqurgon, Xalqobod MFY -",
    "8. Mamayusupuv R: Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N74",
    "9. Mamanazarov O: Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N139",
    "10. Mengaliyev B: Surxondaryo, Jarqurgon, Xalqobod MFY Olmos -",
    "11. Mengliboyeva D: Surxondaryo, Jarqurgon, Xalqobod Xalqparvar -",
    "12. Qahhorov M: Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N27",
    "13. Toʻxtayeva H: Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri -",
    "14. Turdimurodova M: - - -",
    "15. Toshpoʻlatov A: Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N107",
    "16. Xolmirzayeva F: Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N70",
    "17. Xolmirzayev S: Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N58",
    "18. Xudoyberdiyeva N: Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N85",
    "19. Xushvaqtov J: Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N112",
    "20. Oʻrazov M: Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N55",
    "21. Choriyev R: Surxondaryo, Qumqurgon, Bobotogʻ MFY Polvonlar N8",
]

# 🔘 Klaviatura menyu
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Jami o‘quvchilar soni")],
        [KeyboardButton(text="O‘quvchilar F.I")],
        [KeyboardButton(text="Ota-onalar F.I")],
        [KeyboardButton(text="Ota-onalar telefon raqami")],
        [KeyboardButton(text="Uy manzillari")],
        [KeyboardButton(text="Sinf rahbari")],
        [KeyboardButton(text="Maktab direktori")]
    ],
    resize_keyboard=True
)

# /start komandasi
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Menyudan tanlang 👇", reply_markup=menu)

# Menyu tugmalariga javoblar
@dp.message()
async def handle_menu(message: types.Message):
    if message.text == "Jami o‘quvchilar soni":
        await message.answer("Jami 21 nafar o‘quvchi mavjud.")
    elif message.text == "O‘quvchilar F.I":
        await message.answer("\n".join(students))
    elif message.text == "Ota-onalar F.I":
        await message.answer("Bizda hali ota-onalar ma’lumotlari yo‘q.")
    elif message.text == "Ota-onalar telefon raqami":
        await message.answer("Bizda hali ota-onalar telefon raqamlari yo‘q.")
    elif message.text == "Uy manzillari":
        await message.answer("\n".join(addresses))
    elif message.text == "Sinf rahbari":
        await message.answer("Xujanazarov Salim\nTel: +998995550267")
    elif message.text == "Maktab direktori":
        await message.answer("Alixanov Abduxoliq\nTel: Bizda bu ma’lumot yo‘q")
    else:
        await message.answer("Menyudan foydalaning 👆")

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
