from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.custom import Custom

# Ruta a una imagen personalizada para Firebase (puedes usar cualquier imagen o dejarla como texto)
rutaImgFirebase = "./img/firebase.png"  # Usa una imagen de Firebase si tienes, si no, se puede cambiar por texto
rutaImgToken = "./img/token.png"  # También puedes poner una imagen para el token, o dejarla como texto

with Diagram("Proceso de Autenticación con Firebase", show=True, graph_attr={"bgcolor": "transparent"}):
    # Usuario inicia sesión
    user = User("Usuario")

    # Paso 1: Firebase recibe la solicitud de autenticación (nodo personalizado)
    firebase = Custom("Firebase", rutaImgFirebase)  # Cambia la imagen si la tienes o usa un texto personalizado

    # Paso 2: Firebase responde con un token
    token = Custom("Token JWT", rutaImgToken)

    # Paso 3: El sistema valida el token
    with Cluster("Validación de Token", graph_attr={"bgcolor": "transparent"}):
        valid_token = Custom("Token Válido", rutaImgToken)
        invalid_token = Custom("Token Inválido", rutaImgToken)

    # Paso 4: Acceso permitido o denegado
    authorized = Custom("Acceso Autorizado", rutaImgToken)
    unauthorized = Custom("Acceso Denegado", rutaImgToken)

    # Conexiones entre los componentes
    user >> firebase >> token
    token >> valid_token >> authorized
    token >> invalid_token >> unauthorized
