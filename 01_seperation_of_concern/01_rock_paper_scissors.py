import random

# My try
options = ['paper', 'scissors', 'rock']

def get_choice(items):
    for i, item in enumerate(items):
        print(f'({i+1}) {item}')
    choice = items[int(input('Enter the number of your choice: '))-1]
    return choice

def get_human_choice():
    choice = get_choice(options)
    print(f'You chose {choice}')
    return choice

def get_computer_choice():
    choice = random.choice(options)
    print(f'Computer chose {choice}')
    return choice

def decide(human_choice, computer_choice):
    human_choice_idx = options.index(human_choice)
    computer_choice_idx = options.index(computer_choice)
    if human_choice_idx == computer_choice_idx:
        print('Draw !')
    elif (len(options)-1 == human_choice_idx and computer_choice_idx == 0) or \
            (len(options)-1 == computer_choice_idx and human_choice_idx == 0):
        if human_choice_idx < computer_choice_idx:
            print(f'You Won!, {human_choice} beats {computer_choice}')
        else:
            print(f'Computer Won!, {computer_choice} beats {human_choice}')
    else:
        if human_choice_idx > computer_choice_idx:
            print(f'You Won!, {human_choice} beats {computer_choice}')
        else:
            print(f'Computer Won!, {computer_choice} beats {human_choice}')

def my_play():
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()
    decide(human_choice, computer_choice)


if __name__ == "__main__":
    while True:
        my_play()
