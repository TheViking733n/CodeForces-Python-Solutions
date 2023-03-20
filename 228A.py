"""
Is your horseshoe on the other hoof?

Valera the Horse is going to the party with friends.
He has been following the fashion trends for a while,
and he knows that it is very popular to wear all horseshoes of different color.
Valera has got four horseshoes left from the last year, but maybe some of them have the same color.
In this case he needs to go to the store and buy some few more horseshoes,
not to lose face in front of his stylish comrades.

"""

arr = input("").split(" ")

arr.sort()

c=0
for i in range(3):
    if arr[i] == arr[i+1]:
        c += 1

print(c)