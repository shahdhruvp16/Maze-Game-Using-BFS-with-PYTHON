from pyamaze import maze, agent, COLOR, textLabel
import random

def BFS(m):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                
                if childCell in explored:
                    continue
                
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
    
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    
    return fwdPath

if __name__ == '__main__':
    # Randomize the size of the maze and loop percentage for variability
    rows = random.randint(5, 10)
    cols = random.randint(5, 10)
    loopPercent = random.randint(20, 100)

    # Create the maze with the randomized parameters
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=loopPercent)

    # Run the BFS algorithm to solve the maze
    path = BFS(m)

    # Display the agent's path in the maze
    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path})

    # Display the length of the shortest path
    length_label = textLabel(m, 'Length of Shortest Path', len(path) + 1)

    # Display the number of blocks covered in the shortest path
    blocks_label = textLabel(m, 'Blocks Covered in Shortest Path', len(path) + 1)

    # Run the maze visualization
    m.run()
