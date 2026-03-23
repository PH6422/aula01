# 🧮 Calculadora e Conversor Numérico em Python

Este projeto é uma aplicação em Python executada no terminal que combina:

✔ Calculadora interativa  
✔ Conversor entre sistemas numéricos  
✔ Histórico de operações  
✔ Validação completa de entrada  

---

# 📋 Funcionalidades

## 🔢 Calculadora
- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)

### 🛠 Modificação dos números
- Raiz quadrada
- Potência
- Porcentagem

### 🔄 Cálculo contínuo
- Permite usar o resultado como base para novos cálculos

---

## 🔄 Conversor de Bases Numéricas

Conversões entre:

| Tipo | Descrição |
|------|--------|
| Decimal | Base 10 |
| Binário | Base 2 |
| Octal | Base 8 |
| Hexadecimal | Base 16 |

### 🔁 Conversões disponíveis
- Decimal → Binário / Octal / Hexadecimal  
- Binário → Decimal / Octal / Hexadecimal  
- Octal → Decimal / Binário / Hexadecimal  
- Hexadecimal → Decimal / Binário / Octal  

---

## 📜 Histórico

- Armazena todas as operações realizadas na calculadora
- Permite:
  - Visualizar histórico
  - Limpar histórico

---

## ✅ Validação de Entrada

O programa possui diversas validações para evitar erros:

- Números inválidos (`try/except`)
- Operadores incorretos
- Opções de menu inválidas
- Respostas diferentes de `s/n`
- Verificação de números binários válidos

---

# ⚙️ Tecnologias utilizadas

- **Python 3**
- Estrutura `while`
- Estrutura `match case`
- Tratamento de exceções (`try/except`)
- Listas (`list`)
- Manipulação de strings

---

# 📂 Estrutura do Menu

Menu principal:

| Opção | Função |
|------|------|
| 1 | Calculadora |
| 2 | Histórico |
| 3 | Conversão de bases |
| 4 | Finalizar |

---

# ▶️ Como executar

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
2️⃣ Acessar a pasta
cd seu-repositorio
3️⃣ Executar o programa
python main.py
💻 Exemplos de uso
🧮 Calculadora
Insira a ação:
1-Calcular

Insira o primeiro digito: 10
Insira o operador: +
10 + 5

10 + 5 = 15
🔄 Conversão
Tipo do número:
1-Decimal

Número: 10

Converter para:
2-Binário

Resultado: 1010
🗂 Exemplo de histórico
[10, '+', 5, '=', 15, '||', 15, '*', 2, '=', 30, '||']
🚀 Possíveis melhorias
Evitar divisão por zero
Melhorar interface do terminal
Criar interface gráfica (GUI)
Salvar histórico em arquivo
Organizar código em funções
Adicionar testes automatizados
🧠 Objetivo do projeto

Este projeto foi desenvolvido para praticar:

Lógica de programação
Estruturas de repetição
Estruturas condicionais
Manipulação de números
Conversão entre bases numéricas
Tratamento de erros
👨‍💻 Autor

Projeto desenvolvido para estudo de Python e algoritmos.