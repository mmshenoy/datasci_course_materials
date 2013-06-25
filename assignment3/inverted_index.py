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
    value = record[0]
    key = record[1]
    #print value + "\t" + key
    #value = record[1]
    words = key.split()
    for w in words:
      mr.emit_intermediate(w, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = set()
    for v in list_of_values:
      total.add(v)
    total_list = list(total)
    mr.emit((key, total_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
