import React from "react"
import { Link } from "react-router-dom"
import "../App.css"
import 'bootstrap/dist/css/bootstrap.min.css';

const Relatorio = () => {
    return (
        <div class="">
			<div class="container styleVF-container">
			<form class="style-paddingtoptres">
				<div class="card style-card">
					<h4 class="card-header">RELATÓRIO</h4>

					<div id="accordion" role="tablist" aria-multiselectable="true">
						<div class="card">
							<h5 class="card-header" role="tab" id="headingOne">
								<a data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne" class="d-block">
									<i class="fa fa-chevron-down pull-right"></i> Collapsible Group Item #1
								</a>
							</h5>
					
							<div id="collapseOne" class="collapse show" role="tabpanel" aria-labelledby="headingOne">
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
						<div class="card">
							<h5 class="card-header" role="tab" id="headingTwo">
								<a class="collapsed d-block" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
									<i class="fa fa-chevron-down pull-right"></i> Collapsible Group Item #2
								</a>
							</h5>
							<div id="collapseTwo" class="collapse" role="tabpanel" aria-labelledby="headingTwo">
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
						<div class="card">
							<h5 class="card-header" role="tab" id="headingThree">
								<a class="collapsed d-block" data-toggle="collapse" data-parent="#accordion" href="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
									<i class="fa fa-chevron-down pull-right"></i> Collapsible Group Item #3
								</a>
							</h5>
							<div id="collapseThree" class="collapse" role="tabpanel" aria-labelledby="headingThree">
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

				</div>

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

					<div  class="style-threeall">
						<Link className ="App-link" to= "/">
							<button class="btn btn-primary style-marginfive style-fiquegrande" type="button">Home</button>
						</Link>
					</div>
				</div>
			</form>
			</div>
        </div>
    )
}

export default Relatorio