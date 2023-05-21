from poluente import Poluente
from iqa import Iqa

limites = [0, 40, 80, 120, 200]
poluentes = [
    Poluente("MP10", limites, [0, 50, 100, 150, 250]),
    Poluente("MP2.5", limites, [0, 25, 50, 75, 125]),
    Poluente("O3", limites, [0, 100, 130, 160, 200]),
    Poluente("CO", limites, [0, 9, 11, 13, 15]),
    Poluente("NO2", limites, [0, 200, 240, 320, 1130]),
    Poluente("SO2", limites, [0, 20, 40, 365, 800])
]
iqa = Iqa(poluentes)

print("Programa para cálculo do Índice de Qualidade do Ar (IQA)\n")

while True:
    exit = iqa.start()

    if exit:
        break

    iqa.reset()
    print("\n")

print("\nObrigado por usar o programa! :)")
