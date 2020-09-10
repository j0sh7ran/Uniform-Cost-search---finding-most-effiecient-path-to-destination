# Summary: this class holds each path from the input file list
# Attributes:
#   * Nodes - array of strings, values from line of input file for location
#        ^Default to empty
#   * Distance - string, value from line of input file for 
#        ^Default to empty
class Path:
    def __init__(self, point1 = "", point2 = "", distance = ""):
        if(point1 and point2 and distance):
            self.Nodes = [point1, point2] 
            self.Distance = distance


# Summary: this class holds a node either expanded, or added to the fringe
# Attributes:
#   * CurrentCity - string, value from line of input file for 
#   * ParentCity - string, city name of previous node
#        ^Default to empty
#   * ParentNode - NodeState, Parent of this node. Used for traversing 
#        ^Default to empty
#   * Cost - number, cost of traversal 
#        ^Default to 0
#   * Depth - number, how deep we traveled . used for debugging
#        ^Default to 0
#   * TotalCost - number, cost of all traversals to this node
#        ^Default to 0
class NodeState:
    def __init__(self, currentCity, parentCity = None, parentNode = None, cost = 0.0, depth = 0, totalCost = 0.0):
        self.CurrentCity = currentCity
        self.ParentCity = parentCity
        self.CurrentCity = currentCity
        self.ParentNode = parentNode
        self.Cost = cost
        self.Depth = depth
        self.TotalCost = totalCost
