import aiohttp
import asyncio
import random
url = 'http://localhost:8082/'

pathURL = 'url'
pathResult = 'result'
pathCircuit = 'circuit'


urls = {
    "Combinational-Mapping-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/mapping/20QBT_16CYC_32GN_1.0P2_0_vq.py",
    "Combinational-Mapping-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/mapping/20QBT_4CYC_8GN_1.0P2_0_vq.py",
    "Combinational-Mapping-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/mapping/20QBT_8CYC_16GN_1.0P2_0_vq.py",  
    "Popular-dj-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/Deutsch-Jozsa/Deutsch-Jozsa_qcraft.py",
    "Popular-dj-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/Deutsch-Jozsa/dj_indep_14_mqt.py",
    "Popular-dj-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/Deutsch-Jozsa/dj_indep_4_mqt.py",
    "Popular-dj-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/Deutsch-Jozsa/dj_indep_5_mqt.py",
    "Popular-dj-5": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/Deutsch-Jozsa/dj_indep_7_mqt.py",
    "Popular-adder-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/adder/adder_n10_vq.py",
    "Popular-adder-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/adder/adder_n13_vq.py",
    "Popular-adder-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/adder/adder_n16_vq.py",
    "Popular-adder-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/adder/adder_n4_vq.py",
    "Popular-adder-5": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/adder/adder_n7_vq.py",
    "Popular-adder-6": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/adder/adder_qcraft.py",
    "Popular-bv-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/bernstein-vazirani/bernstein-vazirani_qcraft.py",
    "Popular-bv-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/bernstein-vazirani/bv_14_vq.py",
    "Popular-bv-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/bernstein-vazirani/bv_2_vq.py",
    "Popular-bv-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/bernstein-vazirani/bv_3_vq.py",
    "Popular-bv-5": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/bernstein-vazirani/bv_4_vq.py",
    "Popular-bv-6": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/bernstein-vazirani/bv_5_vq.py",
    "Popular-bv-7": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/bernstein-vazirani/bv_9_vq.py",
    "Popular-grover-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover-noancilla_3_mqt.py",
    "Popular-grover-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover-noancilla_4_mqt.py",
    "Popular-grover-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover-v-chain_3_mqt.py",
    "Popular-grover-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover-v-chain_4_mqt.py",
    "Popular-grover-5": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover_3_vq.py",
    "Popular-grover-6": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover_7_vq.py",
    "Popular-grover-7": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover_9_vq.py",
    "Popular-grover-8": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/grover/grover_qcraft.py",
    "Popular-kickback-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/kickback/kickback_7_vq.py",
    "Popular-kickback-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/kickback/kickback_qcraft.py",
    "Popular-pe-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_2_vq.py",
    "Popular-pe-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_3_mqt.py",
    "Popular-pe-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_4_mqt.py",
    "Popular-pe-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_5_mqt.py",
    "Popular-pe-5": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_5_vq.py",
    "Popular-pe-6": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_6_mqt.py",
    "Popular-pe-7": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_6_vq.py",
    "Popular-pe-8": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/pe_7_mqt.py",
    "Popular-pe-9": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/phase_estimation/phase_estimation_qcraft.py",
    "Popular-qft-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/qft/qft_2_mqt.py",
    "Popular-qft-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/qft/qft_3_mqt.py",
    "Popular-qft-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/qft/qft_3_vq.py",
    "Popular-qft-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/qft/qft_4_mqt.py",
    "Popular-qft-5": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/qft/qft_6_mqt.py",
    "Popular-qft-6": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/qft/qft_7_vq.py",
    "Popular-qft-7": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/qft/qft_qcraft.py",
    "Popular-shor-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/shor/shor_mod15_mqt.py",
    "Popular-shor-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/shor/shor_mod21_mqt.py",
    "Popular-shor-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/shor/shor_qcraft.py",
    "Popular-simon-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/simon/simon_qcraft.py",
    "Popular-simon-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/simon/simon_vq.py",
    "Popular-tsp-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/tsp/tsp_indep_4_mqt.py",
    "Popular-tsp-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/tsp/tsp_indep_5_mqt.py",
    "Popular-tsp-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/popularalgorithms/tsp/tsp_qcraft.py",
    "Reversible-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/reversible/3_17tc_vq.py",
    "Reversible-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/reversible/6symd2_vq.py",
    "Reversible-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//combinational/reversible/reversible_5_adder_vq.py",
    "qwalk-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//sequential/qwalk/qwalk-noancilla_3_mqt.py",
    "qwalk-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//sequential/qwalk/qwalk-v-chain_3_mqt.py",
    "qwalk-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//sequential/qwalk/qwalk-v-chain_5_mqt.py",
    "qwalk-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//sequential/qwalk/qwalk_qcraft.py",
    "efficient-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/EfficientSU2/su2_5_vq.py",
    "efficient-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/EfficientSU2/su2random_3_mqt.py",
    "efficient-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/EfficientSU2/su2random_4_mqt.py",
    "qaoa-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/qaoa/qaoa_6_vq.py",
    "qaoa-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/qaoa/qaoa_indep_3_mqt.py",
    "qaoa-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/qaoa/qaoa_indep_4_mqt.py",
    "qaoa-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/qaoa/qaoa_indep_5_mqt.py",
    "qaoa-5": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/qaoa/qaoa_indep_6_mqt.py",
    "qaoa-6": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/qaoa/qaoa_qcraft.py",
    "vqe-1": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/vqe/vqe_indep_3_mqt.py",
    "vqe-2": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/vqe/vqe_indep_4_mqt.py",
    "vqe-3": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/vqe/vqe_indep_5_mqt.py",
    "vqe-4": "https://raw.githubusercontent.com/Qcraft-UEx/QCRAFT-Scheduler/main/circuits-code//variational/vqe/vqe_indep_6_mqt.py",
#   la composicion 4 es desde Reversible-3 hasta vqe-4 sin las dynamic. La composicion 5 es de todos los dynamic
}

