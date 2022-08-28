import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { HashRouter as Router, Route } from 'react-router-dom'

import Home from "./App"
import VerificarPaciente from "./pages/verificarpaciente"
import IniciarDiagnostico from "./pages/iniciardiagnostico"
import Avaliacao from './pages/avaliacao';
import Relatorio from './pages/relatorio';

ReactDOM.render(
    <Router>
        <div>
            <main>
                <Route exact path="/" component={Home} />
                <Route path="/VerificarPaciente" component={VerificarPaciente} />
				<Route path="/IniciarDiagnostico" component={IniciarDiagnostico} />
				<Route path="/Avaliacao" component={Avaliacao} />
				<Route path="/Relatorio" component={Relatorio} />
            </main>
        </div>
    </Router>, 
    document.getElementById("root")
    
)
