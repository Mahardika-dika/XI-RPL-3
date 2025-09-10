import sys
import time

def typeEffect (text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

a = 1
b = "Hello"
c = 1.5
d = ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

print("Type Jenis Ke Satu Adalah: " + str(type(a)))
print("Type Jenis Ke Dua Adalah: " + str(type(b)))
print("Type Jenis Ke Tiga Adalah: " + str(type(c)))
print("Type Jenis Ke Empat Adalah: " + str(type(d)))

Sembako = ['Beras', 'Minyak', 'Telur']
Sembako.append('Ayam')
print(Sembako)
for i in Sembako:
    print("Sembako: " + i)

Belanjaan = {"Beras":12000, "Minyak":17000, "Telur":24000, "Gula":15000, "Kopi":20000}
print(sum(Belanjaan.values()))

# pratikum 2 lanjutan

e = 1

if e == 1:
    print('Anjayyyy')
else:
    print('woiiiiiiiiiii')

def akbar ():
    return'saya akbar dan saya pintar \n'

def loop ():
     text = ""
     for c in range(5):
        text += "\n"
        for i in range(5):
            text += "Aku anak Telkom, dan Aku Hebat \n"
            text += akbar()
        return text


typeEffect(loop())

count = 0

while count < 4:
    typeEffect("Tetap Berhitung !!")
    count += 1

word = "Mahardika Arfuri"
for i in word:
    print(i)
    count += 1