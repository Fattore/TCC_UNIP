import React from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';

const VerificarPaciente = () => {
    return (
        <div className="styleVF-background">
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

				<table id="dtDynamicVerticalScrollExample" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">
				<thead>
					<tr>
						<th class="th-sm">Data Avaliação</th>
						<th class="th-sm">Nome Completo</th>
				</tr>
				</thead>
				<tbody>
					<tr>
						<td>2011/04/25</td>
						<td>Tiger Nixon</td>
					</tr>
					<tr>
						<td>2011/07/25</td>
						<td>Garrett Winters</td>
					</tr>
					<tr>
						<td>2009/01/12</td>
						<td>Ashton Cox</td>
					</tr>
					<tr>
						<td>2012/03/29</td>
						<td>Cedric Kelly</td>
					</tr>
					<tr>
						<td>2008/11/28</td>
						<td>Airi Satou</td>
					</tr>
					<tr>
						<td>2012/12/02</td>
						<td>Brielle Williamson</td>
					</tr>
					<tr>
						<td>2012/08/06</td>
						<td>Herrod Chandler</td>
					</tr>
					<tr>
						<td>2010/10/14</td>
						<td>Rhona Davidson</td>
					</tr>
				</tbody>
				<tfoot>
					<tr>
						<th>Data Avaliação</th>
						<th>Nome Completo</th>
					</tr>
				</tfoot>
			</table>
			</div>
            <Link className ="App-link" to= "/">Link to Home</Link>
        </div>
    )
}

export default VerificarPaciente