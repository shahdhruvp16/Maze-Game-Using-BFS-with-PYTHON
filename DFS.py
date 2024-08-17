from pyamaze import maze, agent, textLabel, COLOR
from collections import deque

def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    
    stack = []
    stack.append(start)
    dfsPath = {}
    explored = [start]
    dSearch = []

    while len(stack) > 0:
        currCell = stack.pop()
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                stack.append(childCell)
                explored.append(childCell)
                dfsPath[childCell] = currCell
                dSearch.append(childCell)
    
    fwdPath = {}
    cell = m._goal
    while cell != (m.rows, m.cols):
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    shortest_path_length = len(fwdPath) + 1
    covered_blocks = len(dSearch)
    
    return dSearch, dfsPath, fwdPath, shortest_path_length, covered_blocks

if __name__ == '__main__':
    m = maze(12, 10)
    m.CreateMaze(loopPercent=10, theme='light')
    dSearch, dfsPath, fwdPath, shortest_path_length, covered_blocks = DFS(m)
    
    a = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=True)
    b = agent(m, footprints=True, color=COLOR.red, shape='square', filled=False)
    c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square', filled=True, goal=(m.rows, m.cols))
    
    m.tracePath({a: dSearch}, delay=100)
    m.tracePath({c: dfsPath}, delay=100)
    m.tracePath({b: fwdPath}, delay=100)

    length_label = textLabel(m, 'Length of Shortest Path', shortest_path_length)
    blocks_label = textLabel(m, 'Covered Blocks', covered_blocks)

    m.run()
