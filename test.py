import socket

def is_connected(host="8.8.8.8", port=53, timeout=3):
    """
    Retorna True si hay conexión a Internet, usando un intento de conexión con DNS de Google.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False
    
# -- 1. Borrar todos los registros+
# DELETE FROM public.reports_drowsinessreport;

# -- 2. Reiniciar el contador de ID (secuencia)
# ALTER SEQUENCE public.reports_drowsinessreport_id_seq RESTART WITH 1;