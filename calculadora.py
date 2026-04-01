def calc (p1,m1,v1,o1,p2,m2,v2):

    match m1:
        case "**":
            p1 = p1**v1
        case "\|":
            p1 = p1**0.5
        case "%":
            p1 = (p1*v1)/100

    match m2:
        case "**":
            p2 = p2**v2
        case "\|":
            p2 = p2**0.5
        case "%":
            p2 = (p2*v2)/100

    match o1:
        case "+":
            defresult = p1+p2
        case "-":
            defresult = p1-p2
        case "*":
            defresult = p1*p2
        case "/":
            defresult = p1/p2

    return defresult
        
def convert (t1,p1):

    match t1:
        case "1":
            return (f"Binario: {bin(int(p1))[2:]} \nOctal: {oct(int(p1))[2:]} \nHexadecimal: {hex(int(p1))[2:].upper()}")
        
        case "2":
            return (f"Decimal: {int(p1, 2)} \nOctal: {oct(int(p1, 2))[2:]} \nHexadecimal: {hex(int(p1, 2))[2:].upper()}")
        
        case "3":
            return (f"Decimal: {int(p1, 8)} \nBinario: {bin(int(p1, 8))[2:]} \nHexadecimal: {hex(int(p1, 8))[2:].upper()}")

        case "4":
            return (f"Decimal: {int(p1, 16)} \nBinario: {bin(int(p1, 16))[2:]} \nOctal: {oct(int(p1, 16))[2:]}")