import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)
    #words = value.split()
    #for w in words:
    #  mr.emit_intermediate(w, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = []
    #for v in list_of_values:
    #  total += v
    #mr.emit((key, total))
	#print "\n" + key
	for v in range(0,len(list_of_values)):
		type_v = list_of_values[v][0]
		for x in range(v+1,len(list_of_values)):
			type_x = list_of_values[x][0]
			if type_v != type_x:
				val = list_of_values[v] + list_of_values[x]
				mr.emit(val)
				#print type((list_of_values[v],list_of_values[x]))
		

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
