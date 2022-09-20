#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:00:59 2022

@author: seba
"""

from clasesSCH import c_estrategia,intersecc_fuzzy 



def obtiene_item_prioridad(lista_interseccion:list[intersecc_fuzzy], prioridad:int)->intersecc_fuzzy:
    for i in range (len(lista_interseccion)):
        if(lista_interseccion[i].prioridad == prioridad):
            return lista_interseccion[i];
      
    print("Prioridad no encontrada")
    return None;

def obtiene_item_estrategia_c(lista_estrategias:list[c_estrategia], prioridad:int)->c_estrategia:
    for i in range (len(lista_estrategias)):
        if(lista_estrategias[i].prioridadTotal == prioridad):
            return lista_estrategias[i];
      
    print("Prioridad no encontrada")
    return None;



#Priorizador de Intesecciones
#Utilizo el metodo de burbuja
def prioriza_intersecciones(lista_interseccion:list[intersecc_fuzzy],alfa:float):
    cambio:bool = True;
    cantidad= len(lista_interseccion)
    if(cantidad >1):
        #Asigno una prioridad Inicial
        for i in range (cantidad):
            lista_interseccion[i].prioridad =i+1;
        
        
        while cambio==True:
            cambio=False;
            for i in range (1,cantidad):
                #Comparo un orden prioridad con el inferior
                #Nota prioridad 1 mayor, 2 menor.... (Ascendente)
                item_1:intersecc_fuzzy =obtiene_item_prioridad(lista_interseccion, i);
                item_2:intersecc_fuzzy =obtiene_item_prioridad(lista_interseccion, i+1);
                if(item_1 !=None and item_2!=None):
                    if(item_2.cj > item_1.cj):
                        prioridad_aux= item_2.prioridad;
                        item_2.prioridad = item_1.prioridad;
                        item_1.prioridad = prioridad_aux;
                        cambio=True;
      
    #Cuando llegue Aqui el grupo esta Ordenado
    print ("Intersecciones de Alfa= "+ str(alfa) + " Priorizado")        

#Priorizador de Intesecciones
#Utilizo el metodo de burbuja
def prioriza_estrategia_ponderada(lista_estrategias:list[c_estrategia]):
    cambio:bool = True;
    cantidad= len(lista_estrategias)
    if(cantidad >1):
        #Asigno una prioridad Inicial
        for i in range (cantidad):
            lista_estrategias[i].prioridadTotal =i+1;
        
        
        while cambio==True:
            cambio=False;
            for i in range (1,cantidad):
                #Comparo un orden prioridad con el inferior
                #Nota prioridad 1 mayor, 2 menor.... (Ascendente)
                item_1:c_estrategia =obtiene_item_estrategia_c(lista_estrategias, i);
                item_2:c_estrategia =obtiene_item_estrategia_c(lista_estrategias, i+1);
                if(item_1 !=None and item_2!=None):
                    if(item_2.prioridadPonderada < item_1.prioridadPonderada):
                        prioridad_aux= item_2.prioridadTotal;
                        item_2.prioridadTotal = item_1.prioridadTotal;
                        item_1.prioridadTotal = prioridad_aux;
                        cambio=True;
              
    #Cuando llegue Aqui el grupo esta Ordenado
    print ("Priorizacion Ponderada Realizada")        


def prioriza_estrategias(lista_estrategias: list[c_estrategia]):
    #Primero tengo que recorrer
    #testeo punteros
    cantidad= len(lista_estrategias);
    if(cantidad <=0):
        print("Error al clasificar - cantidad ");
        return;
    
    cantidad_alfa = len(lista_estrategias[0].alfa);
    
    print( "Priorizando " +str(cantidad) +  " Estrategias con "+str(cantidad_alfa) + " Intersecciones de planos cada Una");
    print("Total: " + str(cantidad_alfa*cantidad))
    
    for i in range (cantidad_alfa):
        lista_priorizar:list[intersecc_fuzzy] = [];
        alfa = lista_estrategias[0].alfa[i];
        for j in range (cantidad):
            lista_priorizar.append(lista_estrategias[j].intersecciones[i]);
        
        prioriza_intersecciones(lista_priorizar, alfa);
  
    #Ahora calculo la prioridad ponderada
    cantidad= len(lista_estrategias);
    for i in range (cantidad):
        lista_estrategias[i].calcula_prioridad_ponderada();
        
    # #Una vez que tengo la prioridad ponderada, Reordeno las estrategias
    prioriza_estrategia_ponderada(lista_estrategias);