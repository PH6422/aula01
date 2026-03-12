menu1 = 1
lista = []

while menu1 == 1:

  menu2 = int(input("Insira a ação que deseja realizar: 1-Calcular, 2-Historico, 3-Finalizar "))
  match menu2:
    case 1:  
      n1 = float (input("Insira o primero digito "))
      op = input("Insira o operador ")
      n2 = float (input("Insira o segundo digito "))

      match op:
        case "+":
          result = n1+n2
        case "-":
          result =  n1-n2
        case "/":
          result =  n1/n2
        case "*":
          result =  n1*n2

      lista.extend([n1, op, n2, "=", result, "||"])
      print (result)
    case 2:
      print(lista)
    case 3:
      menu1 = 0
    