###################
print "test : --- Testing a population"
import Canvas
import FitnessMeasures
import Line
import Population
import Tools
###################
print "test : generating an empty canvas"
width  = 32
height = 32
canvas = Canvas.Canvas(width,height)
print "test : Drawing a square on the board"
canvas.add_line(Line.Line(100,100, 300,100))
canvas.add_line(Line.Line(300,100, 300,300))
canvas.add_line(Line.Line(300,300, 100,300))
canvas.add_line(Line.Line(100,300, 100,100))
file_name = "/zinc/web/copernicium/04/images/ideal.bmp"
canvas.save(file_name)
print "test : Generating fitness measure"
fitness = FitnessMeasures.CanvasFitnessMeasure(canvas)

bases   = Tools.MinBases(max(width,height))
print "test : max dimension: %i, bases: %i (2^%i = %i)"%(max(width,height),bases,bases,2**bases)
n_lines = 4

print "test : --- Generate a population"
population = Population.Population(fitness,n_genotypes=20,n_bases=bases,n_genes=4*n_lines)
print population
print "test : ---"
###################
print "test : --- Select fittest"
fittest = population.select_fittest()
for f in fittest:
    print f, f.eval()
print "test : ---"
###################
print "test : --- Breed the an example of the next generation"
next_gen = population.breed(fittest)
print next_gen
print "test : ---"
###################
print "test : --- Breed the next generation"
population.breed_next_generation()
population.eval()
print population
print "test : ---"
###################
print "test : --- done\n"