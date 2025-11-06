import pandas as pd

# Leer el archivo con codificación segura
df = pd.read_csv("turnos_clinica.csv", encoding="latin1")

# Limpieza completa de nombres de columnas
df.columns = df.columns.str.strip().str.lower()
df.columns = df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

print("\nNombres de columnas después de limpiar:")
print(df.columns)

# Buscar automáticamente la columna que contenga la palabra "asist"
col_asistencia = [c for c in df.columns if "asist" in c][0]
print(f"\nUsando columna de asistencia: {col_asistencia}")

# Calcular el porcentaje
asistieron = df[col_asistencia].value_counts(normalize=True) * 100
print("\nPorcentaje de asistencia:")
print(asistieron)





print("Mostrar primeras diez celdas")

print(df.head())

print("\nInformacion General:")
print(df.info())
print("\nCantidad de turnos:", len(df))
print("\nPromedio de tiempo de espera (min):", df["tiempo_espera_min"].mean())





print("\nEspecialidades con mas turno:")
print(df["especialidad"].value_counts())

print("\nRecaudacion total de clinica:")
print(df["costo_consulta"].sum())

print("\nNombres de columnas:")
print(df.columns)

for col in df.columns:
    print(repr(col))

def calcular_porcentaje_asistencia(df):
    """Calcula el prcentaje de pacientes que asistieron o no."""
    asistencia=df["asistia3"].value_counts(normalize=True)*100
    return asistencia
asistieron= calcular_porcentaje_asistencia(df)
print(asistieron)


#Practicar For, Wile, break, continue

for especialidad in df ["especialidad"]:
  if especialidad == "Cardiologia":
    print("Encontramos a Cardiologia ❤️")
    break

for index, fila in df.iterrows():
    if fila["asistia3"]=="No":
        continue
    print(f"Paciente que asistio:{fila["paciente"]}")
    
    contador= 0 
    while contador < 3:
        print("ejecutando analisis...", contador)
        contador += 1
    else:
        print("Bucle while finalizado correctamente✅")    
        
    try: 
        print(df["tiempo_espera_min"].mean())
    except KeyError:
        print("No se encontro la columna 'tiempo_espera_min'")    
    else: 
        print("Promedio de espera calculado correctamente") 
    finally:
        print("Analisis completado")   
        
        #AGREGAR GRAFICOOOSSSS¡¡¡
import matplotlib.pyplot as plt

asistieron.plot(kind="bar", color= ["mediumseagreen", "salmon"])
plt.title("Porcenbtaje de asistencia de pacientes")
plt.xlabel("Asistencia")
plt.ylabel("Porcentaje(%)")
plt.tight_layout()
plt.show()




espera_promedio= df.groupby("especialidad")["tiempo_espera_min"].mean()
espera_promedio.plot(kind="barh")
plt.title("Promedio de espera por especialidad")
plt.xlabel("Minutos de espera")
plt.tight_layout()
plt.show()





costo_promedio= df.groupby("profecional")["costo_consulta"].mean()
costo_promedio.plot(kind="bar")
plt.title("Costo promedio por profecional")
plt.ylabel("Costo ($)")
plt.tight_layout()
plt.show()

plt.savefig("grafico_asistencia.png")
