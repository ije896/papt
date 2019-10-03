function preload(){

}

function setup() {
  createCanvas(400, 300, WEBGL);
  noFill();
}

// PShape globe;

function draw() {
  // background(0);

  fill(250, 0, 0);
  // // translate(width / 2, height / 2);
  // sphere(40, 10, 10);


  background(175);
  // rotateX(angle);
  // rotateY(angle);
  // rotateZ(angle * 0.75);
  rotateX(frameCount * 0.001);
  rotateY(frameCount * 0.003);
  rotateZ(frameCount * 0.002);
  smooth();
  sphere(75);
  // angle += 0.025;

}

// alert("hello");
