import React from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import MyComp from "../script/component";

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
										{ name: 'Calafrio', id: 'chkcalafrio', value: 'nao' }
									]}
								/>
							</div>
							<div class="col-6">
								<MyComp
									entries={[
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
										{ name: 'Mal Estar', id: 'chkmalestar', value: 'nao' }
									]}
								/>
							</div>
						</div>		
					</div>

					<div class="d-grid gap-2 style-marginbottom">
						<button class="btn btn-primary style-fiquegrande" id="teste">teste</button>
					</div>

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