import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, 
     "genres": {"sci-fi", "drama"}, "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Stage 1
def average_rating(movies):
    total_rating, movie_count = 0, 0

    for movie in movies:
        total_rating += movie["rating"]
        movie_count += 1

    return round(total_rating / max(movie_count, 1), 1)

def catalog_age_stats(movies, current_year=2026):
    newest_age, oldest_age = 1000, 0
    total_age, movie_count = 0, 0

    for movie in movies:
        age = current_year - movie["year"]

        newest_age = min(newest_age, age)
        oldest_age = max(oldest_age, age)

        total_age += age
        movie_count += 1

    return (oldest_age, newest_age, math.ceil(total_age / max(movie_count, 1)))

def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"

# Stage 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"

    return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year <= 2020 and year >= 2015:
            return "недавние"
        case _ if year < 2015:
            return "старые"

# Stage 3
def print_non_comedy_titles(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print(movie["title"])

def find_first_masterpiece(movies):
    index = 0

    while index < len(movies):
        movie = movies[index]

        if movie["rating"] > 9.0:
            break

        index += 1
    else:
        return "Шедевров не найдено"

    return movie["title"]

def count_long_movies(movies, threshold=120):
    count_movies = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count_movies += 1

    return count_movies

# Stage 4
def normalize_title(title):
    normalized_words = []

    for word in title.split():
        normalized_words.append(word[0].upper() + word[1:])

    return " ".join(normalized_words)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )

# Stage 5
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    return [
        (movie["title"], movie["rating"])
        for movie in sorted_movies[:n]
    ]

# Stage 6
def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts

def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(movie["title"])

    return filmography

def ratings_above_average(movies):
    average = average_rating(movies)
    above_average_ratings = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

    return above_average_ratings

# Stage 7
def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)

# Stage 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def print_high_rated_movies(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

def total_duration_high_rated(movies):
    return sum(
        movie["duration_min"]
        for movie in movies
        if movie["rating"] > 7
    )

# Stage 9
def build_report(movies):
    average = average_rating(movies)
    average_age = catalog_age_stats(movies)[2]
    top_movies = top_n_by_rating(movies)
    movies_by_title = {movie["title"]: movie for movie in movies}
    genre_counts = count_by_genre(movies)
    sorted_genre_counts = sorted(
        genre_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )
    genres = ", ".join(sorted(all_genres(movies)))

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average}")
    print(f"Средний возраст фильмов: {average_age} лет")

    print("\nТоп-3 фильма:")
    for title, _ in top_movies:
        print(f"  {format_report_line(movies_by_title[title])}")

    print("\nФильмов по жанрам:")
    for genre, movie_count in sorted_genre_counts:
        print(f"  {genre} — {movie_count}")

    print(f"\nВсе жанры каталога: {genres}")

if __name__ == "__main__":
    build_report(movies)
