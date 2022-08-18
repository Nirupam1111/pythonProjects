import random
from art import logo

def num():
    return random.randint(0,100)

random_number=num()

def play():
    print(logo)
    print('Welcome to Guess a number game!!!')
    total_count=input('which type of game want to play? hard or easy :').lower()
    if total_count=='hard':
        count=5
    elif total_count=='easy':
        count=10
        
    print(f'you have {count} turn')

    while True:
        user_number=int(input('Guess a Number between 0 to 100 :'))
        if user_number>random_number:
            print('The number is too big')
        elif user_number<random_number:
            print('The number is too small')
        elif user_number==random_number:
            print('you guess the right number,you win!!!')
            break

        count-=1
        if count==0:
            print('you lose the game')
            break

        print(f'guess again,you have only {count} turn left.')
    
    re_play=input('want to play again yes or no? :')
    if re_play=='yes':
        play()
play()