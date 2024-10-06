import asyncio
import os
import re
from pytube import YouTube, Search
from typing import Union
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message


async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in (errorz.decode("utf-8")).lower():
            return out.decode("utf-8")
        else:
            return errorz.decode("utf-8")
    return out.decode("utf-8")


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if re.search(self.regex, link):
            return True
        else:
            return False

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        text = ""
        offset = None
        length = None
        for message in messages:
            if offset:
                break
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        if offset in (None,):
            return None
        return text[offset : offset + length]

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        yt = YouTube(link)
        title = yt.title
        duration_min = yt.length // 60  # Converting seconds to minutes
        thumbnail = yt.thumbnail_url
        vidid = yt.video_id
        return title, f"{duration_min} min", yt.length, thumbnail, vidid

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        yt = YouTube(link)
        return yt.title

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        yt = YouTube(link)
        duration_min = yt.length // 60  # Converting seconds to minutes
        return f"{duration_min} min"

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        yt = YouTube(link)
        return yt.thumbnail_url

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        yt = YouTube(link)
        stream = yt.streams.filter(res="720p").first()
        return 1, stream.url if stream else None

    async def search(self, query: str):
        search = Search(query)
        result = search.results[0]  # Fetch the first result
        return result.title, result.length, result.thumbnail_url, result.video_id

    async def download(
        self,
        link: str,
        video: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
    ) -> str:
        yt = YouTube(link)

        def audio_dl():
            audio_stream = yt.streams.filter(only_audio=True).first()
            file_path = audio_stream.download(output_path="downloads")
            return file_path

        def video_dl():
            video_stream = yt.streams.filter(res="720p").first()
            file_path = video_stream.download(output_path="downloads")
            return file_path

        loop = asyncio.get_running_loop()

        if songaudio:
            downloaded_file = await loop.run_in_executor(None, audio_dl)
            return downloaded_file
        elif video:
            downloaded_file = await loop.run_in_executor(None, video_dl)
            return downloaded_file
        else:
            downloaded_file = await loop.run_in_executor(None, audio_dl)
        return downloaded_file


# Example usage of YouTubeAPI class
async def download_video_or_audio(link, is_video=False, is_audio=False):
    yt_api = YouTubeAPI()
    if await yt_api.exists(link):
        if is_video:
            video_file = await yt_api.download(link, video=True)
            print(f"Video downloaded at: {video_file}")
        elif is_audio:
            audio_file = await yt_api.download(link, songaudio=True)
            print(f"Audio downloaded at: {audio_file}")
        else:
            print("Please specify video or audio download option.")
    else:
        print("Invalid YouTube link.")

# Run this function to download a video or audio from YouTube
# You can call the async function inside an event loop
