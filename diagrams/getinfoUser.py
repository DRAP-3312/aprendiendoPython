from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.custom import Custom
from diagrams.onprem.ci import CircleCI
from diagrams.c4 import Relationship
from diagrams.oci.governance import Audit

with Diagram("Obtener los datos del usuario", show=True, graph_attr={"bgcolor": "White"}):

    with Cluster('Proceso de validacion token', graph_attr={"bgcolor": "transparent"}):
        firebase = Custom("Firebase", "../img/firebase.png")
        cliente = User('User')
    
    endpoint2 = CircleCI('endpoint')
    busca = Custom("Busca el usuario", "../img/validacion.png")
    resultados = Audit('Resultados')

    firebase >> Relationship("Token generado") >> cliente >> Relationship("Manda email") >> endpoint2
    endpoint2 >> busca >> Relationship("Retorna los resultados si encontro") >> resultados