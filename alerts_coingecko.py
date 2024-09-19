import requests # Librería solicitudes HTTP

# URL de la API de CoinGecko y parámetos para el consumo de la API CoinGecko 
url = "https://api.coingecko.com/api/v3/simple/price"

PARAMS = {
    'ids': 'bitcoin,ethereum,binancecoin',
    'vs_currencies': 'usd'
}

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

        alert_msg = ""

        bitcoin_price  = prices.get('bitcoin', {}).get('usd')
        ethereum_price = prices.get('ethereum', {}).get('usd')
        binancecoin_price = prices.get('binancecoin', {}).get('usd')
        
        # Validación del los datos
        if bitcoin_price and bitcoin_price > 63000:
            alert_msg += f" Bitcoin ha superado los $30,000 USD, su precio actual es: ${bitcoin_price}\n"

        if ethereum_price and ethereum_price > 2000:
            alert_msg += f" Ethereum ha superado los $2,0000 USD, su precio actual es: ${ethereum_price}\n"

        if binancecoin_price and binancecoin_price > 500:
            alert_msg += f" Binancecoin ha superado los $3000 USD, su precio actual es: ${binancecoin_price}\n"
    
    print(alert_msg)

if __name__ == "__main__":
    value_prices()