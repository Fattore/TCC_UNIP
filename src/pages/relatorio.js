import React, {useState} from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';
const electron = window.require('electron');
const ipcRenderer  = electron.ipcRenderer;



const arrayDesc = [
	{doenca: "Dengue", desc: "A Dengue é uma doença febril aguda causada por um vírus. A transmissão é feita pelo mosquito Aedes aegypti, que se desenvolve em áreas tropicais e subtropicais."},
	{doenca: "Esquistossomose", desc: "É uma doença parasitária, diretamente relacionada ao saneamento precário, causada pelo Schistosoma mansoni. A pessoa adquire a infecção quando entra em contato com água doce onde existam caramujos infectados pelos vermes causadores da esquistossomose."},
	{doenca: "Febre Amarela", desc: "A febre amarela é uma doença infecciosa aguda, de curta incubação (em geral inferior a 10 dias), gravidade variável, causada pelo Flavivirus (vírus da febre amarela), que ocorre na Américas (Central e do Sul) e na África."},
	{doenca: "Febre de Chikungunya", desc: "É uma doença infecciosa febril, causada pelo vírus Chikungunya, que pode ser transmitida pelos mosquitos Aedes aegypti e Aedes albopictus (mesmos mosquitos que transmitem a dengue e a febre amarela, respectivamente)."},
	{doenca: "Filariose", desc: "A filariose é uma doença parasitária causada por vermes e transmitida através da picada de insetos. Ela também é conhecida por filariose linfática ou elefantíase."},
	{doenca: "Hanseníase", desc: "Também conhecida como lepra ou mal de Lázaro, a hanseníase é uma doença infecciosa, contagiosa, que afeta os nervos e a pele e é causada por um bacilo chamado Mycobacterium leprae."},
	{doenca: "Hepatite A", desc: "Hepatite A é uma doença viral aguda do fígado, causada pelo vírus da Hepatite A."},
	{doenca: "Hepatite B", desc: "A hepatite B é uma doença infecciosa causada pelo vírus B (HBV), resultando na inflamação das células do fígado (hepatite). Como o HBV está presente no sangue, no esperma e no leite materno, a hepatite B é considerada uma doença sexualmente transmissível. "},
	{doenca: "Hepatite C", desc: "A hepatite C é causada pelo vírus C (VHC) resultando na inflamação das células do fígado (hepatite) e se não diagnosticada e tratada pode evoluir para formas crônicas (cirrose) e câncer de fígado. Estima-se que cerca de 3% da população mundial, mais de 170 milhões de pessoas, sejam portadores de hepatite C crônica. É atualmente uma das principais indicações para transplante hepático em países desenvolvidos e responsável por 60% das hepatopatias crônicas e pela metade dos casos de câncer de fígado em países ocidentais."},
	{doenca: "Hepatite D", desc: "A hepatite D, também chamada de Delta, está associada com a presença do vírus do B da hepatite para causar a infecção e inflamação das células do fígado. Existem duas formas de infecção pelo HDV: coinfecção simultânea com o HBV e superinfecção do HDV em um indivíduo com infecção crônica pelo HBV. A hepatite D crônica é considerada a forma mais grave de hepatite viral crônica, com progressão mais rápida para cirrose e um risco aumentado para descompensação, CHC e morte (FATTOVICH et al., 2000; MALLET et al., 2017)."},
	{doenca: "Influenza", desc: "A gripe é uma infecção aguda do sistema respiratório, provocado pelo vírus da influenza, com grande potencial de transmissão. Existem quatro tipos de vírus influenza/gripe: A, B, C e D. O vírus influenza A e B são responsáveis por epidemias sazonais, sendo o vírus influenza A responsável pelas grandes pandemias."},
	{doenca: "Leishmanioses", desc: "Doença infecciosa, porém, não contagiosa, causada por parasitas do gênero Leishmania. Os parasitas vivem e se multiplicam no interior das células que fazem parte do sistema de defesa do indivíduo, chamadas macrófagos. Há dois tipos de leishmaniose: leishmaniose tegumentar ou cutânea e a leishmaniose visceral ou calazar. A leishmaniose tegumentar caracteriza-se por feridas na pele que se localizam com maior freqüência nas partes descobertas do corpo. Tardiamente, podem surgir feridas nas mucosas do nariz, da boca e da garganta. Essa forma de leishmaniose é conhecida como “ferida brava”. A leishmaniose visceral é uma doença sistêmica, pois, acomete vários órgãos internos, principalmente o fígado, o baço e a medula óssea. Esse tipo de leishmaniose acomete essencialmente crianças de até dez anos; após esta idade se torna menos freqüente. É uma doença de evolução longa, podendo durar alguns meses ou até ultrapassar o período de um ano."},
	{doenca: "Malária", desc: "Doença infecciosa febril aguda, cujos agentes etiológicos são protozoários transmitidos por vetores (mosquito). Também é conhecida por: paludismo, impaludismo, febre palustre, febre intermitente, febre terçã benigna, febre terçã maligna, além de nomes populares, como maleita, sezão, tremedeira, batedeira ou febre. É reconhecida como grave problema de saúde pública no mundo, ocorrendo em quase 50% da população, em mais de 109 países e territórios. A estimativa anual de casos novos no mundo atinge a cifra de 300 milhões com 1 milhão de mortes, principalmente entre crianças menores de 5 anos e gestantes no continente africano. No Brasil, a região amazônica, zona rural, é considerada área endêmica para malária, responsável por mais de 90% dos casos notificados, concentrados em nove estados: Acre, Amapá, Amazonas, Pará, Rondônia, Roraima, Maranhão, Mato Grosso e Tocantins."},
	{doenca: "Tuberculose", desc: "Tuberculose é uma doença infecciosa que pode acometer diversos órgãos, sendo o pulmão o mais frequente."},
	{doenca: "Zika Vírus", desc: "O Zika Vírus é uma infecção causada pelo vírus Zika, transmitido pelo mosquito Aedes aegypti, o mesmo transmissor da dengue e da febre chikungunya. Ele é considerado uma ameaça à saúde mundial devido as fortes evidências de relação com a microcefalia e outras malformações congênitas – podendo afetar o desenvolvimento de fetos de mulheres contaminadas durante a gestação. Além disso, o Zika também pode acarretar outros problemas neurológicos, como meningite, mielite, encefalite e síndrome de Guillain Barré."},
]

