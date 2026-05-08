````markdown
# 🧮 Calculadora da Paulin

Projeto de uma calculadora com **interface gráfica em Python**, desenvolvida com a biblioteca **CustomTkinter**.

A aplicação possui funções de cálculo, modificadores matemáticos, histórico e conversor de bases numéricas.

---

## 📌 Funcionalidades

- Interface gráfica
- Operações básicas:
  - Soma (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)
- Modificadores:
  - Potência (`**`)
  - Porcentagem (`%`)
  - Raiz quadrada (`|`)
- Histórico de operações
- Botão para limpar histórico
- Conversor de bases numéricas:
  - Decimal
  - Binário
  - Octal
  - Hexadecimal

---

## 📁 Estrutura do Projeto

```text
projeto/
│
├── main.py
├── front_end.py
├── back_end.py
└── README.md
````

### `main.py`

Arquivo principal do projeto.
Ele importa o front-end e inicia a aplicação.

```python
import front_end

front_end.iniciar_app()
```

### `back_end.py`

Arquivo responsável pela lógica do programa.

Contém:

* `calc()` → realiza os cálculos
* `convert()` → converte bases numéricas

### `front_end.py`

Arquivo responsável pela interface gráfica.

Ele cria a janela, botões, campos de entrada, menus, histórico e área de conversão.

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* CustomTkinter
* Modularização em Python
* Funções
* `match case`

---

## ▶️ Como Executar

### 1. Instale o CustomTkinter

```bash
pip install customtkinter
```

### 2. Execute o arquivo principal

```bash
python main.py
```

---

## 🧮 Como Usar a Calculadora

1. Escolha um modificador para o primeiro número, caso queira.
2. Digite o primeiro número.
3. Escolha o operador matemático.
4. Digite o segundo número.
5. Escolha um modificador para o segundo número, caso queira.
6. Clique em **Calcular**.
7. O resultado aparecerá na tela e será salvo no histórico.

---

## 🔄 Como Usar o Conversor

1. Selecione o tipo do número:

   * `1` Decimal
   * `2` Binário
   * `3` Octal
   * `4` Hexadecimal
2. Digite o número.
3. Clique em **Converter**.
4. O resultado será exibido na tela.

---

## 🖼️ Interface

A interface contém:

* Campo para o primeiro número
* Campo para o segundo número
* Menu de operadores
* Menu de modificadores
* Resultado do cálculo
* Histórico
* Conversor de bases

---

## 🚀 Possíveis Melhorias

* Melhorar o visual da interface
* Adicionar modo claro/escuro
* Salvar histórico em arquivo
* Tratar divisão por zero
* Adicionar botão para apagar campos
* Organizar melhor os elementos da janela

---

## 👨‍💻 Autor

Projeto desenvolvido para prática de **Python, lógica de programação, interface gráfica e modularização**.

```

