def palindrome(s):
    # Create a dict to check how many times any char appear 
    charCount = {}
    
    # Loop each character in the string and count its presence
    for i in s:
        if i in charCount:
            charCount[i] += 1
        else:
            charCount[i] = 1
    # initialize the length to save the palindrome length
    pdLength = 0
    isOdd = False  # Flag
    
    # Go through the character counts to calculate how much we can add to the palindrome

    for j in charCount.values():
        if j % 2 == 0:
            pdLength += j
        else:
            isOdd = True
            pdLength += j - 1
    
    # If there's any odd count, we can place exactly one odd character in the center
    
    if isOdd:
        
        pdLength += 1
    
    print(pdLength)


s = "abccccdd"
palindrome(s)

