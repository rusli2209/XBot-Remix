from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^s(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc artoria shiki yi medb Nightingale yu ke i ii iii Hokusai Carmilla Mysterious Mae drake europa paris boudica chacha circe medea murasaki kiara ishtar bradamante brynhildr tomoe gozen irisviel von katou medusa parvati opera stheno euryale nero enkidu yang")
# Owner @erruuu



@register(outgoing=True, pattern='^h(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc arthur gilgamesh edward eric ivan yu yi mephistopheles lancelot Siegfried sieg drake romulus yagyu mac cumhaill Henry Shi i ii iii william Darius solomon Eric Charles Asclepius Mozart Angra David de")
# Owner @erruuu



@register(outgoing=True, pattern='^xx(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc mysterious heroine x xx")
# Owner @erruuu


@register(outgoing=True, pattern='^ll(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc hikari hikari oono kirigaya mio nao ruka rikka erice erika chihiro nakano uesugi yui medusa mito mii boudica akari tomoe mami papi kagome beatrice eru kyons sister sae cabashira ichinose rias kanao akeno futaba koneko meteora kyouko shinku youmu ryouko asuna haruhi natsumi lelei margaret")
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
