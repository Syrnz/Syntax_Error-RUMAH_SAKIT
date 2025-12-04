from database import pasien
from database import kamar
from database import tagihan_rawat_inap
from kamar import lihat_semua_kamar
from validasi_input import cek_input_no_error_all

id_tagihan_kamar = 1

def tagihan_kamar():

    global id_tagihan_kamar

    while True:
        nama_pembayar = input("Masukkan Nama Pembayar : ")
        if cek_input_no_error_all(nama_pembayar):
            continue
        break
    
    while True:
        lihat_semua_kamar()

        try:
            no_kamar = int(input("Masukkan Nomor Kamar yang dibayar: "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        
        if no_kamar not in kamar:
            print("Kamar tidak ditemukan!")
            return

        if not kamar[no_kamar]["status"]:
            print("Kamar masih kosong, tidak dapat dibayar!")
            return

        if kamar[no_kamar]["status_tagihan"]:
            print("Tagihan kamar ini sudah dibayar!!")
            return
        
        data_kamar = kamar[no_kamar]
        pasien_kamar = pasien[data_kamar['pasien_id']]
        break

    while True:
        try:
            jumlah_hari = int(input("Berapa hari pasien telah di rawat inap? : "))
        except:
            print("Input harus angka!")
            continue

        if jumlah_hari <= 0:
            print("Minimal 1 hari!")
            continue

        harga_kamar = data_kamar["harga_kamar"]
        total_tagihan = jumlah_hari * harga_kamar

        print(f"\nTotal Tagihan : Rp{total_tagihan:,}")
        break

    while True:
        try:
            uang_dibayar = int(input("Uang Dibayar: "))
        except:
            print("Input harus angka!")
            continue

        if uang_dibayar < total_tagihan:
            print("Uang kurang!")
            continue
        break

    data_kamar["status_tagihan"] = True

    uang_kembalian = uang_dibayar - total_tagihan

    tambah_tagihan = [id_tagihan_kamar, nama_pembayar, no_kamar, pasien_kamar["nama_pasien"], data_kamar["tanggal_masuk"], harga_kamar, jumlah_hari, total_tagihan, uang_dibayar, uang_kembalian]
    tagihan_rawat_inap.append(tambah_tagihan)
    id_tagihan_kamar += 1

    print("Pembayaran kamar inap berhasil!")

        
    print("\n------  PEMBAYARAN KAMAR INAP PASIEN     ------")
    print(f"PEMBAYARAN KAMAR NO     : {no_kamar} ")
    print(f"NAMA PEMBAYAR           : {nama_pembayar}")
    print(f"NAMA PASIEN             : {pasien_kamar['nama_pasien']}")
    print(f"TAGIHAN KAMAR           : Rp{harga_kamar:,}")
    print(f"TOTAL TAGIHAN           : Rp{total_tagihan:,}")
    print(f"UANG DIBAYAR            : Rp{uang_dibayar:,}")
    print(f"UANG KEMBALIAN          : Rp{uang_kembalian:,}")
    print("-------          TERIMAKASIH               -------\n")
    return

def riwayat_tagihan():

    for info_riwayat in tagihan_rawat_inap:
        id_struk        = info_riwayat[0]
        nama_pembayar   = info_riwayat[1]
        no_kamar        = info_riwayat[2]
        pasien_kamar    = info_riwayat[3]
        tanggal_masuk   = info_riwayat[4]
        harga_kamar     = info_riwayat[5]
        jumlah_hari     = info_riwayat[6]
        total_tagihan   = info_riwayat[7]
        uang_dibayar    = info_riwayat[8]
        uang_kembalian  = info_riwayat[9]

        print(f"\n----  ID STRUK  {id_struk}         ------")
        print(f"----  PEMBAYARAN KAMAR INAP PASIEN   ------")
        print(f"PEMBAYARAN KAMAR NO     : {no_kamar} ")
        print(f"NAMA PEMBAYAR           : {nama_pembayar}")
        print(f"NAMA PASIEN             : {pasien_kamar}")
        print(f"TANGGAL INAP            : {tanggal_masuk}")
        print(f"TAGIHAN KAMAR           : Rp{harga_kamar:,} x {jumlah_hari}/hari")
        print(f"TOTAL TAGIHAN           : Rp{total_tagihan:,}")
        print(f"UANG DIBAYAR            : Rp{uang_dibayar:,}")
        print(f"UANG KEMBALIAN          : Rp{uang_kembalian:,}")
        print("-------          TERIMAKASIH               -------\n")

    return

def data_tagihan_rawat_inap():
        
    while True:
        judul = "DATA TAGIHAN RAWAT INAP"
        label = "PILIH 1-3"
        label_judul1 = "=" * (len(judul) + 14)
        print(label_judul1)
        print(f"\n====== {judul} ======")
        print("|1. BAYAR TAGIHAN    |")
        print("|2. RIWAYAT TAGIHAN  |")
        print("|3. KEMBALI          |")
        print(f"======= {label} =======\n")
        print(label_judul1)
        
        try:
            pilih = int(input("pilih program :"))
        except:
            print("INPUT HARUS ANGKA! MASUKKAN KEMBALI")
            continue
        if pilih == 1:
            tagihan_kamar()
        elif pilih == 2:
            riwayat_tagihan()
            pass
        elif pilih == 3:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR, ULANGI LAGI! ")
            continue
        return

def main_transaksi():
    while True:
        judul = "DATA TRANSAKSI"
        label = "PILIH 1-2"
        label_judul1 = "=" * (len(judul) + 16)
        print(label_judul1)
        print(f"======= {judul} =======")
        print("|1. DATA TAGIHAN RAWAT INAP |")
        print("|2. KEMBALI                 |")
        print(f"========== {label} ==========")
        print(label_judul1)
    
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            data_tagihan_rawat_inap()
        elif pilih == 2:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue