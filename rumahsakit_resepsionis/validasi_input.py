import datetime

def cek_input_no_error_all(input_data):

    cek_input = False
    for valid_input in input_data:
        if valid_input in ['1','2','3','4','5','6','7','8','9','0',
                            '!','@','#','$','%','^','&','*','(',')',
                            '-','+','=','{','}','[',']','|','\\',':',
                            ';','"',"'",'<','>',',','.','?','/','`','~']:
            cek_input = True
            break
    if cek_input:
        print("NAMA TIDAK BOLEH MENGANDUNG ANGKA! SIMBOL! ULANGI!")
        return True

    cek_valid_input_kosong_nama_pasien = input_data.strip()
    if cek_valid_input_kosong_nama_pasien == "":
        print("INPUT! TIDAK BOLEH KOSONG")
        return True
    
def cek_input_no_error_kosong(input_data):

    cek_valid_input_kosong = input_data.strip()
    if cek_valid_input_kosong == "":
        print("INPUT! TIDAK BOLEH KOSONG")
        return True
    
def cek_input_tanggal(input_data):
    try:
        datetime.date.fromisoformat(input_data)
    except ValueError:
        print("Format Data Salah, Contoh Format YYYY-MM-DD")
        return True