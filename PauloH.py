menu1 = 1
lista = []

while menu1 == 1:

  menu2 = input("Insira a ação que deseja realizar: 1-Calcular, 2-Historico, 3-Conversão, 4-Finalizar ")
  while menu2 != "1" and menu2 != "2" and menu2 != "3" and menu2 != "4":
    print("Valor invalito")
    menu2 = input("Insira a ação que deseja realizar: 1-Calcular, 2-Historico, 3-Conversão, 4-Finalizar ")

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

      while True:
 
       
        menu3 = input("Insira o tipo do numero : 1-Decimal, 2-binário, 3-octal, 4-hexadecimal ")
        while menu3 != "1" and menu3 != "2" and menu3 != "3" and menu3 != "4":
          print("Valor invalido")
          menu3 = input("Insira o tipo do numero : 1-Decimal, 2-binário, 3-octal, 4-hexadecimal ")


        n1 = (input("Insira o numero a ser convertido "))


        menu4 = input ("Insira a coverssão: 1-Decimal, 2-binário, 3-octal, 4-hexadecimal ")

        conv = ()

        match menu3:

          
          case "1":
              
            match menu4:

              case "1":

                conv = n1
              
              case "2":

                n1 = int(n1)
              
                if n1 == 0:
                  conv = 0

                numbi = ""

                while n1 > 0:
                  numbi = str(n1%2) + numbi
                  n1 = n1 // 2

                  conv = numbi
          
              case "3":

                n1 = int(n1)

                if n1 == 0:
                  conv = 0

                numoct = ""

                while n1 > 0:
                  numoct = str(n1%8) + numoct
                  n1 = n1 // 8

                  conv = numoct

              case "4":

                n1 = int(n1)

                if n1 == 0:
                  conv = 0

                numhex = "" 
                valores = "0123456789ABCDEF"

                while n1 > 0:
                  resto = n1 % 16
                  numhex = valores[resto] + numhex
                  n1 = n1 // 16

                  conv = numhex
        
          case "2":

            match menu4:

              case "1":

                numbi2 = str(n1)

                if all(d in "01" for d in numbi2):
                  None
                else:
                  print("Erro: número inválido")

                decimal = 0
                potencia = 0

                for digito in reversed (numbi2):
                  decimal += int(digito) * (2 ** potencia)
                  potencia += 1

                conv = decimal

              case "2":

                conv = n1
              
              case "3":


                n1 = str(n1)

                while len(n1) % 3 != 0:
                  n1 = "0" + n1

                binoct = ""

                for i in range (0, len(n1), 3):
                  grupo = n1[i:i+3]
                  decimal = int(grupo, 2)
                  binoct += str(decimal)

                conv = binoct
              
              case "4":
                
                n1 = str(n1)

                while len(n1) % 4 != 0:
                  n1 = "0" + n1

                binhex = ""
                valores = "0123456789ABCDEF"

                for i in range (0, len(n1), 4):
                  grupo = n1[i:i+4]
                  decimal = int(grupo, 2)
                  binhex += valores[decimal]

                conv = binhex

          case "3":

            match menu4:

              case "1":

                octdec = str(n1)

                decimal = 0
                potencia = 0

                for digito in reversed(octdec):
                  decimal += int(digito) * (8 ** potencia)
                  potencia += 1

                conv = decimal

              case "2":

                n1 = str(n1)

                tabela = {
                    "0": "000", "1": "001", "2": "010", "3": "011",
                    "4": "100", "5": "101", "6": "110", "7": "111"
                }
                  
                octbin = ""
                for digito in n1:
                  octbin += tabela[digito]

                octbin = octbin.lstrip("0")
                
                conv = octbin
              
              case "3":

                conv = n1
              
              case "4":
                  
                  n1 = str(n1)

                  tabela = {
                      "0": "000", "1": "001", "2": "010", "3": "011",
                      "4": "100", "5": "101", "6": "110", "7": "111"
                  }

                  octbin2 = ""

                  for d in n1:
                      octbin2 += tabela[d]

                  while len(octbin2) % 4 != 0:
                      octbin2 = "0" + octbin2

                  valores = "0123456789ABCDEF"

                  octhex = ""

                  for i in range(0, len(octbin2), 4):
                      grupo = octbin2[i:i+4]
                      decimal = int(grupo, 2)
                      octhex += valores[decimal]

                  octhex = octhex.lstrip("0")

                  conv = octhex
                  
          case "4":
            
            match menu4:

              case "1":

                valores2 = {
                    "0":0, "1":1, "2":2, "3":3, "4":4,
                    "5":5, "6":6, "7":7, "8":8, "9":9,
                    "A":10, "B":11, "C":12,
                    "D":13, "E":14, "F":15
                }

                decimal = 0
                potencia = 0

                for digito in reversed(n1):
                    decimal += valores2[digito] * (16 ** potencia)
                    potencia += 1
                  
                conv = decimal

              case "2":

                tabela2 = {
                    "0": "0000", "1": "0001", "2": "0010", "3": "0011",
                    "4": "0100", "5": "0101", "6": "0110", "7": "0111",
                    "8": "1000", "9": "1001", "A": "1010", "B": "1011",
                    "C": "1100", "D": "1101", "E": "1110", "F": "1111"
                }

                hexbin = ""

                for d in n1:
                    hexbin += tabela2[d]

                hexbin = hexbin.lstrip("0")

                conv = hexbin

              case "3":

                tabela_hex = {
                    "0":"0000","1":"0001","2":"0010","3":"0011",
                    "4":"0100","5":"0101","6":"0110","7":"0111",
                    "8":"1000","9":"1001","A":"1010","B":"1011",
                    "C":"1100","D":"1101","E":"1110","F":"1111"
                }

                hexbin2 = ""
                for d in n1:
                    hexbin2 += tabela_hex[d]

                while len(hexbin2) % 3 != 0:
                    hexbin2 = "0" + hexbin2

                hexoct = ""

                for i in range(0, len(hexbin2), 3):
                    grupo = hexbin2[i:i+3]
                    hexoct += str(int(grupo, 2))

                hexoct = hexoct.lstrip("0")

                conv = hexoct

              case "4":

                conv = n1
              
        print(conv)
        fim = input("Finalizar? s/n ")
        while fim != "s" and fim != "n":
          print("Resposta invalida")
          fim = input("Finalizar? s/n ")
        if fim == "n":
          None
        elif fim == "s":
          break

    case "4":

      menu1 = 0
    