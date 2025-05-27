import matplotlib.pyplot as plt
import re
import os


CARPETA_SALIDAS = os.path.join("QCRAFT-Scheduler-Machines", "QCRAFT-Scheduler", "salidas")


def graficar_qubits(MaxPD_file, MaxML_file, tiempo_file, tiempo_file_no, criterio):
    planificaciones = []
    qubits_alcanzados_MaxPD = []
    qubits_alcanzados_MaxML = []
    qubits_alcanzados_tiempo = []
    qubits_alcanzados_tiempo_no = []
    
    # Leer y procesar el archivo MaxPD_criterio
    with open(MaxPD_file, 'r') as f:
        contenido_MaxPD = f.read()
    matches_MaxPD = re.findall(r"Maquina utilizada: .*?Suma total de qubits alcanzada: (\d+)", contenido_MaxPD, re.DOTALL)
    
    for i, qubits in enumerate(matches_MaxPD):
        qubits_alcanzados_MaxPD.append(int(qubits))
        planificaciones.append(f'Planif {i+1}')

        # Leer y procesar el archivo MaxML_criterio
    with open(MaxML_file, 'r') as f:
        contenido_MaxML = f.read()
    matches_MaxML = re.findall(r"Maquina utilizada: .*?Suma total de qubits alcanzada: (\d+)", contenido_MaxML, re.DOTALL)
    
    for i, qubits in enumerate(matches_MaxML):
        qubits_alcanzados_MaxML.append(int(qubits))
        planificaciones.append(f'Planif {i+1}')
    
    # Leer y procesar el archivo tiempo_criterio
    with open(tiempo_file, 'r') as f:
        contenido_tiempo = f.read()
    matches_tiempo = re.findall(r"Maquina utilizada: .*?Suma total de qubits alcanzada: (\d+)", contenido_tiempo, re.DOTALL)


    for qubits in matches_tiempo:
        qubits_alcanzados_tiempo.append(int(qubits))
    
    with open(tiempo_file_no, 'r') as f:
        contenido_tiempo_no = f.read()  
    matches_tiempo_no = re.findall(r"Maquina utilizada: .*?Suma total de qubits alcanzada: (\d+)", contenido_tiempo_no, re.DOTALL)

    for qubits in matches_tiempo_no:
        qubits_alcanzados_tiempo_no.append(int(qubits))
        
    
    # Ajustar longitud de listas
    min_length = min(len(qubits_alcanzados_MaxPD), len(qubits_alcanzados_tiempo))
    planificaciones = planificaciones[:min_length]
    qubits_alcanzados_MaxPD = qubits_alcanzados_MaxPD[:min_length]
    qubits_alcanzados_MaxML = qubits_alcanzados_MaxML[:min_length]
    qubits_alcanzados_tiempo = qubits_alcanzados_tiempo[:min_length]
    qubits_alcanzados_tiempo_no = qubits_alcanzados_tiempo_no[:min_length]
    
    # Generar la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(planificaciones, qubits_alcanzados_MaxPD, color='b', marker='o', linestyle='-', label='Qubits MaxPD')
    plt.plot(planificaciones, qubits_alcanzados_MaxML, color='m', marker='^', linestyle='-', label='Qubits MaxML')
    plt.plot(planificaciones, qubits_alcanzados_tiempo, color='g', marker='x', linestyle='-', label='Qubits Tiempo')
    plt.plot(planificaciones, qubits_alcanzados_tiempo_no, color='r', marker='s', linestyle='-', label='Qubits Tiempo Normal')
    
    plt.xlabel('Planificaciones')
    plt.ylabel('Qubits Alcanzados')
    plt.title(f'Comparación de Qubits Alcanzados (Criterio {criterio})')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45, ha='right')
    plt.show()

# Ejecutar para los criterios 1, 2 y 3
for criterio in range(1, 4):
    MaxPD_file = f'criterio_{criterio}_MaxPD.txt'
    MaxML_file = f'criterio_{criterio}_MaxML.txt'
    tiempo_file = f'criterio_{criterio}_tiempo.txt'
    tiempo_file_no = f'criterio_tiempo.txt'
    MaxPD_file = os.path.join(CARPETA_SALIDAS, MaxPD_file)
    MaxML_file = os.path.join(CARPETA_SALIDAS, MaxML_file)
    tiempo_file = os.path.join(CARPETA_SALIDAS, tiempo_file)  
    tiempo_file_no = os.path.join(CARPETA_SALIDAS, tiempo_file_no)
    graficar_qubits(MaxPD_file, MaxML_file, tiempo_file, tiempo_file_no, criterio)
