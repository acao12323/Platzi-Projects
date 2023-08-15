# Proyecto de curso de Tableau

Tabla de contenido

# Caracterización de la población atendida y medición de indicadores de la atención médica en una IPS de primer nivel en 2023.

## Introducción

Hoy terminé el curso de Platzi sobre Tableau, como parte de mi proceso de formación como Data Analyst. La base de datos con la que trabajamos fue sobre las muertes en Game of Thrones. Sin embarco como el objetivo de mi desarrollo profesional es aplicar estos conocimientos en el área de la salud, uní estos conocimientos con los adquiridos en el manejo de base de datos relacionales y utilicé una base de datos de pacientes ficticios de urgencias para crear el siguiente storytelling con los resultados obtenidos.

## Resumen

El objetivo de esta base de datos es recopilar datos sobre los pacientes atendidos en el servicio de urgencias de una Institución Prestdora de Salud (IPS) de primer nivel para categorizar el tipo de población que se atiende, las patologías más comunes, el porcentaje de remisión de los pacientes, el tiempo de estancia en la institución y tratar de medir el desempeño por médico. Para ello se usó un análisis de datos falsos y se uso Tableau public para crear graficas y dashboards para realizar un análisis de los mismos encontrando que en promedio se atienden 3.3 pacientes por turno y 83 pacientes al mes, los principales  dignósticos son psiquatrícos y que el 21.8% de los pacientes que ingresan a la institución fallecen. Estos resultados poco alejados de la realidad se debe al origen aleatorio en la generación de los datos.

## Metodología

### Preparación de los datos

Para realizar este proyecto se creó una base de datos relacional en PostgreSQL llamada db_turnos que se organizaba de la siguiente manera:

![Imagen 1. Diagrama entidad-relacion de db_turnos.](Proyecto%20de%20curso%20de%20Tableau%20c778c241e0a74c349e775a96c6c1aa81/DiagramaER_db_turnos.png)

Imagen 1. Diagrama entidad-relacion de db_turnos.

Con el objetivo de seguir las normas de las buena practicas clínicas y como el objetivo de este proyecto es practicar los conocimientos aprendidos se usaron datos falsos usando ChatGPT 3.5 para crear un script en python que generara datos aleatorios siguiendo una serie de condiciones y de esta manera evitar vulnerar la privacidad de los pacientes.

### Promts y codigo generado

**********************************Promt de la tabla turnos**********************************

Actua como un experto programador en python y crea una script en python que genere una lista de 300 tuplas con la siguien forma:

INSERT INTO public.turnos(
turno_id, medico_id, nombre, hora_inicio, hora_final, fecha, n_pacientes)
VALUES (?, ?, ?, ?, ?, ?, ?);

Teniendo en cuenta las siquientes condiciones:

1. turno_id es la primary key
2. medico_id es un integer aletorio entre 1 y 10
3. nombre sigue la secuencia: mañana8h, tarde8h, noche8h, dia12h, noche12h.
4. hora_inicio y hora_final deben ser respectivamente 06:00 y 14:00 cuando nombre es mañana8h, 14:00 y 22:00 cuando nombre es tarde8h, 22:00 y 06:00 cuando nombre es noche8h, 07:00 y 19:00 cuando nombre es dia12h y 19:00 y 07:00 cuando nombre es noche12h en formato '**hh:mm:ss.nnnnnn**'.
5. fecha debe iniciar el 01/01/2023 en formato DATE de postgresql e ir aumentando hasta 31/12/2023.
6. n_pacientes puede ser cualquier integer entre 5 y 30

Guarda el resultado en un archivo turnos.txt.