const Relatorio = () => {
	const [result, setResult] = useState([]);
	const [max_disease, setMax_Disease] = useState();
	const [desc, setDesc] = useState();

	ipcRenderer.send("request-from-relatorio")
	ipcRenderer.on('response-to-relatorio', (event, arg) => {
		let arrayFromPython = arg.split("_")
		setResult(arg.split("_"))
		// if(arrayFromPython.size() > 1){
		// 	setResult({doenca: arrayFromPython[0], sintomasCompativeis: arrayFromPython[1]})
		// }
		setMax_Disease(arrayFromPython[0])
		verifyDesc()
	
	})

	function verifyDesc(){
		arrayDesc.forEach(item => {
			let itemDoenca = item.doenca
			let itemDesc = item.desc
			if(itemDoenca === max_disease){
				setDesc(itemDesc)
			}
		});
	}

    return (
        <div>
			<div class="container styleVF-container-relatorio">
				<form class="style-paddingtoptres">
					<div class="card style-card">
						<h4 class="card-header">RELATÓRIO</h4>				
						<div class="card">
							<h5 class="card-header" role="tab" id="headingOne">
								Doença Principal: {result[0]}
							</h5>
							<div class="card-body">
								<b>Sintomas Positivos:</b> {result[1]}
								<br/>
								{desc}
							</div>
						</div>
						<div class="card">
							<h5 class="card-header" role="tab" id="headingOne">
								Doença Provavel: {result[2]}
							</h5>
						</div>
						<div class="card">
							<h5 class="card-header" role="tab" id="headingOne">
								Doença Provavel: {result[4]}
							</h5>
						</div>
					</div>

					<div >
						<Link className ="App-link" to= "/">
							<button class="btn btn-primary style-marginfive-relatorio style-fiquegrande" type="button">Home</button>
						</Link>
					</div>
				</form>
			</div>
        </div>
    )
}

export default Relatorio