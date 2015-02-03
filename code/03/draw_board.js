//--- Setup
var width  = 400;
var height = 400;

board_svg = d3.select("#board").append("svg")
        .attr("width", width)
        .attr("height", height);

//--- Board
board_svg.append("rect")
   .attr("width", width)
   .attr("height", height)
   .style("fill-opacity", "0")
   .style("stroke-width", "3")
   .style("stroke",       "black");

//--- Initial cirle distribution
d3.csv("board_setup.csv", function(error, data) {
  console.log(data.length);
  board_svg.selectAll("circle")
     .data(data)
     .enter()
     .append("circle")
     .attr("cx", function(d) {return d.x;})
     .attr("cy", function(d) {return d.y;})
     .attr("r",  5);
});