# A partir de una base de datos .csv, realizar una transformación 

>>> import csv
>>> with open('ibm.csv', newline='') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))


lineaOriginal = [41,'Yes','Travel_Rarely',1102,'Sales',1,2,'Life Sciences',1,1,2,'Female',94,3,2,'Sales Executive',4,'Single',5993,19479,8,'Y','Yes',11,3,1,80,0,8,0,1,6,4,0,5]


# edadEmpleado = [0] JOVEN O NO. Si es <35 entonces es JOVEN. Sino VIEJOVEN.

# distancia = [5] Si es 1 entonces 'CERCA'. Si es 2 entonces 'MEDIO'. Si es 3 entonces 'LEJOS'. Resto: 'MARTE'

# carismaJefe = [-1] Si 3 entonces 'CHUNGO'. >3 y <= 10 entonces 'BUEN_JEFE'. Si >10 entonces 'CRACK'.

# movilidadAscendente = [-3] YearsInCurrentRole / [-4] Years at company 

# departamento = [4] Department: Si es SALES entonces -1. Si es 'Research & Development' 1. ELSE: 0.


edadEmpleado = int(lineaOriginal[0])
if edadEmpleado < 35: 
  edadEmpleado = "JOVEN"
else: 
  edadEmpleado = "VIEJOVEN"

distancia = int(lineaOriginal[5])
if distancia == 1:
  distancia = 'CERCA'
elif distancia == 2:
  distancia = 'MEDIO'
elif distancia == 3:
  distancia = 'LEJOS'
else: 
  distancia == 'MARTE'

carismaJefe = int(lineaOriginal[-1])
if carismaJefe == 3:
  carismaJefe = "CHUNGO"
elif carismaJefe > 3: 
  carismaJefe = 'BUEN JEFE'
elif carismaJefe <= 10:
  carismaJefe = 'BUEN JEFE'
elif carismaJefe > 10:
  carismaJefe = "CRACK"

movilidadAscendente = round(int(lineaOriginal[-3]) / int(lineaOriginal[-4]),2)

departamento = (lineaOriginal[4]).lower()
if departamento == 'sales':
  departamento = -1 
elif departamento ==  'Research & Development':
  departamento = 1 
else: 
  departamento = 0 

lineafinal = [edadEmpleado, distancia, carismaJefe, movilidadAscendente, departamento]
print(lineafinal)
