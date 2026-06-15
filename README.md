# Simulador de Gerência de Memória (Paginação)

**Grupo 10:** LRU vs. Segunda Chance (Clock) — 4 frames: Caetano Marasca, Enrico Pheula, Felipe Ferreira, Gustavo Melleu

## Sobre

Simulador de substituição de páginas: processa uma sequência de acessos à
memória, gerencia uma quantidade fixa de frames e mostra o mapa da memória
passo a passo, contando os page faults ao final.

Algoritmos implementados:
- **LRU** (Least Recently Used) — substitui a página usada há mais tempo.
- **Clock** (Segunda Chance) — aproxima o LRU com bit de referência e ponteiro circular.

## Requisitos

- Python 3.10 ou superior, sem bibliotecas externas.
- No macOS/Linux use `python3`. (No Windows costuma ser `python`.)

## Como executar

```bash
python3 simulador_memoria.py entrada.txt LRU
python3 simulador_memoria.py entrada.txt CLOCK
```

O segundo argumento aceita `LRU` ou `CLOCK`.

## Resultado caso teste

```bash
CLOCK                
Iniciando simulação com 4 frames disponíveis.                                        
========================================

--- Passo 1: Acesso à Página 7 (Page Fault) ---
[Frame 0]: Página 7 <-- Alterado
[Frame 1]: [Vazio]
[Frame 2]: [Vazio]
[Frame 3]: [Vazio]
----------------------------------------

--- Passo 2: Acesso à Página 0 (Page Fault) ---
[Frame 0]: Página 7
[Frame 1]: Página 0 <-- Alterado
[Frame 2]: [Vazio]
[Frame 3]: [Vazio]
----------------------------------------

--- Passo 3: Acesso à Página 1 (Page Fault) ---
[Frame 0]: Página 7
[Frame 1]: Página 0
[Frame 2]: Página 1 <-- Alterado
[Frame 3]: [Vazio]
----------------------------------------

--- Passo 4: Acesso à Página 2 (Page Fault) ---
[Frame 0]: Página 7
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2 <-- Alterado
----------------------------------------

--- Passo 5: Acesso à Página 0 (Hit) ---
[Frame 0]: Página 7
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2
----------------------------------------

--- Passo 6: Acesso à Página 3 (Page Fault) ---
[Frame 0]: Página 3 <-- Alterado
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2
----------------------------------------

--- Passo 7: Acesso à Página 0 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2
----------------------------------------

--- Passo 8: Acesso à Página 4 (Page Fault) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4 <-- Alterado
[Frame 3]: Página 2
----------------------------------------

--- Passo 9: Acesso à Página 2 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

--- Passo 10: Acesso à Página 3 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

--- Passo 11: Acesso à Página 0 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

--- Passo 12: Acesso à Página 3 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

================ STATS FINAIS ================
Total de Acessos: 12
Total de Page Faults: 6
Taxa de Page Faults: 50.00%
==============================================
```
```bash
LRU                  
Iniciando simulação com 4 frames disponíveis.                                        
========================================

--- Passo 1: Acesso à Página 7 (Page Fault) ---
[Frame 0]: Página 7 <-- Alterado
[Frame 1]: [Vazio]
[Frame 2]: [Vazio]
[Frame 3]: [Vazio]
----------------------------------------

--- Passo 2: Acesso à Página 0 (Page Fault) ---
[Frame 0]: Página 7
[Frame 1]: Página 0 <-- Alterado
[Frame 2]: [Vazio]
[Frame 3]: [Vazio]
----------------------------------------

--- Passo 3: Acesso à Página 1 (Page Fault) ---
[Frame 0]: Página 7
[Frame 1]: Página 0
[Frame 2]: Página 1 <-- Alterado
[Frame 3]: [Vazio]
----------------------------------------

--- Passo 4: Acesso à Página 2 (Page Fault) ---
[Frame 0]: Página 7
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2 <-- Alterado
----------------------------------------

--- Passo 5: Acesso à Página 0 (Hit) ---
[Frame 0]: Página 7
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2
----------------------------------------

--- Passo 6: Acesso à Página 3 (Page Fault) ---
[Frame 0]: Página 3 <-- Alterado
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2
----------------------------------------

--- Passo 7: Acesso à Página 0 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 1
[Frame 3]: Página 2
----------------------------------------

--- Passo 8: Acesso à Página 4 (Page Fault) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4 <-- Alterado
[Frame 3]: Página 2
----------------------------------------

--- Passo 9: Acesso à Página 2 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

--- Passo 10: Acesso à Página 3 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

--- Passo 11: Acesso à Página 0 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

--- Passo 12: Acesso à Página 3 (Hit) ---
[Frame 0]: Página 3
[Frame 1]: Página 0
[Frame 2]: Página 4
[Frame 3]: Página 2
----------------------------------------

================ STATS FINAIS ================
Total de Acessos: 12
Total de Page Faults: 6
Taxa de Page Faults: 50.00%
==============================================
```
