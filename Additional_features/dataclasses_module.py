'''
Implement an immutable MusicAlbum class that describes a music album. When instantiated, the class must take four
arguments in the following order:

title — album title (str type)
artist - album author (str type)
genre — album genre (str type)
year — album release year (int type)
An instance of the MusicAlbum class must have four attributes:

title — album title
artist - album author
genre - album genre
year — album release year
Also, an instance of the MusicAlbum class must have the following formal string representation:

MusicAlbum(title='<album title>', artist='<album author>')
Finally, instances of the MusicAlbum class must support comparison between themselves using the == and != operators.
Two music albums are considered equal if their titles, authors and release years are the same.
'''

from dataclasses import dataclass, field

@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)

# Example
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)

# Output
# True
# False