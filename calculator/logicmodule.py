import functions

def checkOp(op, a, b):
    op = op.lower()
    
    if op == "add":
        return functions.add(a, b)
    elif op == "sub":
        return functions.sub(a, b)
    elif op == "mult":
        return functions.mult(a, b)
    elif op == "div":
        return functions.div(a, b)
    else:
        return "Invalid operation"
