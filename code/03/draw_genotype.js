var genotype_margin = {top: 10, right: 10, bottom: 10, left: 10};
var genotype_width  = (document.getElementById('genotype').offsetWidth - genotype_margin.left - genotype_margin.right);
var genotype_height = 20;
var genotype_svg = d3.select("#genotype").append("svg")
genotype_svg.attr("width", genotype_width + genotype_margin.left + genotype_margin.right)
            .attr("height", genotype_height + genotype_margin.top + genotype_margin.bottom);

var tooltip = d3.select("#genotype").append("div")
                          .attr("class", "tooltip")
                          .style("opacity", 0);



function codingToColour(d){
  if (d.in_use){
    return "green";
  }
  return "grey";
}

function codingToOpacity(d){
  if (d.in_use){
    return 1;
  }
  return 0.2;
}

function draw_genotype(data){
  var gene_width  = genotype_width/data.length;
  genotype_svg.selectAll("circle").remove();

  // draw connecting lines
  genotype_svg.selectAll("line")
     .data(data)
     .enter()
     .append("line")
       .attr("class","connector")
       .attr("y1", gene_width/2.)
       .attr("y2", gene_width/2.)
       .attr("x1", function(d,i){
        var dx = gene_width*i;
        return dx;
       })
       .attr("x2", function (d,i){
        var dx = gene_width*i;
        return dx + gene_width;
       })
       .style("opacity", function(d,i){
         if (i == 0) return 0;
         return 0.2;
       });

  // draw circles
  genotype_svg.selectAll("circle")
     .data(data)
     .enter()
     .append("circle")
       .attr("class","gene")
       .attr("cy", gene_width/2.)
       .attr("r",  gene_width/3.)
       .attr("cx", function (d,i){
        // console.log("update: "+d.code);
        var dx = gene_width*(i+1);
        return dx;
       })
       .style("fill",    function(d){return codingToColour(d);})
       .style("opacity", function(d){return codingToOpacity(d);})
       .on("mouseover", function(d) {
        d3.select(this).style("fill", "blue");
        tooltip.transition()
               .duration(200)
               .style("opacity", .9);
        tooltip.html("<strong>Code:</strong> <span style='color:red'>" + d.code +
                     "</span></br><strong>Circle:</strong> <span style='color:red'>" + d.number +"</span>")
               .style("left", d3.select(this).attr("cx") + "px")
               .style("top",  (parseFloat(d3.select(this).attr("cy")) + 20)+ "px");
       })
       .on("mouseout", function(d) {
        d3.select(this).style("fill", codingToColour(d));
        tooltip.transition()
               .duration(500)
               .style("opacity", 0);
       });
}

d3.json("genotype.json", function(error, data) {
  draw_genotype(data.genes);
});