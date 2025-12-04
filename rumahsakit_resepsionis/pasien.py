from validasi_input import cek_input_no_error_all
from validasi_input import cek_input_no_error_kosong

id_pasien = 2
pasien = {
    1: {
        "nama_pasien": "Reno Irvansyah",
        "umur_pasien": 20,
        "kategori_pasien": "REMAJA",
        "alamat_pasien": "Mojokerto"
    }
}

def tambah_data_pasien():

    global id_pasien
    while True:
        print("\n ==========================================")
        print("ketik 'N' untuk membatalkan input")
        input_nama_pasien = input("Masukkan nama pasien : ")

        if input_nama_pasien == "n" or input_nama_pasien == "N":
            print("Tambah Pasien Dibatalkan!")
            return
        if cek_input_no_error_all(input_nama_pasien):
            continue

        while True:
            print("\n ==========================================")
            try:
                umur_pasien = int(input("Masukkan umur pasien : "))
            except:
                print("INPUT HARUS ANGKA! ULANGI!")
                continue
            if umur_pasien <= 0:
                print("Umur tidak valid! Masukkan umur yang benar.")
                continue
            elif umur_pasien <= 12:
                kategori_pasien = "ANAK-ANAK"
                break
            elif 13 <= umur_pasien <= 20:
                kategori_pasien = "REMAJA"
                break
            elif 21 <= umur_pasien <= 59:
                kategori_pasien = "DEWASA"
                break
            elif 60 <= umur_pasien <= 123:
                kategori_pasien = "LANSIA"
                break
            else:
                umur_pasien > 123
                print("Umur tidak valid! Masukkan umur yang benar.")
                continue

        while True:
            print("\n ========================================")
            input_alamat = input("Masukkan alamat pasien : ")
            
            if cek_input_no_error_kosong(input_alamat):
                continue
                
            pasien[id_pasien] = {"nama_pasien": input_nama_pasien,"umur_pasien": umur_pasien, "kategori_pasien": kategori_pasien ,"alamat_pasien": input_alamat}
            print("DATA PASIEN BERHASIL DITAMBAHKAN\n")
            id_pasien += 1
            break
        
        print("")
        pilih = input("Tambah data lagi? (y) : ").lower()
        if pilih == "y" or pilih == "ya" or pilih == "iya":
            continue
        else:
            print("---Kembali ke menu---")
            break
def lihat_semua_data_pasien():
    if not pasien:
        print("============ DATA PASIEN KOSONG! ============\n")
        return
    else:
        print("============ LIST DATA PASIEN ============\n")
        print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
        print("-" * 60)
        for id_data_pasien, data_pasien in pasien.items():
            nama_pasien = data_pasien['nama_pasien']
            umur_pasien = str(data_pasien['umur_pasien'])
            kategori_pasien = data_pasien['kategori_pasien']
            alamat_pasien = data_pasien['alamat_pasien']

            print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")

def cari_data_pasien():

    if not pasien:
        print("============ DATA PASIEN KOSONG! ============\n")
        return
    
    while True:
        cari_pasien = input("Masukkan data pasien berdasarkan nama, umur, kategori, atau alamat : ").lower()
        if cek_input_no_error_kosong(cari_pasien):
            continue

        ketemu = False

        for id_data_pasien, data_pasien in pasien.items():
            nama_pasien = data_pasien['nama_pasien'].lower()
            umur_pasien = str(data_pasien['umur_pasien'])
            kategori_pasien = data_pasien['kategori_pasien'].lower()
            alamat_pasien = data_pasien['alamat_pasien'].lower()
        
            if cari_pasien in nama_pasien:
                if not ketemu:
                    print("\n====== DATA PASIEN DITEMUKAN ======")
                    print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
                    print("-" * 60)
                    ketemu = True
                print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")

            elif cari_pasien in umur_pasien:
                if not ketemu:
                    print("\n====== DATA PASIEN DITEMUKAN ======")
                    print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
                    print("-" * 60)
                    ketemu = True
                print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")

            elif cari_pasien in kategori_pasien:
                if not ketemu:
                    print("\n====== DATA PASIEN DITEMUKAN ======")
                    print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
                    print("-" * 60)
                    ketemu = True
                print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")
                
            elif cari_pasien in alamat_pasien:
                if not ketemu :
                    print("\n====== DATA PASIEN DITEMUKAN ======")
                    print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
                    print("-" * 60)
                    ketemu = True
                print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")
                
        if not ketemu:
            print("\nPASIEN TIDAK DITEMUKAN!")  

        return

