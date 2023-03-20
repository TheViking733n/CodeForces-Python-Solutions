# All subsequences of array using power set

# array = "Hello"
array = [1, 2, 3, 4, 5]

for i in range(1<<len(array)):
    # subseq = ""   # If array is string
    subseq = []     # If array is list; if array is string, it generates list of char
    for j in range(len(array)):
        if (i & (1<<j)) != 0:
            # subseq += array[j]     # If array is string
            subseq.append(array[j])  # If array is list

    print(subseq)
