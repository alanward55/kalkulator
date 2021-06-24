import time, os, sys

B = '\033[1m' #Bold
R = '\033[31m' #Red
G = '\033[32m' #Green
Y = '\033[33m' #Yellow
BL = '\033[34m' #Blue
P = '\033[35m' #Purple
W = '\033[37m' #White
U = '\033[2m' #Underline
N = '\033[0m' #Normal

ulang = ('y')
while (ulang != 'n'):
	os.system('clear')
	print(BL+'''


██╗  ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗
██║ ██╔╝██╔══██╗██║     ██║ ██╔╝██║   ██║
█████╔╝ ███████║██║     █████╔╝ ██║   ██║
██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║   ██║
██║  ██╗██║  ██║███████╗██║  ██╗╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
''')
	print(G+'[Program kalkulator dibuat oleh alanward]')
	print(R+'-----====[copyright \N{COPYRIGHT SIGN} 2021]====-----')
	print(Y+B+'''
Opsi:

1. Tambah       3. Kali        5. Modulus            7. Akar
2. Kurang       4. Bagi        6. Pangkat kali ''')
	print(N+"\n")
	x = int(input(W+'Masukkan angka pertama: '))
	a = int(input(W+'Masukkan opsi: '))
	y = int(input (W+'Masukkan angka kedua: '))
	if a == (1):
		print ('HASIL= ',x+y)
	if a == (2):
		print ('HASIL= ',x-y)
	if a == (3):
		print ('HASIL= ',x*y)
	if a == (4):
		print ('HASIL= ',x/y)
	if a == (5):
		print ('HASIL= ',x%y)
	if a == (6):
		print ('HASIL= ',x**y)
	if a == (7):
		print ('HASIL= ',x//y)
	elif a >= 7:
		print('Maaf opsi yang anda masukkan salah, ulangi!')

	ulang = input("\nApakah Anda Ingin Mencoba Lagi? (y/n)")
	if ulang == ('n'):
		os.system('clear')
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)
		print('copyright \N{COPYRIGHT SIGN} 2021')
		time.sleep(0.1)

		print('Terimakasih telah menggunakan program ini.....')
