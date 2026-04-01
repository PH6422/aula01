# 🧮 Calculadora Modular + Conversor de Bases em Python

Este projeto é uma aplicação em Python executada no terminal que combina:

- 🧮 Calculadora avançada com modificadores
- 🔄 Conversor entre bases numéricas
- 📜 Histórico de operações
- 🧩 Estrutura modular com separação de responsabilidades

---

# 📁 Estrutura do Projeto


📦 projeto
┣ 📜 main.py # Código principal (interface e menu)
┣ 📜 calculos.py # Funções de cálculo e conversão
┗ 📜 README.md


---

# 📋 Funcionalidades

## 🧮 Calculadora Avançada

### Operações básicas:
- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)

### 🛠 Modificadores (antes do cálculo)

| Símbolo | Função |
|--------|------|
| `**` | Potência |
| `\|` | Raiz quadrada |
| `%` | Porcentagem |
| `Enter` | Sem modificação |

✔ Os modificadores são aplicados **antes da operação principal**

---

## 🔄 Conversor de Bases Numéricas

Conversões entre:

- Decimal
- Binário
- Octal
- Hexadecimal

### Exemplos:
- Decimal → Binário, Octal, Hexadecimal  
- Binário → Decimal, Octal, Hexadecimal  
- Octal → Decimal, Binário, Hexadecimal  
- Hexadecimal → Decimal, Binário, Octal  

---

## 📜 Histórico

- Armazena todas as operações realizadas
- Exibe de forma organizada
- Permite limpar o histórico

---

## 🧩 Estrutura Modular

### 🔹 `main.py`
Responsável por:
- Interface com o usuário
- Menus
- Entrada de dados
- Controle do fluxo do programa

### 🔹 `calculos.py`

Contém:

#### Função `calc()`
```python
calc(p1, m1, v1, o1, p2, m2, v2)

Responsável por:

Aplicar modificadores
Executar a operação matemática
Função convert()
convert(tipo, valor)

Responsável por:

Converter números entre diferentes bases
⚙️ Tecnologias utilizadas
Python 3
Estrutura match case
Modularização com import
Listas (list)
Funções
Conversão de bases (bin(), oct(), hex())
▶️ Como executar
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
2️⃣ Acessar a pasta
cd seu-repositorio
3️⃣ Executar o programa
python main.py
💻 Exemplos de uso
🧮 Calculadora
Insira o primeiro número: 9
Modificador: \|
Resultado: 3

3 + 2 = 5
🔄 Conversão
Tipo: Decimal
Número: 10

Resultado:
Binario: 1010
Octal: 12
Hexadecimal: A
🗂 Exemplo de histórico
9\| + 2 = 5
5**2 * 3 = 75
🚀 Possíveis melhorias
Tratar divisão por zero
Melhorar interface do terminal
Criar interface gráfica (GUI)
Salvar histórico em arquivo
Separar ainda mais funções
Adicionar testes automatizados
🧠 Objetivo do projeto

Este projeto foi desenvolvido para praticar:

Modularização em Python
Organização de código
Lógica de programação
Conversão de bases numéricas
Manipulação de entrada do usuário
👨‍💻 Autor

Projeto desenvolvido para estudo de Python, algoritmos e boas práticas de programação.