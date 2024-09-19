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

if __name__ == "__main__":
    get_prices()