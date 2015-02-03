var genotype_margin = {top: 10, right: 10, bottom: 10, left: 10};
var genotype_width  = (document.getElementById('genotype').offsetWidth - genotype_margin.left - genotype_margin.right);
var genotype_height = 20;
var genotype_svg = d3.select("#genotype").append("svg")
genotype_svg.attr("width", genotype_width + genotype_margin.left + genotype_margin.right)
            .attr("height", genotype_height + genotype_margin.top + genotype_margin.bottom);

var counter = 0;
var text_counter = 0;
var tooltip = d3.select("#genotype").append("div")
                          .attr("class", "tooltip")
                          .style("opacity", 0);


d3.json("genotype.json", function(error, data) {
  console.log(data.length);
  var gene_width  = genotype_width/data.genes.length;
  var inner_width = gene_width-5;
  genotype_svg.selectAll("rect")
     .data(data.genes)
     .enter()
     .append("rect")
       .attr("class","gene")
       .attr("width",  function () {return inner_width;})
       .attr("height", genotype_height)
       .attr("x", function (){
        var dx = gene_width*counter;
        counter++;
        return dx;
       })
       .on("mouseover", function(d) {
        d3.select(this).style("fill", "blue");
        tooltip.transition()
               .duration(200)
               .style("opacity", .9);
        tooltip.html("<strong>Code:</strong> <span style='color:red'>" + d.code +
                     "</span></br><strong>Circle:</strong> <span style='color:red'>" + d.number +"</span>")
               .style("left", d3.select(this).attr("x") + "px")
               .style("top",  d3.select(this).attr("y") + "px");
       })
       .on("mouseout", function(d) {
        d3.select(this).style("fill", "green");
        tooltip.transition()
               .duration(500)
               .style("opacity", 0);
       });

  // genotype_svg.selectAll("text")
  //     .data(data.genes)
  //     .enter().append("text")
  //     .attr("class","good")
  //     .attr("x", function (){
  //       var dx = (genotype_width/data.genes.length)*text_counter+(0.2*(genotype_width/data.genes.length));
  //       text_counter++;
  //       return dx;
  //      })
  //     .attr("y", genotype_height/2)
  //     .attr("text-anchor","middle")
  //     .text(function (d){return d.number;});
});