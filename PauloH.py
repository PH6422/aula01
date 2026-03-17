menu1 = 1
lista = []

while menu1 == 1:

  menu2 = input("Insira a ação que deseja realizar: 1-Calcular, 2-Historico, 3-Finalizar ")
  while menu2 != "1" and menu2 != "2" and menu2 != "3":
    print("Valor invalito")

  match menu2:

    case "1": 
      fim = "n"
      while fim != "s":

        while True:
          try:
            n1 = float(input("Insira o primero digito "))
            break
          except ValueError:
            print("Erro: valor insirido não é um numero")
        

        zerar = "n"
        while zerar != "s":

          op = input(f"Insira o operador {n1} ")

          while op != "+" and op != "-" and op != "/" and op != "*":
            print("sinal invalido")
            op = input(f"Insira o operador {n1} ")
          
          while True:
            try:
              n2 = float(input(f" {n1} {op} "))
              break
            except ValueError:
              print("Erro: valor insirido não é um numero")

          mod1 = input(f"Deseja fazer modificar o primeiro numero? s/n {n1} {op} {n2} ")
          
          while mod1 != "s" and mod1 != "n":
            print("Resposta invalida")
            mod1 = input(f"Deseja fazer modificar o primeiro numero? s/n {n1} {op} {n2} ")

          if mod1 == "s":
            mod1 = input("1-Raiz Quadrada, 2-Potencia, 3-Porcentagem ")

            while mod1 != "1" and mod1 != "2" and mod1 != "3":
              print("Valor Invalido")
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

          while mod2 != "s" and mod2 != "n":
            print("Resposta invalida")
            mod2 = input(f" Deseja fazer modificar o segundo numero? s/n  {n1} {op} {n2} ")

          if mod2 == "s":
            mod2 = input("1-Raiz Quadrada, 2-Potencia, 3-Porcentagem ")

            while mod2 != "1" and mod2 != "2" and mod2 != "3":
              print("Valor Invalido")
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
          while zerar != "s" and zerar != "n":
            print("Resposta invalida")
            zerar = input("Finalizar calculo? s/n ")
          
        fim = input("Finalizar calculo? s/n ")
        while fim != "s" and fim != "n":
          print("Resposta invalida")
          fim = input("Finalizar calculo? s/n ")
        

    case "2":

      print(lista)
      limpar = input("Deseja limpar o historico? s/n ")

      while limpar != "s" and limpar != "n":
        print("Resposta invalida")
        limpar = input("Deseja limpar o historico? s/n ")

      if limpar == "s":
        lista.clear()

    case "3":

      menu1 = 0
    