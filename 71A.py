"""
Way Too Long Words

Sometimes some words like "localization" or "internationalization"
are so long that writing them many times in one text is quite tiresome.
"""

n = int(input(""))
for i in range(n):
    word = input("")
    if len(word)>10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)