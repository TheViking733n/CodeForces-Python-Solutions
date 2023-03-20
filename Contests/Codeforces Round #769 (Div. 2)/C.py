answers = []



def solve_bruteforce(a, b, cnt):
    global answers
    global max_ans
    
    if (a==b):
        answers.append(cnt)
        return
    if(cnt+1 > max_ans):
        return
    
    solve_bruteforce(a+1, b, cnt+1)
    solve_bruteforce(a, b+1, cnt+1)
    solve_bruteforce(a|b, b, cnt+1)


def solve(a, b, cnt=0):
    if (a==b):
        return cnt
    
    # if (cnt+1 > max_ans):
    #     return cnt
    
    if (b>a):
        if (a|b)-b < b-a:
            return solve(a|b, b, cnt+1)
        else:
            return solve(a+1, b, cnt+1)

    else:
        return cnt + a-b


a=1
b=3

max_ans = b-a


min_ans = max_ans
for b1 in range(b, a|b+1):
    ans = solve(a, b1) + b1-b
    if (ans<min_ans):
        min_ans = ans

print(min_ans)

# solve_bruteforce(a, b, 0)
# print(min(answers))