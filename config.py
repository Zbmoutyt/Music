import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7521516823:AAHILm76Yflu9kdF_5kr5KaME-to6adqdRo")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","Surya_Putra_Karn")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "Sizhoo_Music_Bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "˹ᴀɴɢʀʏ𓅜 ʙɪʀᴅ˼ ✘ ˹ᴍᴜsɪᴄ˼")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "Angry_Music_Assistant")
EVALOP = list(map(int, getenv("EVALOP", "7176027733").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://RUDRA_JAAT1:RUDRAJAAT@rudrajaat.zbir7lx.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002088928464"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", " 6750212064"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
   "UPSTREAM_REPO",
   "https://github.com/Zbmoutyt/Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Rudra")
GIT_TOKEN = getenv(
   "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/angrybird_worldx")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/angrybird_worldx")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQC6kfsAl0O8C53kfxsNM9JL7aZ67OJQaydSIw_jiFBekG159L2S9AQ2V74s30fxyZrFK3VqqFTdLT9xrZ8xRd9L0g-7B1qjPs0AaZ22G9M04B4yB0jYrdWnb5Kw502QZpq-IGoIYAkLtFrGwgeU_qjW0T-5RODBv4neq0B06iDSMUGNRE_0oYUhmSWfj4z_uNtr2O81Dqpck9VzN5MUDWOCAO3gseW1IVLXoZzjf_jfeNWJbp2O7-JeW-_cZOM-LzBdRVHDEcim7mRFpdFXekTKMFe6bbvUOPbiLT2g7BiNe4sb8IkKb8eZX7gevQ9720xXgLfCx2m-1uVcRKSbjysPwSFI7QAAAAGPYj5JAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
   "START_IMG_URL", "https://envs.sh/w6q.jpg"
)
PING_IMG_URL = getenv(
   "PING_IMG_URL", "https://envs.sh/w6q.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/w6q.jpg"
STATS_IMG_URL = "https://envs.sh/w6q.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/w6q.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/w6q.jpg"
STREAM_IMG_URL = "https://envs.sh/w6q.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/w6q.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/w6q.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/w6q.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/w6q.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/w6q.jpg"


def time_to_seconds(time):
   stringt = str(time)
   return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
   if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
       raise SystemExit(
       "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
       )
       
if SUPPORT_CHAT:
   if not re.match("(?:http|https)://", SUPPORT_CHAT):
       raise SystemExit(
           "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
       )
