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
    type = record[0]
    if type == "a":
		#premultiplier
		row = record[1]
		for i in range(0,5):
			list = []
			list.append(row)
			list.append(i)
			mr.emit_intermediate(tuple(list),record)
	
    else:
		#postmultiplier
		col = record[2]
		for i in range(0,5):
			list = []
			list.append(i)
			list.append(col)
			mr.emit_intermediate(tuple(list),record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = [0 for x in xrange(5)]
    b = [0 for x in xrange(5)]
    row = key[0]
    col = key[1]
    for v in list_of_values:
		if v[0] == "a":
			a[v[2]] = v[3]
		else:
			b[v[1]] = v[3]
	
    val = 0
    for i in xrange(5):
		val += a[i]*b[i]
	
    list_key = list(key)
    list_key.append(val)
    mr.emit(tuple(list_key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
