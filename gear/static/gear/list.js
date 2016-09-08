//js for list.html
function myFunction() {
	var text = prompt ("name item")
    document.getElementById("demo").innerHTML = text;
    
}

//function ran_col() { //function name

   // var color = '#'; // hexadecimal starting symbol
  //  var letters = ['000000','FF0000','00FF00','0000FF','FFFF00','00FFFF','FF00FF','C0C0C0']; //Set your colors here
 //   color += letters[Math.floor(Math.random() * letters.length)];

    
   // 	document.getElementById('list-color').style.background = color; // Setting the random color on your div element.

//}


//keep boxed checked and store state locally
var checkboxValues = JSON.parse(localStorage.getItem('checkboxValues')) || {},
    $checkboxes = $("#checkbox-container :checkbox");

$checkboxes.on("click", function(){
    checkboxValues[this.id] = this.checked;
  
  localStorage.setItem("checkboxValues", JSON.stringify(checkboxValues));
});

// On page load
$.each(checkboxValues, function(key, value) {
  $("#" + key).prop('checked', value);
});


