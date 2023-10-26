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
if __name__ == "__main__":
    main()
