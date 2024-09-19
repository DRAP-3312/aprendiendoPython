from diagrams import Diagram, Cluster
from diagrams.onprem.client import User 
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.custom import Custom

# Crear el diagrama
with Diagram("Per-VU Iterations Diagram", show=True):
    # graph_attr={"style": "dashed", "bgcolor": "transparent", "fontcolor": "black,", "fontname" : "Arial Bold", "fontsize": "20"}
    rutaImg = "../img/iteracion.png"
    styleaNodeattr = {"fontcolor": "green", "fontsize": "14", "fontname": "Arial Bold"}
    load_balancer = Custom("Per VU iterations", "../img/images.png")

    with Cluster("Usuarios virtuales (VUs)", graph_attr= {"style": "dashed", "bgcolor": "transparent"} ):
        vu1 = User("VU 1")
        vu2 = User("VU 2")

    with Cluster("Iteraciones por VU", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        iterations_vu1 = [Custom("Iteration 1", rutaImg), Custom("Iteration 2", rutaImg), Custom("Iteration 3", rutaImg)]
        iterations_vu2 = [Custom("Iteration 1", rutaImg), Custom("Iteration 2", rutaImg), Custom("Iteration 3", rutaImg)]

    load_balancer >> vu1 >> iterations_vu1
    load_balancer >> vu2 >> iterations_vu2
