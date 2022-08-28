import React, { useState } from 'react';
import "../App.css";
import 'bootstrap/dist/css/bootstrap.min.css';

const MyComp = ({ entries }) => {
	const [check, setCheck] = useState({});
  
	const onChange = (id) => {
	  return (e) => {
		const checks = check;
		checks[id] = e.target.checked;
		setCheck({ ...checks });
	  };
	}

	return (
	  <div class="form-check">
		<p>Selected: {JSON.stringify(check)}</p>
		{entries.map((entry) => (
		  <>	
			<input
				class="form-check-label me-2"
			  	key={entry.id}
			  	value={check[entry.id]}
			  	onChange={onChange(entry.id)}
			  	type="checkbox"
			/>
			<label class="form-check-label">{entry.name}</label>
		  </>
		))}
	  </div>
	);
}

export default MyComp