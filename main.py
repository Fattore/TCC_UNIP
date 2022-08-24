from greetings import Greetings
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


def nao_encontrado(max_disease, max_count, mid_disease, mid_count, min_disease, min_count):
    print("")
    id_disease = max_disease
    print("")
    print("A doença mais provavel é %s\n" % (id_disease))
    print("%s sintomas foram compativeis.\n" % (max_count))
    print("")
    print("")

    if mid_count != "":
        print("A segunda doença mais provavel é %s\n" % (mid_disease))
        print("%s sintomas foram compativeis.\n" % (mid_count))
        print("")
        print("")

        if min_count != "":
            print("A terceira doença mais provavel é %s\n" % (min_disease))
            print("%s sintomas foram compativeis.\n" % (min_count))
            print("")
            print("")



# driver function
if __name__ == "__main__":
    preprocess()
    # creating class object
    engine = Greetings(doencas_map, nao_encontrado)
    # loop to keep running the code until user says no when asked for another diagnosis
    while 1:
        engine.reset()
        engine.run()
        print("Gostaria de diagnosticar algum outro sintoma?\n Responda sim ou não.")
        if input() == "nao":
            exit()
