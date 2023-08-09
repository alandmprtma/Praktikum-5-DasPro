#Nama : Aland Mulia Pratama
#NIM : 19622296

#Program Anagram
#KAMUS
#N = int
#a = list of integer
#mini = integer
#selisih = integer

#ALGORITMA
prima = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

N = int(input())
a = list(map(int, input().strip().split()))

j = 0
for i in range (N):
    for j in range(len(prima)):
        angka = a[i]
        bilprim = prima[j]
        cek = 1
        jumlah = 0 
        while cek < angka:
            if cek < angka:
                cek *= bilprim
            elif cek == angka:
                jumlah += 1
print(jumlah)