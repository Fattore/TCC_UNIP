import React, { useState, useEffect } from "react";
import "../App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "../pages/avaliacao.js";

const MyComp = ({ entries, onSubmit }) => {
	const [check, setCheck] = useState({});
  
	useEffect(() => {
	  //* Popula a lista de checks ao inicializar(re-executa quando 'entries' altera)
	  let newChecks = {};
	  for (const entry of entries) {
		newChecks[entry.id] = entry.value === 'sim';
	  }
	  setCheck({ ...newChecks });
	}, [entries]);
  
	const onChange = id => {
	  return e => {
		const checks = check;
		checks[id] = e.target.checked;
		console.log(checks);
		setCheck({ ...checks });
	  };
	};
  
	return (
	  <div className="form-check">
		{Object.keys(check).map((id) => {
		  const entry = check[id];
		  const meta = entries.find((x) => x.id === id);
  
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
		<button class="btn btn-primary" onClick={() => onSubmit(Object.values(check).map((x) => (x ? "sim" : "nao")))}>
		  Enviar
		</button>
	  </div>
	);
  };
  
export default MyComp;