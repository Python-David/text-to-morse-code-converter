# A text-based Python program to convert Strings into Morse Code.

from morse_code_rules import MorseCodeRules
from morse_code_brain import MorseCodeBrain

rules = MorseCodeRules()
rules_dict = rules.morse_code_rules
brain = MorseCodeBrain(rules_dict)
still_translating = True

print("Welcome to the ENGLISH - MORSE CODE TRANSLATOR")
while still_translating:
    user_input = input("Enter your text: ")

    if brain.validate(user_input):
        print(f"({','.join(brain.validate(user_input))}) not allowed. Only use (a-z), (0-9) and space.")
    else:
        print(f"Here is your morse code: {brain.translate(user_input)}")

        is_yes = True

        while is_yes:
            user_still_trans = input("Will you like to keep translating? y/n?: ").lower()
            if user_still_trans == "n":
                is_yes = False
                still_translating = False
            elif user_still_trans == "y":
                is_yes = False
                still_translating = True
            else:
                is_yes = True
                print("Please select ONLY yes or no (y/n).")