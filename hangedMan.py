import random
import string

words = ["python", "intern", "code", "programming", "something", "else", "GOOGLE", "this is list", "hell-o"]

visualHealth = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

def getWord(words):
    word = random.choice(words)
    
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangedMan(): 
    
    print("========================")
    print("  H A N G E D   M A N")
    print("========================")
    
    word = getWord(words)
    
    missingLetters = set(word) #set() hace un conjunto de elementos individuales y no acepta repeticiones
    guessedLetters = set()
    abc = set(string.ascii_uppercase) 
    
    health = 7
    
    while len(missingLetters) > 0 and health > 0:
        print(f"You have {health} lives and have already tried these letters: {' '.join(guessedLetters)}")
        
        #muestra el estado de la palabra
        wordList = [letter if letter in guessedLetters else "-" for letter in word]
        print(visualHealth[health])
        print(f"Word: {' '.join(wordList)}")
        
        userGuess = input("Guess a letter: ").upper()
        
        if userGuess in abc - guessedLetters:
            guessedLetters.add(userGuess)
            if userGuess in missingLetters:
                missingLetters.remove(userGuess)
                print('')
            else:
                health -= 1
                print(f"{userGuess} is not in this word")
        elif userGuess in guessedLetters:
            print("\nYou already guessed that letter. Choose another one!!")
        else:
            
            print("\nInvalid character :]")
    if health == 0:
        print(visualHealth[health])
        print(f"HANGED!! \nYou lost. The word was: {word}.")
    else:
        print(f"you win :(")

hangedMan()
    
    