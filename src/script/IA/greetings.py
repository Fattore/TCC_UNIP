from experta import *
import eventlet
import socketio


class Greetings(KnowledgeEngine):

    def __init__(self, doencas_map, nao_encontrado, dados_usuario):
        self.doencas_map = doencas_map
        self.nao_encontrado = nao_encontrado
        self.dados_usuario = dados_usuario
        self.max_count = 0
        self.mid_count = 0
        self.min_count = 0
        self.max_disease = ""
        self.mid_disease = ""
        self.min_disease = ""
        KnowledgeEngine.__init__(self)

    # code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        # print("")
        # print("Sistema especialista de auxilio médico")
        # print("")
        # print("Você está sentindo algum desses sintomas?")
        # print("Responda sim ou não")
        # print("")
        yield Fact(action="procurar_doenca")

    # perguntar ao usuario
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_de_cabeca=W())), salience=90)
    def sintoma_0(self):
        self.declare(Fact(dor_de_cabeca=self.dados_usuario[0]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(febre=W())), salience=89)
    def sintoma_1(self):
        self.declare(Fact(febre=self.dados_usuario[1]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tontura=W())), salience=88)
    def sintoma_2(self):
        self.declare(Fact(tontura=self.dados_usuario[2]))    
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_olho=W())), salience=87)
    def sintoma_3(self):
        self.declare(Fact(dor_olho=self.dados_usuario[3]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(perda_paladar=W())), salience=86)
    def sintoma_4(self):
        self.declare(Fact(perda_paladar=self.dados_usuario[4]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(manchas_erupcoes=W())), salience=85)
    def sintoma_5(self):
        self.declare(Fact(manchas_erupcoes=self.dados_usuario[5]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(cansaco=W())), salience=84)
    def sintoma_6(self):
        self.declare(Fact(cansaco=self.dados_usuario[6]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_corpo=W())), salience=83)
    def sintoma_7(self):
        self.declare(Fact(dor_corpo=self.dados_usuario[7]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_osso=W())), salience=82)
    def sintoma_8(self):
        self.declare(Fact(dor_osso=self.dados_usuario[8]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_abdominal=W())), salience=81)
    def sintoma_9(self):
        self.declare(Fact(dor_abdominal=self.dados_usuario[9]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(nausea_vomito=W())), salience=80)
    def sintoma_10(self):
        self.declare(Fact(nausea_vomito=self.dados_usuario[10]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tosse=W())), salience=79)
    def sintoma_11(self):
        self.declare(Fact(tosse=self.dados_usuario[11]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(calafrio=W())), salience=78)
    def sintoma_12(self):
        self.declare(Fact(calafrio=self.dados_usuario[12]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(suores=W())), salience=77)
    def sintoma_13(self):
        self.declare(Fact(suores=self.dados_usuario[13]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fraqueza=W())), salience=76)
    def sintoma_14(self):
        self.declare(Fact(fraqueza=self.dados_usuario[14]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(diarreia=W())), salience=75)
    def sintoma_15(self):
        self.declare(Fact(diarreia=self.dados_usuario[15]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(coceira_anal=W())), salience=74)
    def sintoma_16(self):
        self.declare(Fact(coceira_anal=self.dados_usuario[16]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(palpitacao=W())), salience=73)
    def sintoma_17(self):
        self.declare(Fact(palpitacao=self.dados_usuario[17]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(impotencia=W())), salience=72)
    def sintoma_18(self):
        self.declare(Fact(impotencia=self.dados_usuario[18]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(emagrecimento=W())), salience=71)
    def sintoma_19(self):
        self.declare(Fact(emagrecimento=self.dados_usuario[19]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(end_aum_figado=W())), salience=70)
    def sintoma_20(self):
        self.declare(Fact(end_aum_figado=self.dados_usuario[20]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_muscular=W())), salience=69)
    def sintoma_21(self):
        self.declare(Fact(dor_muscular=self.dados_usuario[21]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(sens_plen_gastr=W())), salience=68)
    def sintoma_22(self):
        self.declare(Fact(sens_plen_gastr=self.dados_usuario[22]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_costas=W())), salience=67)
    def sintoma_23(self):
        self.declare(Fact(dor_costas=self.dados_usuario[23]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dor_articulacao=W())), salience=66)
    def sintoma_24(self):
        self.declare(Fact(dor_articulacao=self.dados_usuario[24]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(mal_estar=W())), salience=65)
    def sintoma_25(self):
        self.declare(Fact(mal_estar=self.dados_usuario[25]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(acumulo_liq=W())), salience=64)
    def sintoma_26(self):
        self.declare(Fact(acumulo_liq=self.dados_usuario[26]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(anemia_intensa=W())), salience=63)
    def sintoma_27(self):
        self.declare(Fact(anemia_intensa=self.dados_usuario[27]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(anorexia=W())), salience=62)
    def sintoma_28(self):
        self.declare(Fact(anorexia=self.dados_usuario[28]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(astenia=W())), salience=61)
    def sintoma_29(self):
        self.declare(Fact(astenia=self.dados_usuario[29]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(aum_baco=W())), salience=60)
    def sintoma_30(self):
        self.declare(Fact(aum_baco=self.dados_usuario[30]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(aum_testiculo=W())), salience=59)
    def sintoma_31(self):
        self.declare(Fact(aum_testiculo=self.dados_usuario[31]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(aum_ganglios=W())), salience=58)
    def sintoma_32(self):
        self.declare(Fact(aum_ganglios=self.dados_usuario[32]))
   
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(cefaleia=W())), salience=57)
    def sintoma_33(self):
        self.declare(Fact(cefaleia=self.dados_usuario[33]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(coceira=W())), salience=56)
    def sintoma_34(self):
        self.declare(Fact(coceira=self.dados_usuario[34]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(comp_nervos=W())), salience=55)
    def sintoma_35(self):
        self.declare(Fact(comp_nervos=self.dados_usuario[35]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(constipacao=W())), salience=54)
    def sintoma_36(self):
        self.declare(Fact(constipacao=self.dados_usuario[36]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(convulsao=W())), salience=53)
    def sintoma_37(self):
        self.declare(Fact(convulsao=self.dados_usuario[37]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dim_pelo_suor=W())), salience=52)
    def sintoma_38(self):
        self.declare(Fact(dim_pelo_suor=self.dados_usuario[38]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dim_sens_face=W())), salience=51)
    def sintoma_39(self):
        self.declare(Fact(dim_sens_face=self.dados_usuario[39]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(dispineia=W())), salience=50)
    def sintoma_40(self):
        self.declare(Fact(dispineia=self.dados_usuario[40]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(enjoo=W())), salience=49)
    def sintoma_41(self):
        self.declare(Fact(enjoo=self.dados_usuario[41]))
    
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(est_confusional=W())), salience=48)
    def sintoma_42(self):
        self.declare(Fact(est_confusional=self.dados_usuario[42]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fadiga=W())), salience=47)
    def sintoma_43(self):
        self.declare(Fact(fadiga=self.dados_usuario[43]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fezes_claras=W())), salience=46)
    def sintoma_44(self):
        self.declare(Fact(fezes_claras=self.dados_usuario[44]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fisgadas=W())), salience=45)
    def sintoma_45(self):
        self.declare(Fact(fisgadas=self.dados_usuario[45]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(formigamento=W())), salience=44)
    def sintoma_46(self):
        self.declare(Fact(formigamento=self.dados_usuario[46]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(fotoboia=W())), salience=43)
    def sintoma_47(self):
        self.declare(Fact(fotoboia=self.dados_usuario[47]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(hiperparasitemia=W())), salience=42)
    def sintoma_48(self):
        self.declare(Fact(hiperparasitemia=self.dados_usuario[48]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(hipotensao_arterial=W())), salience=41)
    def sintoma_49(self):
        self.declare(Fact(hipotensao_arterial=self.dados_usuario[49]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(ictericia=W())), salience=40)
    def sintoma_50(self):
        self.declare(Fact(ictericia=self.dados_usuario[50]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(infl_garganta=W())), salience=39)
    def sintoma_51(self):
        self.declare(Fact(infl_garganta=self.dados_usuario[51]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(irritacao_olhos=W())), salience=38)
    def sintoma_52(self):
        self.declare(Fact(irritacao_olhos=self.dados_usuario[52]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(moleza=W())), salience=37)
    def sintoma_53(self):
        self.declare(Fact(moleza=self.dados_usuario[53]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(mucosas_amarelas=W())), salience=36)
    def sintoma_54(self):
        self.declare(Fact(mucosas_amarelas=self.dados_usuario[54]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(muito_cansaco=W())), salience=35)
    def sintoma_55(self):
        self.declare(Fact(muito_cansaco=self.dados_usuario[55]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(nodulos_corpo=W())), salience=34)
    def sintoma_56(self):
        self.declare(Fact(nodulos_corpo=self.dados_usuario[56]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(olhos_amarelados=W())), salience=33)
    def sintoma_57(self):
        self.declare(Fact(olhos_amarelados=self.dados_usuario[57]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(oliguria=W())), salience=32)
    def sintoma_58(self):
        self.declare(Fact(oliguria=self.dados_usuario[58]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(pele_amarelada=W())), salience=31)
    def sintoma_59(self):
        self.declare(Fact(pele_amarelada=self.dados_usuario[59]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(perda_apetite=W())), salience=30)
    def sintoma_60(self):
        self.declare(Fact(perda_apetite=self.dados_usuario[60]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(perda_peso=W())), salience=29)
    def sintoma_61(self):
        self.declare(Fact(perda_peso=self.dados_usuario[61]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(rash_cutanea=W())), salience=28)
    def sintoma_62(self):
        self.declare(Fact(rash_cutanea=self.dados_usuario[62]))
     
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(sudorese_noturna=W())), salience=27)
    def sintoma_63(self):
        self.declare(Fact(sudorese_noturna=self.dados_usuario[63]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(sudorese_profusa=W())), salience=26)
    def sintoma_64(self):
        self.declare(Fact(sudorese_profusa=self.dados_usuario[64]))
 
    @Rule(Fact(action="procurar_doenca"), NOT(Fact(tremor=W())), salience=25)
    def sintoma_65(self):
        self.declare(Fact(tremor=self.dados_usuario[65]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(ulceras=W())), salience=24)
    def sintoma_66(self):
        self.declare(Fact(ulceras=self.dados_usuario[66]))

    @Rule(Fact(action="procurar_doenca"), NOT(Fact(urina_escura=W())), salience=23)
    def sintoma_67(self):
        self.declare(Fact(urina_escura=self.dados_usuario[67]))

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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="sim"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="sim"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="sim"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
 
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="sim"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="sim"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="sim"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="sim"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="sim"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="sim"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="sim"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="sim"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="sim"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="sim"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="sim"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="sim"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="sim"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="sim"),
        Fact(irritacao_olhos="sim"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="sim"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="sim"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="sim"),
        Fact(hipotensao_arterial="sim"),
        Fact(ictericia="sim"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="sim"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="sim"),
        Fact(tremor="sim"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="sim"),
        Fact(rash_cutanea="nao"),
        Fact(sudorese_noturna="sim"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="nao"),
        Fact(urina_escura="nao"),
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
        Fact(hiperparasitemia="nao"),
        Fact(hipotensao_arterial="nao"),
        Fact(ictericia="nao"),
        Fact(infl_garganta="nao"),
        Fact(irritacao_olhos="nao"),
        Fact(moleza="nao"),
        Fact(mucosas_amarelas="nao"),
        Fact(muito_cansaco="nao"),
        Fact(nodulos_corpo="nao"),
        Fact(olhos_amarelados="nao"),
        Fact(oliguria="nao"),
        Fact(pele_amarelada="nao"),
        Fact(perda_apetite="nao"),
        Fact(perda_peso="nao"),
        Fact(rash_cutanea="sim"),
        Fact(sudorese_noturna="nao"),
        Fact(sudorese_profusa="nao"),
        Fact(tremor="nao"),
        Fact(ulceras="sim"),
        Fact(urina_escura="nao"),
    )
    def doenca_14(self):
        self.declare(Fact(doenca="Zika Virus"))

   
    # when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="procurar_doenca"), Fact(doenca=MATCH.doenca), salience=-997)
    def doenca(self, doenca):
        print("")
        id_disease = doenca
        print("")
        print("Os sintomas coincidem com %s\n" % (id_disease))
        print("")
        print("")
        self.max_disease = id_disease
        self.max_count = 100
        

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
        Fact(hiperparasitemia=MATCH.hiperparasitemia),
        Fact(hipotensao_arterial=MATCH.hipotensao_arterial),
        Fact(ictericia=MATCH.ictericia),
        Fact(infl_garganta=MATCH.infl_garganta),
        Fact(irritacao_olhos=MATCH.irritacao_olhos),
        Fact(moleza=MATCH.moleza),
        Fact(mucosas_amarelas=MATCH.mucosas_amarelas),
        Fact(muito_cansaco=MATCH.muito_cansaco),
        Fact(nodulos_corpo=MATCH.nodulos_corpo),
        Fact(olhos_amarelados=MATCH.olhos_amarelados),
        Fact(oliguria=MATCH.oliguria),
        Fact(pele_amarelada=MATCH.pele_amarelada),
        Fact(perda_apetite=MATCH.perda_apetite),
        Fact(perda_peso=MATCH.perda_peso),
        Fact(rash_cutanea=MATCH.rash_cutanea),
        Fact(sudorese_noturna=MATCH.sudorese_noturna),
        Fact(sudorese_profusa=MATCH.sudorese_profusa),
        Fact(tremor=MATCH.tremor),
        Fact(ulceras=MATCH.ulceras),
        Fact(urina_escura=MATCH.urina_escura),
        NOT(Fact(doenca=MATCH.doenca)),
        salience=-998
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
        hiperparasitemia,
        hipotensao_arterial,
        ictericia,
        infl_garganta,
        irritacao_olhos,
        moleza,
        mucosas_amarelas,
        muito_cansaco,   
        nodulos_corpo,
        olhos_amarelados,
        oliguria, 
        pele_amarelada,
        perda_apetite,
        perda_peso,
        rash_cutanea,
        sudorese_noturna,
        sudorese_profusa,
        tremor,
        ulceras,
        urina_escura,
        
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
            hiperparasitemia,
            hipotensao_arterial,
            ictericia,
            infl_garganta,
            irritacao_olhos,
            moleza,
            mucosas_amarelas,
            muito_cansaco,   
            nodulos_corpo,
            olhos_amarelados,
            oliguria, 
            pele_amarelada,
            perda_apetite,
            perda_peso,
            rash_cutanea,
            sudorese_noturna,
            sudorese_profusa,
            tremor,
            ulceras,
            urina_escura,
        ]


        max_count = 0
        mid_count = 0
        min_count = 0
        max_disease = ""
        mid_disease = ""
        min_disease = ""
        for key, val in self.doencas_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and (lis[j] == "alta" or lis[j] == "baixa" or lis[j] == "sim"):
                    count = count + 1
            if count > min_count:
                if count > mid_count:
                    if count > max_count:
                        min_count = mid_count
                        mid_count = max_count
                        max_count = count
                        min_disease = mid_disease
                        mid_disease = max_disease
                        max_disease = val
                    else:
                        min_count = mid_count
                        mid_count = count 
                        min_disease = mid_disease
                        mid_disease = val

                else:
                    min_count = count
                    min_disease = val

        if max_disease != "":
            self.max_disease = max_disease
            self.max_count = max_count

            self.mid_disease = mid_disease
            self.mid_count = mid_count

            self.min_disease = min_disease
            self.min_count = min_count
        
      
            # self.nao_encontrado(max_disease, max_count, mid_disease, mid_count, min_disease, min_count)