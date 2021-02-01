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
    await typew.edit("/protecc artoria yi medb Nightingale (Santa) NP1 2. Yu Miaoyi NP1 3. Katsushika Hokusai (Saber) NP2 4. Carmilla NP1 5. Mysterious Alter-Ego Lambda NP1 6. Tamamo-no-Mae NP3 7. Chacha NP2 8. Circe NP2 9. Medea (Lily) NP2 10. Murasaki Shikibu (Rider) NP2 11. Sessyoin Kiara (Moon Cancer) NP2 12. Space Ishtar NP1 13. Bradamante NP1 14. Brynhildr (Berserker) NP2 15. Tomoe Gozen (Saber) NP2 16. Irisviel (Holy Grail) NP1 17. Artoria Pendragon (Archer) NP1 18. Katou Danzo NP1 19. Stheno NP2 20. Nero Claudius (Bride) NP2")
# Owner @erruuu



@register(outgoing=True, pattern='^husb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.000001)
    await typew.edit("/protecc arthur Gilgamesh Mephistopheles Lancelot Siegfried Yagyu mac Cumhaill Henry Shi i Darius solomon Eric Charles Asclepius Mozart Angra David de")
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
