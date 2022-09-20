#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:41:15 2022

@author: seba
@author: seba
    Analisis Foda Implementado con Lógica Difusa
    
    Programa principal
    
    Parseo de datos de factores internos y externos
    Cargo las clases
    calculo por cada intereseccion
    Realizo priorizacion
    Guardo el resultado en un archivo CSV
    
--- Alea iacta Est ---
"""

from clasesSCH import factor_foda, c_estrategia
from FuncionesCarga import Carga_factores
from FuncionesCarga import imprime_lista
from genEstrategia import genera_lista_estrategia;
from Priorizador import prioriza_estrategias;
from Almacenador import almacena_salida,almacena_salida_inter;


lista_fact_int :list[factor_foda]=[]
lista_fact_ext :list[factor_foda]=[]

alfa=[0.15,0.6,0.9];
lista_estrategias: list[c_estrategia] =[];

archivoSalida:str = "salida.csv"

lista_fact_int = Carga_factores("Factores_internos.csv", True);
print("Factores Internos")
imprime_lista(lista_fact_int)

lista_fact_ext= Carga_factores("Factores_externos.csv", False);

print("")
print("Factores Externos")
imprime_lista(lista_fact_ext)

#Ahora vamos a generar la lista de estrategias
lista_estrategias = genera_lista_estrategia(lista_fact_int,
                                            lista_fact_ext,
                                            alfa);

#almacena_salida_inter("salidainter1.csv",lista_estrategias)
#Realizo priorizacion de Estrategias
prioriza_estrategias(lista_estrategias)
#almacena_salida_inter("salidainter2.csv",lista_estrategias)

#Ahora guardo los archivos de las estrategias

almacena_salida(archivoSalida,lista_estrategias);
