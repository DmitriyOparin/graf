graph ={'0': ['1', '4'],
        '1': ['2'],
        '2': ['3','5'],
        '3': ['6'],
        '4': ['8'],
        '5': ['6','8'],
        '6': ['3'],
        '7': [''],
        '8': ['1','4','7'],
        '9': ['5','6'],
        '10': ['9'],
        '11': [''],
        '12': ['8']}
    
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = all(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
  
x = (input("Введите первую вeршину: "))
tuple(x)

y = (input("Введите вторую вершину: "))
tuple(y)

a = find_path(graph, x, y)

if a == []:
    print('Из вершины', x, 'в вершину', y, 'нет пути')
else:
    print('Все возможные пути из вершины', x, 'в вершину', y, ':', a)


