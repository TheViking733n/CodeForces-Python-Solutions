subsequences = []
def find_subseq(i, sum, subseq, L):
    if sum == 0:
        subsequences.append(subseq[::])
        return
    if i >= len(L) or sum < 0:
        return
    # Take ith element of L
    subseq.append(L[i])
    find_subseq(i+1, sum-L[i], subseq, L)
    # Don't take ith element of L
    subseq.pop()
    find_subseq(i+1, sum, subseq, L)


if __name__ == '__main__':
    L = [int(i) for i in input("Enter space seperated list of numbers:\n").split()]
    k = int(input("Enter required sum: "))
    L.sort()
    find_subseq(0, k, [], L)
    print(subsequences)
