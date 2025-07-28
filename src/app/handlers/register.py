'''import re
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.models.data import courses_by_age
from app.core.env_config import settings
from app.keyboards.reply import main_menu

router = Router()


class RegisterForm(StatesGroup):
    name = State()
    age = State()
    course = State()
    contact = State()


@router.message(F.text == "/register")
@router.message(F.text == "✍️ Записаться")
async def start_register(message: Message, state: FSMContext):
    await message.answer("Как тебя зовут?")
    await state.set_state(RegisterForm.name)


@router.message(RegisterForm.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text.strip()

    if not name.replace(" ", "").isalpha() or len(name) < 2:
        await message.answer("❌ Имя должно содержать только буквы и быть не короче 2 символов.")
        return

    await state.update_data(name=name)
    await message.answer("Сколько тебе лет?")
    await state.set_state(RegisterForm.age)


@router.message(RegisterForm.age)
async def get_age(message: Message, state: FSMContext):
    try:
        age = int(message.text.strip())
        if not 3 <= age <= 100:
            raise ValueError()
    except ValueError:
        await message.answer("❌ Пожалуйста, введи возраст числом от 3 до 100.")
        return

    await state.update_data(age=age)

    suitable_courses = []
    for age_group, courses in courses_by_age.items():
        if "–" in age_group:
            start, end = map(int, age_group.replace(" лет", "").split("–"))
            if start <= age <= end:
                suitable_courses.extend(courses)
        elif "+" in age_group:
            min_age = int(age_group.replace("+ лет", "").strip())
            if age >= min_age:
                suitable_courses.extend(courses)
    if not suitable_courses:
        await message.answer(
            "😔 К сожалению, курсов для этого возраста нет. Попробуй ввести другой возраст (от 3 до 100):"
            )
        await state.set_state(RegisterForm.age) 
        return


    # Сохраняем коды для callback
    courses_map = {f"select_course_{i}": c for i, c in enumerate(suitable_courses)}
    await state.update_data(courses_map=courses_map)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=course, callback_data=code)]
            for code, course in courses_map.items()
        ]
    )

    await message.answer("Выбери курс, который тебе интересен:", reply_markup=keyboard)
    await state.set_state(RegisterForm.course)


@router.callback_query(F.data.startswith("select_course_"))
async def course_selected(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    course_code = callback.data
    courses_map = data.get("courses_map", {})

    course = courses_map.get(course_code)
    if not course:
        await callback.message.answer("❌ Ошибка: курс не найден. Попробуй начать регистрацию заново.")
        await state.clear()
        return

    await state.update_data(course=course)

    await callback.message.edit_reply_markup()

    await callback.message.answer(f"✅ Вы выбрали курс: <b>{course}</b>", parse_mode="HTML")

    
    await callback.message.answer("Укажи свой телефон или email для связи:")
    await state.set_state(RegisterForm.contact)



@router.message(RegisterForm.contact)
async def get_contact(message: Message, state: FSMContext):
    contact = message.text.strip()

    is_email = re.match(r"[^@]+@[^@]+\.[^@]+", contact)
    is_phone = re.match(r"^\+?\d{10,15}$", contact)

    if not (is_email or is_phone):
        await message.answer("❌ Введи корректный email или номер телефона (например, +491234567890).")
        return

    await state.update_data(contact=contact)
    data = await state.get_data()

    await message.answer(
        f"✅ Спасибо, {data['name']}!\n"
        f"Ты записан(а) на курс: <b>{data['course']}</b>.\n"
        f"📞 Мы свяжемся с тобой по: {data['contact']}",
        parse_mode="HTML",
        reply_markup=main_menu
    )

    admin_msg = (
        f" <b>Новая заявка</b>\n\n"
        f"👤 Имя: {data['name']}\n"
        f"🔢 Возраст: {data['age']}\n"
        f"📚 Курс: {data['course']}\n"
        f"📞 Контакт: {data['contact']}"
    )
    await message.bot.send_message(settings.ADMIN_ID, admin_msg, parse_mode="HTML")

    await state.clear()'''
import re
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.models.data import courses_by_age
from app.core.env_config import settings
from app.keyboards.reply import main_menu

router = Router()

class RegisterForm(StatesGroup):
    name = State()
    age = State()
    course = State()
    contact = State()

@router.message(F.text == "/register")
@router.message(F.text == "✍️ Записаться")
async def start_register(message: Message, state: FSMContext):
    await message.answer("Как тебя зовут?")
    await state.set_state(RegisterForm.name)

