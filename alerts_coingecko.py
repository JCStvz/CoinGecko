import requests # Librería solicitudes HTTP
from twilio.rest import Client # Se importa la clase Client desde la librería de Twilio
import time

# URL de la API de CoinGecko y parámetos para el consumo de la API CoinGecko 
url = "https://api.coingecko.com/api/v3/simple/price"

PARAMS = {
    'ids': 'bitcoin,ethereum,binancecoin',
    'vs_currencies': 'usd'
}

# Reqisitos para utilizar Twilio 
account_sid = 'Inserta tu account_sid de Twilio' # Credencial que actúa como nombre de usuario
auth_token = 'Inserta tu auth_token' # Identificador único de la cuenta de Twilio
num_from = 'whatsapp:+14155238886' # Número de WhatsApp de Twilio
num_to = 'whatsapp:+573204693533'  # Número de WhatsApp destino

# Se almacena los precios de validación para cada criptomoneda
coll_crypto = {
    'bitcoin': 30000,
    'ethereum': 2000,
    'binancecoin':300
}

# Precios anteriores
prices_ant = {}

# Funcion que realiza la solicitud GET a la API
def get_prices(): 
    try:
        getdata = requests.get(url, params=PARAMS)
        if getdata.status_code == 200:
            data = getdata.json() 
            print(data)
            return data
        else:
            print("Error al obtener los los precios. Código de estado:", getdata.status_code)
            return None
    except Exception as e:
            print("Error durante la solicitud a la API:", e)
            return None

def value_prices():

    # Se obtiene el JSON con los datos 
    prices = get_prices()
    
    # Se continua con el proceso si la funcion retorna datos validos
    if prices:

        bitcoin_price  = prices.get('bitcoin', {}).get('usd')
        ethereum_price = prices.get('ethereum', {}).get('usd')
        binancecoin_price = prices.get('binancecoin', {}).get('usd')
        
        # Validación del los datos, se recorre cada valor
        for crypto,valuecrypto in coll_crypto.items():
            current_price = prices.get(crypto, {}).get('usd') #Se obtiene el precio actual
            if current_price and current_price > valuecrypto: # Se condiciona los datos para el envio de alerta
                alert_msg += f"⚠️ {crypto.capitalize()} ha superado los: ${valuecrypto:,} USD, su Precio actual: ${current_price:,} USD.\n"

    print(alert_msg)
    return alert_msg

# Función para enviar la alerta por WhatsApp 
def send_alert(alert_msg):

    if alert_msg:
        # Se inicia la cuenta de Twilio con la credenciales
        client = Client(account_sid, auth_token)

        # Se realiza el envio de la notificación 
        message = client.messages.create(
        from_=num_from, # Número de WhatsApp de Twilio
        body=alert_msg,
        to=num_to # Número de WhatsApp destino
        )
        print(message.sid)

def main():
    while True:
        alert_msg = value_prices() 
        send_alert(alert_msg)
        time.sleep(10)

if __name__ == "__main__":
    main()