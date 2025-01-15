## 📝 README - Palindrome Length Calculation

### 🔍 Overview:
This lab determines the **maximum length** of a palindrome that can be formed by rearranging the characters in a given string. A palindrome reads the same forwards and backwards. We can create one by using pairs of characters, and placing one odd character in the center.

### 🔧 Approach:
1. **Character Frequency Count**: Count the occurrences of each character in the string using a dictionary.
2. **Form Palindrome**: 
   - Use characters with even frequencies completely.
   - For characters with odd frequencies, use all but one character.
   - If any odd frequency exists, add one to the final length (for the center of the palindrome).
3. **Output**: The final length of the longest palindrome.

### 🖥️ Code:
```python
def palindrome(s):
    # Count character frequencies
    charCount = {}
    for i in s:
        charCount[i] = charCount.get(i, 0) + 1

    # Calculate the maximum palindrome length
    pdLength = 0
    isOdd = False
    for count in charCount.values():
        if count % 2 == 0:
            pdLength += count  # Add even counts
        else:
            isOdd = True
            pdLength += count - 1  # Add the even part of odd counts

    if isOdd: 
        pdLength += 1  # Add one for the center if there's an odd count

    print(pdLength)

# Test case
palindrome("abccccdd")
```

### 🛠️ Example:
For the input `s = "abccccdd"`, the function returns `7`, as the longest palindrome we can form has a length of 7.

### 🧩 Output:
```bash
7
```

### 🎓 Author:
Roll No: **23-AI-13**

### 🚀 Key Concepts:
- **Palindrome**: A word that reads the same backward as forward.
- **Frequency Count**: Useful in string manipulation problems.

### 📌 Summary:
This lab demonstrates an efficient way to compute the longest palindrome length using character frequencies. Great for applications in **text processing** and **string manipulations**. 😊
