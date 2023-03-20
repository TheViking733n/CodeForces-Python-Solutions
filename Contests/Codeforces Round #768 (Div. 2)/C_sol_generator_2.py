found = False
ans = []   # To store answer as a list of pairs

def generate(arr, k):
    global found
    global ans
    
    if not found and (k<=0 or arr==[]): # base case
        if arr == [] and k==0:  
            found = True
        return
        
    # pick any two elements
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            left_arr = arr[:i] + arr[i+1:j] + arr[j+1:]
            sum = i&j
            generate(left_arr, k-sum)

            if(found):
                ans.append((arr[i], arr[j]))
                break
            
        if(found):
            break
        


# Main program

n = 8      # n must be a power of 2
k = 2


num_arr = list(range(n))
generate(num_arr, k)

print(ans)
                     
