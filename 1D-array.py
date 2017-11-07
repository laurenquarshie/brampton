# 1D ARRAY
# 7/11/17

# DECLARE Ages : ARRAY(0..9) OF INTEGER
Ages = [3,4,5,88,45,12,36,48,40,89]
#for index in range(9, -1, -1):
    #print (Ages[index])

for index in range(0,10):
        for x in range (0,9):
         if Ages[x] > Ages[x + 1] :
          Temp = Ages[x]
          Ages[x] = Ages[x + 1]
          Ages[x + 1] = Temp
for index in range (0,10):
 print (Ages[index])