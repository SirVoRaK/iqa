from faixa import Faixa
from poluente import Poluente, Concentracao
import math
faixas = [
    Faixa(1, "Boa", 0, 40),
    Faixa(2, "Moderada", 40, 80),
    Faixa(3, "Ruim", 80, 120),
    Faixa(4, "Muito Ruim", 120, 200),
    Faixa(5, "Péssima", 200, math.inf)
]
poluentes = [
    Poluente("MP10", [
        Concentracao(1, 0, 50),
        Concentracao(2, 50, 100),
        Concentracao(3, 100, 150),
        Concentracao(4, 150, 250),
        Concentracao(5, 250, math.inf),
    ]),
    Poluente("MP2,5", [
        Concentracao(1, 0, 25),
        Concentracao(2, 25, 50),
        Concentracao(3, 50, 75),
        Concentracao(4, 75, 125),
        Concentracao(5, 125, math.inf),
    ]),
    Poluente("O3", [
        Concentracao(1, 0, 100),
        Concentracao(2, 100, 130),
        Concentracao(3, 130, 160),
        Concentracao(4, 160, 200),
        Concentracao(5, 200, math.inf),
    ]),
    Poluente("CO", [
        Concentracao(1, 0, 9),
        Concentracao(2, 9, 11),
        Concentracao(3, 11, 13),
        Concentracao(4, 13, 15),
        Concentracao(5, 15, math.inf),
    ]),
    Poluente("NO3", [
        Concentracao(1, 0, 200),
        Concentracao(2, 200, 240),
        Concentracao(3, 240, 320),
        Concentracao(4, 320, 1130),
        Concentracao(5, 1130, math.inf),
    ]),
    Poluente("SO2", [
        Concentracao(1, 0, 20),
        Concentracao(2, 20, 40),
        Concentracao(3, 40, 365),
        Concentracao(4, 365, 800),
        Concentracao(5, 800, math.inf),
    ]),
]

class PoluenteOperation:
    poluente = None
    input = 0
    index = 0
    faixa = 0
    concentracao = 0
    def __init__(self, poluente, input):
        self.poluente = poluente
        self.input = input

def input_poluentes(poluentes):
    operations = []
    for poluente in poluentes:
        input = poluente.input_concentracao()
        operations.append(PoluenteOperation(poluente, input))
    return operations

def calculate_faixas(poluente_operations):
    for poluente_operation in poluente_operations:
        (faixa, concentracao_index) = poluente_operation.poluente.get_faixa(poluente_operation.input, faixas)
        poluente_operation.faixa = faixa
        poluente_operation.concentracao = concentracao_index

def calculate_indexes(poluente_operations, faixas):
    for poluente_operation in poluente_operations:
        faixa = get_faixa_by_id(poluente_operation.faixa, faixas)
        poluente_operation.index = poluente_operation.poluente.calculate_index(poluente_operation.input, poluente_operation.concentracao, faixa)

def print_results(poluente_operations, faixas):
    for poluente_operation in poluente_operations:
        faixa = get_faixa_by_id(poluente_operation.faixa, faixas)
        print(f"Poluente {poluente_operation.poluente.name} possui índice {poluente_operation.index}, qualidade {faixa.qualidade}")

def get_faixa_by_id(id, faixas):
    for faixa in faixas:
        if faixa.id == id:
            return faixa

def get_worst_poluente(poluente_operations):
    max = poluente_operations[0]
    for poluente_operation in poluente_operations:
        if math.isnan(poluente_operation.index):
            return poluente_operation
        if poluente_operation.index > max.index:
            max = poluente_operation
    return max

def print_general_result(operation, faixas):
    faixa = get_faixa_by_id(operation.faixa, faixas)
    print(f"Índice da qualidade do ar: {operation.index}, qualidade {faixa.qualidade} definida pelo poluente {operation.poluente.name}")

operations = input_poluentes(poluentes)
calculate_faixas(operations)
calculate_indexes(operations, faixas)
print_results(operations, faixas)

worst_poluente = get_worst_poluente(operations)
print_general_result(worst_poluente, faixas)
