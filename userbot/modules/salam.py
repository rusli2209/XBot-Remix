from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit(f"**Assalamu'alaikum**")
# Owner @eruuu



@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("**Wa'alaikumsalam...**")
# Owner @erruuu


CMD_HELP.update({
    "salam":
    "`p`\
\nUsage: Untuk Memberi salam.\
\n\n`l`\
\nUsage: Untuk Menjawab Salam. Other : serv husb xx"
})
