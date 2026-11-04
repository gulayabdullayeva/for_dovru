# 1.for dovru - saygacli dovurdur
for i in range(10):
    print(i)
    
# 2.eger star yazilmasa default olaraq start = 0 olacaq
for i in range(2, 10):
    print(i)
    
# 3.eger step yazilmasa default olaraq step = 1 olacaq
for i in range(2, 10, 2):
    print(i)

# 4.butun sozler tek tek cap etmek isteyrikse 
for i in "Python":
    print(i)
    
# 5.eger her herifin yaninda * yazmak isteyirkse
for i in "Python":
    print(i, end="*")
    
# 6.eger herifi butov yazmag isteyirikse
for i in "Python":
    print(i, end="")
