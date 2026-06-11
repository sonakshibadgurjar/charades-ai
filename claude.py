def claude_guess(action):
    movies = {
        "ghost": "The Conjuring",
        "fight": "Avengers",
        "love": "Titanic",
        "hero": "Batman",
        "monster": "King Kong"
    }

    return movies.get(action, "Unknown Movie")