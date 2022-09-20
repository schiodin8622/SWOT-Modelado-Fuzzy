#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:33:41 2022

@author: seba

Definicion de las clases de:
    * Factores FODA (Internos y externos)
    * Interseccion de Fuzzificacion (
        Intesecciones de planos Alfa para misma estrategia)
    * Estrategia individual (Contenedor de la estrategia con las variantes)
Ing. Sebastian A. Chiodin, Septiembre 2022 
"""

import math;

#Puede ser interno o externo
class factor_foda:
    
    def __init__(self):
        self.Descripcion="";
        self.interno=False;
        self.id=1;
        self.min = -1.0;
        self.probable=1;
        self.max=2.2
        self.valores:list[float] = [self.min, self.probable, self.max];
  
    def actualiza_valores(self):
        self.valores:list[float] = [self.min, self.probable, self.max];
        
#Una Interseccion para un alfa especifico
class intersecc_fuzzy:
    
    def __init__(self,factor_int:factor_foda,
                 factor_ext:factor_foda, alfa:float):
        self.xmin:float=0;
        self.xmax:float=1.0;
        self.ymin:float=0;
        self.ymax:float=1.0;
        self.xcm:float=1;
        self.ycm:float=2.2
        self.dj_optimo:float=1;
        self.dj_pesimista:float=2.2
        self.cj:float=0.0
        self.alfa:float=alfa
        self.factor_int:factor_foda = factor_int;
        self.factor_int.interno=True;    
        self.factor_ext:factor_foda = factor_ext;
        self.factor_int.interno=False;
        self.prioridad:int=1;
        self.porcentaje_cuadrante:list[float] = [0.0, 0.0, 0.0, 0.0];
        self.area = 0.0;
        
    #Cuadrante 
    #I:     F.O. (Fortaleza, Oportunidad)
    #II:    D.O. (Debilidad, Oportonidad)
    #III:   D.A. (Debilidad, Amenaza)
    #IV:    F.A. (Fortaleza, Amenaza)
    def limita_area_cuadrante(self,cuadrante:int)->float:
        valor=0.0;
        
        xmin =self.xmin;
        ymin = self.ymin;
        
        xmax=self.xmax;
        ymax= self.ymax;
        
        if(cuadrante<1):
            cuadrante=1;
            
        if(cuadrante>4):
            cuadrante =4;
            
            #Cuadrante I
            #Solo x>=0 e y>=0
        if(cuadrante ==1):
            if(xmin<=0):
                xmin=0;

            if(xmax<=0):
                xmax=0;

            if(ymin<=0):
               ymin=0;

            if(ymin<=0):
               ymax=0;                

            #Cuadrante II
            #Solo x<=0 e y>=0
        if(cuadrante ==2):
            if(xmin>=0):
                xmin=0;

            if(xmax>=0):
                xmax=0;

            if(ymin<=0):
               ymin=0;

            if(ymin<=0):
               ymax=0;
               
               #Cuadrante III 
               #Solo x<=0 e y<=0
        if(cuadrante ==3):
               if(xmin>=0):
                   xmin=0;

               if(xmax>=0):
                   xmax=0;

               if(ymin>=0):
                  ymin=0;

               if(ymin>=0):
                  ymax=0;  

               #Cuadrante IV 
               #Solo x>=0 e y<=0
        if(cuadrante ==4):
               if(xmin<=0):
                   xmin=0;

               if(xmax<=0):
                   xmax=0;

               if(ymin>=0):
                  ymin=0;

               if(ymin>=0):
                  ymax=0;
                  
        
        valor = (xmax-xmin)*(ymax-ymin);
            
        return valor;
        

    #Devuelvo el valor minimo y maximo de la interseccion del 
    #triangulo con 
    def calcula_interseccion(self,abcisas:list[float], alfa:float)->list[float]:
        resultado= [0.0, 0.0];
       
        #limito Alfa
        if(alfa<0.0):
            alfa=0.0;
            
        if(alfa>=1.0):
            alfa=1.0
        
        val_min = abcisas[0] + alfa* (abcisas[1] - abcisas[0]);
        val_max = abcisas[2] - alfa * (abcisas[2] - abcisas[1]);
        resultado[0] = val_min;
        resultado[1] = val_max;
        return resultado;
        
    def calcula_parametros(self):
        x_lim:list[float] = self.calcula_interseccion(self.factor_int.valores,self.alfa)
        y_lim:list[float] = self.calcula_interseccion(self.factor_ext.valores,self.alfa)
        xcm = (x_lim[0] + x_lim[1])/2
        ycm = (y_lim[0] + y_lim[1])/2
        #Distancias desde los puntos ideales 
        dj_optimo    = math.sqrt((10-xcm)**2 + (10-ycm)**2 )
        dj_pesimista = math.sqrt((-10-xcm)**2 + (-10-ycm)**2 )
        
        #Coeficiente de cercania
        #Se utiliza para priorizar las 
        coef_cerc= dj_pesimista/ (dj_pesimista + dj_optimo)
        
        #Asigno los valores en la clase
        self.xmin:float=x_lim[0];
        self.xmax:float=x_lim[1];
        self.ymin:float=y_lim[0];
        self.ymax:float=y_lim[1];
        self.xcm:float=xcm;
        self.ycm:float=ycm
        self.dj_optimo:float=dj_optimo;
        self.dj_pesimista:float=dj_pesimista
        self.cj:float=coef_cerc;
        #Calcula los porcentajes en cuadrantes
        area = (self.xmax-self.xmin) * (self.ymax-self.ymin)
        self.area = area;
        
        if(area >= 1e-6):
            for i in range(4):
                area_cuadrante =self.limita_area_cuadrante(i+1);
                self.porcentaje_cuadrante[i] = 100.0* area_cuadrante/area;
        
        acc2=0.0;
        for i in range(4):
            acc2+=self.porcentaje_cuadrante[i];
            
        #print(acc2);
        #print(self.xcm);
        #print(self.ycm);
        
#Nota Para el calculo de las prioridades
#Tengo que comparar las mismas en funcion del mismo Alfa 
#Y luego ponderarlas
#EJ. PRIORIZO TODAS LAS DE 0.1 luego las de 0.6 y luego las de 0.9

#Tiene todas las variantes de las estrategia
class c_estrategia:
    
    def __init__(self,factor_int:factor_foda,
                 factor_ext:factor_foda, alfa:list[float]):
        self.factor_int:factor_foda = factor_int;
        self.factor_int.interno=True;    
        self.factor_ext:factor_foda = factor_ext;
        self.factor_int.interno=False;  
        self.alfa=alfa;
        self.prioridadPonderada=1;
        self.prioridadTotal=1;
        self.intersecciones:list[intersecc_fuzzy]=[];
        self.numFcInt=factor_int.id;
        self.numFcExt=factor_ext.id;
        self.area_cuadrante_ponderada:list[float]=[0.0, 0.0, 0.0, 0.0];
        self.area_ponderada:float = 0.0;
        
        cantidad = len(alfa);
        #Cargo todas las intersecciones de la presente
        #Estrategia
        for i in range(cantidad):
          self.intersecciones.append(intersecc_fuzzy(
              factor_int, factor_ext,alfa[i])); 
        #Una vez cargada, proceso el calculo de parametros
        for i in range(cantidad):
            self.intersecciones[i].calcula_parametros();
        
    #Calculo Prioridad Ponderada Y area
    def calcula_prioridad_ponderada(self):
        cant = len(self.alfa)
        acc:float=0.0;
        for i in range(cant):
            acc+=self.intersecciones[i].prioridad *self.intersecciones[i].alfa;
           # print(self.intersecciones[i].prioridad);
           # print(self.intersecciones[i].alfa);
        #Calculo la prioridad Ponderada
        self.prioridadPonderada = acc;
       # print ("Prioridad Ponderada: " + str(self.prioridadPonderada));

        #Tengo que calcular el area Ponderada en los cuadrantes
        acc=0.0;
        for i in range(cant):
            acc+=self.intersecciones[i].area *self.intersecciones[i].alfa;
        
        self.area_ponderada = acc;
       
        for i in range(4):
            self.area_cuadrante_ponderada[i] = self.intersecciones[0].porcentaje_cuadrante[i];
        #Para Contrastar Cuadrantes de decision, tomo el area mas grande (menor alfa)
        
        # for i in range(4):
        #     area_abs=0.0;
        #     for j in range(cant):
        #         area_abs += self.intersecciones[j].area*self.intersecciones[j].alfa * self.intersecciones[j].porcentaje_cuadrante[i];
        #     if(self.area_ponderada>=1e-5):
        #         self.area_cuadrante_ponderada[i] = area_abs /self.area_ponderada;
    
    #Tengo que devolver este esquema en la fila
    #       header = ["Fila", "Factor Interno", "Factor Exteno",  "% Cuadrante 1", 
    #                 "% Cuadrante 2", "% Cuadrante 3", "% Cuadrante 4", "P alpha1", 
    #                 "P Alpha2", "P Alpha3", "P ponderada", "Prioridad Neta"];
    #           
    def devuelve_fila(self, fila:int):
        lista = [];
        #N de Fila
        lista.append(fila);
        #Factor Interno
        lista.append(self.numFcInt);
        #Factor Externo
        lista.append(self.numFcExt);
        #Areas de Cuadrante
        for i in range(4):
            lista.append(self.area_cuadrante_ponderada[i]);
        #Prioridades por Alfas
        for i in range(len(self.alfa)):
            lista.append(self.intersecciones[i].prioridad);
            
       
        #Prioridad Ponderada
        lista.append(self.prioridadPonderada);
        #Prioridad Neta
        lista.append(self.prioridadTotal);
        
        for i in range(len(self.alfa)):
            lista.append(self.intersecciones[i].cj);    


        lista.append(self.factor_int.Descripcion)
        lista.append(self.factor_ext.Descripcion)
        
        return lista;
    