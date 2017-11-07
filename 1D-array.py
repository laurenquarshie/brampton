# 1D ARRAY
# 7/11/17

# DECLARE Ages : ARRAY(0..9) OF INTEGER
Ages = []
for index in range (0,10):
 num = int(input("enter a number between zero and 10"))
 while num > 10 or num < 0:
  print("error - not within range")
  input("enter a number between 0 and 10")


 Ages.append(num)


#Ages = [3,4,5,88,45,12,36,48,40,89]



for index in range(0,10):
        for x in range (0,9):
         if Ages[x] > Ages[x + 1] :
          Temp = Ages[x]
          Ages[x] = Ages[x + 1]
          Ages[x + 1] = Temp
for index in range (0,10):
 print (Ages[index])