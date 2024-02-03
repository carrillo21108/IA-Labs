from implementations import Fifo,Lifo,PriorityQueue

def bfs(graph,startNode,endNode):
    toBeVisited = []
    visited = []
    queue = Fifo()
    
    toBeVisited.append(startNode)
    queue.insert(startNode)
    
    count = 0
    
    while not queue.empty():
        count+=1
        s = queue.remove_first()
        visited.append(s)
        
        if s==endNode:
            print("Iteraciones BFS: "+str(count))
            return visited
        
        for n in graph[s]:
            if n not in toBeVisited:
                toBeVisited.append(n)
                queue.insert(n)
                
    return None
                
def dfs(graph,startNode,endNode):
    toBeVisited = []
    visited = []
    stack = Lifo()
    
    toBeVisited.append(startNode)
    stack.insert(startNode)
    
    count = 0
    
    while not stack.empty():
        count+=1
        s = stack.remove_first()
        visited.append(s)
        
        if s==endNode:
            print("Iteraciones DFS: "+str(count))
            return visited
        
        for n in reversed(graph[s]):
            if n not in toBeVisited:
                toBeVisited.append(n)
                stack.insert(n)
                
    return None
                
def ucs(graph,startNode,endNode):
    visited = []
    queue = PriorityQueue()
    queue.insert((startNode,[startNode]),0)
    
    count=0
    while not queue.empty():
        count+=1
        actualCost, value = queue.remove_first()
        actualNode, actualPath = value
        
        if actualNode==endNode:
            print("Iteraciones UCS: "+str(count))
            return actualPath
        
        if actualNode not in visited:
            visited.append(actualNode)
            
            for item in graph[actualNode]:
                for neighborNode, cost in item.items():
                    newPath = actualPath+[neighborNode]
                    newCost = actualCost+cost
                    queue.insert((neighborNode,newPath),newCost)
                    
    return None

def gbfs(graph,startNode,heuristic,endNode):
    visited = []
    queue = PriorityQueue()
    queue.insert((startNode,[startNode]),heuristic)
    
    count=0
    while not queue.empty():
        count+=1
        actualNode, actualPath = queue.remove_first()[1]
        
        if actualNode==endNode:
            print("Iteraciones GBFS: "+str(count))
            return actualPath
        
        if actualNode not in visited:
            visited.append(actualNode)
            
            for item in graph[actualNode]:
                for neighborNode, heuristic in item.items():
                    newPath = actualPath+[neighborNode]
                    queue.insert((neighborNode,newPath),heuristic)
                    
    return None

def astar_s(graph,startNode,heuristic,endNode):
    visited = []
    queue = PriorityQueue()
    queue.insert((startNode,[startNode]),0+heuristic)
    accumulated = {startNode:0}
    
    count=0
    
    while not queue.empty():
        count+=1
        actualCost, value = queue.remove_first()
        actualNode, actualPath = value

        if actualNode==endNode:
            print("Iteraciones A*_S: "+str(count))
            return actualPath
        
        if actualNode not in visited:
            visited.append(actualNode)
            
            for item in graph[actualNode]:
                for neighborNode, values in item.items():
                    newPath = actualPath+[neighborNode]
                    newAccumulated = accumulated[actualNode]+values[0]
            
                    if neighborNode not in visited or newAccumulated<accumulated[neighborNode]:
                        accumulated[neighborNode] = newAccumulated
                        newCost = newAccumulated+values[1]
                        queue.insert((neighborNode,newPath),newCost)
                    
    return None