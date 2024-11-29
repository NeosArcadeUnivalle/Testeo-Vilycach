# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página
class URLManager:
    BASE_URL = 'http://127.0.0.1:8000'
    CATALOGO = f"{BASE_URL}/catalogo"
    COMPRA = f"{BASE_URL}/ventas/create"
    LOGIN = f"{BASE_URL}/empleado/login"