```python
import random
from datetime import datetime, timedelta

def generate_time_range(nombre):
    if nombre == 'mañana8h':
        return '06:00:00.000000', '14:00:00.000000'
    elif nombre == 'tarde8h':
        return '14:00:00.000000', '22:00:00.000000'
    elif nombre == 'noche8h':
        return '22:00:00.000000', '06:00:00.000000'
    elif nombre == 'dia12h':
        return '07:00:00.000000', '19:00:00.000000'
    elif nombre == 'noche12h':
        return '19:00:00.000000', '07:00:00.000000'

def generate_insert_statement(turno_id, medico_id, nombre, hora_inicio, hora_final, fecha, n_pacientes):
    return f"INSERT INTO public.turnos(turno_id, medico_id, nombre, hora_inicio, hora_final, fecha, n_pacientes) VALUES ({turno_id}, {medico_id}, '{nombre}', '{hora_inicio}', '{hora_final}', '{fecha}', {n_pacientes});\n"

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
days_range = (end_date - start_date).days

with open('turnos.txt', 'w') as file:
    for turno_id in range(1, 301):
        medico_id = random.randint(1, 10)
        nombre_options = ['mañana8h', 'tarde8h', 'noche8h', 'dia12h', 'noche12h']
        nombre = random.choice(nombre_options)
        hora_inicio, hora_final = generate_time_range(nombre)
        fecha = (start_date + timedelta(days=random.randint(0, days_range))).date()
        n_pacientes = random.randint(5, 30)
        
        insert_statement = generate_insert_statement(turno_id, medico_id, nombre, hora_inicio, hora_final, fecha, n_pacientes)
        file.write(insert_statement)

print("Tuplas generadas y guardadas en 'turnos.txt'.")
```

Prompt **de la tabla pacientes**

Actua como un programador experto y crea un script en python que genere un lista de 1000 tuplas con la siguiente forma:

INSERT INTO public.pacientes(
paciente_id, turno_id, dx_id, salida_id, hora_ingreso, hora_egreso, laboratorios, imagenes, interconsulta, edad, sexo, triage)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

Teniendo en cuenta las siquientes condiciones:

1. paciente_id es la primary key
2. turno_id es un integer entre 1 y 300
3. dx_id es un integer entre 1 y 10
4. salida_id es un integer entre 1 y 5
5. hora_ingreso y hora_egreso deben ser horas aleatorias en formato '**hh:mm:ss.nnnnnn**' donde hora_egreso sea mayor que hora_ingreso.
6. laboratorios, imágenes e interconsulta son booleanos de postgresql
7. edad debe ser un integer aleatorio entre 1 y 102
8. sexo debe ser un booleano
9. triage es un integer entre 1 y 5

Guarda el resultado en un archivo ‘pacientes.txt’

```python
import random
from datetime import datetime, timedelta

def generate_time():
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    microseconds = random.randint(0, 999999)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{microseconds:06d}"

with open('pacientes.txt', 'w') as file:
    for paciente_id in range(1, 1001):
        turno_id = random.randint(1, 300)
        dx_id = random.randint(1, 10)
        salida_id = random.randint(1, 5)
        
        hora_ingreso = generate_time()
        hora_egreso = generate_time()
        
        # Ensure hora_egreso is greater than hora_ingreso
        while hora_egreso <= hora_ingreso:
            hora_egreso = generate_time()
        
        laboratorios = random.choice([True, False])
        imagenes = random.choice([True, False])
        interconsulta = random.choice([True, False])
        
        edad = random.randint(1, 102)
        sexo = random.choice(['F','M'])
        triage = random.randint(1, 5)
        
        insert_statement = f"INSERT INTO public.pacientes(paciente_id, turno_id, dx_id, salida_id, hora_ingreso, hora_egreso, laboratorios, imagenes, interconsulta, edad, sexo, triage) VALUES ({paciente_id}, {turno_id}, {dx_id}, {salida_id}, '{hora_ingreso}', '{hora_egreso}', {laboratorios}, {imagenes}, {interconsulta}, {edad}, '{sexo}', {triage});\n"
        file.write(insert_statement)

print("Tuplas generadas y guardadas en 'pacientes.txt'.")
```

