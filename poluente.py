class Poluente:
    name = ""
    intervalos = []
    limites = []
    inputted_concentracao = 0
    iqa = 0
    limite = 0
    intervalo = 0
    quality = ""
    done = False

    def __init__(self, name, limites, intervalos):
        self.name = name
        self.intervalos = intervalos
        self.limites = limites

    def reset(self):
        self.inputted_concentracao = 0
        self.iqa = 0
        self.limite = 0
        self.intervalo = 0
        self.quality = ""
        self.done = False

    def start(self, concentracao=None):
        if concentracao != None:
            self.inputted_concentracao = concentracao
        else:
            self.inputted_concentracao = self.__input_concentracao()
        self.iqa = self.__calculate_iqa()
        self.done = True

    def print_result(self):
        self.quality = self.__get_air_quality()
        print(f"A concentração de {self.name} é {self.inputted_concentracao} e o IQA é {self.iqa}, qualidade do ar: {self.quality}")

    def __input_concentracao(self):
        concentracao = input_float(f"Digite a concentração de {self.name}: ")
        return concentracao

    def __calculate_iqa(self):
        concentracao = self.inputted_concentracao
        (If, Ii, Cf, Ci) = self.__get_range()
        if (If == None or Ii == None or Cf == None or Ci == None):
            self.iqa = self.intervalos[-1]
            return self.intervalos[-1]

        iqa = calculate_index(If, Ii, Cf, Ci, concentracao)
        self.iqa = iqa
        return iqa

    def __get_range(self):
        concentracao = self.inputted_concentracao
        if concentracao == 0:
            return (self.limites[0], self.limites[1], self.intervalos[0], self.intervalos[1])
        for i in range(len(self.intervalos) - 1):
            if concentracao > self.intervalos[i] and concentracao <= self.intervalos[i + 1]:
                return (self.limites[i], self.limites[i + 1], self.intervalos[i], self.intervalos[i + 1])
        return (None, None, None, None)

    def __get_air_quality(self):
        qualities = ["Bom", "Moderado", "Ruim", "Muito Ruim", "Péssimo"]
        if self.iqa == 0:
            self.limite = 0
            return qualities[0]
        for i in range(len(self.limites) - 1):
            if self.iqa > self.limites[i] and self.iqa <= self.limites[i + 1]:
                self.limite = i
                return qualities[i]
        self.limite = len(self.limites) - 1
        return qualities[-1]

def calculate_index(If, Ii, Cf, Ci, C):
    return ((If - Ii)/(Cf - Ci)) * (C - Ci) + Ii

def input_float(message):
    try:
        return float(input(message))
    except:
        print("Digite apenas números!")
        return input_float(message)
