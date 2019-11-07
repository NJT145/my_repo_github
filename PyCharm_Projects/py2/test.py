#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def int2binStr(number, index_size): # to convert
    bin_number = bin(number) # integeri binarye cevirdik basında 0b olan 2 tabanındaki haline çevirdik. mesela number=2 ise bin_number="0b10"
    dif = index_size - len(str(bin_number))  # istenilen output uzunluğu ile bin_number uzunluğu arasındaki fark.
    if dif >= 0:
        return dif*" " + str(bin_number)
    return None  # index_size uygun değilse None verir.

def binStr2int(binStr): #paket numaralarını geri alırken integera cevirmek icin
    return int(binStr.strip(),2)

#paketin okunması gerceklesiyor
def readNpackageFile(path, index_size, package_size): #index_size değişkeni int2binStr için gerekli. package_size ise her paketin alacağı maximum boyut.
    data_list = []
    package_counter = 0
    f = open(path, 'rb')
    while True: #paketi okumaya devam ediyor
        package = f.read(package_size - index_size)
        if len(package) > 0: #okunacak bir sey kalmıyınca okunan veri boyutu(len) 0 olur.
            package_counter += 1 #her bir ayrılan paketin kacıncı oldugu,bu paketler numaralandırılıyor
            message = bytes(int2binStr(package_counter, index_size)) + package  # paketin alacağı son hali yollanamya hazır olacağısonhal
            data_list.append(message) #her parçalanan paketler listeye eklenir
        else:
            break
    f.close()
    return data_list

def packages2file(packages, index_size): # paketlerin bütün haline gelmesi
    packages_dict = {} # herbiri dict icine konuluyor daıgınık geldikleri icin list kullanmıyoruz
    for package in packages:
        package_number = binStr2int(package[:index_size]) #her paketin numarası :key  numarasıda kacıncı paket oldugu  oluyor
        package_data = package[index_size:]
        packages_dict[package_number] = package_data #paketin içeriğine paket numarasının değeri yapılıyor
    keys = packages_dict.keys()
    keys.sort() #keyler sıralanıyor numaraları
    return b''.join([packages_dict[key] for key in keys])


file_path = os.path.join(os.getcwd(), 'received_file.jpg')

f1 = open(file_path, 'rb')
data = f1.readlines()
f1.close()
data = b''.join(data)
print(data==packages2file(readNpackageFile(file_path, 100, 1000), 100))
print(len(readNpackageFile(file_path, 100, 1000)))
print(int2binStr(2,5))
print(binStr2int(int2binStr(2,5)))