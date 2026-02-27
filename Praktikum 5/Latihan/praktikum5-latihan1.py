# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2
#===========================
#Latihan 1: Rekursi Pangkat
#===========================
def pangkat (a,n):
    #base case
    if n == 0:
        return 1
    
    #recursive case
    return a * pangkat (a, n-1)


print(pangkat(2,4)) #output 16
