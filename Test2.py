#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:51:59 2021

@author: sbarcenas
"""

# 1. 
    
vector = []
i = 1
print('A continuación vamos a realizar operaciones con un vector por favor ingrese los numeros.')
print('o ingrese 0 para salir y obtener el resultado:')
while True:
    numero = int(input(f'Digite el número {i}:'))
    if numero == 0:
        break
    i += 1
    vector.append(numero)
def produc(vec):
    productoria = 1
    for i in vec:
        productoria = productoria * i
    return productoria
    
print(f'La sumatoria del vector es: {sum(vector)}')
print(f'La productoria del vector es: {produc(vector)}')
print(f'El número mayor del vetor es: {max(vector)}')
print(f'El número menor del vetor es: {min(vector)}')

# 2

vector = []
it = int(input('Ingrese el tamaño del vector:'))
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i}:'))
    vector.append(numero)
pair = []
odd = []
def calcVector(vect):
    for i in vector:
        if i % 2 == 0:
            pair.append(i)
        else:
            odd.append(i)
    respuesta = print(f'Los números pares son: {pair}\nLos números imprares son: {odd}')
    return respuesta

print(f'{calcVector(vector)}')

#3.

vector1 = []
vector2 = []
resultado = []
it = int(input('Ingrese el tamaño de los vectores:'))
# FullFill vector 1
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i} en el vector 1:'))
    vector1.append(numero)
# FullFill vector 2
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i} en el vector 2:'))
    vector2.append(numero)
#Sum vectors    
def sum_vec(v,v1):
    for i in range(len(v)):
        resultado.append(v[i]+v1[i])
    return resultado

print(f'La suma de los vectores es: {sum_vec(vector1,vector2)}')


#4.

fourth_vector = []
it = int(input('Ingrese el tamaño de los vectores:'))
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i}:'))
    fourth_vector.append(numero)

def moda(datos):
    repeticiones = 0

    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n
        return print(f'El número que mas se repite es: {i} y se repite {repeticiones} veces')

moda(fourth_vector)



#5.

v = []
it = 1;
while it%2 != 0 :
    print('Debes ingresar un tamaño par...')
    it = int(input('Ingrese el tamaño de los vectores:'));
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i}:'))
    v.append(numero)
B = v[:len(v)//2]
C = v[len(v)//2:]

print(f'El resultado de la primera mitad es {produc(B)}, la sumatoria de la segunda mitad es: {sum(C)}')
print(produc(C))



#6

v = []
it = int(input('Ingrese el tamaño del vector :'))
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i}:'))
    v.append(numero)

B = v[:len(v)//2]
C = v[len(v)//2:]
if B == C:
    print('Vector simetrico')
else:
    print('Vector asimetrico')

#7

import copy # Import a dependency
    
v = []
v1 = []
g = []
x = 1
it = int(input('Ingrese el tamaño de los vectores:'))
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i} para el vector 1:'))
    v.append(numero)
for i in range(it):
    numero = int(input(f'Digite el número para la posición {i} para el vector 2:'))
    v1.append(numero)
v2 = copy.copy(v)
v2.extend([element for element in v1 if element not in v])

def intersection(v,v1):
    v3 = []
    for i in v:
        for j in v1:
           if i == j:
               v3.append(i)
    v3 = list(tuple(v3))
    return v3
v4 = []
v4.append([element for element in v if element not in v1])
v5=[]
v5.append([element for element in v1 if element not in v2])
print(f'La union sin repetir es: {v2}')
print(f'La interseccion es: {intersection(v,v1)}')
print(f'La diferencia entre el primer vector y el segundo es: {v4}')
print(f'La diferencia entre el segundo vector y el primero es: {v5}')
