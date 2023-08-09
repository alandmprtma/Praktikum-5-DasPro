#Nama : Aland Mulia Pratama
#NIM : 19622296

#Program Selisih Maksimum
#KAMUS
#N = int
#a = list of integer
#mini = integer
#selisih = integer

#ALGORITMA
N = int(input())
a = list(map(int, input().strip().split()))


mini = 9999
for i in range (N):
    for j in range (N):
        if i != j:
            selisih = abs(a[i]-a[j])
            if selisih < mini:
                mini = selisih
print(mini)

        