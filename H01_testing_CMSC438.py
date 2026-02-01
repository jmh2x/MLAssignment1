import numpy as np

# your implementation of dotting() here
        

# code inside the "if" will be executed if ran as "python filename.py" 
# but will not be executed if this file is loaded by another python script (e.g. gradescope) using "import"
if __name__ == "__main__":
    
    # example 1

    test_f1 =( ('X', 2.0), ('C', 1.0), ('+', 0, 1), ('*', 0, 2), ('S', 3) )
    
    print(f"Example 1: f = {test_f1}")

    x,y,dy = dotting(test_f1)
    print(f"dotting(f): x = {x}, y = {y}, dotted_y = {dy}")
    
    
    # example 2

    test_f2 =( ('X', 2.0), )
    
    print("\n\n")
    print(f"Example 2: f = {test_f2}")

    x,y,dy = dotting(test_f2)
    print(f"dotting(f): x = {x}, y = {y}, dotted_y = {dy}")
    
    


'''

The code above should print:
    
Example 1: f = (('X', 2.0), ('C', 1.0), ('+', 0, 1), ('*', 0, 2), ('S', 3))
dotting(f): x = 2.0, y = 36.0, dotted_y = 60.0



Example 2: f = (('X', 2.0),)
dotting(f): x = 2.0, y = 2.0, dotted_y = 1.0

'''
