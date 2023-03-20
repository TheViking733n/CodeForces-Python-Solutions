from itertools import permutations
from re import sub


def contains_palin(b_str):
    for i in range(len(b_str)-1):
        for j in range(i+1, len(b_str)):
            sub_str = b_str[i:j+1]
            # print(sub_str)
            if (sub_str==sub_str[::-1]):
                return True
    
    return False




def generate(n):
    for num in range(n):
        b = bin(num)[2:]
        if (not contains_palin(b)):
            print(b)



generate(200)
