def is_vowel(char):
    all_vowels='a,e,i,o,u'
    return char in all_vowels
n=input("enter a character:")
print(is_vowel(n))
