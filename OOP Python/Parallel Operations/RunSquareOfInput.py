def interact():
    print('Please Enter in a number to be squared\n')
    while True:
        try:
            reply = input('#Number: ')
            num = int(reply)
            print('%d Squared is %d\n' % (num, num ** 2))
        except EOFError:
            print('Goodbye')
            break


if __name__ == '__main__':
    interact()
