import asyncio

from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, fsmAdminFile, notifications, inline
from Database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()

inline.register_handlers_inline(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminFile.register_handlers_fsm_anketa(dp)
notifications.register_handlers_notification(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)