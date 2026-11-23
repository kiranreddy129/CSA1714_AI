users = {
    "User1": {"Movie1": 5, "Movie2": 4, "Movie3": 1},
    "User2": {"Movie1": 5, "Movie2": 4, "Movie3": 2},
    "User3": {"Movie1": 1, "Movie2": 2, "Movie3": 5}
}

user = input("Enter user name (User1/User2/User3): ")

if user in users:
    print("Recommended Movies:")

    for movie in users[user]:
        if users[user][movie] >= 4:
            print(movie)
else:
    print("User not found")
