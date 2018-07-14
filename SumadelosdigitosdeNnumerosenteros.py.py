//primer programa
def sumad(num):
    s=0 #suma de los digitos
    while num>0:
        s=s+num%10
        num=num//10
        return s
n=int(input("cantidad de numeros:"))
sumat = 0#sumatotal
while n>0:
        num = int(input("Numero:"))
        sumat=sumat+sumad(num)
        n=n-1
print (sumat)

