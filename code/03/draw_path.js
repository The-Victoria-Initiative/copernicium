
//--- Draw path
d3.csv("path.csv", function(error, data) {
  console.log(data.length);
  board_svg.selectAll("line")
     .data(data)
     .enter()
     .append("line")
     .attr("x1", function(d) {return d.x1;})
     .attr("y1", function(d) {return d.y1;})
     .attr("x2", function(d) {return d.x2;})
     .attr("y2", function(d) {return d.y2;});
});