@router.message(RegisterForm.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text.strip()
    if not name.replace(" ", "").isalpha() or len(name) < 2:
        await message.answer("❌ Имя должно содержать только буквы и быть не короче 2 символов.")
        return
    await state.update_data(name=name)
    await message.answer("Сколько тебе лет?")
    await state.set_state(RegisterForm.age)

@router.message(RegisterForm.age)
async def get_age(message: Message, state: FSMContext):
    try:
        age = int(message.text.strip())
        if not 3 <= age <= 100:
            raise ValueError()
    except ValueError:
        await message.answer("❌ Введи возраст числом от 3 до 100.")
        return

    suitable_courses = []
    for age_group, courses in courses_by_age.items():
        if "–" in age_group:
            start, end = map(int, age_group.replace(" лет", "").split("–"))
            if start <= age <= end:
                suitable_courses.extend(courses)
        elif "+" in age_group:
            min_age = int(age_group.replace("+ лет", "").strip())
            if age >= min_age:
                suitable_courses.extend(courses)

    if not suitable_courses:
        await message.answer(
            "😔 К сожалению, курсов для этого возраста нет. Попробуй ввести другой возраст (от 3 до 100):"
        )
        await state.set_state(RegisterForm.age)
        return

    await state.update_data(age=age)

    courses_map = {f"select_course_{i}": c for i, c in enumerate(suitable_courses)}
    await state.update_data(courses_map=courses_map)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=course, callback_data=code)]
            for code, course in courses_map.items()
        ]
    )

    await message.answer("Выбери курс, который тебе интересен:", reply_markup=keyboard)
    await state.set_state(RegisterForm.course)

@router.callback_query(F.data.startswith("select_course_"))
async def course_selected(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    course_code = callback.data
    courses_map = data.get("courses_map", {})

    course = courses_map.get(course_code)
    if not course:
        await callback.message.answer("❌ Курс не найден. Начни регистрацию заново.")
        await state.clear()
        return

    await state.update_data(course=course)
    await callback.message.edit_reply_markup()
    await callback.message.answer(f"✅ Вы выбрали курс: <b>{course}</b>", parse_mode="HTML")
    await callback.message.answer("Укажи свой телефон или email для связи:")
    await state.set_state(RegisterForm.contact)



@router.message(RegisterForm.contact)
async def get_contact(message: types.Message, state: FSMContext):
    contact = message.text.strip()

    # Проверка: email должен быть tata@gmail.com или tata@mail.ru
    is_email = re.fullmatch(r"[a-zA-Z0-9._%+-]+@(gmail\.com|mail\.ru)", contact)
    
    # Проверка: телефон только +7 и 10 цифр
    is_phone = re.fullmatch(r"\+7\d{10}", contact)

    if not (is_email or is_phone):
        await message.answer(
            "❌ Введи корректный email (например, tata@gmail.com или tata@mail.ru) "
            "или номер телефона в формате +7XXXXXXXXXX."
        )
        return

    await state.update_data(contact=contact)
    data = await state.get_data()

    await message.answer(
        f"✅ Спасибо, {data['name']}!\n"
        f"Ты записан(а) на курс: <b>{data['course']}</b>.\n"
        f"📞 Мы свяжемся с тобой по: {data['contact']}",
        parse_mode="HTML",
        reply_markup=main_menu
    )

    # Отправка админу
    admin_msg = (
        f"<b>Новая заявка</b>\n\n"
        f"👤 Имя: {data['name']}\n"
        f"🔢 Возраст: {data['age']}\n"
        f"📚 Курс: {data['course']}\n"
        f"📞 Контакт: {data['contact']}"
    )
    await message.bot.send_message(settings.ADMIN_ID, admin_msg, parse_mode="HTML")

    await state.clear()


'''
@router.message(RegisterForm.contact)
async def get_contact(message: Message, state: FSMContext):
    contact = message.text.strip()
    is_email = re.match(r"[^@]+@[^@]+\.[^@]+", contact)
    is_phone = re.match(r"^\\+?\\d{10,15}$", contact)

    if not (is_email or is_phone):
        await message.answer("❌ Введи корректный email или номер телефона (например, +79999999999).")
        return

    await state.update_data(contact=contact)
    data = await state.get_data()

    await message.answer(
        f"✅ Спасибо, {data['name']}!\\n"
        f"Ты записан(а) на курс: <b>{data['course']}</b>.\\n"
        f"📞 Мы свяжемся с тобой по: {data['contact']}",
        parse_mode="HTML",
        reply_markup=main_menu
    )

    admin_msg = (
        f"<b>Новая заявка</b>\\n\\n"
        f"👤 Имя: {data['name']}\\n"
        f"🔢 Возраст: {data['age']}\\n"
        f"📚 Курс: {data['course']}\\n"
        f"📞 Контакт: {data['contact']}"
    )
    await message.bot.send_message(settings.ADMIN_ID, admin_msg, parse_mode="HTML")
    await state.clear()
'''  

