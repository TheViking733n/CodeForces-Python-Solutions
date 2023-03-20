def mat_spiral(n):
    visited = [[False]*(n+2) for i in range(n+2)]
    visited[0], visited[-1] = [True]*(n+2), [True]*(n+2)
    for i in range(1,n+1):
        visited[i][0], visited[i][-1] = True, True

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    traversal = []
    x, y, k = 1, 1, 0
    for _ in range(n*n):
        visited[x][y] = True
        traversal.append((x, y))
        if not visited[x+dx[k]][y+dy[k]]:
            x += dx[k]
            y += dy[k]
        else:
            x += dx[k]
            y += dy[k]
            k = (k+1)%4
    
    return traversal

if __name__ == "__main__":
    print(mat_spiral(3))
