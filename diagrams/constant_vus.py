from diagrams import Diagram, Cluster
from diagrams.onprem.client import User 
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.custom import Custom

with Diagram("Constant Vus Diagrams", show = True):
    rutaImg = "../img/iteracion.png"
    load_balancer = Custom("Constant vus", "../img/images.png")

    with Cluster("Usuarios virtuales", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        v1 = User("VU 1")
        v2 = User("VU 2")
        v3 = User("VU 3")
        v4 = User("VU 4")
        v5 = User("VU 5")

    with Cluster("Tiempo", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        time = Custom("Rango de tiempo", "../img/time.jpg")

    load_balancer >> time
    time >> v1
    time >> v2
    time >> v3
    time >> v4
    time >> v5