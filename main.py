from random import randint


def get_word():
    with open("english-nouns.txt", "r", encoding="utf-8") as file:
        words = file.read().split("\n")
        random_number = randint(0, len(words) - 1)
        word = words[random_number]
        return word


def draw_hangman(mistakes):
    if mistakes == 0:
        print('''
        _________________
                |
                
                
        _________________            
        ''')
    if mistakes == 1:
        print('''
        _________________
                |
                0
                

        _________________            
        ''')
    if mistakes == 2:
        print('''
        _________________
                |
                0
                |

        _________________            
        ''')
    if mistakes == 3:
        print(r'''
        _________________
                |
                0
               \|

        _________________            
        ''')
    if mistakes == 4:
        print(r'''
        _________________
                |
                0
               \|/

        _________________            
        ''')
    if mistakes == 5:
        print(r'''
        _________________
                |
                0
               \|/
               /
        _________________            
        ''')
    if mistakes == 6:
        print(r'''
        _________________ 
                |
                0
               \|/
               / \   
        _________________            
        ''')


def user_input_validation(user_input):
    if len(user_input) > 1:
        print("I can write only a char!!!")
        return True
    elif user_input.isupper():
        print("You can write only in lowercase!!!")
        return True
    elif user_input.isdigit():
        print("You can't write integer!!!")
        return True
    elif not user_input.isascii():
        print("You can use only latin letters!!!")
        return True
    elif not user_input.isalpha():
        print("You can use only letters!!!")
        return True


def start_game():
    word = get_word()
    guessed_letters = ["_"] * len(word)
    mistakes = 0
    while mistakes < 6:
        user_input = input("Type a letter: ")
        if user_input_validation(user_input):
            continue
        if user_input in word:
            for index in range(0, len(word)):
                if user_input == word[index]:
                    guessed_letters[index] = user_input
            draw_hangman(mistakes)
            print(guessed_letters)
            if ''.join(guessed_letters) == word:
                return print("You won!!!")
        else:
            mistakes += 1
            draw_hangman(mistakes)
            print(guessed_letters)
            if mistakes == 6:
                return print("You lose!!!")


def main():
    while True:
        print("HANGMAN" + "\n" + ("_" * 30))
        user_input = input("Enter 1 to start, 0 to end the game: ")
        if user_input == "1":
            start_game()
        elif user_input == "0":
            break
        else:
            print("Введены неверные данные")


if __name__ == "__main__":
    main()
