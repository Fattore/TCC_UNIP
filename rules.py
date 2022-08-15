from experta import *


class Rules(KnowledgeEngine):

    def __init__(self, lista_sintomas, nao_encontrado):
        self.lista_sintomas = lista_sintomas
        self.nao_encontrado = nao_encontrado
        KnowledgeEngine.__init__(self)

# code giving instructions on how to use the Expert System


    @DefFacts()
    def _initial_action(self):
        print("")
        print("This is a knowledge based bot to diagnose diseases")
        print("")
        print("Do you feel any of the following symptoms?")
        print("Reply alta or baixa or nao")
        print("")
        yield Fact(action="procurar_doenca")

# perguntar ao usuario


    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_de_cabeca=W())), salience=99)
    def sintoma_0(self):
        self.declare(Fact(dor_de_cabeca=input("dor de cabeça: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(febre=W())), salience=98)
    def sintoma_1(self):
        self.declare(Fact(febre=input("febre: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tontura=W())), salience=97)
    def sintoma_2(self):
        self.declare(Fact(tontura=input("tontura: ")))    
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_olho=W())), salience=96)
    def sintoma_3(self):
        self.declare(Fact(dor_olho=input("dor no olho: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(perda_paladar_apetite=W())), salience=95)
    def sintoma_4(self):
        self.declare(Fact(perda_paladar_apetite=input("perda no paladar e no apetite: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(manchas_erupcoes=W())), salience=94)
    def sintoma_5(self):
        self.declare(Fact(manchas_erupcoes=input("manchas e erupçoes na pele: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(cansaco=W())), salience=93)
    def sintoma_6(self):
        self.declare(Fact(cansaco=input("cansaço: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_corpo=W())), salience=92)
    def sintoma_7(self):
        self.declare(Fact(dor_corpo=input("dor no corpo: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_osso_articulacao=W())), salience=91)
    def sintoma_8(self):
        self.declare(Fact(dor_osso_articulacao=input("dor nos ossos e nas articulações: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_abdominal=W())), salience=90)
    def sintoma_9(self):
        self.declare(Fact(dor_abdominal=input("dor abdominal: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(nausea_vomito=W())), salience=89)
    def sintoma_10(self):
        self.declare(Fact(nausea_vomito=input("nausea e vomito: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tosse=W())), salience=88)
    def sintoma_11(self):
        self.declare(Fact(tosse=input("tosse: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(calafrio=W())), salience=87)
    def sintoma_12(self):
        self.declare(Fact(calafrio=input("calafrio: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(suores=W())), salience=86)
    def sintoma_13(self):
        self.declare(Fact(suores=input("suores: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fraqueza=W())), salience=85)
    def sintoma_14(self):
        self.declare(Fact(fraqueza=input("fraqueza: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(diarreia=W())), salience=84)
    def sintoma_15(self):
        self.declare(Fact(diarreia=input("diarreia: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(coceira_anal=W())), salience=83)
    def sintoma_16(self):
        self.declare(Fact(coceira_anal=input("coceira_anal: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(palpitacao=W())), salience=82)
    def sintoma_17(self):
        self.declare(Fact(palpitacao=input("palpitação: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(impotencia=W())), salience=81)
    def sintoma_18(self):
        self.declare(Fact(impotencia=input("impotencia: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(emagrecimento=W())), salience=80)
    def sintoma_19(self):
        self.declare(Fact(emagrecimento=input("emagrecimento: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(end_aum_figado=W())), salience=79)
    def sintoma_20(self):
        self.declare(Fact(end_aum_figado=input("endurecimento ou aumento do figado: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_muscular=W())), salience=78)
    def sintoma_21(self):
        self.declare(Fact(dor_muscular=input("dor muscular: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(sens_plen_gastr=W())), salience=77)
    def sintoma_22(self):
        self.declare(Fact(sens_plen_gastr=input("sensação de plenitude gastrica: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_costas=W())), salience=76)
    def sintoma_23(self):
        self.declare(Fact(dor_costas=input("dores nas costas: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_articulacao=W())), salience=75)
    def sintoma_24(self):
        self.declare(Fact(dor_articulacao=input("dor articulacao: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(mal_estar=W())), salience=74)
    def sintoma_25(self):
        self.declare(Fact(mal_estar=input("mal estar: ")))





    
    


    ###@Rule(Fact(action="procurar_doenca"), NOT(Fact(sens_plen_gastr=W())), salience=3)
    ###def sintoma_7(self):
        ###self.declare(Fact(sens_plen_gastr=input("sensação de plenitude gastrica: ")))
    


    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="sim"),
        Fact(dor_olho="sim"),
        Fact(perda_paladar_apetite="sim"),
        Fact(manchas_erupcoes="sim"),
        Fact(cansaco="sim"),
        Fact(dor_corpo="sim"),
        Fact(dor_osso_articulacao="sim"),
        Fact(dor_abdominal="sim"),
        Fact(nausea_vomito="sim"),
    )
    def doenca_0(self):
        self.declare(Fact(doenca="Dengue"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="sim"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="sim"),
        Fact(calafrio="sim"),
        Fact(tontura="sim"),
        Fact(diarreia="sim"),
        Fact(mal_estar="nao"),
    )
    def doenca_1(self):
        self.declare(Fact(doenca="Esquistossomose"))


    @Rule(       
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(calafrio="sim"),
        Fact(nausea_vomito="sim"),
        Fact(diarreia="sim"),
        Fact(mal_estar="sim"),
    )
    def doenca_2(self):
        self.declare(Fact(doenca="Febre Amarela"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(dor_costas="sim"),
        Fact(dor_articulacao="sim"),
    )
    def doenca_3(self):
        self.declare(Fact(doenca="Febre de Chikungunya"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_4(self):
        self.declare(Fact(doenca="Filariose"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_5(self):
        self.declare(Fact(doenca="Hanseniase"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="sim"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="sim"),
        Fact(nausea_vomito="sim"),      
    )
    def doenca_6(self):
        self.declare(Fact(doenca="Hepatite A"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_7(self):
        self.declare(Fact(doenca="Hepatite B"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_8(self):
        self.declare(Fact(doenca="Hepatite C"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_9(self):
        self.declare(Fact(doenca="Hepatite D"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_10(self):
        self.declare(Fact(doenca="Leishmanioses"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="alta"),
    )
    def doenca_11(self):
        self.declare(Fact(doenca="Malaria"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_12(self):
        self.declare(Fact(doenca="Tuberculose"))

    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="baixa"),
        Fact(febre="alta"),
    )
    def doenca_13(self):
        self.declare(Fact(doenca="Zika Virus"))


  

    # when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="procurar_doenca"), Fact(doenca=MATCH.doenca), salience=-998)
    def doenca(self, doenca):
        print("")
        id_disease = doenca
        print("")
        print("Your symptoms match %s\n" % (id_disease))
        print(
            "The common medications and procedures suggested by other real doctors are: \n"
        )


    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca=MATCH.dor_de_cabeca),
        Fact(febre=MATCH.febre),
        NOT(Fact(doenca=MATCH.doenca)),
        salience=-999
    )
    def not_matched(
        self,
        dor_de_cabeca,
        febre,
    ):
        print("\nThe bot did not find any diseases that match your exact symptoms.")
        lis = [
            dor_de_cabeca,
            febre,
        ]
        max_count = 0
        max_disease = ""
        for key, val in self.lista_sintomas.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and (lis[j] == "alta" or lis[j] == "baixa" or lis[j] == "sim"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if max_disease != "":
            self.nao_encontrado(max_disease)
