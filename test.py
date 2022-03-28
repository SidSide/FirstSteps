#import re
#def is_palindrome(word):
#	forwards = ''.join(re.findall(r'[a-z]+', word.lower()))
#	backwards = forwards[::-1]
#	return forwards == backwards
#what = input("Слово: ")
#is_palindrome(what)

def is_palindrome(string):
    reversed_string = ""
    # Removing all the spaces
    s = string.replace(" ","")
    # making the whole string in lowercase characters 
    s = s.lower()
    for i in range(len(s), 0, -1):
        if s[i-1] >= 'a' and s[i-1] <= 'z':
            reversed_string += s[i - 1]
    if s == reversed_string:
        print("Palindrome")
    else:
        print("Not a palindrome")
        

if __name__ == '__main__':
    is_palindrome("Too hot to hoot")
    is_palindrome("Python")