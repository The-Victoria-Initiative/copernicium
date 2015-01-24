//--- Setup
var margin = {top: 40, right: 20, bottom: 80, left: 80};
var width  = (document.getElementById('scores').offsetWidth - margin.left - margin.right);
var height = (width - margin.top - margin.bottom);

    // width = 960 - margin.left - margin.right,
    // height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

var xAxis = d3.svg.axis().scale(x).orient("bottom");

var yAxis = d3.svg.axis().scale(y).orient("left");

var line = d3.svg.line()
    .x(function(d) { return x(d.generation); })
    .y(function(d) { return y(d.score); });

var svg = d3.select("#scores").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


d3.csv("evolution.csv", function(error, data) {
  x.domain(d3.extent(data, function(d) { return d.generation; }));
  var y_max = d3.max(data, function(d) { return parseFloat(d.score); });
  y.domain([0, y_max*1.2]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
     .append("text")
      .attr("transform", "translate("+(width-80)+",0)")
      .attr("y", 40)
      .text("Generation");

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", -55)
      .style("text-anchor", "end")
      .text("Score");


  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);
});