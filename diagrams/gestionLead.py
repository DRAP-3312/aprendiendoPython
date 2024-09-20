from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.custom import Custom
from diagrams.aws.general import SslPadlock
from diagrams.oci.governance import Audit
from diagrams.c4 import Relationship
from diagrams.aws.general import SDK
from diagrams.onprem.ci import CircleCI

with Diagram("Proceso Ingreso Gestion leads", show=True, graph_attr={"bgcolor": "White"}):

    leadTracking = CircleCI("get lead traking")
    phase = CircleCI("get Phase")
    user = CircleCI("get User")
    lead = CircleCI("get lead")

    verificacion = Custom("Verficacion", "../img/validacion.png")
    cerbos = SslPadlock("Servicio cerbos")
    notFound = Custom("Excepcion Not found", "../img/error.png")
    formatInvalid = Custom("Formato invalido", "../img/error.png")
    noAuth = Custom("No autorizado", "../img/error.png")
    buscar_datos = Custom("Buscar", "../img/iteracion.png")
    datos = Audit("Datos")

    leadTracking >> verificacion >> Relationship("formato mal") >> formatInvalid
    verificacion >> buscar_datos >> Relationship("Datos encontrados") >> datos
    buscar_datos >> Relationship("datos no encontrados") >> notFound
    phase >> buscar_datos
    user << Relationship("Verifica autorización") >> cerbos
    user >> Relationship("true") >> buscar_datos
    user >> Relationship("false") >> noAuth
    lead >> Relationship("true") >> verificacion
    lead >> Relationship("false") >> noAuth
    lead >> Relationship("Verifica autorización") << cerbos
