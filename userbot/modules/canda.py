from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.bagi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Woii...**")
    sleep(2)
    await typew.edit("**Bagi harem nya dong**")
    sleep(2)
    await typew.edit("**Punya gw masih dikit hiks**")
# Owner @erruuu


@register(outgoing=True, pattern='^.sad(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Aku cinta dia**")
    sleep(2)
    await typew.edit("**Walau dia tidak cinta aku**")
    sleep(2)
    await typew.edit("**Karena cinta tidak harus memiliki.**")
    sleep(2)
    await typew.edit("**Hiksss...**")
# Owner @erruuu


@register(outgoing=True, pattern='^.beban(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Dari 7,4 miliar**")
    sleep(2)
    await typew.edit("**sampah di bumi**")
    sleep(2)
    await typew.edit("**eh maksudnya manusia di bumi**")
    sleep(2)
    await typew.edit("**hanya kamu yang menjadi beban**")
    sleep(2)
    await typew.edit("**di kehidupan alam ini**")
    sleep(2)
    await typew.edit("**canda wkwk, jangan baper...**")
# Owner @erruuu


@register(outgoing=True, pattern='^.newmem(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo**")
    sleep(2)
    await typew.edit("**Selamat bergabung!**")
    sleep(2)
    await typew.edit("**Salken yaa**")
    sleep(2)
    await typew.edit("**Semoga betah disini**")
# Owner @erruuu


@register(outgoing=True, pattern='^.malam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Konbanwa**")
    sleep(2)
    await typew.edit("**Selamat malam semuanya**")
    sleep(2)
    await typew.edit("**Tidur-tidur**")
    sleep(2)
    await typew.edit("**Jaga kesehatan lu**")
    sleep(2)
    await typew.edit("**Soalnya kalo sakit ga ada yg peduli**")
    sleep(2)
    await typew.edit("**Sad...**")
    sleep(2)
    await typew.edit("**Canda kak hehe**")
    sleep(2)
    await typew.edit("**Ada aku yang peduli kok...**")
    sleep(2)
    await typew.edit("**Tapi boong**")
    sleep(2)
    await typew.edit("**Xixixii...**")
# Owner @erruuu


@register(outgoing=True, pattern='^.ohayou(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Ohayou**")
    sleep(2)
    await typew.edit("**Sekai**")
    sleep(2)
    await typew.edit("**Good Morning**")
    sleep(2)
    await typew.edit("**World**")
    sleep(2)
    await typew.edit("**Pagii**")
# Owner @erruuu


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Woii...**")
    sleep(2)
    await typew.edit("`Ganteng doang`")
    sleep (2)
    await typew.edit("`Ganteng doang jemput cewe depan gang`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Cantik doang`")
    sleep(1)
    await typew.edit("`Tapi chat cowok lebih dari satu`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Cantik doang`")
    sleep(1)
    await typew.edit("`Tapi chat cowok lebih dari satu`")
# Owner @Si_Dian

@register(outgoing=True, pattern='^.brokn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit(f"**I'M A BROKENT HOME.**")
    sleep(5)
    await typew.edit("`Tangisan hanya mengacaukan segalanya tapi senyuman membuat mereka yakin aku Tegar`")
    sleep(5)
    await typew.edit("`Setiap anak ingin keluarga yang sempurna\ntapi tidak semua anak memilikinya`")
    sleep(5)
    await typew.edit("`Sayangilah kedua orang tuamu dengan\nsepenuh hati selagi masih ada🙂`")


@register(outgoing=True, pattern='^.oe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**oee....**")
    sleep(3)
    await typew.edit("`Muka kalian 8 bit...`")
    sleep(3)
    await typew.edit("`Kayak Monyet`")
    sleep(3)
    await typew.edit("`Muka gw Gak Burik Kek Kalian`")


@register(outgoing=True, pattern='^.tidr(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Eh, beban keluarga tdr woi**")
    sleep(2)
    await typew.edit("`Sadar gadangnya bukan untukmu.`")
    sleep(2)
    await typew.edit("`Melainkan untuk dia di akun satu`")


@register(outgoing=True, pattern='^.pc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Eh, yelah pc doang jadian kagak**")
    sleep(2)
    await typew.edit("`Percuma Jadian putus iya, ngewe kgk.`")
    sleep(2)
    await typew.edit("`Canda ngewe:v`")
    sleep(2)
    await typew.edit("`Awoawok Canda monyet`")


@register(outgoing=True, pattern='^.tbat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Eh beban keluarga**")
    sleep(2)
    await typew.edit("`Bapak lu kerja keras nafkahin keluarga`")
    sleep(2)
    await typew.edit("`Anaknya kelakuannya kek sempak Dajjal!!`")
    sleep(2)
    await typew.edit("`Tobat sadar lu anak haram`")


@register(outgoing=True, pattern='^.gbt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Nyanyi dikit bolehlah ya:v**")
    sleep(2)
    await typew.edit("`Du🤸‍♂️`")
    sleep(2)
    await typew.edit("`Du di 🤸‍♂️`")
    sleep(0.5)
    await typew.edit("`Du du du🤸‍♂️`")
    await typew.edit("`Du🤸‍♂️`")
    sleep(2)
    await typew.edit("`Du di 🤸‍♂️`")
    sleep(0.5)
    await typew.edit("`Du du du🤸‍♂️`")
    sleep(0.5)
    await typew.edit("`Aye aye kimochi:v`")
    sleep(2)
    await typew.edit("`Asw Gabut bet gw:v`")


CMD_HELP.update({
    "canda":
    "`.g`\
\nUsage: Untuk nyindir laki.\
\n\n`Baru`\
\nCMD: .bagi .sad .newmem .beban .malam. ohayou\
\n\n`.c`\
\nUsage: Untuk nyindir cewe.\
\n\n`.brokn`\
\nUsage: Liat aja dah sendiri.\
\n\n.`oe`\
\nUsage: Buat ngatain orang.\
\n\n`.pc`\
\nUsage: Buat ngatain orang yg sllu pc.\
\n\n`.tbat`\
\nUsage: Tobat woi tobat.\
\n\n`.gbut`\
\nUsage: Buat lu pada yang gabut."
})
