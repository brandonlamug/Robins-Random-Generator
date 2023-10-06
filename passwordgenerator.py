# importing modules
import random
import string

answer = input("Holy cryptography Batman! You forgot your password already? Need me to make one for you? (Y/N)")

if answer.lower() in ["y", "yes"]:
    length = 9

    # strings
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    pass_options = letters + digits + special_chars

    password = random.sample(pass_options, length)
    password = ''.join(password)

    print("Gee Willickers Batman, I think your new password should be:", password)

elif answer.lower() in ["n", "no"]:
    response = input("Are you sure you're not the Riddler? (Y/N)")
    if response.lower() in ["y", "yes"]:
        print("You dastardly villain, stay away from our Batcave!")
    elif response.lower() in ["n", "no"]:
        print("Well, that's a relief.")
    else:
        while True:
            print("Holy Hearing Loss, I didn't catch that. Could you repeat yourself, boss?")
            response = input("Are you sure you're not the Riddler? (Y/N)")
            if response.lower() in ["y", "yes"]:
                print("You dastardly villain, stay away from our Batcave!")
                break
            elif response.lower() in ["n", "no"]:
                print("Well, that's a relief.")
                break

else:
    while True:
        repeat = input("Holy Hearing Loss, I didn't catch that. Could you repeat yourself, boss?(Y/N)")
        if repeat.lower() in ["y", "yes"]:
            length = 9

            # strings
            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation
            pass_options = letters + digits + special_chars

            password = random.sample(pass_options, length)
            password = ''.join(password)

            print("Gee Willickers Batman, I think your new password should be:", password)
            break

        elif repeat.lower() in ["n", "no"]:
            response = input("Are you sure you're not the Riddler? (Y/N)")
            if response.lower() in ["y", "yes"]:
                print("You dastardly villain, stay away from our Batcave!")
                break
            elif response.lower() in ["n", "no"]:
                print("Well, that's a relief.")
                break
            else:
                while True:
                    print("Holy Hearing Loss, I didn't catch that. Could you repeat yourself, boss?")
                    response = input("Are you sure you're not the Riddler? (Y/N)")
                    if response.lower() in ["y", "yes"]:
                        print("You dastardly villain, stay away from our Batcave!")
                    elif response.lower() in ["n", "no"]:
                        print("Well, that's a relief.")
                    break











