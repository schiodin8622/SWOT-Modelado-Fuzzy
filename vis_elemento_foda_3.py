#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:07:55 2022

@author: seba
    Analisis Foda Implementado con Lógica Difusa
    
    Construccion de proceso de Fuzzificacion 
    de Un Factor Interno y otro Externo
    
--- Alea iacta Est ---
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as mpfig
import math;
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  
from matplotlib import style
from matplotlib.patches import Rectangle

#Nota sobre los valores:
#Un array de tres elemenos, pesimista, probable, optimista
#-10: (Minimo: ya sea debilidad o amenaza)*
#+10: (Maximo ya sea fortaleza o )*

#Factor Interno
fact_int = np.array([5,6.5,7]);

#Factor Externo
fact_ext = np.array([5,7,7.8]);

#Niveles de convulsion del mercado
#mas cerca a 0, hay mas Inestabilidad e incertibumbre general
#1 total estabilidad de condiciones
alfa= np.array([0.2,0.6,0.9]);

#Constantes de altura de la funcion triangular
z_triag = np.array([0,1,0]);

#Arrays utilizado para las proyeccinones ortogonales
#de la 
y_cte = np.array([0,0,0]);
x_cte = np.array([10,10,10]);


vert_fact_int = [list(zip(fact_int, y_cte, z_triag))];
vert_fact_ext = [list(zip(x_cte, fact_ext, z_triag))];
plt.figure(1,figsize=(100,40))
custom=plt.subplot(121,projection='3d')

#custom.scatter(x1,y1,z1) 
#Estos son los puntos-
custom.scatter(fact_int,y_cte,z_triag) 
#Ahora los puntos del externo
custom.scatter(x_cte, fact_ext, z_triag) 

#Construcccion de la base de la piramide y los 5 vertices

#                               Vista lateral
#                  #p5              #  p5             
#                                  * * 
#             p4------p3          *   *
#             /       /          *     *
#            /       /          *       *
#           p1-----p2         p1--------p2   
#


p1 =np.array([fact_int[0],fact_ext[0],0]);
p2 =np.array([fact_int[2],fact_ext[0],0]);
p3 =np.array([fact_int[2],fact_ext[2],0]);
p4 =np.array([fact_int[0],fact_ext[2],0]);
p5 =np.array([fact_int[1],fact_ext[1],1]);



#Los puntos de la base en Z=0 son
# Xmin,Ymin ; Xmax,Ymin ;
# Xmax,Ymin; Xmin,Ymax
# 

#Cara Piramide 1

#Triangulo dado por la terna
# Xmin, Ymin, 0; Xmax,Ymin, 0; Xpr, Ypr,1
#p1, p2, p5
#Nota: pr = probable
vert_c1 = [[tuple(p1),tuple(p2),tuple(p5)]]
#vert_cara1= vert_c1.tolist();

srf_cara1_piramide = Poly3DCollection(vert_c1, alpha=.35, facecolor='#900000')


#Cara Piramide 2

#Triangulo dado por la terna
# Xmax,Ymin, 0; Xmax,Ymax, 0, 0; Xpr,
#Nota: pr = probable
vert_c2 = [[tuple(p2),tuple(p3),tuple(p5)]]
#vert_cara1= vert_c1.tolist();

srf_cara2_piramide = Poly3DCollection(vert_c2, alpha=.35, facecolor='#FF0000')


#Cara Piramide 3

#Triangulo dado por la terna
# Xmax,Ymin, 0; Xmax,Ymax, 0, 0; Xpr,
#Nota: pr = probable
vert_c3 = [[tuple(p3),tuple(p4),tuple(p5)]]
#vert_cara1= vert_c1.tolist();

srf_cara3_piramide = Poly3DCollection(vert_c3, alpha=0.1, facecolor='#600000')


#Cara Piramide 4

#Triangulo dado por la terna
# Xmax,Ymin, 0; Xmax,Ymax, 0, 0; Xpr,
#Nota: pr = probable
vert_c4 = [[tuple(p4),tuple(p1),tuple(p5)]]
#vert_cara1= vert_c1.tolist();

srf_cara4_piramide = Poly3DCollection(vert_c4, alpha=0.01, facecolor='#600000')




#descripcion de Alfa
# Son planos de ecuacion z= alpha (Paralelo al XY)

# diagrama de las superfices 3D con 
#srf = Poly3DCollection(verts, alpha=.25, facecolor='#800000')
srf_fact_int = Poly3DCollection(vert_fact_int, alpha=.25, facecolor='#900000')
srf_fact_ext = Poly3DCollection(vert_fact_ext, alpha=.25, facecolor='#900000')
#Nota: este Alfa es distinto del color, es 
#nivel del transparencia de la forma 3D

