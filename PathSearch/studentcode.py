#using A*
import math

class node():
    def __init__(self, state, path = [], cost = 0, parent = None):
        self.state = state
        self.path = path
        self.cost = cost
        self.parent = parent

def dist(M, a, b):
    x0, y0 = M.intersections[a][0], M.intersections[a][1]
    x1, y1 = M.intersections[b][0], M.intersections[b][1]
    return math.sqrt(pow(x0 - x1, 2) + pow(y0 - y1, 2))

def find_shortest(fts, all_nodes):
    exam_cost = 10000
    exam = 0
    for ft in fts:
        if all_nodes[ft].cost < exam_cost:
            exam_cost = all_nodes[ft].cost
            exam = ft
    return exam
        
def shortest_path(M,start,goal):
    print("shortest path called")
    
    
    explored = set()
    frontiers = set()
    frontiers.add(start)
    #dict store all nodes
    all_nodes = {}
    all_nodes[start] = node(start,[start])
    
    #find the closet one
    expand = find_shortest(frontiers, all_nodes)
    while expand != goal:  
        #update frontiers
        for neighbor in M.roads[expand]:
            #if not in e, add to f
            if neighbor in explored:
                pass
            elif neighbor not in frontiers:
                #add to frontiers, add to dict
                frontiers.add(neighbor)
                #print('expand node = ' + str(all_nodes[expand].state) + ' path = ' + str(all_nodes[expand].path))
                #print('neighbor = ' + str(neighbor))
                all_nodes[neighbor] = node(state = neighbor, path = all_nodes[expand].path + [neighbor], cost = all_nodes[expand].cost - dist(M, expand, goal) + dist(M, neighbor, goal) + dist(M, expand, neighbor), parent = all_nodes[expand])
            #update if necessary
                #print('neighbor path = ' + str(all_nodes[neighbor].path))
            else:
                new_cost = all_nodes[expand].cost - dist(M, expand, goal) + dist(M, neighbor, goal) + dist(M, expand, neighbor)
                if new_cost < all_nodes[neighbor].cost:
                    all_nodes[neighbor].path = all_nodes[expand].path + [neighbor]
                    all_nodes[neighbor].cost = new_cost
                    all_nodes[neighbor].parent = all_nodes[expand]
        frontiers.remove(expand)
        #update explored
        explored.add(expand)
        # print('explored = ' + str(explored) + 'frontiers = ' + str(frontiers))
        expand = find_shortest(frontiers, all_nodes)
        # print('expand' + str(expand))
        #print(all_nodes)
    return all_nodes[expand].path
