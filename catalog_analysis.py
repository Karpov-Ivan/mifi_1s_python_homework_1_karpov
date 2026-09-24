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

print("Этап 1")
print(f"average_rating(movies): {average_rating(movies)}")
print(f"catalog_age_stats(movies): {catalog_age_stats(movies)}")
print(f"duration_in_hours(125): {duration_in_hours(125)}")

print("\nЭтап 2")
print(f"rating_tier(7): {rating_tier(7)}")
print(f"decade_label(2017): {decade_label(2017)}")

print("\nЭтап 3")
print("print_non_comedy_titles(movies):")
print_non_comedy_titles(movies)
print(f"find_first_masterpiece(movies): {find_first_masterpiece(movies)}")
print(
    "find_first_masterpiece(movies[:7]): "
    f"{find_first_masterpiece(movies[:7])}"
)
print(f"count_long_movies(movies): {count_long_movies(movies)}")

print("\nЭтап 4")
print(f'normalize_title("silent hours"): {normalize_title("silent hours")}')
print(f'make_slug("Silent Hours"): {make_slug("Silent Hours")}')
print(f"format_report_line(movies[7]): {format_report_line(movies[7])}")
