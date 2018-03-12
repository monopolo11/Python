#declaracion de variables
num = int(input("Escribe el numero: "))
numprint = num
intento = 0
#array con el binario
resbin = []
#proceso

#conversion a binario
while num>=1:
    bina = num%2
    if bina!=0:
        res=1
    else:
        res=0
    #agrega al array
    resbin.append(res)
    num=int(num/2)
    intento=intento+1
intento=intento-1
#array final
binfin = []
#invierte el array
while intento>=0:
    #print(resbin[intento])
    binfin.append(resbin[intento])
    intento=intento-1
    #convierte el array  string
    resfin = ''.join(str(e) for e in binfin)
#imprime el string
print("El numero ", numprint," en binario es: ",resfin)