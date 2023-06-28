import json
import os

from googleapiclient.discovery import build

api_key: str = os.environ.get('API_KEY')
print(api_key)
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        pass

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(channel, indent=2, ensure_ascii=False))
        pass


channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
