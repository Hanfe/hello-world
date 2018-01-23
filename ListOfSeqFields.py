"""
Generates a comma-delimited list of sequentially numbered words or field names.
Useful when writing static SQL statements that include a list of fields with
the same base number and a sequential number.
Input: base word
        upper limit
"""
def printSeqFields(base, limit):
    for i in range(1,limit):   
        print(base + str(i).zfill(2), end=',')
    
printSeqFields("sdcp", 13);