Una vez generados los datos se realizó un JOIN de las tablas pacientes, turnos, diagnósticos y salidas, obteniendo la tabla pacientes_limpia, la cual se descargó en formato csv, lo que permitió realizar el análisis y las gráficas en Tableau public.

```sql
WITH pacientes_limpia AS(SELECT
	p.paciente_id AS paciente,
	t.nombre AS turno,
	d.tipo_dx AS diagnostico,
	s.tipo_salida AS salida,
	EXTRACT(HOUR FROM (p.hora_egreso - p.hora_ingreso)) AS estancia,
	p.laboratorios,
	p.imagenes,
	p.interconsulta,
	p.edad,
	p.sexo,
	p.triage,
	m.nombre AS medico,
	t.fecha
					   
	FROM pacientes p
	JOIN turnos t
		ON p.turno_id = t.turno_id
	JOIN medicos m
		ON m.medico_id = t.medico_id
	JOIN diagnosticos d
		ON p.dx_id = d.dx_id
	JOIN salidas s
		ON p.salida_id = s.salida_id
)

SELECT * FROM pacientes_limpia;
```

```sql
WITH turnos_limpia AS(SELECT
	t.nombre AS turno,
	m.nombre AS medico,
	m.sexo,
	m.años_experiencia AS experiencia,
	m.años_institucion AS vinculacion,
	m.educacion,
	t.fecha,
	t.n_pacientes

FROM turnos t
JOIN medicos m
	ON t.medico_id = m.medico_id
)

SELECT * FROM turnos_limpia;
```

### Análisis exploratorio de datos

Se obtuvo la tabla pacientes_limpia que contenía la información de 1000 pacientes atendidos durante el 2023 a lo largo de 300 turnos en la IPS.

Tabla1. Columnas y descripción de la tabla pacientes.

| Columna | Tipo de dato | Descripción |
| --- | --- | --- |
| paciente | integer | Identifica a cada paciente |
| turno | string | Identifica el tipo de turno |
| diagnostico | string | Identifica el tipo de diagnostico |
| salida | string | Identifica el tipo de salida |
| estancia | integer | Corresponde a las horas que duro en la institución |
| laboratorios | boolean | True significa que si se le realizaron laboratorios, False que no |
| imagenes | boolean | True significa que si se le realizaron imagenes, False que no |
| interconsulta | boolean | True significa que si se le solicito interconsulta, False que no |
| edad | integer | Define la edad del paciente |
| sexo | boolean | F femenino, M masculino |
| triage | integer | Clasifica el triage que tuvo al ingreso entre 1 y 5 |
| medico | string | Identifica el medico que atendió al paciente |
| fecha | date | Identifica la fecha de atención |

La tabla turnos contenía la información resumida de cada turno e identifica al médico que lo realizó.

La tabla fue cargada a Tableau Public donde se planteo responder las siguientes preguntas:

1. ¿Cuántos pacientes se atienden por turno, cuantos por mes?
2. ¿En qué horario llegan más pacientes?
3. ¿Qué tipo de patología es la más común en la institución?
4. ¿A qué porcentaje de pacientes se les solicita paraclínicos?
5. ¿Qué porcentaje de pacientes se remite?
6. ¿Qué porcentaje de pacientes fallece?
7. ¿Existe diferencia de estas medidas por sexo o por edad?

Para ello se realizaron tarjetas para calcular el numero de pacientes, el promedio de edad, el tiempo promedio de estancia, la mediana de triage de los pacientes al ingreso y la mortalidad de los mismos.

Así mismo se creo una grafica de línea que media el número de pacientes atendidos por mes, una gráfica de árbol que mostraba la distribución de los tipos de diagnóstico, graficas de barra que mostraban el tipo de salida del paciente y graficas de pie que mostraban la proporción en cuanto al sexo, el horario en que llegaban los pacientes y el uso de paraclínicos.

