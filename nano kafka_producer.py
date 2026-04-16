import json
import time
import requests
from kafka import KafkaProducer

# Configuración de Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = "trm_data"

# API TRM 
API_URL = "https://www.datos.gov.co/resource/ceyp-9c7c.json"

def get_trm_data():
    print("Consultando API...")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(API_URL, headers=headers)
        print("Status code:", response.status_code)

        if response.status_code != 200:
            print("Error: API no disponible")
            return []

        data = response.json()
        print("Filas obtenidas:", len(data))

        for row in data[:10]:
            try:
                # LIMPIAR VALOR 
                raw_valor = row.get("valor", "0")
                valor_limpio = float(
                    raw_valor.replace("$", "").replace(",", ".")
                )

                #  LIMPIAR FECHA 
                raw_fecha = row.get("vigenciadesde")

                if raw_fecha:
                    fecha_limpia = raw_fecha.split("T")[0]
                else:
                    continue  

                record = {
                    "vigencia": fecha_limpia,
                    "valor": valor_limpio
                }

                print("Enviando:", record)
                yield record

            except Exception as e:
                print("Error procesando fila:", e)

    except Exception as e:
        print("Error general:", e)


if __name__ == "__main__":
    print("Iniciando producer de TRM...\n")

    while True:
        data_found = False

        for trm in get_trm_data():
            data_found = True
            producer.send(TOPIC, value=trm)
            time.sleep(1)  

        if not data_found:
            print("No se obtuvieron datos")

        print("\nEsperando 10 segundos...\n")
        time.sleep(10)