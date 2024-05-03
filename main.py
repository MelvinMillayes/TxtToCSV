#Python funcion join_data()
import csv
import os
import re

#Funcion que recopila la infomacion que no se encuntra en el archivo. Trabajado por Mathew
def collect_data():
    new_data = []
    institucion = input("Entre el nombre de la institucion: ")
    recinto = input("Entre el nombre de recinto: ")
    semestre = input("Entre el semestre: ")
    profesor = input("Entre el nombre del profesor: ")
    new_data.append({'institucion': institucion, 'recinto': recinto, 'semestre': semestre, 'profesor': profesor})
    return new_data






#Funcion para leer archivo, trabajado por Melvin
def read_txt():
  print("Entre el nombre del archivo:")
  filename = input()
  return filename

def output_csv():
  print("Entre el nombre que le desea asignar al archivo de salida")
  csv_name = input() + ".csv"

#funcion que une los datos entrados por el usuario (los nombres de las variables pueden cambiar solo se usaron los anteriores como referencia) 
#Trabajado por Brian, Christian, Melvin
def join_data(): 
  
  data_array = collect_data()
  
  file_name = read_txt()
  try:
    with open(file_name, 'r') as file: # la ‘r’ se utiliza para abrir el file en modo read.
      lines = file.readlines()          # esto se hace para preservar la integridad de el archivo
      file.close()




    with open(file_name + ".csv", 'w', newline= "") as csv_file: # ya aqui se juntan los datos + la conversion
      fieldnames = ["institucion", "recinto", "departamento", "semestre", "profesor"]

      #Cambia el nombre del csv file al nombre ingrsado por el usuario
   
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
      writer.writeheader()  # Escribe header row
    
      for row in data_array:
        writer.writerow(row)

      #loop que coloca comas en cada lugar del archivo que halla espacio en blanco
      for line in lines:
       tokens = re.split(r'\s+', line.strip())
       csv_file.write(",".join(tokens) + "\n")
      
      print("CSV file created successfully.")

  except FileNotFoundError:
    print("File not found:", file_name)


#Cambia el nombre del file.csv al asignado por el usuario 
#Trabajado por Melvin
def rename_file():
  file_name = "ejemploDatos.txt.csv"
  print("Entre el nombre que le desea asignar al archivo .csv(sin la extension)")
  csv_name = input() + ".csv"
  os.rename(file_name, csv_name)



join_data()

rename_file()




