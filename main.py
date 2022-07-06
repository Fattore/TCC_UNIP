from rules import Rules
from experta import *
lista_doencas = []
doencas_sintomas = []
doencas_map = {}


# loads the knowledge from .txt files into variables to allow the code to use it
def preprocess():
    #global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    doencas = open("doencas.txt")
    doencas_t = doencas.read()
    lista_doencas = doencas_t.split("\n")
    doencas.close()

    for doenca in lista_doencas:
        doencas_s_file = open("Sintomas/" + doenca + ".txt")
        doencas_s_data = doencas_s_file.read()
        s_list = doencas_s_data.split("\n")
        doencas_sintomas.append(s_list)
        doencas_map[str(s_list)] = doenca
        doencas_s_file.close()


def identificar_doenca(*arguments):
    sintoma_list = []
    for sintoma in arguments:
        sintoma_list.append(sintoma)

    return doencas_map[str(sintoma_list)]


def if_not_matched(doenca):
    print("")
    id_disease = doenca
    print("")
    print("The most probable disease that you have is %s\n" % (id_disease))
    print("not matched")


# driver function
if __name__ == "__main__":
    preprocess()
    # creating class object
    engine = Rules(doencas_map, if_not_matched)
    # loop to keep running the code until user says no when asked for another diagnosis
    while 1:
        engine.reset()
        engine.run()
        print("Would you like to diagnose some other symptoms?\n Reply sim or nao")
        if input() == "nao":
            exit()
