# Praktikum-5-DasPro
Praktikum 5 Dasar Pemrograman Institut Teknologi Bandung yang menggunakan bahasa Python
## Soal 1
Program menerima sebuah bilangan positif N (N dijamin lebih dari 1) serta array A yang terdiri atas N buah bilangan bulat. Tentukan nilai selisih minimum dari keseluruhan kemungkinan pasangan dua elemen berbeda pada array


Note: dilarang menggunakan fungsi sort

Hint: Untuk membaca array pada satu baris gunakan kode berikut

a = list(map(int, input().strip().split()))
## Soal 2
Program menerima N dan bilangan sebanyak N yang menggambarkan ketinggian balon. Balon memiliki kemunculan terurut berdasarkan indeks. Seorang penembak akan menembak balon dari ketinggian balon pertama yang muncul (indeks ke-0), lalu balon kedua yang muncul (indeks ke-1), dan seterusnya. Setiap mengenai balon, ketinggian tembakan akan berkurang 1. Jika tidak mengenai balon, ketinggian tetap. Keluarkan jumlah balon yang berhasil ditembak dan balon tertinggi kedua yang tidak tertembak. Jika tidak ada balon tertinggi kedua, keluarkan “Tidak ada”, tetapi tetap keluarkan jumlah balon yang berhasil ditembak.    

Note: 

Tidak diperkenankan menggunakan sort, max, min, pop, dan remove.
## Soal 3
Alice dan Bob sedang bermain sebuah Game, Alice diberikan dua buah bilangan N dan X yang merupakan bilangan bulat positif (X<=N) dan array A yang berisi N bilangan bulat. Pada game ini Bob akan memberikan M buah perintah kepada Alice. Perintah dari Bob formatnya dalam “S K”, S bisa berupa 1 atau 2 sedangkan K merupakan sebuah bilangan bulat non negatif. 

- Jika S merupakan 1 maka tukar nilai A pada posisi ke-X dengan elemen A pada posisi ke-(X-K) lalu assign X dengan nilai baru berupa X-K. 

- Jika S merupakan 2 maka tukar nilai A pada posisi ke-X dengan elemen A pada posisi ke-(X+K) lalu assign X dengan nilai baru berupa X+K. 

Keluarkan hasil array yang telah dilakukan M buah operasi, jika pada suatu saat X menunjuk elemen A yang berada di luar jangkauan array maka keluarkan “Tidak Valid”.
## Soal 4
nagram adalah salah satu jenis permainan kata yang huruf-huruf di kata awal biasanya diacak untuk membentuk kata lain atau sebuah kalimat. Program menerima dua buah kata. Kata pertama diinputkan per huruf dan selesai ketika pengguna memasukkan “a”. Kata kedua diinputkan per huruf dan selesai ketika pengguna memasukkan “b”. Huruf yang diinputkan adalah huruf kapital dan dijamin valid. Cek apakah kata pertama adalah anagram dari kata kedua. Jika benar, keluarkan tulisan “Benar”. Jika salah, keluarkan ada berapa huruf di kata pertama yang tidak ada di kata kedua. 

Note: 

Tidak diperkenankan menggunakan hash map, map, dictionary, in, dan sort.
## Soal 5
Diberikan sebuah bilangan bulat positif N dan array A yang berisi N buah bilangan bulat positif. Tentukan berapa banyak elemen array yang dapat direpresentasikan dalam bilangan p^x (‘^’ menyatakan operasi perpangkatan) dimana p merupakan bilangan prima dan x merupakan bilangan bulat non negatif. A[i] dijamin tidak lebih besar dari 500 dan N tidak lebih besar dari 100.
