def encoder(password):
    encodedPW = ''
    print("Your password has been encoded and stored!")
    for i in range(len(password)):
        encodedPW += str((int(password[i]) + 3)%10)
    return encodedPW
