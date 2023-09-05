'''import random
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

print("Tuplas generadas y guardadas en 'turnos.txt'.")'''


# Codigo para generar pacientes
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