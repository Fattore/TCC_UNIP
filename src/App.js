import React from 'react';
import { Link } from "react-router-dom"
import logo from './logo.jpeg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <header className="App-header styleVF-background">
        <img src={logo} className="App-logo rounded mx-auto d-block style-indexmargin" alt="logo" />
			<div class="d-grid gap-2 col-6 mx-auto tyle-index">
				<Link id="iniciarDiagnostico" className="App-link" to="/Avaliacao">
					<button id="iniciarDiagnostico" class="btn btn-primary style-fiquegrande">Iniciar</button>
				</Link>
					{/*
				<Link id="verificarPacientes" className="App-link" to="/VerificarPaciente">
					<button id="iniciarDiagnostico" class="btn btn-primary style-fiquegrande">Verificar</button>
				</Link>
  					*/}
			</div>
      </header>
    </div>
  );
}

export default App;
