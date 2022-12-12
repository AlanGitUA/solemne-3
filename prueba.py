



import pandas as pd

#Cargar el archivo .csv
datos=pd.read_csv("Solemne03.csv")
#Quitar todas las filas que contengan NaN, Null, True, False
datos.dropna(how="any",inplace=True)
datos2=datos.drop(datos.index[datos.Nombres == "TRUE"],axis=0)
datos3=datos2.drop(datos2.index[datos2.Nombres == "FALSE"],axis=0)
#Quitar todas las filas donde la edad sea menor que 0 y mayor a 120
datos4=datos3.drop(datos3.index[datos3.Edad < 0],axis=0)
datos5=datos4.drop(datos4.index[datos4.Edad > 120],axis=0)
df=pd.DataFrame(datos5)
#Eliminar las filas con nombres duplicados, considerando el sueldo más alto
#La columna 'Sueldo' de mayor a menor
df2=df.sort_values(by=["Sueldo"],ascending=[False])
df3=df2.drop_duplicates(subset="Nombres")
#Agregar una nueva columna
#Según la terminal hay un error en esta parte pero igualmente sigue su funcionamiento
df3["Profesion"] = ""
df3.loc[df3["Edad"] > int("60"),"Profesion"]="Docente"
df3.loc[df3["Edad"] < int("60"),"Profesion"]="Estudiante"
df4=df3
#Creamos un archivo nuevo con todos los cambios ya realizados
df4.reset_index().to_csv("FINAL.csv",header=True,index=False)
