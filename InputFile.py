from Path import Path

# It will also generate the list of Nodes

# Summary: This class will contain the file and read mode.
# Attributes:
#   * fileString - string, file to access
#        ^Default to given input file
#   * mode - string, value of file action
#        ^Default to read mode
class InputFile:
    def __init__(self, newFile = "input1.txt", newMode = "r"):
        self.fileString = newFile
        self.mode = newMode

    # Summary: generates paths from input file
    # Params:
    #   * self - this class (InputFile)
    # Returns: List of Path class
    def getPaths(self):
        Paths = [] 
        try:
            with open(self.fileString, self.mode) as fileHandler: # open file on a specific mode
                for text in fileHandler: # read each line from file
                    line = text.split() # grab data
                    if(line[0] == "END"): # end of file
                        break
                    Paths.append(Path(line[0], line[1], line[2]))
            return Paths
        except:
            print("An Error occured with opening the file, check spelling and if file exists")
            quit()
        
