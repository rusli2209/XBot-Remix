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
    sleep(1)
    await typew.edit(f"**Misi lort, ikut nimbrung**")
    sleep(2)
    await typew.edit("**Assalamualaikum...**")
# Owner @eruuu



@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Jawab Salam Dong...**")
    sleep(1)
    await typew.edit("**Wa'alaikumsalam...**")
# Owner @erruuu



@register(outgoing=True, pattern='^ll(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("*Jawab Salam Dong...*")
    sleep(1)
    await typew.edit("**Wa'alaikumsalam lort**")
# Owner @erruuu



@register(outgoing=True, pattern='^arto(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("*protecc ah*")
    sleep(1)
    await typew.edit("/protecc artoria")
# Owner @erruuu



@register(outgoing=True, pattern='^Arthur(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("*protecc ah*")
    sleep(1)
    await typew.edit("/protecc Arthur")
# Owner @erruuu



@register(outgoing=True, pattern='^heroine(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("*protecc ah*")
    sleep(1)
    await typew.edit("/protecc mysterious heroine x xx")
# Owner @erruuu



CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
