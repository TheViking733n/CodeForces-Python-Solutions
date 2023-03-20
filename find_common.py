"""
AACTTGAC is the lengthiest alphabet sequence given the following two strings.


Alpha='AAATTTAACTTGACGGTTACTTGCCCC'

Beta='TAGCTGGAACTTGACCCCGGGAAATAGAGGAACCTT'

"""


alpha = input("Enter the DNA Sequence for Alpha: ")
beta = input("Enter the DNA Sequence for Beta: ")

l1, l2, max_len = len(alpha), len(beta), 0
sequence = ""
for i in range(l1):
    for j in range(l2):
        i1, j1, common_len = i, j, 0
        while i1<l1 and j1<l2:
            if alpha[i1] == beta[j1]:
                common_len += 1
                i1 += 1
                j1 += 1
            else:
                break
        if common_len > max_len:
            max_len = common_len
            sequence = alpha[i:i1]

print(sequence)
    

