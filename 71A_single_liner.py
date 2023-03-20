print(*[(lambda w:((w[0]+str(len(w)-2)+w[-1]) if (len(w)>10) else w))(input("")) for i in range(int(input("")))],sep="\n")



"""
n = int(input(""))
for i in range(n):
    word = input("")
    if len(word)>10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)


def shorten(word):
    return (word[0] + str(len(word)-2) + word[-1]) if (len(word)>10) else word

shorten = (lambda w:((w[0]+str(len(w)-2)+w[-1]) if (len(w)>10) else w))

"""