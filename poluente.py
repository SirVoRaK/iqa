import math
class Poluente:
    name = ""
    concentracoes = []
    def __init__(self, name, concentracoes):
        self.name = name
        self.concentracoes = concentracoes
    
    def input_concentracao(self):
        concentracao = input_float(f"Digite o valor de {self.name}: ")
        return concentracao
    
    def get_faixa(self, concentracao_digitada, faixas):
        for index in range(0, len(self.concentracoes)):
            concentracao = self.concentracoes[index]
            faixa = get_faixa_by_id(concentracao.faixa_id, faixas)
            if concentracao_digitada > concentracao.min and concentracao_digitada <= concentracao.max:
                return (concentracao.faixa_id, index)
    
    def calculate_index(self, concentracao_digitada, concentracao_index, faixa):
        concentracao = self.concentracoes[concentracao_index]
        index = calculate_index(faixa.max, faixa.min + 1, concentracao.max, concentracao.min, concentracao_digitada)
        return index

def calculate_index(If, Ii, Cf, Ci, C):
    return ((If - Ii)/(Cf - Ci)) * (C - Ci) + Ii

def input_float(message):
    try:
        return float(input(message))
    except:
        print("Digite apenas números!")
        return input_float(message)

class Concentracao:
    faixa_id = 0
    min = 0
    max = 0
    def __init__(self, faixa_id, min, max):
        self.faixa_id = faixa_id
        self.min = min
        self.max = max

def get_faixa_by_id(id, faixas):
    for faixa in faixas:
        if faixa.id == id:
            return faixa