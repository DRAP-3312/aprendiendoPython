from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.security import IdentityAndAccessManagementIamAddOn
from diagrams.custom import Custom

# Ruta a las imágenes personalizadas
rutaImgFirebase = "../img/firebase.png"
rutaImgAutorizado = "../img/autorizado.png"
rutaImgNoAutorizado = "../img/noautorizado.jpg"
rutaImgTokenOk = "../img/llaveOk.jpg"

with Diagram("Proceso de Autenticación y Verificación de Token", show=True, graph_attr={"bgcolor": "White"}):
    user = User("Inicio sesión")
    firebase = Custom("Firebase", rutaImgFirebase)

    token = Custom("Token JWT", rutaImgTokenOk)

    with Cluster("Proceso de Verificación del Token", graph_attr={"bgcolor": "transparent"}):
        token_split = Custom("Bearer Token Split", rutaImgTokenOk)

        with Cluster("Validación por Firebase", graph_attr={"bgcolor": "transparent"}):
            valid_token = Custom("Token Válido", rutaImgTokenOk)
            invalid_token = IdentityAndAccessManagementIamAddOn("Token Inválido")

    authorized = Custom("Acceso Autorizado", rutaImgAutorizado)
    unauthorized = Custom("Acceso Denegado", rutaImgNoAutorizado)

    user >> firebase
    firebase >> user
    user >> token >> token_split
    token_split >> valid_token >> authorized
    token_split >> invalid_token >> unauthorized