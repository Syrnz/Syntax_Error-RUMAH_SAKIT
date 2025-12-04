from dokter import dokter
from dokter import lihat_semua_data_dokter
from pasien import pasien
from pasien import lihat_semua_data_pasien
from validasi_input import cek_input_no_error_all
from validasi_input import cek_input_no_error_kosong
from validasi_input import cek_input_tanggal

kamar = {
    101: {
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    102: {
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    103: {
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    104: {
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    105: {
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    106: {
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    107: {
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    108:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    109:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    110:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    201:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    202:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    203:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    204:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        },
    205:{
            "status": False,
            "pasien_id": None,
            "dokter": None,
            "deskripsi_pasien": None,
            "harga_kamar": 350000,
            "tanggal_masuk": None,
            "status_tagihan": False
        }
}

def cek_pasien_sudah_menginap(id_pasien, kamar):

    for nomor, info in kamar.items():
        if info["status"] and info["pasien_id"] == id_pasien:
            return True
        
    return False


def cek_cari_pasien_inap(cari_pasien):
        
    cek_ketemu = False

    for nomor, data in kamar.items():
        tagihan = "Sudah Lunas" if data['status_tagihan'] else "Belum Lunas"
        if data['status']:
            p = pasien[data["pasien_id"]]
            d = dokter[data["dokter_id"]]
            data_pasien = p["nama_pasien"].lower()
            if cari_pasien in data_pasien:
                if not cek_ketemu:
                    print("============ PASIEN RAWAT INAP DITEMUKAN! ============\n")
                    print(f"{'NO KAMAR':<10}|{'NAMA PASIEN':<25}|{'NAMA DOKTER':<25}|{'DESKRIPSI':<30}|{'TANGGAL MASUK':15}|{'TAGIHAN':<10}")
                    cek_ketemu = True
                print(f"{nomor:<10}|{p['nama_pasien']:<25}|{d['nama_dokter']:<25}|{data['deskripsi']:<30}|{data['tanggal_masuk']:15}|{tagihan:<10}")
    if not cek_ketemu:
        print("Pasien rawat inap tidak ditemukan!")

    return

def lihat_semua_kamar():

    print("\n=== RUANG INAP ===")
    print(f"{'NO KAMAR':<10}|{'NAMA PASIEN':<25}|{'NAMA DOKTER':<25}|{'DESKRIPSI':<30}|{'TANGGAL MASUK':15}|{'TAGIHAN':<10}")
    for nomor, data in kamar.items():
        tagihan = "Sudah Lunas" if data['status_tagihan'] else "Belum Lunas"
        if not data["status"]:
            print(f"{nomor:<10}|{'KOSONG':<25}|{'---':<25}|{'---':<30}|{'---':15}|{'---':<10}")
        else:
            p = pasien[data["pasien_id"]]
            d = dokter[data["dokter_id"]]
            print(f"{nomor:<10}|{p['nama_pasien']:<25}|{d['nama_dokter']:<25}|{data['deskripsi']:<30}|{data['tanggal_masuk']:15}|{tagihan:<10}")
    return

def cari_pasien_rawatinap():
    
    while True:
        cari_pasien = input("Masukkan nama pasien rawat inap : ").lower()

        if cek_input_no_error_kosong(cari_pasien):
            continue

        if cek_cari_pasien_inap(cari_pasien):
            return
        else:
            break

def lihat_data_kamar():
    while True:
        judul = "DATA KAMAR"
        label = "PILIH 1-3"
        label_judul1 = "=" * (len(judul) + 18)
        print(label_judul1)
        print(f"======== {judul} ========")
        print("|1. LIHAT SEMUA KAMAR      |")
        print("|2. CARI PASIEN RAWAT INAP |")
        print("|3. KEMBALI                |")
        print(f"========= {label} ========")
        print(label_judul1)
    
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            lihat_semua_kamar()
        elif pilih == 2:
            cari_pasien_rawatinap()
        elif pilih == 3:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue

    return

def checkinPasien():

    if not pasien:
        print("============ DATA PASIEN KOSONG! ============\n")
        return
    
    if all(data["status"] for data in kamar.values()):
        print("SEMUA kamar di rumah sakit ini PENUH!\n")
        return
            
    lihat_semua_kamar()

    print("\n=== ISI RUANG INAP ===")

    while True:

        try:
            print("\nketik '0' untuk batal input")
            no_kamar = int(input("Masukkan nomor kamar : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        
        if no_kamar == 0:
            print("Regristrasi Dibatalkan")
            return
        
        if no_kamar not in kamar:
            print("Nomor kamar tidak tersedia!")
            continue

        if kamar[no_kamar]["status"]:
            print("Kamar sudah terisi!")
            continue
        break

    while True:
        lihat_semua_data_pasien()
        try:
            print("\nketik '0' untuk batal input")
            id_pasien = int(input("Masukkan ID pasien: "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue

        if id_pasien == 0:
            print("Regristrasi Dibatalkan")
            return

        if cek_pasien_sudah_menginap(id_pasien, kamar):
            print("pasien ini sudah ada di kamar lain!")
            continue

        if id_pasien not in pasien:
            print("ID Pasien tidak ditemukan!")
            continue
        break

    while True:
        lihat_semua_data_dokter()
        try:
            id_dokter = int(input("Masukkan ID Dokter: "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!!")
            continue

        if id_dokter not in dokter:
            print("ID Dokter tidak ditemukan!")
            continue
        break

    while True:
        deskripsi = input("Masukkan deskripsi pasien: ")
        if cek_input_no_error_all(deskripsi):
            continue
        break

    while True:
        tanggal_masuk = input("Tanggal masuk (YYYY-MM-DD): ")
        if cek_input_no_error_kosong(tanggal_masuk):
            continue
        if cek_input_tanggal(tanggal_masuk):
            continue
        break

    data = kamar[no_kamar]
    data["status"] = True
    data["pasien_id"] = id_pasien
    data["dokter_id"] = id_dokter
    data["deskripsi"] = deskripsi
    data["tanggal_masuk"] = tanggal_masuk
    print(f"\nPasien {pasien[id_pasien]['nama_pasien']} berhasil masuk ke kamar {no_kamar}.\n")

    return


def checkoutPasien():

    lihat_semua_kamar()
    while True:
        try:
            no_kamar = int(input("Masukkan Nomor kamar pasien yang ingin Check-Out kamar : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue

        if no_kamar not in kamar:
            print("Kamar tidak ditemukan!")
            return
        
        if not kamar[no_kamar]["status"]:
            print("Kamar masih kosong, tidak dapat dibayar!")
            return
        
        if not kamar[no_kamar]["status_tagihan"]:
            print("Tagihan kamar ini belum DIBAYAR!!")
            return

        data = kamar[no_kamar]
        data["status"] = False
        data["pasien_id"] = None
        data["dokter_id"] = None
        data["deskripsi"] = None
        data["tanggal_masuk"] = None
        data["status_tagihan"] = False
        print(f"Ruang No {no_kamar} berhasil dikosongkan.")
        return


def main_kamar():
    while True:
        judul = "DATA KAMAR"
        label = "PILIH 1-4"
        label_judul1 = "=" * (len(judul) + 16)
        print(label_judul1)
        print(f"======= {judul} =======")
        print("|1. LIHAT DATA KAMAR INAP|")
        print("|2. CHECK-IN PASIEN      |")
        print("|3. CHECK-OUT PASIEN     |")
        print("|4. KEMBALI              |")
        print(f"======== {label} =======")
        print(label_judul1)
    
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            lihat_data_kamar()
            pass
        elif pilih == 2:
            checkinPasien()
        elif pilih == 3:
            checkoutPasien()
        elif pilih == 4:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue
