def dfs(data,start,visited=set()):
    
    if start not in visited :
        print(start,end=" ")
    visited.add(start)

    for i in data[start]-visited:
        dfs(data,i,visited)
    return


if __name__ == '__main__':

    data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
        }

    dfs(data, 'A')