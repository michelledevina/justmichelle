import math

# Diketahui
P = 200_000_000  
A = 400_000_000  
r = 0.10         
n = 1            

t = math.log(A / P) / (n * math.log(1 + r / n))

t_bulat = round(t, 2)

print("Waktu yang dibutuhkan:", t_bulat, "tahun")
