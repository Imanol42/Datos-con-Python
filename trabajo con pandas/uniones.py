import pandas as pd

notas = pd.DataFrame({'nombre':['imanol','flor','jony','juan','melanie','pablo','imanol','jony','melanie'],'nota' :[3,8,9,7,9,6,7,9,10]})
edad = pd.DataFrame({ 'nombre':['imanol','flor','jony','juan','melanie'],'edad' :[19,28,39,27,9]})
df = pd.DataFrame({'nombre':['imanol','flor','jony','juan','melanie'],'notas' :[9,8,9,7,9]})

print(notas)
print("------------------------")
print(edad)

#combinar tablas con las columnas en común
merged_df = pd.merge(notas,edad,on='nombre',how='outer')
print('------------------------')
print(merged_df)

#combinar tablas con los datos de la columna derecha en comun
print('------------------------')
merged_df2 = pd.merge(notas,edad,on='nombre',how='right')
print(merged_df2)

#combinar tablas con los datos de la columna izquierda en comun
print('------------------------')
merged_df2 = pd.merge(notas,edad,on='nombre',how='left')
print(merged_df2)

#agrupar por notas
print('------------------------')
grouped_df = notas.groupby('nota').count()
#print(grouped_df)

#sacar promedio de notas en tabla notas por columna nombre
print('------------------------') 
tabla_pivot = notas.pivot_table('nota', index='nombre', aggfunc='mean')
print(tabla_pivot) 

#apply y normalizacion de columna
print('------------------------') 
def aprobados(nota):
    return 'aprobado' if nota >= 6 else 'desaprobado'

tabla_pivot['notas'] = tabla_pivot['nota'].apply(aprobados)
print(tabla_pivot)

#para eliminar valores que tengan Nan (Not a Namber) en columna se hace de la siguiente manera 
merged_df = merged_df.dropna()
print(merged_df)


#convertir de un dato a otro
print('------------------------') 
tabla_pivot['nota'] = tabla_pivot['nota'].round().astype(int)
print(tabla_pivot)
