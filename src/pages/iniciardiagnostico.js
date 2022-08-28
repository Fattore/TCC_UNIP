import React from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';

export default function IniciarDiagnostico() {

    return (
			<div class="container styleVF-container">
				<div class="row">
					<div class="col-2">
						<div class="form-outline styleVF-formoutline">
							<span class="input-group-append">
								<button type="button" class="btn btn-primary border-right-0 border">
									<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
										<path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
									</svg>
								</button>
							</span>
						</div>
					</div>
					<div class="col-10">
						<div class="form-outline styleVF-table-search">
						<input type="search" id="procurarPaciente" class="form-control py-2 border-left-0 border" placeholder="Procurar Paciente"/>
						</div>
					</div>
				</div>

				<div class="position-absolute top-20 start-50 translate-middle">
					<h4 id="teste">FORMULÁRIO DO PACIENTE</h4>
				</div>

				<form id="formularioFP">
					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="nomepaciente">Nome Completo</label>
						<input type="text" id="nomepaciente" class="form-control"/>
					</div>

					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="cpfpaciente">CPF</label>
						<input type="number" id="cpfpaciente" class="form-control"/>
					</div>

					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="telefonepaciente">Telefone</label>
						<input type="number" id="telefonepaciente" class="form-control"/>
						<div class="alert alert-warning" role="alert">
							inserir número válido
						</div>
					</div>
				
					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="startDate">Data da Avaliação</label>
						<input id="startDate" type="date" class="form-control"/>
						<span id="startDateSelected"></span>
					</div>

					<label class="form-label style-largefont">Assinale as condições que se aplicam a você ou qualquer de seus parentes mais próximos:</label>
					
					<div class="form-check">
						<label class="form-check-label" for="condicaoasma">Asma</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="condicaoasma" />
					</div>

					<div class="form-check">	
						<label class="form-check-label" for="condicaocardiaca">Doença Cardíaca</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="condicaocardiaca" />
					</div>

					<div class="form-check">
						<label class="form-check-label" for="condicaohipertensao">Hipertensão Arterial</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="condicaohipertensao" />
					</div>

					<div class="form-check">
						<label class="form-check-label" for="condicaocancer">Câncer</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="condicaocancer" />
					</div>

					<div class="form-check">
						<label class="form-check-label" for="condicaodiabetes">Diabetes</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="condicaodiabetes" />
					</div>

					<div class="form-check">
						<label class="form-check-label" for="condicaopsiquiatrico">Transtorno Psiquiátrico</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="condicaopsiquiatrico" />
					</div>
				
					<div class="style-marginfive"></div>

					<label class="form-label style-largefont">Você tem alguma alergia a medicamento ?</label>
					
					<div class="form-check">
						<label class="form-check-label" for="medicamentosim">Sim</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="medicamentosim" />
					</div>

					<div class="form-check">	
						<label class="form-check-label" for="medicamentonao">Não</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="medicamentonao" />
					</div>

					<div class="form-check">
						<label class="form-check-label" for="medicamentonsei">Não tenho certeza</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="medicamentonsei" />
					</div>
				
					<div class="style-marginfive"></div>

					<label class="form-label style-largefont">Qual é o seu gênero ?</label>
					
					<div class="form-check">
						<label class="form-check-label" for="generofeminino">Feminino</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="generofeminino" />
					</div>

					<div class="form-check">	
						<label class="form-check-label" for="generomasculino">Masculino</label>
						<input class="form-check-input me-2" type="checkbox" value="" id="generomasculino" />
					</div>

					<div class="style-marginfive"></div>

					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="enderecopaciente">Endereço</label>
						<input type="text" id="enderecopaciente" class="form-control"/>
					</div>

					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="cidadepaciente">Cidade</label>
						<input type="text" id="cidadepaciente" class="form-control"/>
					</div>

					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="estadopaciente">Estado</label>
						<input type="text" id="estadopaciente" class="form-control"/>
					</div>

					<div class="form-outline mb-4">
						<label class="form-label style-largefont" for="ceppaciente">CEP</label>
						<input type="text" id="ceppaciente" class="form-control"/>
					</div>
				
					<button class="btn btn-primary style-marginbottom style-fiquegrande">Teste</button>

					<div class="d-grid gap-2 style-largefont style-marginbottom">
						<Link className ="App-link" to= "/Avaliacao">
							<button class="btn btn-primary style-marginbottom style-fiquegrande">Continuar</button>
						</Link>
					</div>

					<div class="d-grid gap-2 style-largefont style-marginbottom">
						<Link className ="App-link" to= "/">
							<button class="btn btn-primary style-marginbottom style-fiquegrande">Home</button>
						</Link>
					</div>
				</form>
			</div>
    )
}