import React from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';
const electron = window.require('electron');
const ipcRenderer  = electron.ipcRenderer;

ipcRenderer.on("fromPython", (event, data) => {
	console.log(data)
})
const Relatorio = () => {
    return (
        <div>
			<div class="container styleVF-container">
				<form class="style-paddingtoptres">
					<div class="card style-card">
						<h4 class="card-header">RELATÓRIO</h4>

						<div id="accordion" role="tablist" aria-multiselectable="true">
							<div class="card">
								<h5 class="card-header" role="tab" id="headingOne">
									Doença Principal
								</h5>
								<div class="card-body">
									Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf
									moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod.
									Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda
									shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
									proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim
									aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
								</div>
							</div>
						</div>
					</div>

		{/*
					<div class="d-grid gap-2 d-md-block">
						
						<div  class="style-threeall">
							<button class="btn btn-primary style-marginfive style-fiquegrande" type="button">Refazer</button>
						</div>

						<div  class="style-threeall">
							<button class="btn btn-primary style-marginfive style-fiquegrande" type="button">Gerar</button>
						</div>

						<div  class="style-threeall">
							<button class="btn btn-primary style-marginfive style-fiquegrande" type="button">Concluir</button>
						</div>
		*/}

					<div class="style-threeall">
						<Link className ="App-link" to= "/">
							<button class="btn btn-primary style-marginfive style-fiquegrande" type="button">Home</button>
						</Link>
					</div>
				</form>
			</div>
        </div>
    )
}

export default Relatorio