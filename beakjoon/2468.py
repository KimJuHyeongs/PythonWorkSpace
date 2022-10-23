def checkWater(height) :
    visited, tmp_result = [[False]*n for _ in range(n)], 0

    for r in range(n) :
        for c in range(n) :
            stack = list()

            if not visited[r][c] and matrix[r][c] > height :
                visited[r][c] = True
                tmp_result += 1
                stack.append([r,c])

            while stack :
                tx, ty = stack.pop()

                for idx in range(4):
                    x, y = tx + px[idx], ty + py[idx]
                    
                    if (0 <= x < n) and (0 <= y < n) and (not visited[x][y]) and (matrix[x][y] > height) :
                        visited[x][y] = True
                        stack.append([x,y])
        
    return tmp_result

if __name__ == '__main__' :
    n = int(input())
    matrix = list()
    px, py = [1, -1, 0, 0], [0, 0, 1, -1]

    for _ in range(n) :
        matrix.append(list(map(int,input().split())))
    
    min_water, max_water, result = min(map(min,matrix)), max(map(max,matrix)), 1
    
    for idx in range(min_water,max_water) :
        result = max(result, checkWater(idx))
    
    
    print(result)