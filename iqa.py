description = [
    "Nenhuma restrição.",
    "Pessoas de grupos sensiveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.",
    "Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensiveis (crianças, idosos e pessoas com doengas respiratórias e cardiacas) podem apresentar efeitos mais sérios na saúde.",
    "Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saude de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas).",
    "Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensiveis."
]
class Iqa:
    poluentes = []
    def __init__(self, poluentes):
        self.poluentes = poluentes

    def start(self):
        for poluente in self.poluentes:
            poluente.start()
        for poluente in self.poluentes:
            poluente.print_result()

    def reset(self):
        for poluente in self.poluentes:
            poluente.reset()

    def print_result(self):
        worst_poluente = self.__get_worst_poluente()
        description = self.__get_description(worst_poluente.limite)
        quality = worst_poluente.quality
        iqa = worst_poluente.iqa

        print(f"\nO poluente mais prejudicial é {worst_poluente.name} com um iqa de {iqa} e qualidade {quality}.")
        print(f"Descrição: {description}")

    def __get_description(self, limite):
        return description[limite]

    def __get_worst_poluente(self):
        worst_poluente = self.poluentes[0]
        for poluente in self.poluentes:
            if poluente.iqa > worst_poluente.iqa:
                worst_poluente = poluente
        return worst_poluente