# 3. add polygon to the figure (current axes)
#plt.gca().add_collection3d(srf)
plt.gca().add_collection3d(srf_fact_int)
plt.gca().add_collection3d(srf_fact_ext)
plt.gca().add_collection3d(srf_cara1_piramide)
plt.gca().add_collection3d(srf_cara2_piramide)
plt.gca().add_collection3d(srf_cara3_piramide)
plt.gca().add_collection3d(srf_cara4_piramide)
#Remarco la cara frontal con mas Alfa
plt.gca().add_collection3d(srf_cara1_piramide)


#Planos de interseccion Alfa

# create x,y
xx, yy = np.meshgrid(range(0,11), range(0,11))

# calculate corresponding z
z0 = 0.0*xx + 0.0*yy + alfa[0]
z1 = 0.0*xx + 0.0*yy + alfa[1]
z2 = 0.0*xx + 0.0*yy + alfa[2]

#Todo Corregir el Z
plt.gca().plot_surface(xx, yy, z0, alpha=0.2)
plt.gca().plot_surface(xx, yy, z1, alpha=0.2)
plt.gca().plot_surface(xx, yy, z2, alpha=0.2)
 
custom.set_xlabel('Factores Internos',fontsize=54,labelpad=40)

custom.set_ylabel('Factores Externos',fontsize=54,labelpad=40)
custom.set_zlabel('Z',fontsize=54,labelpad=40)
custom.zaxis.set_tick_params(labelsize=35,pad=20)

plt.xticks(fontsize=35)
plt.yticks(fontsize=35)

plt.show()


#Bien Ahora tengo que crear el segundo plot con las intersecciones

#Calculo de xmin, ymin, xmax, ymax

#Las base del triangulo es 
#A Peor de los casos
#B Probable
#C Mejor de los Casos
#alfa: plano de corte

#xmin = A + alfa *(B-A)
#xmax = C - alfa * (C-A)

plt.figure(2,figsize=(100,40))

plt.xticks(fontsize=100)

plt.yticks(fontsize=100)


for tick in plt.gca().get_xaxis().get_major_ticks():
    tick.set_pad(20.)
    
for tick in plt.gca().get_yaxis().get_major_ticks():
    tick.set_pad(40.0)
    

for i in range(len(alfa)):
    print ("Iteracion " + str(i) + " Alfa = " + str(alfa[i]))
    xmin = fact_int[0] + alfa[i] * (fact_int[1] - fact_int[0])
    xmax = fact_int[2] - alfa[i] * (fact_int[2] - fact_int[1])
    ymin = fact_ext[0] + alfa[i] * (fact_ext[1] - fact_ext[0])
    ymax = fact_ext[2] - alfa[i] * (fact_ext[2] - fact_ext[1])
    #deltas del rectangulo
    delta_x = xmax - xmin
    delta_y = ymax - ymin
    #calculo de centro de masa de los puntos
    xcm = (xmax + xmin)/2
    ycm = (ymax + ymin)/2
    #Distancias desde los puntos ideales 
    dj_optimo    = math.sqrt((10-xcm)**2 + (10-ycm)**2 )
    dj_pesimista = math.sqrt((-10-xcm)**2 + (-10-ycm)**2 )
    
    #Coeficiente de cercania
    #Se utiliza para priorizar las 
    coef_cerc= dj_pesimista/ (dj_pesimista + dj_optimo)
    
    print( "xmin =" + str(xmin))
    print( "xmax =" + str(xmax))
    
    print( "ymin =" + str(ymin))
    print( "ymax =" + str(ymax))
    
    print( "xcm =" + str(xcm))
    print( "ycm =" + str(ycm))
 
    print( "Doptimo =" + str(dj_optimo))
    print( "Dpesimista =" + str(dj_pesimista))
    
    print( "Coeficiente de cercania:" + str(coef_cerc))
    
    print( "--------------------")  
    #Dibujo el rectangulo con los vertices
    rectangulo = [[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)]]
    plt.gca().add_patch(Rectangle((xmin, ymin), delta_x, delta_y,alpha=0.23))
    plt.gca().text(xmin - 0.1 , ymin + 0.35, r'$\alpha=$'+str(alfa[i]), fontsize=100)
    #Diagramo los centros de masa
    plt.gca().scatter(xcm,ycm,1000)
    
plt.gca().set_xlabel('Factores Internos',fontsize=100,labelpad=40)
plt.gca().set_ylabel('Factores Externos',fontsize=100,labelpad=40)
plt.xlim([5, 8])
plt.ylim([5, 10])
plt.show()   
    
