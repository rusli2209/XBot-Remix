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
    await typew.edit("/protecc quetzalcoatl jinako chevalier artoria qin rhyme matahari shiki yi medb Nightingale yu ke i ii iii Hokusai Carmilla mata Mysterious Mae drake europa paris boudica chacha circe medea murasaki kiara ishtar williams jeanne jane bradamante brynhildr tomoe gozen irisviel von katou medusa parvati orion opera stheno euryale nero enkidu hassan yang abigail")
# Owner @erruuu



@register(outgoing=True, pattern='^h(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc arthur gilgamesh edward eric arjuna emiya gaius ivan yu yi mephistopheles benkei chiron lancelot the Siegfried sieg spartacus drake romulus sakata antonio helmes red yagyu mac cumhaill Henry henri roberts paris columbus bedivere amakusa okada hans prince iskandar tristan Shi i ii iii william geronimo hood georgios hijikata caligula alexander li lu lobo aesclepius Darius solomon Eric hassan chen ashwatthama jason james Charles enkidu asterios Asclepius yan cu merlin  mozart Angra David de heracles karna fuuma tawara arash ozymandias odysseus opera orion")
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
    await typew.edit("/protecc hikari hikari oono kirigaya mio atago gaen araragi yuuna izumi izuna nao ruka rikka erice erika chihiro nakano uesugi yui yukino hanyuu medusa mito mii boudica akari tomoe mami papi kagome beatrice eru kyons sister sae cabashira ichinose rias kanao akeno futaba koneko meteora aoko kyouko shinku youmu ryouko asuna haruhi natsumi lelei margaret")
# Owner @erruuu


CMD_HELP.update({
    "harem":
    "`s`\
\nUsage: Protecc servant (beta).\
\n\n`h`\
\nUsage: Protecc husbu (beta).\
\n\n`ll`\
\nUsage: Protecc loli (beta).\
\n\n`xx`\
\nUsage: Protecc servant char mysterious."
})
