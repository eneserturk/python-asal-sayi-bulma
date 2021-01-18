"istenilen iki sayı arasıda bulunan asal sayıları bulma"

def asalmi(x):
    asal_mi = True
    if x == 1 :
        asal_mi = False
    if x == 2 :
        asal_mi = True
    for i in range(2, x):
        if (x % i == 0) :
            asal_mi = False
            break
    if asal_mi:
        print(f'{x} prime.')
    else:
        print(f'{x} not prime.')

def asalbul(sayi1=1,sayi2=1):
    if ((sayi1 and sayi2) > 0) and (sayi1 != sayi2):
        if sayi1 > sayi2:
            for i in range(sayi2, sayi1+1):
                asalmi(i)
        elif sayi2 > sayi1:
            for i in range(sayi1, sayi2+1):
                asalmi(i)
        else:
            print(f"Eşit sayılar girdiğiniz için girilen sayının asal olıp olmadığı kontrol edilecektir")
            asalmi(sayi1)
    else: print("Negatif sayıların tümü asal olarak kabul edilmemektedir.\nLütfen girilmesi gereken iki sayıyı da pozitif farklı doğal sayı olarak giriniz.")

num1 = int(input('Firs Number: '))
num2 = int(input('Second Number: '))
asalbul(num1,num2)