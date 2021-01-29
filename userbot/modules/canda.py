from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Woii...**")
    sleep(2)
    await typew.edit("`Ganteng doang`")
    sleep(2)
    await typew.edit("`Jemput cewe depan gang`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Woii...**")
    sleep(2)
    await typew.edit("`Ganteng doang`")
    sleep (2)
    await typew.edit("`Jemput cewe depan gang`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Cantik doang`")
    sleep(1)
    await typew.edit("`Tapi fakgirls`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Cantik doang`")
    sleep(1)
    await typew.edit("`Tapi fakgirls`")
# Owner @Si_Dian


CMD_HELP.update({
    "canda":
    "`.g`\
\nUsage: Untuk nyindir laki.\
\n\n`.c`\
\nUsage: Untuk nyindir cewe."
})
