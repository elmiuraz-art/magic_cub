import streamlit as st
from random import choice

# --------- ДАННЫЕ ИГРЫ ---------
ANSWERS = [
    'Бесспорно','Предрешено','Никаких сомнений','Определённо да',
    'Можешь быть уверен в этом','Мне кажется - да','Вероятнее всего',
    'Хорошие перспективы','Знаки говорят - да','Да','Пока неясно', 'попробуй снова',
    'Спроси позже','Лучше не рассказывать','Сейчас нельзя предсказать',
    'Сконцентрируйся и спроси опять','Даже не думай','Мой ответ - нет',
    'По моим данным - нет','Перспективы не очень хорошие','Весьма сомнительно'
]

st.set_page_config(page_title="Магический шар", page_icon="🔮")

# --------- СОСТОЯНИЕ ---------
if "name" not in st.session_state:
    st.session_state.name = ""
if "last_answer" not in st.session_state:
    st.session_state.last_answer = None
if "playing" not in st.session_state:
    st.session_state.playing = True  # идёт сессия вопросов

st.title("🔮 Магический шар")

# Ввод имени
if not st.session_state.name:
    st.write("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
    st.write("Как тебя зовут?")
    name = st.text_input("Введи имя", key="name_input")
    if st.button("Продолжить"):
        st.session_state.name = name.strip() or "Друг"
        st.rerun()

# Основной экран
if st.session_state.name:
    st.write(f"Привет, **{st.session_state.name}**!")

    if st.session_state.playing:
        st.write("Задай свой вопрос, а я предскажу тебе твоё будущее!")
        question = st.text_input("Твой вопрос", key="q_input")

        col1, col2 = st.columns([1,1])
        with col1:
            ask = st.button("Спросить")
        with col2:
            reset = st.button("Начать заново")

        if reset:
            st.session_state.name = ""
            st.session_state.last_answer = None
            st.session_state.playing = True
            st.rerun()

        if ask and question.strip():
            st.session_state.last_answer = choice(ANSWERS)

        if st.session_state.last_answer:
            st.success(st.session_state.last_answer)

            st.markdown("**Ещё есть вопросы?**")
            c1, c2 = st.columns(2)
            with c1:
                more = st.button("Да")
            with c2:
                stop = st.button("Нет")

            if more:
                # просто очистить поле вопроса и последнюю реплику
                st.session_state.last_answer = None
                st.session_state.q_input = ""  # очистим input
                st.rerun()

            if stop:
                st.session_state.playing = False
                st.rerun()

    else:
        st.info("Спасибо за игру! Можешь начать заново в любой момент.")
        if st.button("Сыграть ещё раз"):
            st.session_state.last_answer = None
            st.session_state.playing = True
            st.rerun()
