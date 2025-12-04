dokter = {
    1:{
        "nama_dokter": "Dr. Andi Pratama",
        "spesialis": "Dokter Anak"
    },
    2:{
        "nama_dokter": "Dr. Halimatus Zahro",
        "spesialis": "Spesialis Bedah"
    },
    3:{
        "nama_dokter": "Dr. Budi Hartono",
        "spesialis": "Spesialis Jantung"
    },
    4:{
        "nama_dokter": "Dr. Rina Agustina",
        "spesialis": "Spesialis Pembuluh Darah"
    },
    5:{
        "nama_dokter": "Dr. Kamelia Sari",
        "spesialis": "Spesialis Kandungan"
    },
    6:{
        "nama_dokter": "Dr. Muhammad Soekarno",
        "spesialis": "Spesialis THT"
    },
    7:{
        "nama_dokter": "Dr. Reno Irvansyah",
        "spesialis": "Spesialis Orang Dewasa"
    },
    8:{
        "nama_dokter": "Dr. habibi",
        "spesialis": "Dokter UMUM"
    }
}

def lihat_semua_data_dokter():

    if not dokter:
        print("============ DATA DOKTER KOSONG! ============\n")
        return
    
    print("\n============ LIST DATA DOKTER ============\n")
    print(f"{'ID':<4}|{'NAMA DOKTER':<25}|{'SPESIALIS':<30}")
    print("-" * 60)
    for id_data_dokter, data_dokter in dokter.items():
        nama_dokter = data_dokter['nama_dokter']
        bidang_dokter = data_dokter['spesialis']
        print(f"{id_data_dokter:<4}|{nama_dokter:<25}|{bidang_dokter:<30}")
    return

def cari_data_dokter():

    if not dokter:
        print("============ DATA DOKTER KOSONG! ============\n")
        return
    
    cari_dokter = input("Masukkan nama/spesialis dokter yang ingin dicari : ").lower()

    ketemu = False

    for id_data_dokter, data_dokter in dokter.items():
        nama_dokter = data_dokter["nama_dokter"].lower()
        bidang_dokter = data_dokter["spesialis"].lower()

        if cari_dokter in nama_dokter:
            if not ketemu:
                print("\n====== DATA DOKTER DITEMUKAN ======")
                print(f"{'ID':<4}|{'NAMA DOKTER':<25}|{'SPESIALIS':<30}|")
                print("-" * 60)
                ketemu = True
            print(f"{id_data_dokter:<4}|{nama_dokter:<25}|{bidang_dokter:<30}|")

        elif cari_dokter in bidang_dokter:
            if not ketemu:
                print("\n====== DATA DOKTER DITEMUKAN ======")
                print(f"{'ID':<4}|{'NAMA DOKTER':<25}|{'SPESIALIS':<30}")
                print("-" * 60)
                ketemu = True
            print(f"{id_data_dokter:<4}|{nama_dokter:<25}|{bidang_dokter:<30}|")

    if not ketemu:
        print("\nDOKTER TIDAK DITEMUKAN!\n") 
    return

def lihat_data_dokter():
    while True:
        judul = "LIHAT DATA DOKTER"
        label = "PILIH 1-3"
        print(f"\n====== {judul} ======")
        print("|1. LIHAT SEMUA DATA           |")
        print("|2. CARI DATA DOKTER           |")
        print("|3. KEMBALI                    |")
        print(f"========== {label} ==========\n")
        
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            lihat_semua_data_dokter()
            pass
        elif pilih == 2:
            cari_data_dokter()
        elif pilih == 3:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue
        return

def main_dokter():
    while True:
        judul = "DATA DOKTER"
        label = "PILIH 1-2"
        label_judul1 = "=" * (len(judul) + 14)
        print(f"\n{label_judul1}")
        print(f"====== {judul} ======")
        print("|1. LIHAT DATA DOKTER   |")
        print("|2. KEMBALI MENU        |")
        print(f"======= {label} =======")
        print(label_judul1)
    
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            lihat_data_dokter()
        elif pilih == 2:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue

