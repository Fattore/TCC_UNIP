import React, {useState, useEffect} from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';
const electron = window.require('electron');
const ipcRenderer  = electron.ipcRenderer;


let array1 = [
	{ name: 'Dor de Cabeça', id: 'chkdordecabeca', value: 'nao'},
	{ name: 'Febre', id: 'chkfebre', value: 'nao' },
	{ name: 'Tontura', id: 'chktontura', value: 'nao' },
	{ name: 'Dor no Olho', id: 'chkdorolho', value: 'nao' },
	{ name: 'Perda no Paladar e no Apetite', id: 'chkperdapaladarapetite', value: 'nao' },
	{ name: 'Manchas e Erupçoes na Pele', id: 'chkmanchaserupcoes', value: 'nao' },
	{ name: 'Cansaço', id: 'chkcansaco', value: 'nao' },
	{ name: 'Dor no Corpo', id: 'chkdornocorpo', value: 'nao' },
	{ name: 'Dor nos Ossos e nas Articulações', id: 'chkdorossoarticulacoes', value: 'nao' },
	{ name: 'Dor Abdominal', id: 'chkdorabdominal', value: 'nao' },
	{ name: 'Nausea e Vomito', id: 'chknausevomito', value: 'nao' },
	{ name: 'Tosse', id: 'chktosse', value: 'nao' },
	{ name: 'Calafrio', id: 'chkcalafrio', value: 'nao' },
	{ name: 'Suores', id: 'chksuores', value: 'nao' },
	{ name: 'Fraqueza', id: 'chkfraqueza', value: 'nao' },
	{ name: 'Diarreia', id: 'chkdiarreia', value: 'nao' },
	{ name: 'Coceira Anal', id: 'chkcoceiranal', value: 'nao' },
	{ name: 'Impotencia', id: 'chkimpotencia', value: 'nao' },
	{ name: 'Palpitação', id: 'chkpalpitacao', value: 'nao' },
	{ name: 'Emagrecimento', id: 'chkemagrecimento', value: 'nao' },
	{ name: 'Endurecimento ou Aumento do Figado', id: 'chkendurecimentofigado', value: 'nao' },
	{ name: 'Dor Muscular', id: 'chkdormuscular', value: 'nao' },
	{ name: 'Sensação de Plenitude Gastrica', id: 'chksensacaogastrica', value: 'nao' },
	{ name: 'Dores nas Costas', id: 'chkdorcosta', value: 'nao' },
	{ name: 'Dor Articulacao', id: 'chkdorarticulacao', value: 'nao' },
	{ name: 'Mal Estar', id: 'chkmalestar', value: 'nao' },
	{ name: 'Acumulo Liq. Braço/Perna', id: 'chkliqbracoperna', value: 'nao' },
	{ name: 'Anemia Intensa', id: 'chkanemia', value: 'nao' },
	{ name: 'Anorexia', id: 'chkanorexia', value: 'nao' },
	{ name: 'Astenia', id: 'chkastenia', value: 'nao' },
	{ name: 'Aumento do Baço', id: 'chkaumbaco', value: 'nao' },
	{ name: 'Aumento Vol. Testículo', id: 'chkaumtesticulo', value: 'nao' },
	{ name: 'Aumento Gânglios Linfáticos', id: 'chkaumganglioslinfaticos', value: 'nao' },
	{ name: 'Cefalia', id: 'chkcefalia', value: 'nao' },
	{ name: 'Coceira', id: 'chkcoceira', value: 'nao' },
	{ name: 'Compromentimento Nervo Periférico', id: 'chkcompromentimentonervoper', value: 'nao' },
	{ name: 'Constipação', id: 'chkconstipacao', value: 'nao' },
	{ name: 'Convulsão', id: 'chkconvulsao', value: 'nao' },
	{ name: 'Diminuição de pelo ou suor', id: 'chkdimpelosuor', value: 'nao' },
	{ name: 'Diminuição da sensibilidade muscular facial', id: 'chkdimsensibilidadefacial', value: 'nao' },
	{ name: 'Dispineia', id: 'chkdispineia', value: 'nao' },
	{ name: 'Enjoo', id: 'chkenjoo', value: 'nao' },
	{ name: 'Estado Confusional Agudo', id: 'chkconfusaoaguda', value: 'nao' },
	{ name: 'Fadiga', id: 'chkfadiga', value: 'nao' },
	{ name: 'Fezes Claras', id: 'chkfezesclaras', value: 'nao' },
	{ name: 'Fisgadas', id: 'chkfisgadas', value: 'nao' },
	{ name: 'Formigamento', id: 'chkformigamento', value: 'nao' },
	{ name: 'Fotofobia', id: 'chkfotofobia', value: 'nao' },
	{ name: 'Hiperparasitemia', id: 'chkhiperparasitemia', value: 'nao' },
	{ name: 'Hipotensão Arterial', id: 'chkhipotensaoarterial', value: 'nao' },
	{ name: 'Ictericia', id: 'chkictericia', value: 'nao' },
	{ name: 'Inflamação Garganta', id: 'chkinflamacaogarganta', value: 'nao' },
	{ name: 'Irritação Olhos', id: 'chkirritacaolhos', value: 'nao' },
	{ name: 'Moleza', id: 'chkmoleza', value: 'nao' },
	{ name: 'Mucosas Amarelas', id: 'chkmucosasamarelas', value: 'nao' },
	{ name: 'Muito Cansaço', id: 'chkmuitocansaco', value: 'nao' },
	{ name: 'Nodulo no Corpo', id: 'chknodulocorpo', value: 'nao' },
	{ name: 'Olhos Amarelados', id: 'chkolhosamarelados', value: 'nao' },
	{ name: 'Insuficiência Renal', id: 'chkinsuficienciarenal', value: 'nao' },
	{ name: 'Pele Amarelada', id: 'chkpeleamarelada', value: 'nao' },
	{ name: 'Perda de Apetite', id: 'chkperdapetite', value: 'nao' },
	{ name: 'Perda de Peso', id: 'chkperdapeso', value: 'nao' },
	{ name: 'Rash Cutânea', id: 'chkrashcutanea', value: 'nao' },
	{ name: 'Sudorese noturna', id: 'chksudoresenoturna', value: 'nao' },
	{ name: 'Sudorese profusa', id: 'chksudoreseprofusa', value: 'nao' },
	{ name: 'Tremor', id: 'chktremor', value: 'nao' },
	{ name: 'Úlceras', id: 'chkulceras', value: 'nao' },
	{ name: 'Urina escura', id: 'chkurinaescura', value: 'nao' }
]

