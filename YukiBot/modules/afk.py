import time, re
from YukiBot import BOT_USERNAME
from pyrogram.enums import MessageEntityType
from pyrogram import filters
from pyrogram.types import Message
from YukiBot import pbot as app
from YukiBot.Love.readable_time import get_readable_time
from YukiBot.Love.afkdb import add_afk, is_afk, remove_afk
import random 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


POLICE = [

"https://graph.org/file/888a5eaa8bd56e55f28b5.jpg",
"https://graph.org/file/151513db11c93ad5d6aea.jpg",
"https://graph.org/file/786911fbf610009c6e653.jpg",
"https://graph.org/file/93c90aa555f4e9832d563.jpg",
"https://graph.org/file/72397e18d8cbaa590d46d.jpg",
"https://graph.org/file/6cf0959b7676df2364af9.jpg",
"https://graph.org/file/302425f91cd14414b1881.jpg",
"https://graph.org/file/7890aed2cc5a11ef72a12.jpg",
"https://graph.org/file/be7da38e21a7a2b58baa4.jpg",
"https://graph.org/file/6364032206d2c0e7d7641.jpg",
"https://graph.org/file/89cfb8832979558aaa6a6.jpg",
"https://graph.org/file/3aacb2dfa9b9f3bee6ac7.jpg",
"https://graph.org/file/a4d2ef2a8092d4b2cbf57.jpg",
"https://graph.org/file/fe6bf2d7630b51536e39d.jpg",
"https://graph.org/file/971603e9649a99156c2f1.jpg",
"https://graph.org/file/07d24c06d7845b6a392e6.jpg",
"https://graph.org/file/b094bdafdffb7c3bf37da.jpg",
"https://graph.org/file/fa61cc86d951ff00ac943.jpg",
"https://graph.org/file/36fd12d412c59e8cdc870.jpg",
"https://graph.org/file/ee055b3d553837ca1dada.jpg",
"https://graph.org/file/79145769deff07b16584e.jpg",
"https://graph.org/file/2f93f167a73b41df0f634.jpg",
"https://graph.org/file/aa66878529061abb7aab7.jpg",
"https://graph.org/file/f9ee6b486c29e775c2849.jpg",
"https://graph.org/file/99e30c1462483d6946f24.jpg",
"https://graph.org/file/596d850cd780b53c27c74.jpg",
"https://graph.org/file/99edd1b66446e377daff8.jpg",
"https://graph.org/file/4fd1e9d619d449d600b2e.jpg",
"https://graph.org/file/f5f0712bc6e81c1ea99a0.jpg",
"https://graph.org/file/7871bc1236fbf5f936eed.jpg",
"https://graph.org/file/21e3d95a3525b85ecf2be.jpg",
"https://graph.org/file/b07e1016b296921e01979.jpg",
"https://graph.org/file/6f2493edb567825c74c49.jpg",
"https://graph.org/file/034f7d7e051ba29d11f22.jpg",
"https://graph.org/file/21829b55ee68f3dd10f66.jpg",
"https://graph.org/file/a5c3687bc1db9fd06ac41.jpg",
"https://graph.org/file/52db654696dce3d44b545.jpg",
"https://graph.org/file/9ad20cba8c0671663d15d.jpg",
"https://graph.org/file/c79f54af4ee4323ee9aa7.jpg",
"https://graph.org/file/f66af4fb194f6ada367c8.jpg",
"https://graph.org/file/39d70e6bebcb7a95b7e8e.jpg",
"https://graph.org/file/59ca7d31870a60c61fdbf.jpg",
"https://graph.org/file/9ee36c6b1aa28c0f54f9c.jpg",
"https://graph.org/file/ea3a68fff57b8d02f617a.jpg",
"https://graph.org/file/3e3211d88394ad47694d4.jpg",
"https://graph.org/file/68c13d09ee5cca9b5479d.jpg",
"https://graph.org/file/cfc2f89f4e13cac3aff97.jpg",
"https://graph.org/file/8e08202f3299af62ee479.jpg",
"https://graph.org/file/3888300e20e70f79e8ba8.jpg",


"https://graph.org/file/5b2e6ca61047491795136.jpg",
"https://graph.org/file/740339616d692378f027c.jpg",
"https://graph.org/file/51c9284724e28e85ada0c.jpg",
"https://graph.org/file/4b857ba3b38101ed4f216.jpg",
"https://graph.org/file/6308ec539befdf4a335d1.jpg",
"https://graph.org/file/c75324cdc66c8ee5793bb.jpg",
"https://graph.org/file/8caee2c63b2066401e3fa.jpg",
"https://graph.org/file/7d318b2f294e49066e83c.jpg",
"https://graph.org/file/daad921f632f13602d66b.jpg",
"https://graph.org/file/ffca769fa5a991d24c197.jpg",
"https://graph.org/file/4b8dc683c54534c2d72b3.jpg",
"https://graph.org/file/85fe976f1af3a74efa9d3.jpg",
"https://graph.org/file/179f6d3bf8df202691db9.jpg",
"https://graph.org/file/73fe32bb4f1b6f3375e8b.jpg",
"https://graph.org/file/da2323ecba87a8ab4c182.jpg",
"https://graph.org/file/774d0e8bd0327e8e35df0.jpg",
"https://graph.org/file/3d5226b35a97e6c7e6a0e.jpg",
"https://graph.org/file/5fbb1c03db1d8f30856ad.jpg",
"https://graph.org/file/7e1730067ecef12e37652.jpg",
"https://graph.org/file/8b93bce15df14d7225811.jpg",
"https://graph.org/file/b4dd66e242d7661b9dcd2.jpg",
"https://graph.org/file/6efa078b16256a76a1b39.jpg",

"https://graph.org/file/28337379488b8e6af5f54.jpg",
"https://graph.org/file/8c77f65576497f0e3f70d.jpg",
"https://graph.org/file/a1b46e87326e3cf5c868d.jpg",
"https://graph.org/file/606a34cd8f6f454d58378.jpg",
"https://graph.org/file/86390ff86341dbbe98f91.jpg",
"https://graph.org/file/2f68563873477a328ccc2.jpg",
"https://graph.org/file/dbf93aa1c20e4382e64db.jpg",
"https://graph.org/file/7d69d63e399131c050885.jpg",
"https://graph.org/file/602f47667830361f0eb64.jpg",
"https://graph.org/file/777f3ab8abefa835b1059.jpg",
"https://graph.org/file/9beced7d1a18d744cc18a.jpg",
"https://graph.org/file/1867b0db4fcfa20284a6b.jpg",

    "https://graph.org/file/109a941700ce02944afc6.jpg",
    "https://graph.org/file/dd197a3fad2715816528a.jpg",
    "https://graph.org/file/273c4e8811f5249135ae7.jpg",
    "https://graph.org/file/84486beb0429c04806f6c.jpg",
    "https://graph.org/file/609b50e4a4aa03c708247.jpg",
    "https://graph.org/file/6b0a1052c7b64b403a22c.jpg",
    "https://graph.org/file/7ee808520d792c083cdeb.jpg",
    "https://graph.org/file/4db798283a5c3db91c6f6.jpg",
    "https://graph.org/file/bcee30973b23ebd52afcb.jpg",
    "https://graph.org/file/2c402620225d9e117ec54.jpg",
    "https://graph.org/file/7e5229934d9c7858554ab.jpg",
    "https://graph.org/file/adbbf7189416318f40678.jpg",
    "https://graph.org/file/462224ce506163b529e99.jpg",
    "https://graph.org/file/b086290a5c467914d26f6.jpg",
    "https://graph.org/file/df23aa7226f168f2a3a17.jpg",
    "https://graph.org/file/f2ee0e5aa200d8b49a4d1.jpg",
    "https://graph.org/file/d59b342693f4f967de270.jpg",
    "https://graph.org/file/0d10617aa97ece8b7c636.jpg",
    "https://graph.org/file/c37b606a7e940779b7d02.jpg",
    "https://graph.org/file/03a6541f04ad09c048d61.jpg",
    "https://graph.org/file/30696cb28b54f5193e6c4.jpg",
    "https://graph.org/file/d0dd3367dc8cc6db8bd14.jpg",
    "https://graph.org/file/f6effebdf17d142ed52af.jpg",
    "https://graph.org/file/734d7f06f06d892c609fe.jpg",
    "https://graph.org/file/2d6127fef949f898a47ae.jpg",

"https://graph.org/file/7f861f26f80097d869086.jpg",

"https://graph.org/file/07a99f24e310f972c66d6.jpg"
]

