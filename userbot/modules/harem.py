from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^serv(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc artoria shiki yi medb Nightingale yu ke i ii iii Hokusai Carmilla Mysterious Mae chacha circe medea murasaki kiara ishtar bradamante brynhildr tomoe gozen irisviel von katou stheno euryale nero enkidu yang")
# Owner @erruuu



@register(outgoing=True, pattern='^husb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc arthur gilgamesh edward eric ivan yu yi mephistopheles lancelot Siegfried yagyu mac cumhaill Henry Shi i ii iii Darius solomon Eric Charles Asclepius Mozart Angra David de")
# Owner @erruuu



@register(outgoing=True, pattern='^xx(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc mysterious heroine x xx")
# Owner @erruuu



CMD_HELP.update({
    "harem":
    "`.serv`\
\nUsage: Untuk protecc servant.\
\n\n`husb`\
\nUsage: Untuk protecc husbu.\
\n\n`xx`\
\nUsage: Untuk protecc servant char mysterious."
})
