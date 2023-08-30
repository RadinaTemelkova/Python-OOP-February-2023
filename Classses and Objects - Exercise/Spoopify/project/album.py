from typing import Tuple, List
from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs: List[Song] = [*songs]
        self.published: bool = False

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        try:
            result = [s for s in self.songs if s.name == song_name][0]
            self.songs.remove(result)
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):

        songs_info = "\n".join([f"== {s.get_info()}" for s in self.songs])
        return f"Album {self.name}\n{songs_info}\n"

