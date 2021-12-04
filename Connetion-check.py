import requests, time

url = """https://www.google.com/"""
while True:
    try:
        print("Prueba de conexion")
        start = time.time()
        test = requests.get(url)
        end = time.time()
        ping = end - start
        print("Conexion exitosa con un ping = " + str(ping))
        pause = input()
        break
    except requests.exceptions.ConnectionError:
        print("No hay conexión a internet, siguiente prueba en 60s\n")
        time.sleep(60)
