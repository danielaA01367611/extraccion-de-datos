import pandas as pd

print("Aplicacion de extraccion de datos")
df=pd.read_excel("detalle_precios_productos_fabricados_2022.xlsx")
print(df.info)
df.head()

filtro1=df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
filtro1