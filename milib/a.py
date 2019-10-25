fo = open("./prueba.txt", "w+")
while (True):
    entrada=input("Numero: ")
    if (int(entrada)<0):
        print (fo.tell())
        fo.seek(0,0)
        print (fo.tell())
        line=fo.readlines()
        print(line)
        fo.close
        break
    else:
        entrada+=" "
        fo.write(entrada)
        #fo.writelines(entrada)


fe = open("./prueba.txt", "r")
print (fe.readlines())


