//--- Setup
var margin = {top: 40, right: 20, bottom: 80, left: 80};
var width  = (document.getElementById('scores').offsetWidth - margin.left - margin.right);
var height = (width - margin.top - margin.bottom);

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

// mouse capture focus
focus = svg.append("g").style("display", "none"); // defaults to off
var bisectDate = d3.bisector(function(d) { return d.generation; }).left;


d3.csv("evolution.csv", function(error, data) {
  x.domain(d3.extent(data, function(d) { return parseFloat(d.generation); }));
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
      .text("Minimum distance");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);

  // tool tip
  focus.append("circle")                            
       .attr("class", "y")                           
       .style("fill", "none")                        
       .style("stroke", "#428bca")   
       .style("stroke-width", "1.5px")                   
       .attr("r", 4); 
  focus.append("line")
       .attr("class", "y")
       .style("stroke", "grey")
       .style("stroke-dasharray", "3,3")
       .style("stroke-width", "1.5px")
       .attr("x1", width)
       .attr("x2", width);
  focus.append("line")
       .attr("class", "x")
       .style("stroke", "grey")
       .style("stroke-dasharray", "3,3")
       .style("stroke-width", "1.5px")
       .attr("y1", height)
       .attr("y2", 0);

  // append the rectangle to capture mouse          
  svg.append("rect")                                
     .attr("width", width)                         
     .attr("height", height)                       
     .style("fill", "none")                        
     .style("pointer-events", "all")               
     .on("mouseover", function() {
        focus.style("display", null);
     })
     .on("mousemove", mousemove);                  

  function mousemove() {                            
    var x0 = x.invert(d3.mouse(this)[0]),         
        i = bisectDate(data, x0, 1),              
        d0 = data[i - 1],                         
        d1 = data[i],                             
        d = x0 - d0.generation > d1.generation - x0 ? d1 : d0;
        i = x0 - d0.generation > d1.generation - x0 ? i : i-1;
    current_datum = d;

    focus.select("circle.y")                   
        .attr("transform",                        
              "translate(" + x(d.generation) + "," +    
                             y(d.score) + ")"); 

   focus.select("line.y")
        .attr("transform", "translate(0," +y(d.score) + ")")
        .attr("x1", x(d.generation))
        .attr("x2", 0);
    focus.select("line.x")
        .attr("transform","translate(" + x(d.generation) + ",0)")
        .attr("y1", height)
        .attr("y2", y(d.score));

    // board_svg.selectAll("circle").filter(".a")
    //          .attr("cx",d.x)
    //          .attr("cy",d.y)
    //          .attr("r", d.r);
  }
});

// function loadResults(results) {
//   svg.append("line")
//      .attr("class","best")
//      .attr("x1", 0)
//      .attr("x2", width)
//      .attr("y1", function (){ return y(parseFloat(results["Brute force score"]));})
//      .attr("y2", function (){ return y(parseFloat(results["Brute force score"]));});
// }

// d3.json("results.json", loadResults);
