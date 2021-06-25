def checkIfPalindrome(s):
    return s == s[::-1]


while True:
    userInput = str(input("Enter a string or number: "))
    userInput = userInput.lower()
    inputStatus = checkIfPalindrome(userInput)
    
    if inputStatus == True:
        inputStatus = " is a Palindrome"
    elif inputStatus == False:
        inputStatus = " isn't a Palindrome"
    
    print(str(userInput) + inputStatus)
