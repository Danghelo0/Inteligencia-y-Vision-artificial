# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:13:57 2024

@author: PC
"""

import pandas as pd

V=list('abcdefgh')
grafo=pd.DataFrame(index=V,columns=V)
#grafo.loc[] #esto en consola es para ver lo que hay en a y b
grafo.loc['a',['b','c','g']]=1 
grafo.loc['b',['a','d','g']]=1 
grafo.loc['c',['a','d','e']]=1 
grafo.loc['d',['b','c','f']]=1 
grafo.loc['e',['c','f','g']]=1 
grafo.loc['f',['d','e','h']]=1 
grafo.loc['g',['a','b','e']]=1
grafo.loc['h',['f']]=1
grafo=grafo.fillna(0)#llena nan con 0
grafo.to_json("grafo.json",orient='split')
#grafo.to_json("grafo.json") sale error con esta linea sabe porque
v1='a' #este nodo se cambia para que de distinta Ep

S=[v1]
Vp=[v1]
Ep=[]
s=[]
d=V.copy()
d.remove(v1)
while True:
    for x in S:

        #escribir en consola: grafo['a']>0
        v=[y for y in d if y in grafo.loc[grafo[x]>0,x]]
        _=[(Ep.append((x,y)),Vp.append(y),d.remove(y),s.append(y)) for y in v]
        #escribir en consola: Ep , x
        
    if s==[]:
        break
    S=s.copy()
    s=[]