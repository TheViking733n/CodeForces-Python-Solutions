import sys
input = sys.stdin.readline

def main():
    
    tt = 1
    
    tt = int(input())
    
    for _ in range(tt):
        n = int(input())
        ans = 0
        arr = list(map(int, input().split()))
        summation = 0
        sig = []
        
        for i in range(n):
            if arr[i] == 0:
                sig.append(8)
            elif arr[i] < 0:
                sig.append(1)
            else:
                sig.append(0)
            summation += abs(arr[i])
        
        up = False
        for i in range(n):
            if sig[i] == 8:
                continue
            elif not up and sig[i] == 1:
                up = True
            elif up and sig[i] == 0:
                ans += 1
                up = False
        
        if up:
            ans += 1
        
        print(summation, ans)
        


if __name__ == "__main__":
    main()
