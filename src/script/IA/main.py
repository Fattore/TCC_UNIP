import sys
import os 
import eventlet
import socketio
from greetings import Greetings
lista_doencas = []
doencas_sintomas = []
doencas_map = {}
cwd = os.getcwd() 

sio = socketio.Server()
app = socketio.WSGIApp(sio)


# loads the knowledge from .txt files into variables to allow the code to use it
def preprocess():
    #global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    doencas = open(cwd+"/src/script/IA/doencas.txt")
    doencas_t = doencas.read()
    lista_doencas = doencas_t.split("\n")
    doencas.close()

    for doenca in lista_doencas:
        doencas_s_file = open(cwd+"/src/script/IA/Sintomas/" + doenca + ".txt")
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

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on('get-data-python')
def msg(sid, data):
    print('message ', data)

    preprocess()
    engine = Greetings(doencas_map, nao_encontrado, data)
    engine.reset()
    engine.run()
    resultado = ""

    if(engine.max_disease != ""):
        resultado = engine.max_disease + "_" +  engine.max_count.__str__() + "_"

    if(engine.mid_disease != ""):
        resultado = resultado + engine.mid_disease + "_" +  engine.mid_count.__str__() + "_"

    if(engine.min_disease != ""):
        resultado = resultado + engine.min_disease + "_" +  engine.min_count.__str__() + "_"


    # print(engine.max_disease)
    return "OK", resultado
@sio.event
def disconnect(sid):
    print('disconnect ', sid)

# driver function
if __name__ == "__main__":
    print("PYTHON MAIN INICIADO")
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

    # preprocess()

    # creating class object
    # engine = Greetings(doencas_map, nao_encontrado, sys.argv[1])
    # # loop to keep running the code until user says no when asked for another diagnosis
    # while 1:
    #     engine.reset()
    #     engine.run()
    #     print(engine.max_disease)
    #     # print(str(sys.argv))
    #     print("Gostaria de diagnosticar algum outro sintoma?\n Responda sim ou não.")
    #     if input() == "nao":
    #         exit()

# sys.stdout.flush()