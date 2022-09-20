#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 09:04:25 2022

@author: seba
"""
from clasesSCH import factor_foda,c_estrategia 

#Funcion de Generacion de la matriz FODA para las estrategias

def genera_estrategia_ind(fac_interno:factor_foda, 
                          fac_externo:factor_foda,
                          alfa:list[float])->c_estrategia:

    estrategia = c_estrategia(fac_interno,fac_externo,alfa);
    return estrategia;

def genera_lista_estrategia(lista_fac_interno:list[factor_foda],
                            lista_fac_externo:list[factor_foda],
                            alfa:list[float])->list[c_estrategia]:
    
    cant_int = len(lista_fac_interno);
    cant_ext = len(lista_fac_externo);
    resultado:list[c_estrategia] = [];
    
    for i in range(cant_int):
        for j in range (cant_ext):
            resultado.append(c_estrategia(lista_fac_interno[i],
                                          lista_fac_externo[j],alfa));
    
    
    return resultado;
