menu1 = 1
lista = []
import calculadora as c

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
          
          mod1 = input(f"Insira um mod: ** ; \| ; % : Enter para pular {n1} ")
          
          while mod1 != "**" and mod1 != "\|" and mod1 != "%" and mod1 != "":
            print("mod invalido")
            mod1 = input(f"Insira um mod: ** ; \| ; % : Enter para pular {n1} ")

          if mod1 == "**":
            vmod = int(input("Insira o valor da potencia "))
          elif mod1 == "%":
            vmod = int(input("Insira o valor da porcentage "))
          elif mod1 == "\|" or mod1 == "":
            vmod = ""
            

          op = input(f"Insira o operador {n1}{mod1}{vmod} ")

          while op != "+" and op != "-" and op != "/" and op != "*":
            print("sinal invalido")
            op = input(f"Insira o operador {n1}{mod1}{vmod} ")
          
          while True:
            try:
              n2 = float(input(f" {n1}{mod1}{vmod} {op} "))
              break
            except ValueError:
              print("Erro: valor insirido não é um numero")

          mod2 = input(f"Insira um mod: ** ; \| ; % : Enter para pular {n1}{mod1}{vmod} {op} {n2} ")

          while mod1 != "**" and mod1 != "\|" and mod1 != "%" and mod1 != "":
            print("mod invalido")
            mod1 = input(f"Insira um mod: ** ; \| ; % : Enter para pular {n1} ")

          if mod2 == "**":
            vmod2 = int(input(f"Insira o valor da potencia {n1}{mod1}{vmod} {op} {n2}{mod2}"))
          elif mod2 == "%":
            vmod2 = int(input(f"Insira o valor da porcentage {n1}{mod1}{vmod} {op} {n2}{mod2}"))
          elif mod2 == "\|" or mod2 == "":
            vmod2 = ""
           
          result = c.calc(n1,mod1,vmod,op,n2,mod2,vmod2)
          lista.append([
            f"{n1}{mod1}{vmod} {op} {n2}{mod2}{vmod2} = {result}"
          ])
          print (f"{n1}{mod1}{vmod} {op} {n2}{mod2}{vmod2} = {result} ")
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

      for conta in lista:
        print(f"{conta[0]}")

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

        print(c.convert(menu3,n1))

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
    