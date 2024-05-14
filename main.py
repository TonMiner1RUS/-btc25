import asyncio
import logging 
import sys
import aiosqlite


from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class States(StatesGroup):
    id = State()
    balance = State()
    wallet = State()
    invited = State()
    invite_id = State()
   




class DataBase:
    def __init__(self, name: str, table: str) -> None:
        self.name = name
        self.table =...



    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            
            query = """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            balance INTEGER(2),
            wallet 
            invited INTEGER(1),
            invite_id 
            )
            """
            await cursor.executescript(query)
            await db.commit()

        async def insert(self, **kwargs) -> None:
            async with aiosqlite.connect(self.name) as db:
                cursor = await db.cursor()
                await cursor.execute(
                    """
                    INSERT INTO users(
                    id,
                    balance,
                    wallet,
                    invited,
                    invite_id
                    )VALUES (?, ?, ?, ?, ?)
                    
                    """,
                    tuple(kwargs.values())
                )
                await db.commit()

TOKEN = '7140820903:AAG4iCDYNXWoe3-1I0pEqONrDL3vMQgaOAQ'

router = Router()


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="let's click", web_app=WebAppInfo(
        url="https://foxiinc.github.io/"
    )
                   )
    return builder.as_markup()


@router.message(CommandStart(deep_link=True))
async def handler(message: Message, state: FSMContext, command: CommandObject):
    
    args = command.args
    reference = decode_payload(args)
    print(reference)
    
    await state.update_data(invited_id=reference)
    
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    link = await create_start_link(bot,str(message.from_user.id), encode=True)
    
    await message.answer(f'Play game!!!\nYou referral link: {link}',
                        reply_markup=webapp_builder())
    
    await state.update_data(id=message.from_user.id)
    
    



@router.message(Command("Ref"))
async def referral(message: Message):
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    link = await create_start_link(bot,str(message.from_user.id), encode=True)

    await message.answer(f"You referral link: {link}")






    
async def main():
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    db = DataBase("users_db.db", "users")

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, db=db)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))