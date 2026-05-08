# Importa a biblioteca da interface gráfica
import customtkinter as ctk

# Importa o back-end da calculadora
import back_end as bke


# Função principal da aplicação
def iniciar_app():

    # Lista para armazenar o histórico das contas
    historico = []

    # ---------------- MODIFICADOR 1 ----------------
    def verificar_mod1(op):

        # Permite alterar a variável da função externa
        nonlocal entrada_valor_mod1

        # Remove o campo antigo caso exista
        if entrada_valor_mod1 is not None:
            entrada_valor_mod1.destroy()
            entrada_valor_mod1 = None

        # Cria o campo de valor do modificador
        if op == "**" or op == "%":
            entrada_valor_mod1 = ctk.CTkEntry(
                app,
                placeholder_text="Valor do modificador 1"
            )

            entrada_valor_mod1.grid(
                row=1,
                column=2,
                padx=10,
                pady=10
            )

    # ---------------- MODIFICADOR 2 ----------------
    def verificar_mod2(op):

        nonlocal entrada_valor_mod2

        # Remove o campo antigo
        if entrada_valor_mod2 is not None:
            entrada_valor_mod2.destroy()
            entrada_valor_mod2 = None

        # Cria o campo do modificador
        if op == "**" or op == "%":
            entrada_valor_mod2 = ctk.CTkEntry(
                app,
                placeholder_text="Valor do modificador 2"
            )

            entrada_valor_mod2.grid(
                row=2,
                column=2,
                padx=10,
                pady=10
            )

    # ---------------- BOTÃO CALCULAR ----------------
    def acao_botao_calc():

        try:
            # Captura os números digitados
            n1 = float(entrada_n1.get())
            n2 = float(entrada_n2.get())

            # Captura operador e modificadores
            op = operador.get()
            mod1 = modificador1.get()
            mod2 = modificador2.get()

            # Valores padrão dos modificadores
            vm1 = 0
            vm2 = 0

            # Pega o valor do modificador 1
            if mod1 == "**" or mod1 == "%":
                vm1 = float(entrada_valor_mod1.get())

            # Pega o valor do modificador 2
            if mod2 == "**" or mod2 == "%":
                vm2 = float(entrada_valor_mod2.get())

            # Chama a função de cálculo
            resultado = bke.calc(
                n1,
                mod1,
                vm1,
                op,
                n2,
                mod2,
                vm2
            )

            # Texto inicial do histórico
            texto_n1 = f"{n1}{mod1}"
            texto_n2 = f"{n2}{mod2}"

            # Ajusta exibição do modificador 1
            if mod1 == "**" or mod1 == "%":
                texto_n1 = f"{n1}{mod1}{vm1}"

            # Ajusta exibição do modificador 2
            if mod2 == "**" or mod2 == "%":
                texto_n2 = f"{n2}{mod2}{vm2}"

            # Cria a string completa da conta
            conta = f"{texto_n1} {op} {texto_n2} = {resultado}"

            # Adiciona ao histórico
            historico.append(conta)

            # Mostra resultado na tela
            result_label.configure(text=str(resultado))

            # Mostra no campo de histórico
            caixa_historico.insert("end", conta + "\n")

        # Caso o usuário digite algo inválido
        except ValueError:
            result_label.configure(
                text="Erro: digite números válidos"
            )

    # ---------------- LIMPAR HISTÓRICO ----------------
    def limpar_historico():

        # Limpa lista
        historico.clear()

        # Limpa caixa de texto
        caixa_historico.delete("1.0", "end")

    # ---------------- CONVERSOR ----------------
    def acao_converter():

        try:
            # Tipo do número
            tipo = tipo_numero.get()

            # Número digitado
            numero = entrada_conversao.get().strip().upper()

            # Chama a função de conversão
            resultado = bke.convert(tipo, numero)

            # Mostra resultado
            resultado_conversao.configure(text=resultado)

        except ValueError:

            # Mensagem de erro
            resultado_conversao.configure(
                text="Erro: número inválido"
            )

    # ---------------- CRIAÇÃO DA JANELA ----------------
    app = ctk.CTk()

    app.geometry("750x550")
    app.title("Calculadora da Paulin")

    # ---------------- TÍTULO ----------------
    msg_inicial = ctk.CTkLabel(
        app,
        text="Bem vindo a Calculadora do Paulin!"
    )

    msg_inicial.grid(row=0, column=0, padx=5, pady=5)

    # ---------------- MODIFICADOR 1 ----------------
    modificador1 = ctk.StringVar(value="")

    menu_mod1 = ctk.CTkOptionMenu(
        app,
        variable=modificador1,
        values=["", "**", "%", "|"],
        command=verificar_mod1
    )

    menu_mod1.grid(row=1, column=0, padx=5, pady=5)

    entrada_valor_mod1 = None

    # ---------------- PRIMEIRO NÚMERO ----------------
    entrada_n1 = ctk.CTkEntry(
        app,
        placeholder_text="Primeiro numero"
    )

    entrada_n1.grid(row=2, column=0, padx=5, pady=5)

    # ---------------- OPERADOR ----------------
    operador = ctk.StringVar(value="+")

    menu_op = ctk.CTkOptionMenu(
        app,
        variable=operador,
        values=["+", "-", "*", "/"]
    )

    menu_op.grid(row=3, column=0, padx=5, pady=5)

    entrada_valor_mod2 = None

    # ---------------- SEGUNDO NÚMERO ----------------
    entrada_n2 = ctk.CTkEntry(
        app,
        placeholder_text="Segundo numero"
    )

    entrada_n2.grid(row=4, column=0, padx=5, pady=5)

    # ---------------- MODIFICADOR 2 ----------------
    modificador2 = ctk.StringVar(value="")

    menu_mod2 = ctk.CTkOptionMenu(
        app,
        variable=modificador2,
        values=["", "**", "%", "|"],
        command=verificar_mod2
    )

    menu_mod2.grid(row=5, column=0, padx=5, pady=5)

    # ---------------- RESULTADO ----------------
    result_label = ctk.CTkLabel(app, text="")

    result_label.grid(row=6, column=0, padx=5, pady=5)

    # ---------------- BOTÃO CALCULAR ----------------
    botao_calc = ctk.CTkButton(
        app,
        text="Calcular",
        command=acao_botao_calc
    )

    botao_calc.grid(row=7, column=0, padx=5, pady=5)

    # ---------------- HISTÓRICO ----------------
    caixa_historico = ctk.CTkTextbox(
        app,
        width=300,
        height=120
    )

    caixa_historico.grid(row=3, column=2, padx=5, pady=5)

    # ---------------- BOTÃO LIMPAR ----------------
    botao_limpar = ctk.CTkButton(
        app,
        text="Limpar histórico",
        command=limpar_historico
    )

    botao_limpar.grid(row=4, column=2, padx=5, pady=5)

    # ---------------- CONVERSOR ----------------
    msg_conversao = ctk.CTkLabel(
        app,
        text="Conversor de bases numéricas"
    )

    msg_conversao.grid(row=5, column=2, padx=5, pady=5)

    # Explicação do conversor
    msg_explicacao_conversao = ctk.CTkLabel(
        app,
        text="Selecione o tipo de número "
             "(1-decimal, 2-binário, "
             "3-octal, 4-hexadecimal)"
    )

    msg_explicacao_conversao.grid(
        row=6,
        column=2,
        padx=5,
        pady=5
    )

    # Menu de seleção do tipo
    tipo_numero = ctk.StringVar(value="1")

    menu_conversao = ctk.CTkOptionMenu(
        app,
        variable=tipo_numero,
        values=["1", "2", "3", "4"]
    )

    menu_conversao.grid(row=7, column=2, padx=5, pady=5)

    # Campo do número
    entrada_conversao = ctk.CTkEntry(
        app,
        placeholder_text="Número para converter"
    )

    entrada_conversao.grid(row=8, column=2, padx=5, pady=5)

    # Resultado da conversão
    resultado_conversao = ctk.CTkLabel(app, text="")

    resultado_conversao.grid(
        row=9,
        column=2,
        padx=5,
        pady=5
    )

    # Botão converter
    botao_converter = ctk.CTkButton(
        app,
        text="Converter",
        command=acao_converter
    )

    botao_converter.grid(
        row=10,
        column=2,
        padx=5,
        pady=5
    )

    # Mantém a janela aberta
    app.mainloop()