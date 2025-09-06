from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8234701116:AAHd9KqH2__HZltfht0RM-98-aF978YRHhI"  # bu joyga o'z tokeningizni yozing

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# --- Ma'lumotlar ---
students = [
    "Abduvohidova G",
    "Abdujalilov Y",
    "Absoatov F",
    "Bozorova B",
    "Eshmurodov S",
    "Jumayeva D",
    "Ko‘chkinov A",
    "Mamayusupuv R",
    "Mamanazarov O",
    "Mengaliyev B",
    "Turdimurodova M",
    "Toshpo‘latov A",
    "Xolmirzayeva F",
    "Xolmirzayev S",
    "Xudoyberdiyeva N",
    "Xushvaqtov J",
    "O‘razov M",
    "Choriyev R",
    "Mengliboyeva D",
    "Qahhorov M",
    "To‘xtayeva H",
]

addresses = [
    "Surxondaryo, Jarqurgon, Xalqobod MFY Novroʻz N124",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N91",
    "Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N29",
    "Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N57",
    "Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N22",
    "Surxondaryo, Qumqorgon, Bobotogʻ MFY Polvonlar N28",
    "Surxondaryo, Jarqurgon, Xalqobod MFY -",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N74",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N139",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Olmos -",
    "Surxondaryo, Jarqurgon, Xalqobod Xalqparvar -",
    "Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri N27",
    "Surxondaryo, Jarqurgon, Xalqobod MFY IslomNuri -",
    "- - -",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N107",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N70",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N58",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N85",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Doʻstlik N112",
    "Surxondaryo, Jarqurgon, Xalqobod MFY Olmos N55",
    "Surxondaryo, Qumqorgon, Bobotogʻ MFY Polvonlar N8",
]

# --- Start komandasi ---
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("📋 O‘quvchilar F.I.")
    keyboard.add("👨‍👩‍👧 Ota-onalar F.I.")
    keyboard.add("📞 Ota-onalar telefon raqami")
    keyboard.add("🏠 Uy manzillari")
    keyboard.add("📊 Jami o‘quvchilar soni")
    keyboard.add("👩‍🏫 Sinf rahbari")
    keyboard.add("🏫 Maktab direktori")
    await message.answer("Assalomu alaykum!\nQuyidagi menyudan birini tanlang 👇", reply_markup=keyboard)

# --- O‘quvchilar F.I. ---
@dp.message_handler(lambda msg: msg.text == "📋 O‘quvchilar F.I.")
async def students_list(message: types.Message):
    text = "\n".join([f"{i+1}. {name}" for i, name in enumerate(students)])
    await message.answer(text)

# --- Ota-onalar F.I. ---
@dp.message_handler(lambda msg: msg.text == "👨‍👩‍👧 Ota-onalar F.I.")
async def parents_names(message: types.Message):
    await message.answer("Biz hali maʼlumot yoʻq.\nBu maʼlumotni olishga ruxsat yoʻq.")

# --- Ota-onalar telefonlari ---
@dp.message_handler(lambda msg: msg.text == "📞 Ota-onalar telefon raqami")
async def parents_phones(message: types.Message):
    await message.answer("Bizda hali maʼlumot yoʻq.")

# --- Uy manzillari ---
@dp.message_handler(lambda msg: msg.text == "🏠 Uy manzillari")
async def addresses_list(message: types.Message):
    text = "\n".join([f"{i+1}. {addr}" for i, addr in enumerate(addresses)])
    await message.answer(text)

# --- Jami soni ---
@dp.message_handler(lambda msg: msg.text == "📊 Jami o‘quvchilar soni")
async def total_students(message: types.Message):
    await message.answer(f"Hozircha {len(students)} nafar")

# --- Sinf rahbari ---
@dp.message_handler(lambda msg: msg.text == "👩‍🏫 Sinf rahbari")
async def class_teacher(message: types.Message):
    await message.answer("Sinf rahbari: Xujanazarov Salim\nTelefon: +998995550267")

# --- Maktab direktori ---
@dp.message_handler(lambda msg: msg.text == "🏫 Maktab direktori")
async def school_director(message: types.Message):
    await message.answer("Maktab direktori: Alixanov Abduxoliq\nTelefon: (menda hali bu maʼlumot yoʻq)")
