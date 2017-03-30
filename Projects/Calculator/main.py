import math_functions
import sys

quit_calls = ('q', 'quit')
help_calls = ('h', 'help')
history = []


def print_menu():
    _help_text = "\n-----------\nPlease Add, Subtract, "\
        "Multiply, or Divide two numbers.\n\n"\
        "'f' or 'float' to change the length of the float "\
        "dividend acuracy\n\n"\
        "'h' or 'help' for this menu.\n\n"\
        "'q' or 'quit' to exit this program.\n-----------\n"
    print(_help_text)


if __name__ == "__main__":
    print_menu()
    while True:

        user_input = input("Calculate: ")

        if user_input.lower() in quit_calls:
            print("\nExiting main loop of the program.\n")
            sys.exit(0)
        elif user_input.lower() in help_calls:
            user_input
            print_menu()
        else:
            answer = math_functions.parse_input(user_input)
            hist_tuple = (answer, user_input)
            history.append(hist_tuple)
            print("Answer: %.3f" % answer)
            print()
            print(history)
