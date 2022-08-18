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
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_de_cabeca=W())), salience=90)
    def sintoma_0(self):
        self.declare(Fact(dor_de_cabeca=input("dor de cabeça: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(febre=W())), salience=89)
    def sintoma_1(self):
        self.declare(Fact(febre=input("febre: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tontura=W())), salience=88)
    def sintoma_2(self):
        self.declare(Fact(tontura=input("tontura: ")))    
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_olho=W())), salience=87)
    def sintoma_3(self):
        self.declare(Fact(dor_olho=input("dor no olho: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(perda_paladar=W())), salience=86)
    def sintoma_4(self):
        self.declare(Fact(perda_paladar=input("perda no paladar e no apetite: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(manchas_erupcoes=W())), salience=85)
    def sintoma_5(self):
        self.declare(Fact(manchas_erupcoes=input("manchas ou erupçoes na pele: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(cansaco=W())), salience=84)
    def sintoma_6(self):
        self.declare(Fact(cansaco=input("cansaço: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_corpo=W())), salience=83)
    def sintoma_7(self):
        self.declare(Fact(dor_corpo=input("dor no corpo: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_osso=W())), salience=82)
    def sintoma_8(self):
        self.declare(Fact(dor_osso=input("dor nos ossos ou nas articulações: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_abdominal=W())), salience=81)
    def sintoma_9(self):
        self.declare(Fact(dor_abdominal=input("dor abdominal: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(nausea_vomito=W())), salience=80)
    def sintoma_10(self):
        self.declare(Fact(nausea_vomito=input("nausea ou vomito: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tosse=W())), salience=79)
    def sintoma_11(self):
        self.declare(Fact(tosse=input("tosse: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(calafrio=W())), salience=78)
    def sintoma_12(self):
        self.declare(Fact(calafrio=input("calafrio: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(suores=W())), salience=77)
    def sintoma_13(self):
        self.declare(Fact(suores=input("suores: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fraqueza=W())), salience=76)
    def sintoma_14(self):
        self.declare(Fact(fraqueza=input("fraqueza: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(diarreia=W())), salience=75)
    def sintoma_15(self):
        self.declare(Fact(diarreia=input("diarreia: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(coceira_anal=W())), salience=74)
    def sintoma_16(self):
        self.declare(Fact(coceira_anal=input("coceira_anal: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(palpitacao=W())), salience=73)
    def sintoma_17(self):
        self.declare(Fact(palpitacao=input("palpitação: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(impotencia=W())), salience=72)
    def sintoma_18(self):
        self.declare(Fact(impotencia=input("impotencia: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(emagrecimento=W())), salience=71)
    def sintoma_19(self):
        self.declare(Fact(emagrecimento=input("emagrecimento: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(end_aum_figado=W())), salience=70)
    def sintoma_20(self):
        self.declare(Fact(end_aum_figado=input("endurecimento ou aumento do figado: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_muscular=W())), salience=69)
    def sintoma_21(self):
        self.declare(Fact(dor_muscular=input("dor muscular: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(sens_plen_gastr=W())), salience=68)
    def sintoma_22(self):
        self.declare(Fact(sens_plen_gastr=input("sensação de plenitude gastrica: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_costas=W())), salience=67)
    def sintoma_23(self):
        self.declare(Fact(dor_costas=input("dores nas costas: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_articulacao=W())), salience=66)
    def sintoma_24(self):
        self.declare(Fact(dor_articulacao=input("dor articulacao: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(mal_estar=W())), salience=65)
    def sintoma_25(self):
        self.declare(Fact(mal_estar=input("mal estar: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(acumulo_liq=W())), salience=64)
    def sintoma_26(self):
        self.declare(Fact(acumulo_liq=input("Acumulo de liquido nas pernas ou braços: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(anemia_intensa=W())), salience=63)
    def sintoma_27(self):
        self.declare(Fact(anemia_intensa=input("Anemia instensa: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(anorexia=W())), salience=62)
    def sintoma_28(self):
        self.declare(Fact(anorexia=input("Anorexia: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(astenia=W())), salience=61)
    def sintoma_29(self):
        self.declare(Fact(astenia=input("Astenia: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(aum_baco=W())), salience=60)
    def sintoma_30(self):
        self.declare(Fact(aum_baco=input("Aumento do baço: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(aum_testiculo=W())), salience=59)
    def sintoma_31(self):
        self.declare(Fact(aum_testiculo=input("Aumento do volume do testículo: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(aum_ganglios=W())), salience=58)
    def sintoma_32(self):
        self.declare(Fact(aum_ganglios=input("Aumento dos gânglios linfáticos: ")))
   
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(cefaleia=W())), salience=57)
    def sintoma_33(self):
        self.declare(Fact(cefaleia=input("Cefaleia: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(coceira=W())), salience=56)
    def sintoma_34(self):
        self.declare(Fact(coceira=input("Coceira: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(comp_nervos=W())), salience=55)
    def sintoma_35(self):
        self.declare(Fact(comp_nervos=input("Comprometimento do(s) nervo(s) periférico(s): ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(constipacao=W())), salience=54)
    def sintoma_36(self):
        self.declare(Fact(constipacao=input("Constipação: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(convulsao=W())), salience=53)
    def sintoma_37(self):
        self.declare(Fact(convulsao=input("Convulsão: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dim_pelo_suor=W())), salience=52)
    def sintoma_38(self):
        self.declare(Fact(dim_pelo_suor=input("Diminuição de pelo e/ou suor: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dim_sens_face=W())), salience=51)
    def sintoma_39(self):
        self.declare(Fact(dim_sens_face=input("Diminuição ou ausência da sensibilidade muscular na face: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dispineia=W())), salience=50)
    def sintoma_40(self):
        self.declare(Fact(dispineia=input("Dispineia: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(enjoo=W())), salience=49)
    def sintoma_41(self):
        self.declare(Fact(enjoo=input("Enjoo: ")))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(est_confusional=W())), salience=48)
    def sintoma_42(self):
        self.declare(Fact(est_confusional=input("Estado confusional agudo: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fadiga=W())), salience=47)
    def sintoma_43(self):
        self.declare(Fact(fadiga=input("Fadiga: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fezes_claras=W())), salience=46)
    def sintoma_44(self):
        self.declare(Fact(fezes_claras=input("Fezes claras: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fisgadas=W())), salience=45)
    def sintoma_45(self):
        self.declare(Fact(fisgadas=input("Fisgadas: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(formigamento=W())), salience=44)
    def sintoma_46(self):
        self.declare(Fact(formigamento=input("Formigamento: ")))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fotoboia=W())), salience=43)
    def sintoma_47(self):
        self.declare(Fact(fotoboia=input("Fotofobia: ")))


    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="sim"),
        Fact(dor_olho="sim"),
        Fact(perda_paladar="sim"),
        Fact(manchas_erupcoes="sim"),
        Fact(cansaco="sim"),
        Fact(dor_corpo="sim"),
        Fact(dor_osso="sim"),
        Fact(dor_abdominal="sim"),
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
        Fact(dor_articulacao="sim"),
        Fact(mal_estar="nao"),
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_0(self):
        self.declare(Fact(doenca="Dengue"))

    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="sim"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),

    )
    def doenca_1(self):
        self.declare(Fact(doenca="Esquistossomose"))


    @Rule(       
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="nao"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
 
    )
    def doenca_2(self):
        self.declare(Fact(doenca="Febre Amarela"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(dor_costas="sim"),
        Fact(dor_articulacao="sim"),
        Fact(mal_estar="nao"), 
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_3(self):
        self.declare(Fact(doenca="Febre de Chikungunya"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="sim"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="sim"),
        Fact(aum_ganglios="sim"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_4(self):
        self.declare(Fact(doenca="Filariose"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="nao"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="sim"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="sim"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="sim"),
        Fact(dim_sens_face="sim"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="sim"),
        Fact(formigamento="sim"),
        Fact(fotoboia="nao"),
    )
    def doenca_5(self):
        self.declare(Fact(doenca="Hanseniase"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
        Fact(dor_abdominal="sim"),
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
        Fact(acumulo_liq="nao"), 
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_6(self):
        self.declare(Fact(doenca="Hepatite A"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="sim"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="sim"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="sim"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_7(self):
        self.declare(Fact(doenca="Hepatite B"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="nao"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(mal_estar="sim"), 
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_8(self):
        self.declare(Fact(doenca="Hepatite C"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="sim"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="sim"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
        Fact(dor_abdominal="sim"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="sim"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="sim"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_9(self):
        self.declare(Fact(doenca="Hepatite D"))

    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
        Fact(dor_abdominal="nao"),
        Fact(nausea_vomito="sim"),
        Fact(tosse="sim"),
        Fact(calafrio="sim"),
        Fact(suores="nao"),
        Fact(fraqueza="nao"),
        Fact(diarreia="sim"),
        Fact(coceira_anal="nao"),
        Fact(palpitacao="nao"),
        Fact(impotencia="nao"),
        Fact(emagrecimento="nao"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="sim"),
        Fact(mal_estar="sim"),  
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_10(self):
        self.declare(Fact(doenca="Influenza"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(emagrecimento="sim"),
        Fact(end_aum_figado="nao"),        
        Fact(dor_muscular="nao"),
        Fact(sens_plen_gastr="nao"),
        Fact(dor_costas="nao"),
        Fact(dor_articulacao="nao"),
        Fact(mal_estar="nao"),  
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="sim"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_11(self):
        self.declare(Fact(doenca="Leishmanioses"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="sim"),
        Fact(anorexia="sim"),
        Fact(astenia="sim"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="sim"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="sim"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="sim"),
        Fact(enjoo="nao"),
        Fact(est_confusional="sim"),
        Fact(fadiga="sim"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_12(self):
        self.declare(Fact(doenca="Malaria"))
    
    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="nao"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="nao"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="nao"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="nao"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="nao"),
    )
    def doenca_13(self):
        self.declare(Fact(doenca="Tuberculose"))

    @Rule(
        Fact(action="procurar_doenca"),
        Fact(dor_de_cabeca="sim"),
        Fact(febre="sim"),
        Fact(tontura="nao"),
        Fact(dor_olho="sim"),
        Fact(perda_paladar="nao"),
        Fact(manchas_erupcoes="nao"),
        Fact(cansaco="nao"),
        Fact(dor_corpo="nao"),
        Fact(dor_osso="nao"),
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
        Fact(acumulo_liq="nao"),
        Fact(anemia_intensa="nao"),
        Fact(anorexia="nao"),
        Fact(astenia="nao"),
        Fact(aum_baco="nao"),
        Fact(aum_testiculo="nao"),
        Fact(aum_ganglios="nao"),
        Fact(cefaleia="nao"),
        Fact(coceira="sim"),
        Fact(comp_nervos="nao"),
        Fact(constipacao="sim"),
        Fact(convulsao="nao"),
        Fact(dim_pelo_suor="nao"),
        Fact(dim_sens_face="nao"),
        Fact(dispineia="nao"),
        Fact(enjoo="nao"),
        Fact(est_confusional="nao"),
        Fact(fadiga="nao"),
        Fact(fezes_claras="nao"),
        Fact(fisgadas="nao"),
        Fact(formigamento="nao"),
        Fact(fotoboia="sim"),
    )
    def doenca_14(self):
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
        Fact(perda_paladar=MATCH.perda_paladar),
        Fact(manchas_erupcoes=MATCH.manchas_erupcoes),
        Fact(cansaco=MATCH.cansaco),
        Fact(dor_corpo=MATCH.dor_corpo),
        Fact(dor_osso=MATCH.dor_osso),
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
        Fact(acumulo_liq=MATCH.acumulo_liq),
        Fact(anemia_intensa=MATCH.anemia_intensa),
        Fact(anorexia=MATCH.anorexia),
        Fact(astenia=MATCH.astenia),
        Fact(aum_baco=MATCH.aum_baco),
        Fact(aum_testiculo=MATCH.aum_testiculo),
        Fact(aum_ganglios=MATCH.aum_ganglios),
        Fact(cefaleia=MATCH.cefaleia),
        Fact(coceira=MATCH.coceira),
        Fact(comp_nervos=MATCH.comp_nervos),
        Fact(constipacao=MATCH.constipacao),
        Fact(convulsao=MATCH.convulsao),
        Fact(dim_pelo_suor=MATCH.dim_pelo_suor),
        Fact(dim_sens_face=MATCH.dim_sens_face),
        Fact(dispineia=MATCH.dispineia),
        Fact(enjoo=MATCH.enjoo),
        Fact(est_confusional=MATCH.est_confusional),
        Fact(fadiga=MATCH.fadiga),
        Fact(fezes_claras=MATCH.fezes_claras),
        Fact(fisgadas=MATCH.fisgadas),
        Fact(formigamento=MATCH.formigamento),
        Fact(fotoboia=MATCH.fotoboia),


        NOT(Fact(doenca=MATCH.doenca)),
        salience=-999
    )

    def not_matched(
        self,
        dor_de_cabeca,
        febre,
        tontura,
        dor_olho,
        perda_paladar,
        manchas_erupcoes,
        cansaco,
        dor_corpo,
        dor_osso,
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
        acumulo_liq,
        anemia_intensa,
        anorexia,
        astenia,
        aum_baco,
        aum_testiculo,
        aum_ganglios,
        cefaleia,
        coceira,
        comp_nervos,
        constipacao,
        convulsao,
        dim_pelo_suor,
        dim_sens_face,
        dispineia,
        enjoo,
        est_confusional,
        fadiga,
        fezes_claras,
        fisgadas,
        formigamento,
        fotoboia,
        

    ):
        print("\nNão foi encontrado nenhuma doença que coincide exatamente com os sintomas informados.")
        lis = [
            dor_de_cabeca,
            febre,
            tontura,
            dor_olho,
            perda_paladar,
            manchas_erupcoes,
            cansaco,
            dor_corpo,
            dor_osso,
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
            acumulo_liq,
            anemia_intensa,
            anorexia,
            astenia,
            aum_baco,
            aum_testiculo,
            aum_ganglios,
            cefaleia,
            coceira,
            comp_nervos,
            constipacao,
            convulsao,
            dim_pelo_suor,
            dim_sens_face,
            dispineia,
            enjoo,
            est_confusional,
            fadiga,
            fezes_claras,
            fisgadas,
            formigamento,
            fotoboia,


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