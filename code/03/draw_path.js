
//--- Draw path
d3.csv("path.csv", function(error, data) {
  console.log(data.length);
  board_svg.selectAll("path")
     .data(data)
     .enter()
     .append("path")
     .attr("class","journey")
     .attr("d", function(d) {return d.path;});
});