from telethon import Button

from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/447ec551360a04632d5b9.jpg"


@register(pattern=("/credits"))
async def awake(event):
    HYDRA = """
    Credits
BOT OWNER : [OTAZUKI](https://telegram.dog/OTAZUKI_004)
REPO OWNER : [ð©ð§á´á´É´ ðÉªÉ´á´á´¢ðª](https://telegram.dog/Toon_LinkZ)
HELPER : [ð¤ã GT ASHâ¢ ãð¤](https://telegram.dog/Awesome_GtashXD)
SUPPORTER : [ð§ð¢ðð¨ é¬¼](https://telegram.dog/Awesome_Tofu)


â¢ SUPPORT : [Here](https://telegram.dog/FutureCity005)
â¢ UPDATES : [Here](https://telegram.dog/Updates004)
---------------------------------------------------------
**DEV LIST**

DEV 1 - @OTAZUKI_004 & @Toon_LinkZ *Owner
DEV 2 - @Awesome_GtashXD *Some module he maked
DEV 3 - @NandhaXD *He solved Many errors 
DEV 4 - @Awesome_Tofu *helped On V-5 Music player
----------------------------------------------------------
I Hope Hydra Users Have Humanity. 
Thanks For Using! 

ð©ð§á´á´É´ ðÉªÉ´á´á´¢ðª â¢
"""

    BUTTON = [
        [
            Button.url("Û ððªð©ðªð§ð ð¾ðð©ð® Û", "https://telegram.dog/FutureCity005"),
            Button.url(" ð©ð§á´á´É´ ðÉªÉ´á´á´¢ðª ", "https://telegram.dog/Toon_LinkZ"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=HYDRA, buttons=BUTTON)
#V-5

__help__ = """
**Users Only**
/credits - Know Hydra Devlopers And Helpers
"""

__mod_name__ = "Credits"