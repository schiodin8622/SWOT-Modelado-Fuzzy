#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 21:26:15 2022

@author: seba
"""
import csv
from clasesSCH import * 

def Carga_factores(archivo,interno)->list[factor_foda]:
    
    lista_datos=[];
    with open(archivo) as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            factor = factor_foda()
            id= int(row[0]);
            minimo  = float(row[2]);
            probable = float (row[3]);
            maximo = float(row[4]);
            descripcion = row[1];
            factor.Descripcion = descripcion;
            factor.id = id;
            factor.min = minimo;
            factor.max = maximo;
            factor.probable =probable;
            factor.actualiza_valores();
            lista_datos.append(factor)
            #Impresion de Debug
            #print(minimo,probable,maximo);
    return lista_datos;

def imprime_lista(lista:list[factor_foda]):
    cant = len(lista);
    for i in range(cant):
        print (str(lista[i].id) + " - " + lista[i].Descripcion )
        
    