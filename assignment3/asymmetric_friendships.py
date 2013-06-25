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
    personA = record[0]
    personB = record[1]
    key_set = list(personA)
    key_set.append(personB)
    key = frozenset((personA,personB))
    #print key
    value = 1
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = len(list_of_values)
    print key
    print total
    if len(list_of_values) == 1:
		output = []
		for v in key:
			output.append(v)
		op = tuple(output)
		r_op = tuple(reversed(op))
		mr.emit(op)
		mr.emit(r_op)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
