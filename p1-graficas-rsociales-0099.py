# Anais Medina NC 0099 fecha noviembre
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por listas
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012] 
# Creamos una lista de listas (corformando la tabla)
lista_redes_sociales=[fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
#utilizar panda parab organizar la tabla (DataFrame)
# a cada columna le pones un nombre
df_redes_sociales=pd.DataFrame(lista_redes_sociales, columns=["Nombre","Cantidad","Es_FB","Año"])
print(df_redes_sociales)
# creamos el archivo CSV y lo guardamos en CSV
# df_redes_sociales.to_csv("redessociales.csv", index=False)
# ahora creamremos una grafica de lineas 
# donde X es Nombre en el eje horinzontal
# donde Y es Cantidad en el eje vertical
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"]) 
plt.title("Grafica redes sociales 0099")
plt.xlabel("Nombre de redes Sociales")
plt.ylabel("Cantidad de usuarios")
plt.show()

# ceamos una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"]) 
plt.show()

# grafica de barras 
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"]) 
plt.title("Redes sociales 0099")
plt.xlabel("las redes")
plt.ylabel("Cantidad usuarios")
plt.show()

# ordena la grafica de barras de manera descendente
# de la mas grande a la pequeña
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()

# coloreando la grafica 
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

# grafica de pastel
# plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()