Con lo anterior se generó el siguiente dashboard:

[Imagen 2. Dashboard de caracterización de pacientes atendidos en 2023 en una IPS de primer nivel. (Datos falsos)](https://public.tableau.com/shared/3JPXK9GWT?:display_count=n&:origin=viz_share_link)

Imagen 2. Dashboard de caracterización de pacientes atendidos en 2023 en una IPS de primer nivel. (Datos falsos)

### Resultados

Dado la naturaleza ficticia de los datos se obtuvieron resultados poco coherentes con la realidad que se vive diariamente en un servicio de urgencias de primer nivel. Ejemplo de ello es que el promedio de pacientes por turno es de 3.3 pacientes y el promedio por mes de 83 pacientes.

A su vez por la naturaleza de la librería `random` de python la relación en cuanto a sexo, laboratorio, imágenes, interconsultas se mantiene cercano a 1:1. El promedio de edad, tiempo de estancia en la institución, horario en el que se acude a la misma también es bastante cercano, Lo que le resta interés a los hallazgos.

Sin embargo se puede apreciar que el numero de pacientes que se atienden en la institución tiende al aumento, El mes mas concurrido fue agosto, el cual fue también donde más fallecidos hubo, tendencia que se mantiene prácticamente estable a lo largo del año. 

El grupo de patologías más comunes en la institución son las psiquiátricas, dato que cambia por sexo ya que en mujeres son más comunes las patologías gastrointestinales.

En la institución se remite el 21.6% de los pacientes. Los meses en que más remisiones se hicieron fueron agosto y octubre, ambas con 26 pacientes lo que se aleja bastante del promedio de 16 remisiones mensuales y es un campo que sigue una tendencia al aumento. siendo las patologías neurológicas el principal motivo en general y en hombres. En mujeres el principal motivo de remisión son las patologías ginecológicas *(mera casualidad, ya que al generar los datos olvidé definir que los hombres no tuvieran patologías ginecológicas por lo que sí, en esta base de datos hay masculinos con diagnósticos ginecológicos)*.

De los datos más chistosos encontramos la mortalidad de la institución, que alcanza un 21.8% general, siendo un poco mayor en hombres que en mujeres (23% y 20.5% respectivamente). El principal tipo de diagnóstico relacionado con la muerte de los pacientes son los ginecológicos, dato que se mantiene en los hombres (LOL) pero cambia en las mujeres, ya que estas fallecen principalmente por causas gastrointestinales. 

## Conclusiones

El objetivo de este proyecto era practicar las habilidades obtenidas sobre la creación y manipulación de datos en una base de datos relacional, la limpieza y manipulación de los mismos en un entorno como Tableau para generar visualización de datos que puedan generar resultados valiosos de cara a los objetivos de una empresa y que sirvan como pilares a la hora de tomar decisiones en la misma. Por lo que considero que un análisis de este tipo podría ser fácilmente realizado en las instituciones de primer nivel del país que cuenten con historias clínicas digitalizadas, ya que los datos que aquí se analizan no comprometen la privacidad de ningún paciente y pueden ser fácilmente obtenidos de cualquier software de gestión de historias clínicas y procedimientos. Así mismo esta idea se puede ampliar para albergar en el análisis datos sobre las ganancias de la institución, los gastos de insumos, así como generar modelos predictivos sobre el comportamiento de los pacientes y sus patologías.

<aside>
<img src="https://www.notion.so/icons/card_gray.svg" alt="https://www.notion.so/icons/card_gray.svg" width="40px" /> Realizado por: Andrés Camilo Atencia Ortega, MD
e-mail: acao12323@gmail.com
LinkedIn: [LinkedIn](http://www.linkedin.com/in/andr%C3%A9s-camilo-atencia-ortega-5a79691b3)
Twitter: [@acatencia](https://twitter.com/acatencia)

</aside>