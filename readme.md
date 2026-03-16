
````markdown
# 🧮 Calculadora Avançada em Python

Este projeto é uma **calculadora interativa em Python executada no terminal**, que permite realizar operações matemáticas básicas e aplicar **modificações nos números antes do cálculo**, além de manter um **histórico das operações realizadas**.

---

# 📋 Funcionalidades

✔ Operações matemáticas básicas  
- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)

✔ Modificação dos números antes do cálculo  
- Raiz quadrada  
- Potência  
- Porcentagem  

✔ Cálculo encadeado  
- O resultado de uma operação pode ser usado como **primeiro número da próxima operação**

✔ Histórico de cálculos  
- Visualização do histórico
- Opção de **limpar histórico**

✔ Menu interativo no terminal

---

# ⚙️ Tecnologias utilizadas

- **Python 3**
- Estrutura de repetição `while`
- Estrutura de decisão `match case`
- Listas (`list`)
- Entrada de dados com `input()`
- Operações matemáticas básicas

---

# 📂 Estrutura do Programa

O programa possui um **menu principal** com três opções:

| Opção | Função |
|------|------|
| 1 | Realizar cálculos |
| 2 | Ver histórico |
| 3 | Finalizar programa |

Durante o cálculo o usuário pode:

1. Inserir dois números
2. Escolher um operador matemático
3. Modificar qualquer um dos números com:
   - Raiz quadrada
   - Potência
   - Porcentagem
4. Continuar calculando usando o **resultado anterior**

---

# ▶️ Como executar

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
````

## 2️⃣ Entrar na pasta do projeto

```bash
cd seu-repositorio
```

## 3️⃣ Executar o programa

```bash
python main.py
```

---

# 💻 Exemplo de uso

```
Insira a ação que deseja realizar:
1 - Calcular
2 - Historico
3 - Finalizar

1

Insira o primeiro digito: 9
Insira o operador: +
9 + 3

Deseja modificar o primeiro numero? s/n
n

Deseja modificar o segundo numero? s/n
n

9 + 3 = 12
```

---

# 🗂 Exemplo de histórico

```
[9, '+', 3, '=', 12, '||', 12, '*', 2, '=', 24, '||']
```

---

# 🚀 Possíveis melhorias

* Tratar erros de entrada do usuário
* Evitar divisão por zero
* Melhorar a exibição do histórico
* Salvar histórico em arquivo `.txt`
* Criar interface gráfica

---

# 👨‍💻 Autor

Projeto desenvolvido para **prática de lógica de programação em Python**.

```