def lihat_data_pasien():

    while True:
        judul = "LIHAT DATA PASIEN"
        label = "PILIH 1-3"
        print(f"\n====== {judul} ======")
        print("|1. LIHAT SEMUA DATA          |")
        print("|2. CARI DATA                 |")
        print("|3. KEMBALI                   |")
        print(f"========== {label} ==========\n")
        
        try:
            pilih = int(input("pilih program :"))
        except:
            print("INPUT HARUS ANGKA! MASUKKAN KEMBALI")
            continue
        if pilih == 1:
            lihat_semua_data_pasien()
        elif pilih == 2:
            cari_data_pasien()
        elif pilih == 3:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR, ULANGI LAGI! ")
            continue
        return
    
def update_data_nama_pasien():

    lihat_semua_data_pasien()
    if not pasien:
        return
    
    while True:
        try:
            cari_data_id_pasien = int(input("Masukkan ID Pasien yang ingin di ubah: "))
        except:
            print("Input harus berupa angka!")
            continue

        ketemu = False
        for id_data_pasien, data_pasien in pasien.items():
            nama_pasien = data_pasien['nama_pasien']
            umur_pasien = str(data_pasien['umur_pasien'])
            kategori_pasien = data_pasien['kategori_pasien']
            alamat_pasien = data_pasien['alamat_pasien']

            if id_data_pasien == cari_data_id_pasien:
                if not ketemu:
                    print("\n====== DATA PASIEN DITEMUKAN ======")
                    print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
                    print("-" * 60)  
                    ketemu = True
                print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")

                print("\n =============== UPDATE NAMA ================")
                while True:
                    input_nama_pasien_baru = input("Masukkan nama pasien baru : ")

                    if cek_input_no_error_all(input_nama_pasien_baru):
                        continue

                    yakin = input("Yakin ingin update data ini? (y/n) : ").lower()
                    if yakin == "y" or yakin == "ya" or yakin == "iya" or yakin == "yes":
                        pasien.update({id_data_pasien:{"nama_pasien": input_nama_pasien_baru, "umur_pasien": umur_pasien, "kategori_pasien": kategori_pasien, "alamat_pasien": alamat_pasien}})
                        print("\nDATA BERHASIL DI UPDATE")
                        break
                    elif yakin == "n" or yakin == "no" or yakin == "tidak":
                        print("\nData pasien batal di update!")
                        break
                    else:
                        print("HANYA Y/N !")
                        continue
            if not ketemu:
                print("\n Data pasien tidak ditemukan!")
                
        return

