from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.custom import Custom
from diagrams.aws.general import SslPadlock
from diagrams.oci.governance import Audit
from diagrams.c4 import Relationship
from diagrams.onprem.ci import CircleCI
from diagrams.aws.general import SDK

with Diagram("Proceso Ingreso a dashboard", show=True, graph_attr={"bgcolor": "White"}):

    while Cluster("Parametros", graph_attr={"bgcolor": "transparent"}):
        user_roles = SDK("User roles")
        user_identifier = SDK("user identifier")
        permissions = SDK("special permissions")
        workspace = SDK("id workspace")
        role = SDK("role")

    endpoind = CircleCI("Cargar asesores")
    cerbos = SslPadlock("Servicio cerbos")

    user_roles >> endpoind
    