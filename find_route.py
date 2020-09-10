# Joshua Tran
# 1001296598
# CSE-4308-001
# Assignment 1

# Goal: Implement a graph search with uniformed cost search to solve a 
#       Uninformed path finding problem.
#### MAIN PROGRAM ####
import sys
from Path import Path, NodeState
from InputFile import InputFile
from Routines import UniformedCostSearch


# check for command line arguments
if(len(sys.argv) == 4):
    operation = "find_route"
    inputFile = sys.argv[1]
    orginCity = sys.argv[2]
    destinationCity = sys.argv[3]
# if no commandline arguments check user input
elif(len(sys.argv) == 1):
    userInput = input().split()
    if(len(userInput) != 4):
        print("ERROR: user input arguments should be formatted as such:\n find_route [input file] [origin city] [destination city]")
        quit()
    operation = userInput[0]
    inputFile = userInput[1]
    orginCity = userInput[2]
    destinationCity = userInput[3]
# exit with input error
else:
    print("ERROR: command line arguments should be formatted as such:\npython find_route.py [input file] [origin city] [destination city]")
    quit()

# check for valid operation
if(operation == "find_route"):
    # Construct and parse input file for paths in format:
    # [Location1] [Location2] [Distance]
    File = InputFile(inputFile)
    paths = File.getPaths()

    # Perform the Uniformed Cost Search (Prints output on completion)
    UniformedCostSearch(orginCity, destinationCity, paths)
# exit with input error
else:
    print("ERROR: invalid operation: " + operation)




