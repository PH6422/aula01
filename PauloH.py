menu1 = 1
lista = []

while menu1 == 1:

  menu2 = int(input("Insira a ação que deseja realizar: 1-Calcular, 2-Historico, 3-Finalizar "))
  match menu2:

    case 1: 
     
      while True:
        n1 = float (input("Insira o primero digito "))
        while True:
          op = input(f"Insira o operador {n1} ")
          n2 = float (input(f" {n1} {op} "))
          mod1 = input(f"Deseja fazer modificar o primeiro numero? s/n {n1} {op} {n2} ")
          if mod1 == "s":
            mod1 = input("1-Raiz Quadrada, 2-Potencia, 3-Porcentagem ")
            match mod1:
              case "1":
                n1 = n1 ** 0.5
              case "2":
                pot = int (input("Insira o valor da potencia "))
                n1 = n1 ** pot
              case "3":
                porc = input("Insira o valor da porcetagem ")
                n1 = (n1 * porc)/100
            
          mod2 = input(f" Deseja fazer modificar o segundo numero? s/n  {n1} {op} {n2} ")
          if mod2 == "s":
            mod2 = input("1-Raiz Quadrada, 2-Potencia, 3-Porcentagem ")
            match mod2:
              case "1":
                n2 = n2 ** 0.5
              case "2":
                pot = int (input("Insira o valor da potencia "))
                n2 = n2 ** pot
              case "3":
                porc = input("Insira o valor da porcetagem ")
                n2 = (n2 * porc)/100
          
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
          print (f"{n1} {op} {n2} = {result} ")
          n1 = result
          zerar = (input("zerar o primeiro numero? s/n "))
          if zerar == "s":
            break
        fim = input("Finalizar calculo? ")
        if fim == "s":
          break

    case 2:
      print(lista)
      limpar = input("Deseja limpar o historico? s/n ")
      if limpar == "s":
        lista.clear()
    case 3:
      menu1 = 0
    