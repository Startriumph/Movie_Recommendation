movies = {
    "Action": [
        {"name": "Avengers", "rating": 8.4, "year": 2012},
        {"name": "Batman", "rating": 8.2, "year": 2008},
        {"name": "John Wick", "rating": 7.9, "year": 2014}
    ],
    "Comedy": [
        {"name": "Hangover", "rating": 7.7, "year": 2009},
        {"name": "Devil Wears Prada", "rating": 7.0, "year": 2006},
        {"name": "Mr Bean", "rating": 7.5, "year": 1997}
    ],
    "Sci-Fi": [
        {"name": "Interstellar", "rating": 8.7, "year": 2014},
        {"name": "Inception", "rating": 8.8, "year": 2010},
        {"name": "The Matrix", "rating": 8.7, "year": 1999}
    ],
    "Romance":[
        {"name": "The Notebook", "rating": 7.8, "year": 2004},
        {"name": "Titanic", "rating": 7.8, "year": 1997},
        {"name": "The fault in our stars", "rating": 7.6, "year":2014}
    ]

}

genre = input("Enter genre (Action/Comedy/Sci-Fi/Romance): ")
min_rating = float(input("Enter minimum rating: "))

if genre in movies:
    recommended = []

    for movie in movies[genre]:
        if movie["rating"] >= min_rating:
            recommended.append(movie)

    recommended.sort(key=lambda x: x["rating"], reverse=True)

    if recommended:
        print("\nRecommended Movies:")
        for movie in recommended:
            print(movie["name"], "-", movie["rating"], "-", movie["year"])
    else:
        print("No movies found with that rating.")
else:
    print("Genre not found.")