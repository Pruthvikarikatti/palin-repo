string = "madam"
if string.lower() == string[::-1].lower():
    print(f"'{string}' Is a Palindrome.")
else:
    print(f"'{string}' is not a palindrome")