import os
from executeCircuitAWS import AWS
from executeCircuitIBM import executeCircuitIBM

# Nombre de la carpeta de salida
CARPETA_SALIDAS = os.path.join("QCRAFT-Scheduler-Machines", "QCRAFT-Scheduler", "salidas")

# Asegurarse de que la carpeta "salidas" exista
os.makedirs(CARPETA_SALIDAS, exist_ok=True)

# Lista de archivos donde guardaremos la información
ARCHIVOS_TXT = [os.path.join(CARPETA_SALIDAS, nombre) for nombre in [
    "maquina_principal.txt",
    "maquinas_tiempo_1.txt",
    "maquinas_tiempo_2.txt",
    "maquinas_tiempo_3.txt",
    "maquinas_MaxPD_1.txt",
    "maquinas_MaxPD_2.txt",
    "maquinas_MaxPD_3.txt",
    "maquinas_MaxML_1.txt",
    "maquinas_MaxML_2.txt",
    "maquinas_MaxML_3.txt",
]]

class GestionarDispositivo:
    def __init__(self):
        self.executeCircuitIBM = executeCircuitIBM()

    def obtener_dispositivos_ibm(self):
        """Obtiene la lista de dispositivos de IBM Quantum."""
        try:
            dispositivos = self.executeCircuitIBM.IBM()
            return dispositivos
        except Exception as e:
            print(f"❌ Error al obtener dispositivos de IBM: {e}")
            return []

    def obtener_dispositivos_aws(self):
        """Obtiene la lista de dispositivos de AWS."""
        try:
            dispositivos = AWS()
            return dispositivos
        except Exception as e:
            print(f"❌ Error al obtener dispositivos de AWS: {e}")
            return []

    def eliminar_archivos_existentes(self):
        """Elimina solo los archivos especificados en ARCHIVOS_TXT si existen."""
        for archivo in ARCHIVOS_TXT:
            if os.path.exists(archivo):
                try:
                    os.remove(archivo)
                    print(f"🗑️ Archivo eliminado: {archivo}")
                except Exception as e:
                    print(f"❌ Error al eliminar archivo {archivo}: {e}")

    def guardar_en_archivos_txt(self, dispositivos):
        """Guarda la lista de dispositivos en cada archivo de ARCHIVOS_TXT."""
        try:
            for archivo in ARCHIVOS_TXT:
                with open(archivo, "w") as f:
                    for dispositivo in dispositivos:
                        f.write(f"{dispositivo}\n")
                print(f"📁 Dispositivos guardados en: {archivo}")
        except Exception as e:
            print(f"❌ Error guardando archivos: {e}")

    def actualizar_dispositivos(self):
        """Actualiza los dispositivos y guarda los resultados."""
        self.eliminar_archivos_existentes()
        dispositivos_aws = self.obtener_dispositivos_aws()
        dispositivos_ibm = self.obtener_dispositivos_ibm()
        todos_los_dispositivos = dispositivos_aws + dispositivos_ibm
        self.guardar_en_archivos_txt(todos_los_dispositivos)

# Ejecutar la actualización
if __name__ == "__main__":
    gestionar = GestionarDispositivo()
    gestionar.actualizar_dispositivos()
