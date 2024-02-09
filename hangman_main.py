import categories
import pyfiglet
import time

print(pyfiglet.figlet_format("LET'S PLAY HANGMAN!", font="varsity", justify="centre", width=110))
hangman_game = categories.Categories()


def get_word():
    global hints
    time.sleep(3)
    categories_text = """CATEGORIES 
    1. CAR BRANDS
    2. PLACES OF INDIA
    3. HARRY POTTER
    4. PLACES AROUND THE WORLD
    5. AVENGERS"""

    font_name = "wet_letter"

    for line in categories_text.split('\n'):
        ascii_art = pyfiglet.figlet_format(line, font=font_name)
        print(ascii_art)
        time.sleep(1)
    while True:

        category_input = input("Enter the category (1, 2, 3, 4, 5): ")
        if category_input.isdigit() and 1<=int(category_input)<=5:
            category_input = int(category_input)
            
        else:
            print("Enter a valid number (1,2,3,4,5) please")
            continue
        
        while True:
            level_input = input("Enter the difficulty level (easy, hard): ")

            if level_input == 'easy':
                word = hangman_game.choose_word(category_input, level_input)
                return word
            elif level_input == 'hard':
                
                word = hangman_game.choose_word(category_input, level_input)

                if word:
                    hints = hangman_game.choices[category_input][level_input][word]
                    return word, hints
            else:
                print("Invalid difficulty chosen!")



tries = 6


def play_game(tries):

    result = get_word()

    if isinstance(result, tuple):
        w, h = result
    else:
        w, h = result, None

    
    
    word_to_guess = w.upper() 
    
    guessed_alphabets = []

    incorrect_guess = 0

    dashes = ["_ "] * len(word_to_guess)
    if ' ' in word_to_guess:
        dashes = []
        for char in word_to_guess:
            if char == ' ':
                dashes.append('   ')
            else:
                dashes.append('_ ')

    while True:

        print(" ".join(dashes))

        guess = input("Guess a letter/word (Enter 0 for hint): ").upper()
        if guess=='0':
            print(h)
            continue

        if guess in guessed_alphabets:
            if len(guess) == 1:
                print("Alphabet already guessed, try a different one!")
            else:
                print("Word already guessed, try a different one!")
            continue

        guessed_alphabets.append(guess)

        if len(guess) == 1 and guess.isalpha():
            if guess in word_to_guess:
                print("You're guessed alphabet is in the word!")

                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        dashes[i] = guess
                print(" ".join(dashes))
            else:
                print("Your guessed letter is incorrect!")
                tries -= 1
                display_hangman(6 - tries)
                if tries == 0:
                    print(pyfiglet.figlet_format("""SORRY U LOST    !     :(""", font="utopiab",width=120))
                    print("The word is: ", word_to_guess)
                    break

            if '_ ' not in dashes:
                print(pyfiglet.figlet_format("""CONGRATULATIONS! U GUESSED THE WORD    !     :)""", font="utopiab",width=120))
                break
        elif len(guess) == len(word_to_guess) and guess.isalpha():
            if guess == word_to_guess:
                print(pyfiglet.figlet_format("""CONGRATULATIONS! U GUESSED THE WORD    !     :)""", font="utopiab",width=120))
                break
            else:
                print("YOUR GUESS IS INCORRECT! TRY AGAIN.")
                tries -= 1
                display_hangman(6 - tries)
                if tries == 0:
                    print(pyfiglet.figlet_format("""SORRY U LOST    !     :(""", font="utopiab",width=120))
                    break


        else:
            print("Not a valid guess")


def display_hangman(tries):
    l = [("""     ╔════════╗
     ║     ║
     ║     
     ║    
     ║    
     ║
    ═╩═══════╩══"""),
         ("""     ╔════════╗
     ║     ║
     ║     O
     ║    
     ║    
     ║
    ═╩═══════╩══"""),
         ("""     ╔════════╗
     ║     ║
     ║     O
     ║    /
     ║    
     ║
    ═╩═══════╩══"""),
         ("""     ╔════════╗
     ║     ║
     ║     O
     ║    /|
     ║    
     ║
    ═╩═══════╩══"""),
         ("""     ╔════════╗
     ║     ║
     ║     O
     ║    /|\\
     ║    
     ║
    ═╩═══════╩══"""),
         ("""     ╔════════╗
     ║     ║
     ║     O
     ║    /|\\
     ║    / \\
     ║
    ═╩═══════╩══""")]

    print(l[tries - 1])


play_game(6)