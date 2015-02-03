//--- Setup
parameters_div = d3.select("#parameters");

d3.csv("parameters.csv", function(error, data) {
  parameters_div.selectAll("li")
     .data(data)
     .enter()
     .append("li").html( function (d) {
        return "<strong>"+d.parameter+"</strong>: "+d.value;
     });
});

results_div = d3.select("#results");

function loadResultsText(results) {
   results_div.selectAll("li")
     .data(d3.keys(results).sort())
     .enter()
     .append("li").html( function (d) {
        return "<strong>"+d+"</strong>: "+results[d];
     });
}

d3.json("results.json", loadResultsText);