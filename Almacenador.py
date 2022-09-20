#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 13:25:26 2022

@author: seba
"""

from clasesSCH import factor_foda,c_estrategia, intersecc_fuzzy;
from Priorizador import obtiene_item_estrategia_c;
import csv;


def almacena_salida(archivo:str, lista_estrategias:c_estrategia ):
    header = ["Fila", "Factor Interno", "Factor Exteno",  "% Cuadrante 1", 
              "% Cuadrante 2", "% Cuadrante 3", "% Cuadrante 4", "P alpha1", 
              "P Alpha2", "P Alpha3", "P ponderada", "Prioridad Neta",
              "ci1","ci2","ci3"];

    data = []
    with open(archivo, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)    
        # write the header
        writer.writerow(header)
        for i in range(len(lista_estrategias)):
            # write the data
            data=obtiene_item_estrategia_c(lista_estrategias,i+1).devuelve_fila(i+1);
            writer.writerow(data)

    
def almacena_salida_inter(archivo:str, lista_estrategias:c_estrategia ):
    header = ["Fila", "Factor Interno", "Factor Exteno",  "% Cuadrante 1", 
              "% Cuadrante 2", "% Cuadrante 3", "% Cuadrante 4", "P alpha1", 
              "P Alpha2", "P Alpha3", "P ponderada", "Prioridad Neta",
              "ci1","ci2","ci3", "desc Interna", "Desc Externa"];

    data = []
    with open(archivo, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)    
        # write the header
        writer.writerow(header)
        for i in range(len(lista_estrategias)):
            # write the data
            data=lista_estrategias[i].devuelve_fila(i+1);
            writer.writerow(data)


