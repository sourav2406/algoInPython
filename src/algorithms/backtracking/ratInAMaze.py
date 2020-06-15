#python3 programe for solving rat in a maze problem using backtraking

N = 4

def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end='')
        print("")

def isSafe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    return False

def solveMaze(maze):
    sol = [[0 for j in range(N)] for i in range(N)]

    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution does not exist!!")
        return False

    printSolution(sol)
    return True

def solveMazeUtil(maze, x, y, sol):
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y) == True:
        sol[x][y] = 1

        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True

        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True

        sol[x][y] = 0
        return False

#driver code
if __name__ == "__main__":
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1]]
    solveMaze(maze)