from typing import List
from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            result = next(filter(lambda a: a.name == album_name, self.albums))
            if result.published:
                return "Album has been published. It cannot be removed."
            else:
                self.albums.remove(result)
                return f"Album {album_name} has been removed."

        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):

        albums_info = "\n".join([current_album.details() for current_album in self.albums])
        return f"Band {self.name}\n{albums_info}\n"


first_song = Song("Some song", 3.67, False)
print(first_song.get_info())
album = Album("Some album", first_song)
second_song = Song("Another song", 2.43, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Some band")
print(band.add_album(album))
print(band.remove_album("Some album"))
print(band.details())




