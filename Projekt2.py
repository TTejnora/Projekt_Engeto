import random
import time

def greeting():
    global spacer
    # just welcome speech to the player
    printing = ['Hi there!',
                "I've generated a random 4 digit number for you",
                "The number can't start with 0 and digits are unique.",
                "Let's play a bulls and cows game."]
    spacer = len(max(printing)) * '-'
    printing.insert(4, spacer)
    printing.insert(1, spacer)
    print(*printing, sep='\n')
    print(f'Enter a number: \n{spacer}')

def rnd_number(digits : int) -> list:
# generating and returning a list with len of digits,
# first number not zero and no repeating numbers
    assert digits < 10, 'This function works only for creating 1-9 digit random number without zero'
    rng = list(range(1, 10))
    number = digits * [0]
    for i in range(0, digits):
        number[i] = random.choices(rng)[0]
        rng.remove(number[i])
    print(rng, number)
    return number

def ver_input() -> int:
    # player enters the number and it is verified, output is the correct number
# only digits, no starting 0, no same digit
    print(spacer)
    while True:
        number = input('>>>')
        if number.isdigit() and len(set(list(number))) == 4 and len(number) == 4:
            break
        else:
            print('Enter unique four digit number')
    return number

def bulls_cowd(guess : int, num_to_guess : list) -> dict:
    # receives a guess and returns number of bulls and cows
    test = list()
    for j in list(str(guess)):
        test.append(int(j))
    bul_cow = {'Bulls':0,'Cows':0}
    for i in range(len(test)):
        if test[i] == num_to_guess[i]:
            bul_cow['Bulls'] += 1
        elif test[i] in num_to_guess:
            bul_cow['Cows'] += 1
    return bul_cow

def print_progress(goal: int, bull_cow : dict ) -> bool:
    #printing actual status and returning if the guessing is over
    over = False
    if bull_cow['Bulls'] == 4:
        over = True
    else :
        bull = 'bull'
        cow = 'cow'
        if bull_cow['Bulls'] > 1:
            bull = 'bulls'
        if bull_cow['Cows'] > 1:
            cow = 'cows'
        tisk = '{Bulls} {bull},{Cows} {cow}.'
        print(tisk.format(bull=bull, cow=cow, **bull_cow))
    return over

def results(guess: int, time_sec : int, tries : int):
    # load the results from the result.csv / if empty / create the file
    # calculate avg result and compare to last result
    # add the all results, including the last one in the result.csv
    pass

def main():
    #greeting and writing initial text
    greeting()
    # creating a secret number of 4 digits
    secret_num = rnd_number(4)
    tries = 0   # number of tries
    # guessing number
    while True:
        t_start = time.time()
        guess = ver_input()
        tries += 1
        if print_progress(guess,bulls_cowd(guess,secret_num)):
            print(f"Correct, you've guessed the right number in {tries} guesses.\n{spacer}")
            break
    t_result = int(time.time()-t_start)
    print(f'Your guessing time was {t_result} seconds')
    #results(secret_num,t_result,tries)

main()