def update_data_umur_pasien():

    lihat_semua_data_pasien()
    if not pasien:
        return
    
    while True:
        try:
            cari_data_id_pasien = int(input("Masukkan ID Pasien yang ingin di ubah: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue
        ketemu = False
        for id_data_pasien, data_pasien in pasien.items():
            nama_pasien = data_pasien['nama_pasien']
            umur_pasien = str(data_pasien['umur_pasien'])
            kategori_pasien = data_pasien['kategori_pasien']
            alamat_pasien = data_pasien['alamat_pasien']
            
            if cari_data_id_pasien == id_data_pasien:
                if not ketemu:
                    print("\n====== DATA PASIEN DITEMUKAN ======")
                    print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
                    print("-" * 60)  
                    ketemu = True
                print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")

                print("\n =============== UPDATE UMUR ================")
                while True:
                    try:
                        umur_pasien_baru = int(input("Masukkan umur pasien baru : "))
                    except:
                        print("INPUT HARUS ANGKA! ULANGI!")
                        continue
                    if umur_pasien_baru <= 0:
                        print("Umur tidak valid! Masukkan umur yang benar.")
                        continue
                    elif umur_pasien_baru <= 12:
                        kategori_pasien_baru = "ANAK-ANAK"
                    elif 13 <= umur_pasien_baru <= 20:
                        kategori_pasien_baru = "REMAJA"
                    elif 21 <= umur_pasien_baru <= 59:
                        kategori_pasien_baru = "DEWASA"
                    elif umur_pasien_baru >= 60:
                        kategori_pasien_baru = "LANSIA"
                    else:
                        umur_pasien_baru >= 150
                        print("Umur tidak valid! Masukkan umur yang benar.")
                        continue
                    
                    yakin = input("Yakin ingin update data ini? (y/n) : ").lower()
                    if yakin == "y" or yakin == "ya" or yakin == "iya" or yakin == "yes":
                        pasien.update({id_data_pasien:{"nama_pasien": nama_pasien, "umur_pasien": umur_pasien_baru, "kategori_pasien": kategori_pasien_baru, "alamat_pasien": alamat_pasien}})
                        print("\nDATA BERHASIL DI UPDATE")
                        break
                    elif yakin == "n" or yakin == "no" or yakin == "tidak":
                        print("\nData pasien batal di update!")
                        break
                    else:
                        print("HANYA Y/N !")
                        continue

            if not ketemu:
                print("\n Data pasien tidak ditemukan!")
                    
        return
def update_data_alamat_pasien():

    lihat_semua_data_pasien()
    if not pasien:
        return

    while True:
        try:
            cari_data_id_pasien = int(input("Masukkan ID Pasien yang ingin di ubah: "))
        except:
            print("Input harus berupa angka!")
            continue
        ketemu = False
        for id_data_pasien, data_pasien in pasien.items():
            nama_pasien = data_pasien['nama_pasien']
            umur_pasien = str(data_pasien['umur_pasien'])
            kategori_pasien = data_pasien['kategori_pasien']
            alamat_pasien = data_pasien['alamat_pasien']

            if cari_data_id_pasien == id_data_pasien:
                if not ketemu:
                    print("\n====== DATA PASIEN DITEMUKAN ======")
                    print(f"{'ID':<4}|{'NAMA':<20}|{'UMUR':<6}|{'KATEGORI':<10}|{'ALAMAT':<25}")
                    print("-" * 60)  
                    ketemu = True
                print(f"{id_data_pasien:<4}|{nama_pasien:<20}|{umur_pasien:<6}|{kategori_pasien:<10}|{alamat_pasien:<25}")

                print("\n =============== UPDATE ALAMAT ================")
                input_alamat_pasien_baru = input("Masukkan alamat baru pasien: ")
                if cek_input_no_error_kosong(input_alamat_pasien_baru):
                    continue
                yakin = input("Yakin ingin update data ini? (y/n) : ").lower()
                if yakin == "y" or yakin == "ya" or yakin == "iya" or yakin == "yes":
                    pasien.update({id_data_pasien: {"nama_pasien": nama_pasien, "umur_pasien": umur_pasien, "kategori_pasien": kategori_pasien, "alamat_pasien": input_alamat_pasien_baru}})
                    print("\nDATA PASIEN BERHASIL DI UPDATE!")
                    break
                elif yakin == "n" or yakin == "no" or yakin == "tidak":
                    print("\nData pasien batal di update!")
                    break
                else:
                    print("HANYA Y/N !")
                    continue 
                
            if not ketemu:
                print("\n Data pasien tidak ditemukan!")
        return

def update_data_pasien():

    while True:
        judul = "UPDATE DATA PASIEN"
        label = "PILIH 1-3"

        print(f"\n====== {judul} ======")
        print("|1. UPDATE BERDASARKAN NAMA   |")
        print("|2. UPDATE BERDASARKAN UMUR   |")
        print("|3. UPDATE BERDASARKAN ALAMAT |")
        print("|4. KEMBALI                   |")
        print(f"========== {label} ==========\n")
        
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            update_data_nama_pasien()
        elif pilih == 2:
            update_data_umur_pasien()
        elif pilih == 3:
            update_data_alamat_pasien()
        elif pilih == 4:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue
    return

def hapus_data_pasien():

    lihat_semua_data_pasien()
    if not pasien:
        return
    
    try:
        cari_data_id = int(input("Masukkkan ID pasien yang ingin dihapus : "))
    except:
        print("INPUT HARUS ANGKA, ULANGI LAGI!")

    ketemu = False
    for id_data_pasien, data_pasien in pasien.items():
        nama_pasien = data_pasien['nama_pasien']
        umur_pasien = str(data_pasien['umur_pasien'])
        kategori_pasien = data_pasien['kategori_pasien']
        alamat_pasien = data_pasien['alamat_pasien']
        if id_data_pasien == cari_data_id:
            if not ketemu:
                print("\n===== DATA PASIEN DITEMUKAN =====")
                ketemu = True
            print(f"ID Pasien : {id_data_pasien} | Nama Pasien : {nama_pasien}| Umur Pasien : {umur_pasien} | Kategori Pasien : {kategori_pasien} | Alamat Pasien : {alamat_pasien}\n")
            hapus = input("Yakin ingin menghapus data ini? (y/n) : ").lower()
            if hapus == "y" or hapus == "ya" or hapus == "iya":
                pasien.pop(id_data_pasien)
                print("Data pasien berhasil dihapus!")
                break
            else:
                print("Data pasien batal untuk di hapus!")
                break

    if not ketemu:
        print("\nPASIEN TIDAK DITEMUKAN!\n")    
    return

def main_pasien():
    
    while True:
        judul = "DATA PASIEN"
        label = "PILIH 1-5"
        label_judul1 = "=" * (len(judul) + 14)
        print(f"\n{label_judul1}")
        print(f"====== {judul} ======")
        print("|1. TAMBAH DATA PASIEN  |")
        print("|2. LIHAT DATA PASIEN   |")
        print("|3. UPDATE DATA PASIEN  |")
        print("|4. HAPUS DATA PASIEN   |")
        print("|5. KEMBALI             |")
        print(f"======= {label} =======")
        print(label_judul1)
    
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            tambah_data_pasien()
        elif pilih == 2:
            lihat_data_pasien()
        elif pilih == 3:
            update_data_pasien()
        elif pilih == 4:
            hapus_data_pasien()
        elif pilih == 5:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue
