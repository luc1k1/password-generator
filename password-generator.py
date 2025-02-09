import random
import string


def random_password(length: int) -> str: #Generating password
    digit = string.punctuation + string.ascii_letters + string.digits #adding symbols for our future pass
    return ''.join(random.choice(digit) for _ in range(length)) #Return final password

while True: #Simple try/except
    try:
        your_length = int(input("Write number of symbols: "))
        if your_length <= 0: #Check for 0 symbols
            print("Please,write number greater than 0")
            continue
        break
    except ValueError as err:
        print(err)

print("Your password is: " , random_password(your_length))
