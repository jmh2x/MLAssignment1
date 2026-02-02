#Govan Henry    H01    CMSC438    1/30/26
import numpy as np

def dotting(f):
    var = [] #store variables
    dotted = [] #store dotted

    for instruction in f: #iterate through each instruction
        op = instruction[0] #operation type

        if op == 'X': #x
            value = instruction[1]
            var.append(value)
            dotted.append(1.0)

        
        elif op == 'C':#constant
            value = instruction[1]
            var.append(value)
            dotted.append(0.0)

        
        elif op == '+':#Add
            u, v = instruction[1], instruction[2]
            var.append(var[u] + var[v])
            dotted.append(dotted[u] + dotted[v])

        
        elif op == '-':#subtract
            u, v = instruction[1], instruction[2]
            var.append(var[u] - var[v])
            dotted.append(dotted[u] - dotted[v])

        
        elif op == '*':#multiply
            u, v = instruction[1], instruction[2]
            var.append(var[u] * var[v])
            dotted.append(dotted[u] * var[v] + var[u] * dotted[v])


        
        elif op == '/':#divide
            u, v = instruction[1], instruction[2]
            var.append(var[u] / var[v])
            dotted.append((dotted[u] * var[v] - var[u] * dotted[v]) / (var[v] ** 2))

        
        elif op == 'S':#^2
            u = instruction[1]
            var.append(var[u] ** 2)
            dotted.append(2.0 * var[u] * dotted[u])

        
        elif op == 'E':#^x
            u = instruction[1]
            var.append(np.exp(var[u]))
            dotted.append(np.exp(var[u]) * dotted[u])


        
        elif op == 'L':#log
            u = instruction[1]
            var.append(np.log(var[u]))
            dotted.append(dotted[u] / var[u])


    
    #eeturn x, y, and dotted y
    x = var[0]
    y = var[-1]
    dotted_y = dotted[-1]
    return x, y, dotted_y
