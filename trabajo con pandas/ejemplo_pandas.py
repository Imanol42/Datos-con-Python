import pandas as pd
#cargar un archivo de excel
datos_excel = pd.read_excel('C:/Users/Imanol/Desktop/analisis de datos/Base.xlsx', index_col=0, engine='openpyxl')
print(datos_excel.head(5))