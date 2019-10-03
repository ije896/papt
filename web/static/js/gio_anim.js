// get the container to hold the IO globe
var container = document.getElementById( "globalArea" );

// create controller for the IO globe, input the container as the parameter
var controller = new GIO.Controller( container );


var data;


/**
* use addData() API to add the the data to the controller
* know more about data format, check out documentation about data: http://giojs.org/html/docs/dataIntro.html
* we provide sample data for test, get sample data from: https://github.com/syt123450/giojs/blob/master/examples/data/sampleData.json
*/
// controller.addData( data );

// call the init() API to show the IO globe in the browser
function draw() {
  controller.init();
}

draw();

console.log("hit eof")
