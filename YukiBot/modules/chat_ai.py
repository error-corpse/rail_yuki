import html
import json
import re
from time import sleep
import requests
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
    User,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html

import YukiBot.modules.sql.chatbot_sql as sql
from YukiBot import BOT_ID, BOT_NAME, BOT_USERNAME, dispatcher
from YukiBot.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from YukiBot.modules.log_channel import gloggable


@user_admin_no_reply
@gloggable
def yukidisable(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"rm_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_yuki = sql.set_yuki(chat.id)
        if is_yuki:
            is_yuki = sql.set_yuki(user_id)
            return (
                f"⌥ <b>{html.escape(chat.title)} </b>\n"
                f"⌥ ᴀɪ ᴅɪꜱᴀʙʟᴇᴅ\n"
                f"⌥ <b>ᴀᴅᴍɪɴ ➥</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "⌥ {} ᴄʜᴀᴛʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʙʏ {}.".format(
                    dispatcher.bot.first_name, mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@gloggable
def yukiable(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"add_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_yuki = sql.rem_yuki(chat.id)
        if is_yuki:
            is_yuki = sql.rem_yuki(user_id)
            return (
                f"⌥ <b>{html.escape(chat.title)} </b>\n"
                f"⌥ ᴀɪ ᴇɴᴀʙʟᴇ\n"
                f"⌥ <b>ᴀᴅᴍɪɴ ➥</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "⌥ {} ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʙʏ {}.".format(
                    dispatcher.bot.first_name, mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@gloggable
def yuki(update: Update, context: CallbackContext):
    message = update.effective_message
    msg = "⌥ ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="add_chat({})"),
                InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="rm_chat({})"),
            ],
        ]
    )
    message.reply_text(
        text=msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


def yuki_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if message.text.lower() == "yuki":
        return True
    elif BOT_USERNAME in message.text.upper():
        return True
    elif reply_message:
        if reply_message.from_user.id == BOT_ID:
            return True
    else:
        return False

def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    bot = context.bot
    is_yuki = sql.is_yuki(chat_id)
    
    if is_yuki:
        return

    if message.text and not message.document:
        if not yuki_message(context, message):
            return
        
        bot.send_chat_action(chat_id, action="typing")
        api_url = f"http://api.brainshop.ai/get?bid=183083&key=1gjodyDGiFSasdcd&uid={user_id}&msg={message.text}"
        response = requests.get(api_url).json()["cnt"]

        message.reply_text(response)






CHATBOTK_HANDLER = CommandHandler("chatbot", yuki, run_async=True)
ADD_CHAT_HANDLER = CallbackQueryHandler(yukiable, pattern=r"add_chat", run_async=True)
RM_CHAT_HANDLER = CallbackQueryHandler(yukidisable, pattern=r"rm_chat", run_async=True)
CHATBOT_HANDLER = MessageHandler(
    Filters.text
    & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!") & ~Filters.regex(r"^\/")),
    chatbot,
    run_async=True,
)

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(CHATBOTK_HANDLER)
dispatcher.add_handler(RM_CHAT_HANDLER)
dispatcher.add_handler(CHATBOT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
    CHATBOT_HANDLER,
]

__mod_name__ = "ᴄʜᴀᴛ-ʙᴏᴛX"

__help__ = """

 `/chatbot enable` ➥ ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ
"""
          
