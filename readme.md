# 🧮 Calculadora Interativa em Python (com Validação de Entrada)

Este projeto é uma **calculadora em Python executada no terminal**, com foco em **validação de dados**, **tratamento de erros** e **interatividade**.

Diferente de versões mais simples, este programa garante que o usuário insira apenas valores válidos, evitando falhas durante a execução.

---

## 📋 Funcionalidades

### 🔢 Operações matemáticas
- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)

### 🛠 Modificação dos números
Antes do cálculo, é possível alterar os valores:
- Raiz quadrada
- Potência
- Porcentagem

### 🔄 Cálculo contínuo
- O resultado pode ser reutilizado como próximo valor
- Permite várias operações em sequência

### 📜 Histórico
- Armazena todas as operações realizadas
- Opção de limpar o histórico

### ✅ Validação de entrada
- Impede entrada de valores inválidos
- Garante operadores corretos
- Verifica respostas como `s/n`
- Trata erros com `try/except`

---

## ⚙️ Tecnologias utilizadas

- **Python 3**
- Estrutura `while`
- Estrutura `match case`
- Tratamento de exceções (`try/except`)
- Listas (`list`)
- Entrada de dados com `input()`

---

## 🧠 Diferenciais do projeto

✔ Tratamento de erro para números inválidos  
✔ Validação completa de entradas do usuário  
✔ Fluxo de uso mais seguro e controlado  
✔ Estrutura organizada com múltiplos loops  

---

## 📂 Estrutura do Programa

Menu principal:

| Opção | Função |
|------|------|
| 1 | Iniciar cálculo |
| 2 | Ver histórico |
| 3 | Finalizar programa |

Durante o cálculo:
1. O usuário insere o primeiro número
2. Escolhe o operador
3. Insere o segundo número
4. Pode modificar os números
5. Visualiza o resultado
6. Decide continuar ou encerrar

---

## ▶️ Como executar

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
2️⃣ Entrar na pasta
cd seu-repositorio
3️⃣ Executar o programa
python main.py
💻 Exemplo de uso
Insira a ação que deseja realizar:
1-Calcular, 2-Historico, 3-Finalizar

1

Insira o primero digito: 10
Insira o operador: *
10 * 2

Deseja modificar o primeiro numero? s/n
n

Deseja modificar o segundo numero? s/n
n

10 * 2 = 20
⚠️ Tratamento de erros

O programa lida com erros como:

Entrada de letras no lugar de números

Operadores inválidos

Respostas diferentes de s ou n

Exemplo:

Erro: valor inserido não é um numero
🗂 Exemplo de histórico
[10, '*', 2, '=', 20, '||', 20, '+', 5, '=', 25, '||']
🚀 Melhorias futuras

Evitar divisão por zero

Melhorar visual do histórico

Interface gráfica (GUI)

Salvar histórico em arquivo

Refatorar código em funções

👨‍💻 Autor

Projeto desenvolvido para prática de lógica de programação e tratamento de erros em Python.