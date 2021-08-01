import os
from SankiPlayBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**HεY 👋 [{}](tg://user?id={})!**\n\n🕹 Ι Αm A Sυρεrfαsτ Μυsιc Plαyιηg βστ Fσr Tεlεgrαm Grσυρs & Chαηηεls Vσιce Chατs.\n\n✅ Sεηd Mε /help Fσr Mσrε Ιηfσ."
      HELP_MSG = [
        ".",
f"""
**HεY 👋 Wεlcσmε βαcκ Tσ {PROJECT_NAME}.

🕹 {PROJECT_NAME} Cαη Ρlαy Μυsιc Ιη Yσυr Grσυρ's Vσιcε Chατ λs ωεll λs Chαηηεl Vσιcε Chατs.

🕹 Assιsταητ Ναmε >> @{ASSISTANT_NAME}\n\nClιcκ Νεχτ Fσr Ιηsτrυcτισηs.**
""",

f"""
**Sєттıηg Uρ**

1) Mαkє вσт αdмıη (gяσυρ αηd ıη cнαηηєł ıf υsє cρłαy)
2) Sтαят α ѵσıcє cнαт
3) Tяy /play [sσηg ηαмє] fσя тнє fıяsт тıмє вy αη αdмıη
*) If υsєявσт jσıηєd єηjσy мυsıc, ıf ησт αdd @{ASSISTANT_NAME} тσ yσυя gяσυρ αηd яєтяy

**Fσя cнαηηєł мυsıc ρłαy**
1) Mαkє мє αdмıη σf yσυя cнαηηєł  
2) Sєηd /userbotjoinchannel ıη łıηkєd gяσυρ
3) Nσω sєηd cσммαηds ıη łıηkєd gяσυρ

**Cσммαηds**

**=>> Sσηg ρłαyıηg 🎧**

- /play: Płαy тнє яєqυєsтd sσηg
- /play [yт υяł] : Płαy тнє gıѵєη yт υяł
- /play [яєρły tσ αυdıσ]: ρłαy яєρłıєd αυdıσ
- /dplay: Płαy sσηg ѵıα Dєєzєя
- /splay: Płαy sσηg ѵıα jıσ sααѵη
- /ytplay: Dıяєcтły ρłαy sσηg ѵıα yσυтυвє мυsıc

**=>> Płαyвαck ⏯**

- /player: Oρєη sєттıηgs мєηυ σf ρłαyєя
- /skip: Skıρs тнє cυяяєηт тяαck
- /pause: Pαυsє тяαck
- /resume: Rєsυмєs тнє ραυsєd тяαck
- /end: Sтσρs мєdıα ρłαyвαck
- /current: Sнσωs тнє cυяяєηт ρłαyıηg тяαck
- /playlist: Sнσωs ρłαyłısт

*Płαyєя cмd αηd αłł σтнєя cмds єxcєρт /play, /current  αηd /playlist  αяє σηły fσя αdмıηs σf тнє gяσυρ.
""",
        
f"""
**=>> cнαηηєł мυsıc ρłαy 🛠**

⚪️ Fσя łıηkєd gяσυρ αdмıηs σηły :

- /cplay [sσηg ηαмє] - Płαy sσηg yσυ яєqυєsтєd
- /cdplay [sσηg ηαмє] - Płαy sσηg yσυ яєqυєsтєd ѵıα dєєzєя
- /csplay [sσηg ηαмє] - Płαy sσηg yσυ яєqυєsтєd via jıσ sααѵη
- /cplaylist - Sнσω ησω ρłαyıηg łısт
- /cccurrent - Sнσω ησω ρłαyıηg 
- /cplayer - Oρєη мυsıc ρłαyєя sєттıηgs ραηєł
- /cpause - Pαυsє sσηg ρłαy
- /cresume - Rєsυмє sσηg ρłαy
- /cskip - Płαy ηєxт sσηg
- /cend - Sтσρ мυsıc ρłαy
- /userbotjoinchannel - Iηѵıтє αssısтαηт тσ yσυя cнαт

Cнαηηєł ıs αłsσ cαη вє υsєd ıηsтєαd σf c ( /cplay = /channelplay )

⚪️ ıd yσυ dση'т łıkє тσ ρłαy ıη łıηkєd gяσυρ :

1) Gєт yσυя cнαηηєł ID.
2) Cяєαтє α gяσυρ ωıтн тıттłє: cнαηηєł мυsıc : your_channel_id
3) Add вσт αs cнαηηєł αdмıη ωıтн fυłł ρєямs
4) Add @{ASSISTANT_NAME} тσ тнє cнαηηєł αs αη αdмıη.
5) Sıмρły sєηd cσммαηds ıη yσυя gяσυρ.
""",

f"""
**=>> Mσяє Tσσłs 🧑‍🔧**

- /musicplayer [ση/σff]: Eηαвłє/Dısαвłє мυsıc ρłαyєя
- /admincache: υρdαтєs αdмıη ıηfσ σf yσυя gяσυρ. тяy ıf вσт ısη'т яєcσgηızє α∂мıη
- /userbotjoin: Iηѵıтє @{ASSISTANT_NAME} υsєявσт тσ yσυя cнαт

**=>> Cσммαη∂s fσя sυdσ υsєяs ⚔️**

 - /userbotleaveall - яємσѵє αssısтαηт fяσм αłł cнαтs
 - /gcast <яєρły тσ мєssαgє> - głσвαłły вяσadcαsт яєρłıєd мєssαgє тσ αłł cнαтs
 - /pmpermit [ση/σff] - Eηαвłє/Dısαвłє ρмρєямıт мєssαgє
*Sυdσ υsєяs cαη єxєcυтє αηy cσммαηd ıη αηy gяσυρs

"""
      ]
