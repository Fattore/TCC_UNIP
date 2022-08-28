export function createCheckbox(){
 
	var i = 1;
	var range = 5;

	while(i <= range){
		//cria a div que junta tudo
		var element = document.createElement("DIV");
		element.className += "form-check";

		//cria o checkbox do sintoma
		var newCheckbox = document.createElement("INPUT");
		//newCheckbox.classList.add("form-check-label me-2");
		newCheckbox.className += "form-check-label me-2";
		newCheckbox.setAttribute("type", 'checkbox');
		newCheckbox.setAttribute("value", '');
		newCheckbox.setAttribute("id", 'checkboxsintoma');

		//cria a label do sintoma
		var  newLabel = document.createElement("LABEL");
		//newLabel.classList.add("form-check-label");
		newLabel.className += "form-check-label"
		newLabel.setAttribute("for", 'checkboxsintoma');
		newLabel.innerHTML = "Sintoma";

		element.appendChild(newCheckbox);
		element.appendChild(newLabel);

		document.getElementById("sintomasForm").appendChild(element);

		i++;
	}
}