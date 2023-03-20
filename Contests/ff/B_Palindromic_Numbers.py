TestCases = int(input())
for _ in range(TestCases):

    length = int(input())
    num = input()
    
    # Check whether first digit is 9 or not
    if num[0] == '9':
        one_one_one = '1' * (length+1)
        print(int(one_one_one) - int(num))

    else:
        nine_nine_nine = '9' * length
        print(int(nine_nine_nine) - int(num))
