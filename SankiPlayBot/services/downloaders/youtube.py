from os import path

from youtube_dl import YoutubeDL

from SankiPlayBot.config import DURATION_LIMIT
from SankiPlayBot.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"❌ Vιdεσ ιs Lσηgεr Thαη {DURATION_LIMIT} Μιηυτε's Arεη'τ Αllσωεd Tσ Ρlαy."
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"❌ Vιdεσ ιs Lσηgεr Thαη {DURATION_LIMIT} Μιηυτε's Arεη'τ Αllσωεd Tσ Ρlαy."
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