let array2 =[
	{ name: 'Coceira', id: 'chkcoceira', value: 'nao' },
	{ name: 'Compromentimento Nervo Periférico', id: 'chkcompromentimentonervoper', value: 'nao' },
	{ name: 'Constipação', id: 'chkconstipacao', value: 'nao' },
	{ name: 'Convulsão', id: 'chkconvulsao', value: 'nao' },
	{ name: 'Diminuição de pelo ou suor', id: 'chkdimpelosuor', value: 'nao' },
	{ name: 'Diminuição da sensibilidade muscular facial', id: 'chkdimsensibilidadefacial', value: 'nao' },
	{ name: 'Dispineia', id: 'chkdispineia', value: 'nao' },
	{ name: 'Enjoo', id: 'chkenjoo', value: 'nao' },
	{ name: 'Estado Confusional Agudo', id: 'chkconfusaoaguda', value: 'nao' },
	{ name: 'Fadiga', id: 'chkfadiga', value: 'nao' },
	{ name: 'Fezes Claras', id: 'chkfezesclaras', value: 'nao' },
	{ name: 'Fisgadas', id: 'chkfisgadas', value: 'nao' },
	{ name: 'Formigamento', id: 'chkformigamento', value: 'nao' },
	{ name: 'Fotofobia', id: 'chkfotofobia', value: 'nao' },
	{ name: 'Hiperparasitemia', id: 'chkhiperparasitemia', value: 'nao' },
	{ name: 'Hipotensão Arterial', id: 'chkhipotensaoarterial', value: 'nao' },
	{ name: 'Ictericia', id: 'chkictericia', value: 'nao' },
	{ name: 'Inflamação Garganta', id: 'chkinflamacaogarganta', value: 'nao' },
	{ name: 'Irritação Olhos', id: 'chkirritacaolhos', value: 'nao' },
	{ name: 'Moleza', id: 'chkmoleza', value: 'nao' },
	{ name: 'Mucosas Amarelas', id: 'chkmucosasamarelas', value: 'nao' },
	{ name: 'Muito Cansaço', id: 'chkmuitocansaco', value: 'nao' },
	{ name: 'Nodulo no Corpo', id: 'chknodulocorpo', value: 'nao' },
	{ name: 'Olhos Amarelados', id: 'chkolhosamarelados', value: 'nao' },
	{ name: 'Insuficiência Renal', id: 'chkinsuficienciarenal', value: 'nao' },
	{ name: 'Pele Amarelada', id: 'chkpeleamarelada', value: 'nao' },
	{ name: 'Perda de Apetite', id: 'chkperdapetite', value: 'nao' },
	{ name: 'Perda de Peso', id: 'chkperdapeso', value: 'nao' },
	{ name: 'Rash Cutânea', id: 'chkrashcutanea', value: 'nao' },
	{ name: 'Sudorese noturna', id: 'chksudoresenoturna', value: 'nao' },
	{ name: 'Sudorese profusa', id: 'chksudoreseprofusa', value: 'nao' },
	{ name: 'Tremor', id: 'chktremor', value: 'nao' },
	{ name: 'Úlceras', id: 'chkulceras', value: 'nao' },
	{ name: 'Urina escura', id: 'chkurinaescura', value: 'nao' }
]

