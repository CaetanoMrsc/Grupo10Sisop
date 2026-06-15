###
###     S I M U L A D O R    D E    M E M Ó R I A
###
### Prof. Filipo - github.com/ProfessorFilipo/MemSim/
### Grupo 10: LRU vs. Segunda Chance (Clock) — 4 frames
###

import sys


class Frame:
    def __init__(self, id_frame):
        self.id_frame = id_frame
        self.pagina_alocada = None
        self.timestamp = 0  # LRU: instante do último acesso
        self.ref_bit = 0    # Clock: bit de referência


class TabelaPaginas:
    def __init__(self, num_frames, algoritmo):
        self.frames = [Frame(i) for i in range(num_frames)]
        self.total_page_faults = 0
        self.total_acessos = 0
        self.algoritmo = algoritmo.upper()
        self.clock_ptr = 0  # ponteiro circular do algoritmo Clock

    def acessar_pagina(self, numero_pagina):
        self.total_acessos += 1

        # 1. Verificar se a página já está em algum frame (Hit)
        for frame in self.frames:
            if frame.pagina_alocada == numero_pagina:
                if self.algoritmo == "LRU":
                    frame.timestamp = self.total_acessos
                elif self.algoritmo == "CLOCK":
                    frame.ref_bit = 1
                return True, frame.id_frame

        # 2. Page Fault
        self.total_page_faults += 1

        # 3. Frame vazio disponível?
        for frame in self.frames:
            if frame.pagina_alocada is None:
                frame.pagina_alocada = numero_pagina
                if self.algoritmo == "LRU":
                    frame.timestamp = self.total_acessos
                elif self.algoritmo == "CLOCK":
                    frame.ref_bit = 1
                return False, frame.id_frame

        # 4. Memória cheia — aplicar algoritmo de substituição
        frame_vitima_id = self.substituir_pagina(numero_pagina)
        return False, frame_vitima_id

    def substituir_pagina(self, nova_pagina):
        if self.algoritmo == "LRU":
            return self._substituir_lru(nova_pagina)
        elif self.algoritmo == "CLOCK":
            return self._substituir_clock(nova_pagina)

    def _substituir_lru(self, nova_pagina):
        # Escolhe o frame com menor timestamp (usado há mais tempo)
        vitima = min(self.frames, key=lambda f: f.timestamp)
        vitima.pagina_alocada = nova_pagina
        vitima.timestamp = self.total_acessos
        return vitima.id_frame

    def _substituir_clock(self, nova_pagina):
        # Percorre circularmente: ref_bit=1 → zera e avança; ref_bit=0 → substitui
        while True:
            frame = self.frames[self.clock_ptr]
            if frame.ref_bit == 0:
                frame.pagina_alocada = nova_pagina
                frame.ref_bit = 1
                vitima_id = self.clock_ptr
                self.clock_ptr = (self.clock_ptr + 1) % len(self.frames)
                return vitima_id
            else:
                frame.ref_bit = 0
                self.clock_ptr = (self.clock_ptr + 1) % len(self.frames)

    def imprimir_mapa_memoria(self, passo, pagina_acessada, foi_hit, frame_alterado=None):
        status = "Hit" if foi_hit else "Page Fault"
        print(f"\n--- Passo {passo}: Acesso à Página {pagina_acessada} ({status}) ---")

        for frame in self.frames:
            conteudo = f"Página {frame.pagina_alocada}" if frame.pagina_alocada is not None else "[Vazio]"
            marcador = " <-- Alterado" if frame.id_frame == frame_alterado and not foi_hit else ""
            print(f"[Frame {frame.id_frame}]: {conteudo}{marcador}")

        print("-" * 40)


class Simulador:
    def __init__(self, caminho_arquivo, algoritmo):
        self.caminho_arquivo = caminho_arquivo
        self.algoritmo = algoritmo

    def executar(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.caminho_arquivo}' não foi encontrado.")
            return

        linhas = [l.strip() for l in linhas if l.strip() and not l.strip().startswith('#')]

        if not linhas:
            print("Erro: Arquivo de entrada vazio.")
            return

        num_frames = int(linhas[0])
        tabela_paginas = TabelaPaginas(num_frames, self.algoritmo)

        print(f"Iniciando simulação com {num_frames} frames disponíveis.")
        print("=" * 40)

        passo = 1
        for linha in linhas[1:]:
            numero_pagina = int(linha)
            foi_hit, frame_id = tabela_paginas.acessar_pagina(numero_pagina)
            tabela_paginas.imprimir_mapa_memoria(passo, numero_pagina, foi_hit, frame_id)
            passo += 1

        print("\n================ STATS FINAIS ================")
        print(f"Total de Acessos: {tabela_paginas.total_acessos}")
        print(f"Total de Page Faults: {tabela_paginas.total_page_faults}")
        if tabela_paginas.total_acessos > 0:
            taxa_faults = (tabela_paginas.total_page_faults / tabela_paginas.total_acessos) * 100
            print(f"Taxa de Page Faults: {taxa_faults:.2f}%")
        print("==============================================")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python simulador_memoria.py <arquivo_entrada> <algoritmo>")
        print("Algoritmos disponíveis: LRU, CLOCK")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    algoritmo = sys.argv[2].upper()

    if algoritmo not in ("LRU", "CLOCK"):
        print(f"Algoritmo '{algoritmo}' não reconhecido. Use LRU ou CLOCK.")
        sys.exit(1)

    simulador = Simulador(arquivo_entrada, algoritmo)
    simulador.executar()
