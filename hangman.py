import random
words = ['python','java','kotlin','javascript','ruby','swift']

#Randomly choose a word from the list
chosen_word = random.choice(words)
word_dislay = ['_' for _ in chosen_word] #create a list of underscores
attempts = 8 # Number of attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_dislay:
    print("\n" + ' '.join(word_dislay))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_dislay[index] = guess #revel letter
    else:
        print("that letter dosen't appear in the word !!!")
        attempts -=1

#Game conclusion
if '_' not in word_dislay:
    print("You guessed the word!!")
    print(" ".join(word_dislay))
    print("you survived!!")
else: 
    print("you ran out of attempts. The word was: " + chosen_word)
    print("Youn lost!")
