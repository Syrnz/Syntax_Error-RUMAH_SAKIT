from dokter import main_dokter
from pasien import main_pasien
from kamar import main_kamar
from transaksi import main_transaksi

def main():
    while True:
        judul = "RUMAH SAKIT"
        label = "PILIH 1-5"
        label_judul1 = "=" * (len(judul) + 10)
        print(label_judul1)
        print(f"==== {judul} ====")
        print("|1. DATA DOKTER     |")
        print("|2. DATA PASIEN     |")
        print("|3. DATA KAMAR INAP |")
        print("|4. DATA TRANSAKSI  |")
        print("|5. SELESAI         |")
        print(f"===== {label} =====")
        print(label_judul1)

        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            main_dokter()
        elif pilih == 2:
            main_pasien()
        elif pilih == 3:
            main_kamar()
        elif pilih == 4:
            main_transaksi()
        elif pilih == 5:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue

main()