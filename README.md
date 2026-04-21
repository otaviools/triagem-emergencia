# 🏥 Sistema de Triagem Hospitalar

> Fila de atendimento com prioridade automática e promoção por tempo de espera — feito em Python puro.

-----

## 📋 Sobre o projeto

Sistema de gerenciamento de fila para triagem hospitalar que organiza pacientes em dois níveis de prioridade: **Normal** e **Preferencial** (idosos, gestantes, PCD). Inclui uma regra de promoção automática: pacientes normais que aguardam mais de 5 chamadas sem serem atendidos sobem automaticamente para preferencial.

-----

## ⚙️ Como funciona

```
Paciente entra
     │
     ├── Preferencial ──► fila_preferencial (deque)
     │
     └── Normal ──────► fila_normal (deque)
                              │
                        espera += 1 a cada chamada
                              │
                        espera > 5? ──► promovido para preferencial
```

### Regras de negócio

- Preferenciais **sempre** são chamados antes dos normais
- A cada chamada, todos os normais restantes têm seu contador de espera incrementado
- Ao atingir **6 chamadas sem atendimento**, o paciente normal é promovido automaticamente
- A fila preferencial tem inserção e remoção em **O(1)**

-----

## 🚀 Como usar

**Requisitos:** Python 3.7+, nenhuma dependência externa.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/triagem-hospitalar.git
cd triagem-hospitalar

# Execute
python triagem.py
```

### Menu interativo

```
1 - Inserir paciente
2 - Chamar próximo
3 - Mostrar fila
4 - Sair
```

Ao inserir um paciente, o sistema pergunta o tipo:

```
Nome do paciente: Carlos
Carlos é (1) Normal ou (2) Preferencial? 1
✅ Carlos entrou como Normal
```

-----

## 💻 Exemplo de execução

```
Nome do paciente: Maria
Maria é (1) Normal ou (2) Preferencial? 2
✅ Maria entrou como Preferencial

Nome do paciente: Carlos
Carlos é (1) Normal ou (2) Preferencial? 1
✅ Carlos entrou como Normal

🔔 Chamando: Maria (Preferencial)
🔔 Chamando: Carlos (Normal)

# Após 6 chamadas sem atendimento:
⚡ PROMOÇÃO: Carlos esperou 5 chamadas e subiu para Preferencial!
```

-----

## 🗂️ Estrutura do código

|Função            |O quê faz                                |Complexidade|
|------------------|-----------------------------------------|------------|
|`inserir(nome)`   |Aloca o paciente na fila correta         |O(1)        |
|`chamar_proximo()`|Remove e chama o próximo paciente        |O(n)        |
|`mostrar_fila()`  |Exibe o estado atual das filas           |O(n)        |
|Regra de promoção |Incrementa espera e promove se necessário|O(n)        |

-----

## 🧱 Estrutura de dados

Duas filas do tipo `deque` (double-ended queue) da biblioteca `collections`:

```python
from collections import deque

fila_preferencial = deque()  # idosos, gestantes, PCD
fila_normal = deque()        # demais pacientes

# Cada paciente é um dicionário simples:
{"nome": "Carlos", "espera": 3}
```

O `deque` foi escolhido por oferecer `append()` e `popleft()` em **O(1)**, ideal para filas.

-----

## 📄 Relatório técnico

O projeto inclui um relatório em PDF com diagramas de arquitetura, fluxogramas e análise de complexidade.  
Veja: [`relatorio_triagem.pdf`](./relatorio_triagem.pdf)

-----

## 📌 Possíveis melhorias

- [ ] Substituir o contador de chamadas por **tempo real em minutos** (`datetime`)
- [ ] Persistir a fila em arquivo JSON para sobreviver a reinicializações
- [ ] Adicionar interface gráfica com `tkinter` ou web com `Flask`
- [ ] Criar testes unitários com `pytest`
- [ ] Adicionar categorias de prioridade (ex: emergência, urgência, eletivo)

-----

## 📝 Licença

MIT — fique à vontade para usar, modificar e distribuir.