@app.on_message(filters.command(["afk"], prefixes=["/", "!"]))
async def active_afk(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    verifier, reasondb = await is_afk(user_id)
    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                send = await message.reply_text(
                    f"**༗ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
                    disable_web_page_preview=True,
                )
            if afktype == "text_reason":
                send = await message.reply_text(
                    f"**༗ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`",
                    disable_web_page_preview=True,
                )
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"**༗ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**༗ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`",
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**༗ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**༗ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`",
                    )
        except Exception:
            send = await message.reply_text(
                f"**༗ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ",
                disable_web_page_preview=True,
            )

    if len(message.command) == 1 and not message.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and not message.reply_to_message:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(message.command) > 1 and message.reply_to_message.sticker:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_afk(user_id, details)    
    await message.reply_photo(
        photo=random.choice(POLICE),
        caption=f"༗ {message.from_user.first_name} ɪs ɴᴏᴡ ᴀғᴋ !"
    )




chat_watcher_group = 1


@app.on_message(
    ~filters.me & ~filters.bot & ~filters.via_bot,
    group=chat_watcher_group,
)
async def chat_watcher_func(_, message):
    if message.sender_chat:
        return
    userid = message.from_user.id
    user_name = message.from_user.first_name
    if message.entities:
        possible = ["/afk", f"/afk@{BOT_USERNAME}"]
        message_text = message.text or message.caption
        for entity in message.entities:
            if entity.type == MessageEntityType.BOT_COMMAND:
                if (message_text[0 : 0 + entity.length]).lower() in possible:
                    return

    msg = ""
    replied_user_id = 0


    
    verifier, reasondb = await is_afk(userid)
    if verifier:
        await remove_afk(userid)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                msg += f"**༗ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n"
            if afktype == "text_reason":
                msg += f"**༗ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n"
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"**༗ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n"
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**༗ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n", 
                      
                     )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"**༗ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n"
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"**༗ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n",
                    )
        except:
            msg += f"**༗ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ\n\n"


    if message.reply_to_message:
        try:
            replied_first_name = message.reply_to_message.from_user.first_name
            replied_user_id = message.reply_to_message.from_user.id
            verifier, reasondb = await is_afk(replied_user_id)
            if verifier:
                try:
                    afktype = reasondb["type"]
                    timeafk = reasondb["time"]
                    data = reasondb["data"]
                    reasonafk = reasondb["reason"]
                    seenago = get_readable_time((int(time.time() - timeafk)))
                    if afktype == "text":
                        msg += (
                            f"**༗ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"
                        )
                    if afktype == "text_reason":
                        msg += f"**༗ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n"
                    if afktype == "animation":
                        if str(reasonafk) == "None":
                            send = await message.reply_animation(
                                data,
                                caption=f"**༗ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"  
                            )
                        else:
                            send = await message.reply_animation(
                                data,
                                caption=f"**༗ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n"  
                            )
                    if afktype == "photo":
                        if str(reasonafk) == "None":
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"**༗ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n" 
                            )
                        else:
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"**༗ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n"  
                            )
                except Exception:
                    msg += f"**༗ {replied_first_name}** ɪs ᴀғk"
        except:
            pass

    if message.entities:
        entity = message.entities
        j = 0
        for x in range(len(entity)):
            if (entity[j].type) == MessageEntityType.MENTION:
                found = re.findall("@([_0-9a-zA-Z]+)", message.text)
                try:
                    get_user = found[j]
                    user = await app.get_users(get_user)
                    if user.id == replied_user_id:
                        j += 1
                        continue
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user.id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += (
                                f"**༗ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"
                            )
                        if afktype == "text_reason":
                            msg += f"**༗ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**༗ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",  
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**༗ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n",  
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"**༗ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",  
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"**༗ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n",  
                                )
                    except:
                        msg += f"**༗ {user.first_name[:25]}** ɪs ᴀғᴋ\n\n"
            elif (entity[j].type) == MessageEntityType.TEXT_MENTION:
                try:
                    user_id = entity[j].user.id
                    if user_id == replied_user_id:
                        j += 1
                        continue
                    first_name = entity[j].user.first_name
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user_id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += f"**༗ {first_name[:25]}** is ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"
                        if afktype == "text_reason":
                            msg += f"**༗ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**༗ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",  
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**༗ {first_name[:25]}** ɪs AFK sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n",  
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"**༗ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",  
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"**༗ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➾ `{reasonafk}`\n\n",  
                                )
                    except:
                        msg += f"**༗ {first_name[:25]}** ɪs ᴀғᴋ\n\n"
            j += 1
    if msg != "":
        try:
            send = await message.reply_text(msg, disable_web_page_preview=True)
        except:
            return

__mod_name__ = "ᴀғᴋ"

__help__ = """

⬤ /afk <reason> *➾* ᴍᴀʀᴋ ʏᴏᴜʀsᴇʟғ ᴀs ᴀғᴋ.
⬤ brb, !afk <reason> *➾* sᴀᴍᴇ ᴀs ᴛʜᴇ ᴀғᴋ ᴄᴏᴍᴍᴀɴᴅ.
"""