# criterios = [1, 2, 3]  # Lista con los tres criterios

# async def post_request(session, url, data):
#     async with session.post(url, json=data) as response:
#         return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for criterio in criterios:  # Iteramos sobre los tres criterios
#             for name, url_value in urls.items():
#                 data = {
#                     "url": url_value,
#                     "shots": 10000,
#                     "provider": ['ibm'],
#                     "policy": "fran", # time, shots, depth y fran
#                     "criterio": criterio  # Agregamos el criterio
#                 }
#                 print(f"Enviando petición con datos: {data}")
#                 task = post_request(session, url + pathCircuit, data)
#                 tasks.append(task)

#         responses = await asyncio.gather(*tasks)
#         for response in responses:
#             print(response)

# asyncio.run(main())

#A PARTIR DE AQUI ESTA BIEN


# # Lista de circuitos disponibles
# urls_list = list(urls.values())

# # Generar 2000 URLs aleatorias
# num_urls = 2000
# random_urls = [random.choice(urls_list) for _ in range(num_urls)]

# # Políticas y criterios
# policies = ["fran", "time"]
# criterios = [1, 2, 3]

# async def post_request(session, url, data):
#     async with session.post(url, json=data) as response:
#         return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for policy in policies:
#             for criterio in criterios:
#                 for url_value in random_urls:
#                     data = {
#                         "url": url_value,
#                         "shots": 10000,
#                         "provider": ['ibm'],
#                         "policy": policy,
#                         "criterio": criterio
#                     }
#                     print(f"Enviando petición con datos: {data}")
#                     task = post_request(session, url + pathCircuit, data)
#                     tasks.append(task)

#         responses = await asyncio.gather(*tasks)
#         for response in responses:
#             print(response)

# asyncio.run(main())


#PRUEBAS
# # Lista de circuitos disponibles
# urls_list = list(urls.values())

# # Generar 2000 URLs aleatorias
# num_urls = 2000
# random_urls = [random.choice(urls_list) for _ in range(num_urls)]

# # Políticas y criterios
# policies = ["fran", "time"]
# criterios = [1, 2, 3]

# async def post_request(session, url, data):
#     async with session.post(url, json=data) as response:
#         return await response.text()

# async def send_requests_for_policy(session, policy):
#     tasks = []
#     for criterio in criterios:
#         for url_value in random_urls:
#             data = {
#                 "url": url_value,
#                 "shots": 10000,
#                 "provider": ['ibm'],
#                 "policy": policy,
#                 "criterio": criterio
#             }
#             print(f"Enviando petición con datos: {data}")
#             task = post_request(session, url_value + pathCircuit, data)
#             tasks.append(task)
    
#     responses = await asyncio.gather(*tasks)
#     for response in responses:
#         print(response)

# async def main():
#     async with aiohttp.ClientSession() as session:
#         policy_tasks = [asyncio.create_task(send_requests_for_policy(session, policy)) for policy in policies]
#         await asyncio.gather(*policy_tasks)

# asyncio.run(main())


# Lista de circuitos disponibles
urls_list = list(urls.values())

# Generar 2000 URLs aleatorias
num_urls = 2000
random_urls = [random.choice(urls_list) for _ in range(num_urls)]

# Políticas y criterios
policies = ["MaxML", "MaxPD", "time_maquinas"]
criterios = [1, 2, 3]
acum=0

async def post_request(session, url, data):
    async with session.post(url, json=data) as response:
        return await response.text()

async def main():
    global acum
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url_value in random_urls:
            time_policy_data = {
                "url": url_value,
                "shots": 10000,
                "provider": ['ibm'],
                "policy": "time",
                "criterio": 0
            }
            print(f"Enviando petición con datos: {time_policy_data}")
            acum += 1
            print(f"ACUMMMM: {acum}")
            task = post_request(session, url + pathCircuit, time_policy_data)
            tasks.append(task)
            for criterio in criterios:
                for policy in policies:
                    data = {
                        "url": url_value,
                        "shots": 10000,
                        "provider": ['ibm'],
                        "policy": policy,
                        "criterio": criterio
                    }
                    print(f"Enviando petición con datos: {data}")

                    acum += 1
                    print(f"ACUMMMM: {acum}")

                    task = post_request(session, url + pathCircuit, data)
                    tasks.append(task)
                    

        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)
            
asyncio.run(main())

