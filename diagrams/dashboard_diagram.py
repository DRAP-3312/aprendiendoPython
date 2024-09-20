from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.custom import Custom
from diagrams.aws.general import SslPadlock
from diagrams.oci.governance import Audit
from diagrams.c4 import Relationship, Container
from diagrams.onprem.ci import CircleCI

with Diagram("Proceso Ingreso a dashboard", show=True, graph_attr={"bgcolor": "White"}):

    procesoAnterior = Custom("Procesos anteriores", "../img/iteracion.png")
    endpoid = CircleCI("endPoint")
    cerbos = SslPadlock("Servicio cerbos")
    busca = Custom("Busca stats", "../img/validacion.png")
    resultados = Audit("Resultados")
    error = Custom("No autorizado", "../img/error.png")

    procesoAnterior >> Relationship("Ingreso a virture") >> endpoid
    endpoid << Relationship("Verifica autorizacion") >> cerbos
    endpoid >> Relationship("true") >> busca >> resultados
    endpoid >> Relationship("false") >> error