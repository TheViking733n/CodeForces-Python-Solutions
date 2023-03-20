"""
You are given a string s consisting of lowercase Latin letters "a", "b" and "c" and question marks "?".

Let the number of question marks in the string s be k. Let's replace each question mark with one of the letters "a", "b" and "c". Here we can obtain all 3k possible strings consisting only of letters "a", "b" and "c". For example, if s="ac?b?c" then we can obtain the following strings: ["acabac", "acabbc", "acabcc", "acbbac", "acbbbc", "acbbcc", "accbac", "accbbc", "accbcc"].

Your task is to count the total number of subsequences "abc" in all resulting strings. Since the answer can be very large, print it modulo 109+7.

A subsequence of the string t is such a sequence that can be derived from the string t after removing some (possibly, zero) number of letters without changing the order of remaining letters. For example, the string "baacbc" contains two subsequences "abc" — a subsequence consisting of letters at positions (2,5,6) and a subsequence consisting of letters at positions (3,5,6).

Input
The first line of the input contains one integer n (3≤n≤200000) — the length of s.

The second line of the input contains the string s of length n consisting of lowercase Latin letters "a", "b" and "c" and question marks"?".

Output
Print the total number of subsequences "abc" in all strings you can obtain if you replace all question marks with letters "a", "b" and "c", modulo 109+7.

Examples:
input
6
ac?b?c
output
24

input
7
???????
output
2835

input
9
cccbbbaaa
output
0

input
5
a???c
output
46

"""


def get_abc_seq(num):
    # Accepts an int and returns corresponding abc sequence in string

    ans = ""

    while num>0:
        rem = num%3
        ans = str(rem) + ans
        num = num//3

    ans = ans.replace("0","a")
    ans = ans.replace("1","b")
    ans = ans.replace("2","c")

    ans = "a"*(k-len(ans)) + ans

    return ans



def counter(x):
    count = 0
    a_index_arr = []
    b_index_arr = []
    c_index_arr = []

    for i in range(len(x)):
        ch = x[i]
        if ch == "a":
            a_index_arr.append(i)
        elif ch == "b":
            b_index_arr.append(i)
        elif ch == "c":
            c_index_arr.append(i)

    if a_index_arr==[] or b_index_arr==[] or c_index_arr==[]:
        return 0
    
    for i in range(len(a_index_arr)):
        a = a_index_arr[i]
        for j in range(len(b_index_arr)):
            b = b_index_arr[j]
            if b < a:
                continue
            
            # Using binary search alg to find b in c_index_arr
            
            if len(c_index_arr)==1 and b < c_index_arr[0]:
                count += 1
            
            elif c_index_arr[0] < b and b < c_index_arr[-1]:
                first = 0
                last = len(c_index_arr) - 1
                while first < last-1:
                    mid = (first + last)//2
                    if c_index_arr[mid] > b:
                        last = mid
                    else:
                        first = mid

                count+=len(c_index_arr)-last

            



    return count


##############
# _main_
##############

# Taking Input
length = int(input(""))
s = input("")

s=s.lower()

arr = s.split("?")





k = len(arr) - 1

# Creating all possibility of substrings by insterting a, b and c
# We know total no. of possibility = 3**k

total_occurances = 0

for i in range(3**k):
    word = ""
    abc_seq = get_abc_seq(i)

    # print(abc_seq)
    for j in range(len(arr)-1):
        word = word + arr[j] + abc_seq[j]
    
    word += arr[-1]

    total_occurances += counter(word)

print(total_occurances)
