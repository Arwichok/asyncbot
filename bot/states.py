from aiogram.dispatcher.filters.state import (
    State, StatesGroup)


class ExampleState(StatesGroup):
    name = State()
    age = State()
    gender = State()