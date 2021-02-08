import random

print('=======================')
print('**  Guessing Game  **')
print('=======================')
random_number=random.randint(1,10)
guess_number=int(input('please enter the guess number:'))
count=1
while random_number!=guess_number:
    if count<3:
        guess_number = int(input('please enter the guess number:'))
        count=count+1
    else:
        print('Uffs ! sorry ..you have finish your limit')
        break
else:
    print('ooh Congratulation! u guess the right number')









