from experta import *

class Greetings(KnowledgeEngine):

    def __init__(self, doencas_map, nao_encontrado):
        self.doencas_map = doencas_map
        self.nao_encontrado = nao_encontrado
        KnowledgeEngine.__init__(self)

    # code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Sistema especialista de auxilio médico")
        print("")
        print("Você está sentindo algum desses sintomas?")
        print("Responda sim ou não")
        print("")
        yield Fact(action="procurar_doenca")

    # perguntar ao usuario
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_de_cabeca=W())), salience=26)
    def sintoma_0(self):
        self.declare(Fact(dor_de_cabeca=input("dor de cabeça: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(febre=W())), salience=25)
    def sintoma_1(self):
        self.declare(Fact(febre=input("febre: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tontura=W())), salience=24)
    def sintoma_2(self):
        self.declare(Fact(tontura=input("tontura: ")))    
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_olho=W())), salience=23)
    def sintoma_3(self):
        self.declare(Fact(dor_olho=input("dor no olho: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(perda_paladar_apetite=W())), salience=22)
    def sintoma_4(self):
        self.declare(Fact(perda_paladar_apetite=input("perda no paladar e no apetite: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(manchas_erupcoes=W())), salience=21)
    def sintoma_5(self):
        self.declare(Fact(manchas_erupcoes=input("manchas e erupçoes na pele: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(cansaco=W())), salience=20)
    def sintoma_6(self):
        self.declare(Fact(cansaco=input("cansaço: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_corpo=W())), salience=19)
    def sintoma_7(self):
        self.declare(Fact(dor_corpo=input("dor no corpo: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_osso_articulacao=W())), salience=18)
    def sintoma_8(self):
        self.declare(Fact(dor_osso_articulacao=input("dor nos ossos e nas articulações: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_abdominal=W())), salience=17)
    def sintoma_9(self):
        self.declare(Fact(dor_abdominal=input("dor abdominal: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(nausea_vomito=W())), salience=16)
    def sintoma_10(self):
        self.declare(Fact(nausea_vomito=input("nausea e vomito: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tosse=W())), salience=15)
    def sintoma_11(self):
        self.declare(Fact(tosse=input("tosse: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(calafrio=W())), salience=14)
    def sintoma_12(self):
        self.declare(Fact(calafrio=input("calafrio: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(suores=W())), salience=13)
    def sintoma_13(self):
        self.declare(Fact(suores=input("suores: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fraqueza=W())), salience=12)
    def sintoma_14(self):
        self.declare(Fact(fraqueza=input("fraqueza: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(diarreia=W())), salience=11)
    def sintoma_15(self):
        self.declare(Fact(diarreia=input("diarreia: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(coceira_anal=W())), salience=10)
    def sintoma_16(self):
        self.declare(Fact(coceira_anal=input("coceira_anal: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(palpitacao=W())), salience=9)
    def sintoma_17(self):
        self.declare(Fact(palpitacao=input("palpitação: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(impotencia=W())), salience=8)
    def sintoma_18(self):
        self.declare(Fact(impotencia=input("impotencia: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(emagrecimento=W())), salience=7)
    def sintoma_19(self):
        self.declare(Fact(emagrecimento=input("emagrecimento: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(end_aum_figado=W())), salience=6)
    def sintoma_20(self):
        self.declare(Fact(end_aum_figado=input("endurecimento ou aumento do figado: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_muscular=W())), salience=5)
    def sintoma_21(self):
        self.declare(Fact(dor_muscular=input("dor muscular: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(sens_plen_gastr=W())), salience=4)
    def sintoma_22(self):
        self.declare(Fact(sens_plen_gastr=input("sensação de plenitude gastrica: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_costas=W())), salience=3)
    def sintoma_23(self):
        self.declare(Fact(dor_costas=input("dores nas costas: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_articulacao=W())), salience=2)
    def sintoma_24(self):
        self.declare(Fact(dor_articulacao=input("dor articulacao: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(mal_estar=W())), salience=1)
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
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="sim"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="sim"),
        Fact(calafrio="sim"),
        Fact(suores="sim"),
        Fact(fraqueza="sim"),
        Fact(diarreia="sim"),
        Fact(coceira_anal="sim"),
        Fact(palpitacao="sim"),
        Fact(impotencia="sim"),
        Fact(emagrecimento="sim"),
        Fact(end_aum_figado="sim"),        
        Fact(dor_muscular="sim"),
        Fact(sens_plen_gastr="sim"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"),
    )
    def doenca_0(self):
        self.declare(Fact(doenca="Esquistossomose"))


    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="alta"),
        Fact(febre="alta"),
        Fact(tontura="alta"),
        Fact(dor_olho="alta"),
        Fact(perda_paladar_apetite="alta"),
        Fact(manchas_erupcoes="alta"),
        Fact(cansaco="alta"),
        Fact(dor_corpo="alta"),
        Fact(dor_osso_articulacao="alta"),
        Fact(dor_abdominal="alta"),
        Fact(nausea_vomito="alta"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"),
    )
    def doenca_1(self):
        self.declare(Fact(doenca="Dengue"))


    @Rule(       
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="sim"),
        Fact(tosse="nao"),
        Fact(calafrio="sim"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="sim"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="sim"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="sim"), 
    )
    def doenca_2(self):
        self.declare(Fact(doenca="Febre Amarela"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="sim"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="sim"),
        Fact(dor_articulacao="sim"),
        Fact(mal_estar="nao"), 
    )
    def doenca_3(self):
        self.declare(Fact(doenca="Febre de Chikungunya"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="nao"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="nao"),
        Fact(calafrio="sim"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"),
    )
    def doenca_4(self):
        self.declare(Fact(doenca="Filariose"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="nao"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="sim"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"),
    )
    def doenca_5(self):
        self.declare(Fact(doenca="Hanseniase"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="sim"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"), 
    )
    def doenca_6(self):
        self.declare(Fact(doenca="Hepatite A"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="sim"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="sim"), 
    )
    def doenca_7(self):
        self.declare(Fact(doenca="Hepatite B"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="nao"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="sim"),
        Fact(dor_corpo="sim"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="sim"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="sim"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"),
    )
    def doenca_8(self):
        self.declare(Fact(doenca="Hepatite C"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="sim"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="sim"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="sim"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"), 
    )
    def doenca_9(self):
        self.declare(Fact(doenca="Hepatite D"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"), 
    )
    def doenca_10(self):
        self.declare(Fact(doenca="Leishmanioses"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="sim"),
        Fact(tosse="nao"),
        Fact(calafrio="sim"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"), 
    )
    def doenca_11(self):
        self.declare(Fact(doenca="Malaria"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="sim"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="nao"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"), 
    )
    def doenca_12(self):
        self.declare(Fact(doenca="Tuberculose"))

    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="sim"),
        Fact(perda_paladar_apetite="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso_articulacao="nao"),
        Fact(dor_abdominal="sim"),
        Fact(nausea_vomito="nao"),
        Fact(tosse="nao"),
        Fact(calafrio="nao"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="sim"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="sim"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"), 
    )
    def doenca_13(self):
        self.declare(Fact(doenca="Zika Virus"))

    # when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="procurar_doenca"), Fact(doenca=MATCH.doenca), salience=-998)
    def doenca(self, doenca):
        print("")
        id_disease = doenca
        print("")
        print("Os sintomas coincidem com %s\n" % (id_disease))
        print("")
        print("")
        
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca=MATCH.dor_de_cabeca),
        Fact(febre=MATCH.febre),
        Fact(tontura=MATCH.tontura),
        Fact(dor_olho=MATCH.dor_olho),
        Fact(perda_paladar_apetite=MATCH.perda_paladar_apetite),
        Fact(manchas_erupcoes=MATCH.manchas_erupcoes),
        Fact(cansaco=MATCH.cansaco),
        Fact(dor_corpo=MATCH.dor_corpo),
        Fact(dor_osso_articulacao=MATCH.dor_osso_articulacao),
        Fact(dor_abdominal=MATCH.dor_abdominal),
        Fact(nausea_vomito=MATCH.nausea_vomito),
        Fact(tosse=MATCH.tosse),
        Fact(calafrio=MATCH.calafrio),
        Fact(suores=MATCH.suores),
        Fact(fraqueza=MATCH.fraqueza),
        Fact(diarreia=MATCH.diarreia),
        Fact(coceira_anal=MATCH.coceira_anal),
        Fact(palpitacao=MATCH.palpitacao),
        Fact(impotencia=MATCH.impotencia),
        Fact(emagrecimento=MATCH.emagrecimento),
        Fact(end_aum_figado=MATCH.end_aum_figado),
        Fact(dor_muscular=MATCH.dor_muscular),
        Fact(sens_plen_gastr=MATCH.sens_plen_gastr),
        Fact(dor_costas=MATCH.dor_costas),
        Fact(dor_articulacao=MATCH.dor_articulacao),
        Fact(mal_estar=MATCH.mal_estar),
        NOT(Fact(doenca=MATCH.doenca)),
        salience=-999
    )

    def not_matched(
        self,
        dor_de_cabeca,
        febre,
        tontura,
        dor_olho,
        perda_paladar_apetite,
        manchas_erupcoes,
        cansaco,
        dor_corpo,
        dor_osso_articulacao,
        dor_abdominal,
        nausea_vomito,
        tosse,
        calafrio,
        suores,
        fraqueza,
        diarreia,
        coceira_anal,
        palpitacao,
        impotencia,
        emagrecimento,
        end_aum_figado,
        dor_muscular,
        sens_plen_gastr,
        dor_costas,
        dor_articulacao,
        mal_estar,
    ):
        print("\nNão foi encontrado nenhuma doença que coincide exatamentecom os sintomas informados.")
        lis = [
            dor_de_cabeca,
            febre,
            tontura,
            dor_olho,
            perda_paladar_apetite,
            manchas_erupcoes,
            cansaco,
            dor_corpo,
            dor_osso_articulacao,
            dor_abdominal,
            nausea_vomito,
            tosse,
            calafrio,
            suores,
            fraqueza,
            diarreia,
            coceira_anal,
            palpitacao,
            impotencia,
            emagrecimento,
            end_aum_figado,
            dor_muscular,
            sens_plen_gastr,
            dor_costas,
            dor_articulacao,
            mal_estar,
        ]
        max_count = 0
        max_disease = ""
        for key, val in self.doencas_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and (lis[j] == "alta" or lis[j] == "baixa" or lis[j] == "sim" or lis[j] == "nao"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if max_disease != "":
            self.nao_encontrado(max_disease)