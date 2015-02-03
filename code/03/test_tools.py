###################
print "test : --- Testing tools"
import Tools
import Point
import time
###################
print "test : --- Test filling an area with points"
width  = 400
height = 400
n_points  = 33
points = Tools.FillBoard(width,height,n_points)
print points
###################
print "test : --- Write points to file"
file_name = "board_setup.csv"
# for c in extra_points:
#     points.append(Circle.Circle(c.x,c.y,c.r,c="b"))
Tools.WritePointsToCSV(points,file_name)
###################
print "test : --- Work out the number of bases needed to encode n points"
bases = Tools.MinBases(n_points)
print "test : points: %i, bases: %i (2^%i = %i)"%(n_points,bases,bases,2**bases)
###################
print "test : --- Write a path to a file"
path = [0,1,2]
file_name = "path.csv"
Tools.WritePathToFile(path,points,file_name)
###################
print "test : --- Write genotype to file"
import TSGenotype
ts_genotype = TSGenotype.TSGenotype(n_bases=4,n_genes=2)
file_name = "genotype.json"
Tools.WriteGenotypeToJSON(ts_genotype,file_name)
###################
print "test : --- done\n"