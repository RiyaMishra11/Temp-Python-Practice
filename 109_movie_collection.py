"""109 - Movie Collection Manager"""
from dataclasses import dataclass, asdict
import json
from pathlib import Path

@dataclass
class Movie:
    title: str
    year: int
    genre: str
    rating: float

class MovieCollection:
    def __init__(self, filename="movies.json"):
        self.filename = Path(filename)
        self.movies = self.load()

    def load(self):
        if not self.filename.exists():
            return []
        try:
            data = json.loads(self.filename.read_text(encoding="utf-8"))
            return [Movie(**item) for item in data]
        except (json.JSONDecodeError, OSError, TypeError):
            return []

    def save(self):
        self.filename.write_text(
            json.dumps([asdict(m) for m in self.movies], indent=2),
            encoding="utf-8"
        )

    def add_movie(self, title, year, genre, rating):
        self.movies.append(Movie(title, int(year), genre, float(rating)))
        self.save()

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            movie for movie in self.movies
            if keyword in movie.title.lower() or keyword in movie.genre.lower()
        ]

    def top_rated(self, limit=5):
        return sorted(self.movies, key=lambda m: m.rating, reverse=True)[:limit]

def main():
    collection = MovieCollection()
    collection.add_movie("Inception", 2010, "Sci-Fi", 8.8)
    collection.add_movie("Interstellar", 2014, "Sci-Fi", 8.7)
    collection.add_movie("3 Idiots", 2009, "Drama", 8.4)

    print("Sci-Fi movies:")
    for movie in collection.search("sci-fi"):
        print(movie)

    print("\nTop rated:")
    for movie in collection.top_rated():
        print(movie.title, movie.rating)

if __name__ == "__main__":
    main()
