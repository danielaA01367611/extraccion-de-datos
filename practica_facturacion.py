import pandas as pd

df=pd.read_excel("datos_facturacion.xlsx")
#print(df.head())

filtro1=df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
#print(filtro1)
filtro1.to_csv('practica_facturacion1.csv')

filtro2 = df[~(df["CVE_VEND"] == 5.0 ) & ~(df["CVE_VEND"] == 4.0)]
#print(filtro2)
filtro2.to_csv('practica_facturacion2.csv')

# year
#filtro3=df[ df["FECHA_ENT"].dt.strftime('%Y') == '2019']
# year-month
#filtro3=df[ df["FECHA_ENT"].dt.strftime('%Y-%m') == '2019-10']
# year-month-day
df['FECHAELAB'] = pd.to_datetime(df['FECHAELAB'])
filtro3=df[ df["FECHAELAB"].dt.strftime('%Y-%m-%d') == '2019-10-02']
#print(filtro3)
filtro3.to_csv('practica_facturacion3.csv')

filtro4=df[(df["CAN_TOT"] < 5951.7)| (df["STATUS"] == "E")]
#print(filtro4)
filtro4.to_csv('practica_facturacion4.csv')

filtro5 = df.iloc[ : , [0, 6, 7,9]]  
print(filtro5)
filtro5.to_csv('practica_facturacion5.csv')