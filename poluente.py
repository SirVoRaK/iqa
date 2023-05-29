from colors import Colors


class Poluente:
    name = ""
    intervalos = []
    limites = []
    inputted_concentracao = 0
    iqa = 0
    limite = 0
    intervalo = 0
    quality = ""

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

    def calculate_iqa(self, concentracao):
        self.inputted_concentracao = concentracao
        self.iqa = self.__calculate_iqa()
        return self.iqa

    def input_concentracao(self):
        return input_float(f"{Colors.YELLOW}{self.name}:{Colors.RESET} ")

    def __calculate_iqa(self):
        concentracao = self.inputted_concentracao
        (If, Ii, Cf, Ci) = self.__get_range()
        if (If == None or Ii == None or Cf == None or Ci == None):
            self.iqa = self.intervalos[-1]
            return self.intervalos[-1]

        iqa = calculate_index(If, Ii, Cf, Ci, concentracao)
        self.iqa = iqa
        self.quality = self.__get_air_quality()
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
        Colors.print("Digite apenas números!", Colors.RED)
        return input_float(message)