const Avaliacao = () => {
	const [check, setCheck] = useState({});

	const setArray1 = useEffect;
	const setArray2 = useEffect;

	let arrayResult = [
	]

	setArray1(() => {
		let newChecks = {};
		for (const entry of array1) {
			newChecks[entry.id] = entry.value === 'sim';
		}
		setCheck({ ...newChecks });
	}, [array1]);

	setArray2(() => {
		let newChecks = {};
		for (const entry of array1) {
			newChecks[entry.id] = entry.value === 'sim';
		}
		setCheck({ ...newChecks });
	}, [array2]);

	const onChange = id => {
		return e => {
			const checks = check;
			checks[id] = e.target.checked;
			console.log(checks);
			setCheck({ ...checks });
		};
	};

	const verifyButton = () => {
		const btn1 = document.getElementById('diagnosticar');
		const btn2 = document.getElementById('finalizar');

		if(btn1.disabled === false) {
			arrayResult = Object.values(check).map((x) => (x ? "sim": "nao"));
			ipcRenderer.send("msg", arrayResult);
			btn1.disabled = true;
			btn2.disabled = false;
		} else {
			btn1.disabled = true;
			btn2.disabled = false;
		}
	}

    return (
		<>
        <div>
            <div class="container styleVF-container">
				<div class="position-absolute top-0 start-50 translate-middle style-paddingtop">
					<h4>DIAGNÓSTICO</h4>
				</div>

				<form class="style-paddingtop">
					<label class="form-label style-largefont">Assinale os sintomas que se aplicam ao paciente</label>

					<div id="sintomasForm">
						<div class="row">
							<div class="col-6">
								<div className="form-check">
									{Object.keys(check).map((id) => {
									const entry = check[id];
									const meta = array1.find((x) => x.id === id);
									return (
										<div key={id}>
										<input
											className="form-check-label me-2 teste"
											value={entry.value}
											onChange={onChange(id)}
											type="checkbox"
										/>
										<label className="form-check-label">{meta.name}</label>
										<br />
										</div>
									);
										})}
								</div>
							</div>
							<div class="col-6">	
							</div>
						</div>		
					</div>

					<div class="d-grid gap-2 style-marginbottom">
						<button
							id="diagnosticar" 
							class="btn btn-primary style-fiquegrande" 
							type="button" 
							onClick={verifyButton}>Diagnosticar</button>
					</div>

					<div class="d-grid gap-2 style-marginbottom">
						<Link to="/Relatorio">
							<button id="finalizar" class="btn btn-primary style-fiquegrande" type="button" disabled>Finalizar</button>
						</Link>
					</div>

					<div class="d-grid gap-2 style-marginbottom">
						<Link to="/">
							<button class="btn btn-primary style-marginbottom style-fiquegrande" type="button">Home</button>
						</Link>
					</div>
				</form>
			</div>
			
        </div>
		</>
    );

}

export default Avaliacao