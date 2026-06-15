# Simulador de Gerência de Memória (Paginação)

**Grupo 10:** LRU vs. Segunda Chance (Clock) — 4 frames.

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
