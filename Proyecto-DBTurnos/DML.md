# Proyecto

# Data Manipulation Language

Debido a que no conté con el tiempo necesario, usé datos ficticios para nutrir la base de datos. Para generar dichos datos use ChatGPT, aqui detallo los prompts y las respuestas.

## **Ingresar datos  las tablas 'diagnosticos' y 'salidas'**

```sql
INSERT INTO analisis_turnos.diagnosticos (tipo_dx) VALUES
	 ('respiratorio'),
	 ('gastrointestinal'),
	 ('neurologico'),
	 ('psiquiatrico'),
	 ('trauma'),
	 ('cardiovascular'),
	 ('urologico'),
	 ('ginecologico'),
	 ('osteomuscular'),
	 ('otros');

INSERT INTO analisis_turnos.salidas (tipo_salida) VALUES
	 ('casa'),
	 ('remision'),
	 ('salida voluntaria'),
	 ('muerto'),
	 ('fuga');
```

## Ingresar los datos a la tabla turnos

### Prompt a chatGPT para generar valores a la tabla turnos:

‘’’ Crea una script sql para insertar 15 valores con la siguiente forma:

INSERT INTO analisis_turnos.turnos
(nombre, hora_inicio, hora_final, fecha, n_pacientes)
VALUES('', '', '', '', 0);

Teniendo en cuenta las siquientes condiciones:
1. nombre sigue la secuencia: mañana, tarde, noche, dia12h, noche12h.
2. hora_inicio y hora_final deben ser respectivamente 06:00 y 14:00 cuando nombre es mañana, 14:00 y 22:00 cuando nombre es tarde, 22:00 y 06:00 cuando nombre es noche, 07:00 y 19:00 cuando nombre es dia12h y 19:00 y 07:00 cuando nombre es noche12h en formato TIME.
3. fecha debe iniciar el 01/01/2023 en formato DATE, debe haber minimo 24 horas de diferencia entre cada valor.
4. n_pacientes puede ser cualquier integer entre 0 y 30’’’

### Resultado generado:

```sql
INSERT INTO analisis_turnos.turnos 
(nombre, hora_inicio, hora_final, fecha, n_pacientes)
VALUES
('mañana', '06:00:00', '14:00:00', '2023-01-01', 10),
('tarde', '14:00:00', '22:00:00', '2023-01-02', 20),
('noche', '22:00:00', '06:00:00', '2023-01-03', 5),
('dia12h', '07:00:00', '19:00:00', '2023-01-04', 15),
('noche12h', '19:00:00', '07:00:00', '2023-01-05', 25),
('mañana', '06:00:00', '14:00:00', '2023-01-06', 8),
('tarde', '14:00:00', '22:00:00', '2023-01-07', 12),
('noche', '22:00:00', '06:00:00', '2023-01-08', 0),
('dia12h', '07:00:00', '19:00:00', '2023-01-09', 18),
('noche12h', '19:00:00', '07:00:00', '2023-01-10', 22),
('mañana', '06:00:00', '14:00:00', '2023-01-11', 5),
('tarde', '14:00:00', '22:00:00', '2023-01-12', 17),
('noche', '22:00:00', '06:00:00', '2023-01-13', 7),
('dia12h', '07:00:00', '19:00:00', '2023-01-14', 12),
('noche12h', '19:00:00', '07:00:00', '2023-01-15', 28);
```

En total fueron 15 días de turno, para un total de 255 pacientes.

## Ingresar los datos a la tabla pacientes

### Prompt para generar los datos en la tabla pacientes

’’’Actua como un programador experto y crea un script en python que genere un lista de 255 tuplas con la siguiente forma:

(0, 0, 0, '', '', 0, 0, 0, 0, '', 0)

Teniendo en cuenta las siquientes condiciones:
1. El primer item debe ser un integer entre 1 y 15
2. El segunto item debe ser un integer entre 1 y 10
3. El tercer item deber ser un integer entre 1 y 5, siendo la moda 1.
4. El cuarto y quinto item pueden ser cualquier hora en formato TIME SQL. el promedio de las diferencias entre ambos valores debe ser un tiempo aproximado de 3 horas.
5. El sexto, septimo y octavo items debe ser 0 o 1
6. El noveno item debe ser un integer al entre 1 y 5
7. El decimo item debe ser 'F' o 'M'
8. El undecimo item debe ser un integer entre 0 y 1320’’’

### Respuesta:

```sql
import random
import datetime

def generate_random_time():
    """Genera un tiempo aleatorio entre las 00:00 y las 23:59 en formato TIME SQL"""
    return datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)).strftime('%H:%M:%S')

def generate_data():
    """Genera una tupla aleatoria que cumple con las condiciones dadas"""
    first = random.randint(1, 15)
    second = random.randint(1, 10)
    third = random.randint(1, 5)
    fourth = generate_random_time()
    fifth = generate_random_time()
    while abs(datetime.datetime.strptime(fourth, '%H:%M:%S') - datetime.datetime.strptime(fifth, '%H:%M:%S')).total_seconds() / 3600 < 3:
        # Si la diferencia entre los tiempos generados es menor a 3 horas, se generan nuevos tiempos hasta cumplir la condición
        fourth = generate_random_time()
        fifth = generate_random_time()
    sixth = random.randint(0, 1)
    seventh = random.randint(0, 1)
    eighth = random.randint(0, 1)
    ninth = random.randint(1, 5)
    tenth = random.choice(['F', 'M'])
    eleventh = random.randint(0, 1320)
    return (first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh)

data = [generate_data() for i in range(255)]

# Guardar las tuplas en un archivo de texto
with open('pacientes.txt','w') as f:
    for d in data[:-1]:
        f.write(str(d)+ ',\n')
    f.write(str(data[-1])+';')
```

Los datos de los 255 pacientes se encuentran en el archivo pacientes.txt