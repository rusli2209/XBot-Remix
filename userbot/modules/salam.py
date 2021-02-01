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
    sleep(0.1)
    await typew.edit(f"**Assalamu'alaikum**")
# Owner @eruuu



@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Wa'alaikumsalam...**")
# Owner @erruuu



@register(outgoing=True, pattern='^sere(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("/protecc artoria yi medb Nightingale (Santa) NP1 2. Yu Miaoyi NP1 3. Katsushika Hokusai (Saber) NP2 4. Carmilla NP1 5. Mysterious Alter-Ego Lambda NP1 6. Tamamo-no-Mae NP3 7. Chacha NP2 8. Circe NP2 9. Medea (Lily) NP2 10. Murasaki Shikibu (Rider) NP2 11. Sessyoin Kiara (Moon Cancer) NP2 12. Space Ishtar NP1 13. Bradamante NP1 14. Brynhildr (Berserker) NP2 15. Tomoe Gozen (Saber) NP2 16. Irisviel (Holy Grail) NP1 17. Artoria Pendragon (Archer) NP1 18. Katou Danzo NP1 19. Stheno NP2 20. Nero Claudius (Bride) NP2")
# Owner @erruuu



@register(outgoing=True, pattern='^sero(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("/protecc arthur Gilgamesh Mephistopheles Lancelot NP6 4. Gilgamesh NP1 5. Siegfried NP1 6. Munenori Yagyu NP3 7. Fionn mac Cumhaill NP3 8. Henry Jekyll & Hyde NP5 9. Shi Huang Di NP3 10. Leonidas I NP2 11. Darius NP4 12. Solomon NP4 13. Eric Bloodaxe NP3 14. Charles-Henri Sanson NP1 15. Asclepius NP2 16. Wolfgang Amadeus Mozart NP3 17. Angra Mainyu NP1 18. David NP3 19. Gilles de Rais (Caster) NP3 20. Fergus mac")
# Owner @erruuu



@register(outgoing=True, pattern='^xx(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("/protecc mysterious heroine x xx")
# Owner @erruuu



CMD_HELP.update({
    "salam":
    "`p`\
\nUsage: Untuk Memberi salam. Other CMD : sere sero xx\
\n\n`l`\
\nUsage: Untuk Menjawab Salam."
})
