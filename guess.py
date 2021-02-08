import random

rand_num=random.randint(1,10)
guess_num=int(input('Please guess the number:'))
count=1
while rand_num !=guess_num:
    if count<3:
        guess_num = int(input('Please guess the number:'))
        count=count+1
    else:
        print(' sorry, your guess limit is over')
        break
else:
    print('your guess is right !..Congratulations')







