import React from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import MyComp from "../script/component";
import { createFile } from "../script/saveFile";

const Avaliacao = () => {

    return (
        <div class="">
            <div class="container styleVF-container">
				<div class="position-absolute top-0 start-50 translate-middle style-paddingtop">
					<h4>DIAGNÓSTICO</h4>
				</div>

				<form class="style-paddingtop">
					<label class="form-label style-largefont">Assinale os sintomas que se aplicam ao paciente</label>

					<div id="sintomasForm">
						<div class="row">
							<div class="col-6">
								<MyComp
								entries={[
									{ name: 'Dor de Cabeça', id: 'chkdordecabeca', value: false },
									{ name: 'Febre', id: 'chkfebre', value: false },
									{ name: 'Tontura', id: 'chktontura', value: false },
									{ name: 'Dor no Olho', id: 'chkdorolho', value: false },
									{ name: 'Perda no Paladar e no Apetite', id: 'chkperdapaladarapetite', value: false },
									{ name: 'Manchas e Erupçoes na Pele', id: 'chkmanchaserupcoes', value: false },
									{ name: 'Cansaço', id: 'chkcansaco', value: false },
									{ name: 'Dor no Corpo', id: 'chkdornocorpo', value: false },
									{ name: 'Dor nos Ossos e nas Articulações', id: 'chkdorossoarticulacoes', value: false },
									{ name: 'Dor Abdominal', id: 'chkdorabdominal', value: false },
									{ name: 'Nausea e Vomito', id: 'chknausevomito', value: false },
									{ name: 'Tosse', id: 'chktosse', value: false },
									{ name: 'Calafrio', id: 'chkcalafrio', value: false }
								]}
								/>
							</div>
							<div class="col-6">
							<MyComp
								entries={[
									{ name: 'Suores', id: 'chksuores', value: false },
									{ name: 'Fraqueza', id: 'chkfraqueza', value: false },
									{ name: 'Diarreia', id: 'chkdiarreia', value: false },
									{ name: 'Coceira Anal', id: 'chkcoceiranal', value: false },
									{ name: 'Impotencia', id: 'chkimpotencia', value: false },
									{ name: 'Palpitação', id: 'chkpalpitacao', value: false },
									{ name: 'Emagrecimento', id: 'chkemagrecimento', value: false },
									{ name: 'Endurecimento ou Aumento do Figado', id: 'chkendurecimentofigado', value: false },
									{ name: 'Dor Muscular', id: 'chkdormuscular', value: false },
									{ name: 'Sensação de Plenitude Gastrica', id: 'chksensacaogastrica', value: false },
									{ name: 'Dores nas Costas', id: 'chkdorcosta', value: false },
									{ name: 'Dor Articulacao', id: 'chkdorarticulacao', value: false },
									{ name: 'Mal Estar', id: 'chkmalestar', value: false }
								]}
								/>
							</div>
						</div>		
					</div>
					
					<button class="btn btn-primary style-fiquegrande" id="teste" onClick={createFile}>teste</button>

					<div class="d-grid gap-2 style-marginbottom">
						<Link to="/Relatorio">
							<button class="btn btn-primary style-fiquegrande" type="button">Finalizar</button>
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
    );
}

export default Avaliacao