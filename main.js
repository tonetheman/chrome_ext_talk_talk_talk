
function speak() {
	var msg = new SpeechSynthesisUtterance(
	document.getElementById("ta").value);
	window.speechSynthesis.speak(msg);
}

function clear_textarea() {
	document.getElementById("ta").value = "";
}

window.onload = function() {
	console.log("onload is called");
	var btn = document.getElementById("speak");
	btn.addEventListener("click", speak);
	
	document.getElementById("clear").addEventListener("click", clear_textarea);

}