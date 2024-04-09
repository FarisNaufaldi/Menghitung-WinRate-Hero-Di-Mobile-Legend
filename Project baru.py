import math

def  memperbaikiWR(K,L,T,Z,P):
    W = (Z/100)*T
    W_akhir = math.ceil(W)
    print(f"Total kemenangan yang telah {K} raih menggunakan hero {L} adalah sebanyak {W_akhir}")
    Y = P-1
    X = float(W_akhir-(P*T))/Y
    X_akhir = math.ceil(X)
    print(f"Jadi {K}, Total kemenangan untuk {L} yang harus diraih secara beruntun tanpa kekalahan adalah {X_akhir} pertandingan")

nama = input("Hallo Selamat datang kembali di perhitungan Winrate yang dibuat Oleh Kreator, Kami ingin mengetahui nama kamu nih, Kasih tau dong, Jawab = ")
nama_hero = input(f"Jadi {nama}, nama hero favorit kamu apa nih yang mau diprediksi = ")
t = int(input(f"{nama}, Jumlah Total pertandingan {nama_hero} anda mainkan, ada berapa banyak sih, jawab = "))
z = float(input(f"Persentase kemenangan {nama_hero} yang sekarang dimiliki, jawab dengan angka saja, Isi: "))
c = float(input(f"Persentase kemenangan {nama_hero} yang diinginkan, jawab dengan angka saja, Isi: "))
p = c/100
memperbaikiWR(nama,nama_hero,t,z,p)