import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
        
    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
        
        if len(guess) != CODE_LENGTH:
            print("You must guess 4 colors")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
            else:
                break
            
        return guess 


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    
    for i, color in enumerate(real_code):
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    
    for i, (guess_color, real_color) in enumerate(zip(guess, real_code)):
        if guess_color == real_color:
            correct_pos += 1
        elif guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
            
    return correct_pos, incorrect_pos



def game():
    print(f'Welcome to mastermind, you have {TRIES} to guess the code...')
    print(f'The valid colors are: {COLORS}')
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f'You guessed the code in {attempts} tries!')
            break
        
        print(f'Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}')
        
    else:
        print('You ran out of tries')
        
        
if __name__ == "__main__":
    game()