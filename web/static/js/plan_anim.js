

(function(){

  var planet = planetaryjs.planet();

  // planet.loadPlugin(autorotate(10));


  planet.loadPlugin(planetaryjs.plugins.earth({
    topojson: { file: 'static/js/assets/world-110m-withlakes.json'},
    oceans:   { fill:   'transparent' },
    land:     { fill:   'transparent', stroke:'#000000' },
    borders:  { stroke: '#000000' }
  }))

  // planet.loadPlugin(lakes({
  //   fill: '#000080'
  // }));

  planet.loadPlugin(planetaryjs.plugins.zoom({
    scaleExtent: [100, 300]
  }));

  planet.loadPlugin(planetaryjs.plugins.drag({
    onDragStart: function () {
      //
    },
    onDragEnd: function () {
      //
    }
  }));

  planet.projection.scale(175).translate([175, 175]).rotate([0, -10, 0]);


  var canvas = document.getElementById('globalArea');
  planet.projection
    .scale(canvas.width / 2)
    .translate([canvas.width / 2, canvas.height / 2]);
  planet.draw(canvas);

})();
