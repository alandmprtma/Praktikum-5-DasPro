#Nama : Aland Mulia Pratama
#NIM : 19622296

#Program Anagram
#KAMUS
#N = int
#a = list of integer
#mini = integer
#selisih = integer

#ALGORITMA
arr1 = []
a = input()
while a != "a":
    arr1.append(a)
    a = input()

arr2 = []
b = input()
while b != "b":
    arr2.append(b)
    b = input()

found = 0
if len(arr1) < len(arr2):
    print(0)
elif len (arr1) > len(arr2):
    for i in range (len(arr2)):
        for j in range  (len(arr1)):
            if arr2[i] == arr1[j]:
                found += 1
    if found > len(arr2):
        print(len(arr1)-len(arr2))
    else:
        print(len(arr1) - found)
else:
    for i in range (len(arr1)):
        for j in range  (len(arr2)):
            if arr1[i] == arr2[j]:
                found += 1 
    if found == len(arr1):
        print("Benar")
    else:
        print(len(arr1)-found)