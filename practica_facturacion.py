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
#print(filtro5)
filtro5.to_csv('practica_facturacion5.csv')

#filtro nivel renglon
filtro6 = df.iloc[7001:7003, [0,1,2] ] 
#print(filtro6)
filtro6.to_csv('practica_facturacion6.csv')

df1= pd.read_excel('datos_facturacion.xlsx', index_col=3)
#df1.head()

filtro7=df1.loc[[1.0,2.0], ["FECHAELAB"]]
print(filtro7)
filtro7.to_csv('practica_facturacion7.csv')