def main():
    condition = True
    password = ''
    while condition == True:
        print('Menu')
        print('-------------')
        selection = int(input('1. Encode \n2. Decode \n3. Quit\n\nPlease Enter an option: '))
        if selection == 1:
            encoder()
        elif selection == 2:
            print('The encoded password is ',encodedPW,'and the orignal password is ',decode(encodedPW))
        elif selection ==3:
            condition = False 
def encoder():
    password = input('Please enter your password to encode:')
    encodedPW = ''
    print("Your password has been encoded and stored!")
    for i in range(len(password)):
        encodedPW += str((int(password[i]) + 3)%10)
if __name__ == "__main__":
    main()
