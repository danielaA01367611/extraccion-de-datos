import pandas as pd

print("Aplicacion de extraccion de datos")
df=pd.read_excel("detalle_precios_productos_fabricados_2022.xlsx")
#print(df.info)
#df.head()

#por objeto
filtro1=df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
#print(filtro1)
filtro1.to_csv('entregable1.csv')

#por filas
filtro2= df.iloc[2:8,: ]   
#print(filtro2)
filtro2.to_csv('entregable2.csv')

#Filtro por columnas
filtro3=df.iloc[ : , [1, 3, 4,10]]  
print(filtro3)
filtro3.to_csv('entregable3.csv')