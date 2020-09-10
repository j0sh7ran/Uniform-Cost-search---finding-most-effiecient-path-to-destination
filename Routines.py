from Path import Path, NodeState

# Summary: Output for success
# Params:
#   * node - NodeState class, used to traverse up from finish to start
#   * nodesExpanded - number, count of nodes expanded
#   * nodesGenerated - number, count of nodes generated
# Returns: Nothing, but on completion prints Success output
def PrintSuccess(node, nodesExpanded, nodesGenerated):
    print("nodes expanded: %d"%(nodesExpanded))
    print("nodes generated: %d"%(nodesGenerated))
    print("total distance: %.1f km"%(node.TotalCost))
    print("route:")
    routeString = ""
    while node.ParentNode != None:
        routeString = "%s to %s, %.1f km\n"%(node.ParentCity, node.CurrentCity, node.Cost) + routeString
        node = node.ParentNode
    print(routeString)


# Summary: Output for failure
# Params:
#   * nodesExpanded - number, count of nodes expanded
#   * nodesGenerated - number, count of nodes generated
# Returns: Nothing, but on completion prints Failure output
def PrintFailure(nodesExpanded, nodesGenerated):
    print("nodes expanded: %d"%(nodesExpanded))
    print("nodes generated: %d"%(nodesGenerated))
    print("total distance: infinity")
    print("route:")
    print("none")


# Summary: Generates Nodes when expanding
# Params:
#   * target - NodeState class, particularly the one we are expanding
#   * paths - List of Path class
# Returns: GeneratedNodes - List of NodeState class, the children of target
def GenerateNodes(target, paths):
    GeneratedNodes = []
    for path in paths:
        if (target.CurrentCity == path.Nodes[0]):# if the target city exists, 
            GeneratedNodes.append(NodeState(path.Nodes[1], path.Nodes[0], target, int(path.Distance), target.Depth + 1, target.TotalCost + int(path.Distance))) # add the other city from the line as a node
        elif(target.CurrentCity == path.Nodes[1]):# if the target city exists, 
            GeneratedNodes.append(NodeState(path.Nodes[0], path.Nodes[1], target, int(path.Distance), target.Depth + 1, target.TotalCost + int(path.Distance))) # add the other city from the line as a node
    return GeneratedNodes


# Summary: Preforms the Uniformed Cost Search Algorithm
# Params:
#   * start - string, starting location
#   * end - string, ending location
#   * paths - List of Path class
# Returns: Nothing, but on completion prints Success or Failure outputs
def UniformedCostSearch(start, end, paths):
    closed = [] # List of strings, visted/closed list 
    fringe = [ NodeState(start) ] # List of NodeStates, Priority Que. Ordered on total cost.
    expandedNodes = 0 # number, we just started with the start node above, so we start at 1
    nodesGenerated = 1 # number, we just started with the start node above, so we start at 1
    
    while(len(fringe) > 0 and fringe[0].CurrentCity != end):# loop do, while fringe is not empty and the top of the fringe is not the end
        target = fringe.pop(0) # NodeState class, 
        expandedNodes += 1
        if(target.CurrentCity not in closed):
            closed.append(target.CurrentCity) # add to visted/closed list
            newNodes = GenerateNodes(target, paths) # List of NodeState, new nodes generated from target
            fringe += newNodes # add new nodes to fringe
            nodesGenerated += len(newNodes) # add to number generated statistic
            fringe.sort(key=lambda node: node.TotalCost) # sort and order by totalCost

    if len(fringe) > 0 and fringe[0].CurrentCity == end: # Success, Goal test
        PrintSuccess(fringe[0], expandedNodes + 1, nodesGenerated)
    else: # Fail
        PrintFailure(expandedNodes, nodesGenerated)