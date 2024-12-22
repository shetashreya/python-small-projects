import random
import movies


choice = {
    '1' : 'sci_fic',
    '2' : 'romantic',
    '3' : 'comedy',
    '4' : 'ancient_history_movies',
    '5' : 'futuristic_movies',
    '6' : 'top_movies',
    '7' : 'mix_movies'
}

print('''what type of movie you want to watch (type number):
      1. science fiction
      2. romantic
      3. comedy
      4. ancient history
      5. futuristic
      6. top movies
      7. mix of above''')

user_input = input()


if user_input in choice:
    category_name = choice[user_input]
    movie_list = getattr(movies, category_name)  # Access the corresponding list from the `movies` module
    random_movie = random.choice(movie_list)  # Select a random movie
    print("\nHere is a random movie recommendation for you:")
    print(f"Title: {random_movie['Title']}")
    print(f"Rank: {random_movie['Rank']}")
    print(f"Duration: {random_movie['Duration']}")
    print(f"Category: {random_movie['Category']}")
else:
    print("\nInvalid choice. Please try again.")
