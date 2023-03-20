
def f(turn, score, one, zero):
    if one == 0 and zero == 0:
        return score[0]&1
    
    if one == 0:
        score[turn] += 0
        zero -= 1
        return f(1-turn, score, one, zero)
    
    if zero == 0:
        score[turn] += 1
        one -= 1
        return f(1-turn, score, one, zero)
    
    # Both move are available
    # Lets move 1
    score_copy = score[:]; one_copy = one
    score[turn] += 1; one -= 1
    winner = f(1-turn, score, one, zero)
    if winner != turn:
        # We must do some other move
        score = score_copy[:]; one = one_copy
        score[turn] += 0; zero -= 1
        winner = f(1-turn, score, one, zero)
    
    return winner
    
    


one = 3
zero = 3
score = [0, 0]
# print(f(0, score, one, zero))
print("  n   One  Zero")
# n = 10
for n in range(1, 20, 2):
    for one in range(n+1):
        zero = n-one
        # print(f'{one:^5}{zero:^5}{["Alice", "Bob"][f(0, score, one, zero)]}')
        if f(0, score, one, zero):
            print(f'{n:^5}{one:^5}{zero:^5}')
    print()