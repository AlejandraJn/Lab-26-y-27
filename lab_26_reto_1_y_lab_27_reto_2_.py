# -*- coding: utf-8 -*-
"""Lab 26 reto 1 y Lab 27 Reto 2.

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XTY8ePlujclbUt2r12fJKT3n6J2LRNL5
"""

import pandas as pd

file_path = "Producto_licores.csv"
df = pd.read_csv(file_path)

#Mostrar las primeras 5 filas

print("primeras filas del dataset: ")
print(df.head())

#Ver ultimas filas del dataset

print("ultimas filas del dataset: ")
print(df.tail())

#Mostrar información general

print("información general del dataset: ")
print(df.info())

#Vereficar valores nulos por columna

print("valores nulos por columna: ")
print(df.isnull().sum())

#Verificar si hay datos duplicados

print("numero de filas duplicadas: ")
print(df.duplicated().sum())

#Número de filas y de columnas

print("numero de filas y columnas: ")
print(df.shape)

#Mostar nombres de las columnas

print("nombres de las columnas: ")
print(df.columns)

#Mostrar de columnas categoricas

for colum in df.select_dtypes(include=['object']).columns:
    print(f"{colum}: ")
    print(df[colum].unique()[:5])

#Cantidad de valores unicos por columna

print("valores unicos por columna: ")
print(df.nunique())

#Columnas con valores unicos bajos

print("columnas con valores unicos bajos: ")

for column in df.columns:
  unique_count = df[colum].nunique()
  if unique_count < 10:
    print(f"{colum}: {unique_count} valores unicos")

#Mostar ejemplos nulos

print("ejemplos de valores nulos: ")
print(df[df.isnull().any(axis=1)].head())

#Describir columnas de texto o cadenas de caracteres

print("Descripcion de columnas de texto: ")
for column in df.select_dtypes(include=['object']).columns:
  print(f"{column}: {df[column].str.len().describe()}")

# Valores unicos que podrían ser inconsistencias

print("Inconsistencias potenciales: ")
for column in df.select_dtypes(include=['object']).columns:
  print(f"{column}: {df[column].unique()[:10]}")

#Valores duplicados y valores nulos antes de la limpieza

nulos_antes = df.isnull().sum()
duplicados_antes = df.duplicated().sum()

print("valores duplicados y valores nulos antes de la limpieza: ")
print(f"duplicados: {duplicados_antes}")
print(f"nulos: {nulos_antes}")

#Limpieza

# a. Eliminar filas con valores nulos en columnas críticas

columnas_criticas = ['ORIGEN', 'PRODUCTO', 'GRADO DE ALCOHOL', 'REGISTRO SANITARIO']
df = df.dropna(subset=columnas_criticas)

nulos_antes = df.isnull().sum()
print(nulos_antes)

#Rellenar valores nulosen caso de ser necesario

df['NOMBRE EMPRESA DISTRIBUIDORA'].fillna('Desconocido', inplace=True)
print(df.isnull().sum())

df = df.dropna()

nulos_despues = df.isnull().sum()
print(nulos_despues)

df = df.drop_duplicates()

duplicados_despues = df.duplicated().sum()
print(duplicados_despues)

print("Datos depues de nuestra limpieza: ")
print(df.head())

df.to_csv('Producto_licores_limpio.csv', index=False)
print("El dataset ha sido guardado como 'producto_licores_limpio.csv'")

from google.colab import files
files.download('Producto_licores_limpio.csv')

descriptive_stats = df.describe()
print(descriptive_stats)