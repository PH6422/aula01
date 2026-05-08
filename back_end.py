# Função responsável pelos cálculos da calculadora
def calc(n1, mod1, vm1, op, n2, mod2, vm2):

    # Aplica modificadores no primeiro número
    match mod1:
        case "**":  # Potência
            n1 **= vm1

        case "%":   # Porcentagem
            n1 = (n1 * vm1) / 100

        case "|":   # Raiz quadrada
            n1 **= 0.5

    # Aplica modificadores no segundo número
    match mod2:
        case "**":
            n2 **= vm2

        case "%":
            n2 = (n2 * vm2) / 100

        case "|":
            n2 **= 0.5

    # Realiza a operação matemática escolhida
    match op:
        case "+":
            return n1 + n2

        case "-":
            return n1 - n2

        case "*":
            return n1 * n2

        case "/":
            return n1 / n2

        # Caso a operação seja inválida
        case _:
            return "Erro!"


# Função responsável pela conversão de bases numéricas
def convert(t1, p1):

    # Decimal
    match t1:
        case "1":
            return (
                f"Binario: {bin(int(p1))[2:]} \n"
                f"Octal: {oct(int(p1))[2:]} \n"
                f"Hexadecimal: {hex(int(p1))[2:].upper()}"
            )

        # Binário
        case "2":
            return (
                f"Decimal: {int(p1, 2)} \n"
                f"Octal: {oct(int(p1, 2))[2:]} \n"
                f"Hexadecimal: {hex(int(p1, 2))[2:].upper()}"
            )

        # Octal
        case "3":
            return (
                f"Decimal: {int(p1, 8)} \n"
                f"Binario: {bin(int(p1, 8))[2:]} \n"
                f"Hexadecimal: {hex(int(p1, 8))[2:].upper()}"
            )

        # Hexadecimal
        case "4":
            return (
                f"Decimal: {int(p1, 16)} \n"
                f"Binario: {bin(int(p1, 16))[2:]} \n"
                f"Octal: {oct(int(p1, 16))[2:]}"
            )