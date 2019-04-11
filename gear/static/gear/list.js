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


