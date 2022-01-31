# class tv
class TV:
  # attribute / class varible
  chanel = ['rcti', 'tvri', 'global tv']
  tv_menyala = False

  # method contructor / __init_ 
  def __init__ (self, brand , size):
    # asignmet / memasukan ke varible class
    self.brand = brand
    self.size = size

  # menyalakan tv
  def menyalakanTv(self):
    self.tv_menyala = True
    print("tv menayala")

  # metode / funsgi menambah chanel dan menghapus chanel
  def tambahChanel(self, nama_chanel):
    if(self.tv_menyala):
      self.chanel.append(nama_chanel)      
      print("chanel ditambahkan")
    else:
      print("tv belum menayala")

  # metode / funsgi menambah chanel dan menghapus chanel
  def hapusChanel(self, nama_chanel):
    if(self.tv_menyala):
      self.chanel.remove(nama_chanel)      
      print("chanel dihapus")
    else:
      print("tv belum menayala")

class Android(TV):
  # app
  aplikasi = ['youtube','netflix']

  # metode / funsgi menambah apliakasi
  def tambahApikasi(self, nama_aplikasi):
    if(self.tv_menyala):
      self.aplikasi.append(nama_aplikasi)      
      print("aplikasi ditambahkan")
    else:
      print("tv belum menayala")

  # metode / funsgi menghapus apliakasi
  def hapusApikasi(self, nama_aplikasi):
    if(self.tv_menyala):
      self.aplikasi.remove(nama_aplikasi)      
      print("aplikasi dihapus")
    else:
      print("tv belum menayala")

# mebuat object dari clas tv
tv_kamar = TV('TCL', '32inc')
tv_tamu = Android('Samsung', '32inc')


while True:
  print("1) nyalakan tv")
  print("2) tambakan chanel tv")
  print("3) keluar dari program")
  pilihan = int(input("silahkan masukan pilihan anda "))
  if(pilihan == 1):
    tv_kamar.menyalakanTv()
  elif(pilihan == 2):
    print('chanel sekarang:')
    print(tv_kamar.chanel)
    chanel = input("silahkan masukan chanel: ")
    tv_kamar.tambahChanel(chanel)
    print('chanel sekarang:')
    print(tv_kamar.chanel)
  elif(pilihan == 3):
    print('anda keluar program')
    break
  else:
    print('pilihan tidak ditemukan')
