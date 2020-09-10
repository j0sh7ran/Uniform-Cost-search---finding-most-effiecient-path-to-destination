Student Info:
    Name: Joshua Tran
    ID: 1001296598
    Language: Python 3

Base Info:
    * you can run this program by either using User Input, or Command Line. 
    * The program will then find the optimal path from a origin city to a destination city

How to run:
    * Pre-requisites:
        ~ make sure python 3 is installed
        ~ make sure that the files are in the same directory:
            = find_route.py
            = Path.py
            = InputFile.py
            = Routines.py
            = [YOUR INPUT FILE] (input1.txt is already included)

    * Option 1 - Command line, run and execute the program by typing:
        ~ python ./find_route.py [input file] [origin city] [destination city]
      if there are no errors in input, the program should run to completion

    * Option 2 - User input, run the program by typing:
        ~ python ./find_route.py
      then, enter this as the user input:
        ~ find_route [input file] [origin city] [destination city]
      if there are no errors in input, the program should run to completion
    
    * NOTE: a picture has been made showing how to run the program should run. Option 1 is the first execution, Option 2 is the second exectution

File Structure summary:
    * find_route.py:
        ~ this is the main program. It will look at what input is given,
          then it will parse the input file for all the paths given in the file.
          then it will run the UniformedCostSearch function
    * Routines.py:
        ~ this is where the main program's routine functions are held. 
    * InputFile.py:
        ~ class that holds file info and a function to generate the data for our UniformedCostSearch
    * Path.py:
        ~ classes that hold data for finding the path from nodes.