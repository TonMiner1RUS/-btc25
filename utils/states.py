from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    id = State()
    user_id = State()
    balance = State()
    wallet = State()
    invited = State()
    inviter_id = State()