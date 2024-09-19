from diagrams import Diagram, Cluster
from diagrams.onprem.client import User 
from diagrams.custom import Custom


with Diagram("Ramping Vus Diagrams", show = True):
    load_balancer = Custom("Ramping vus", "../img/images.png")

    with Cluster("Usuarios virtuales1", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        grupo1 = [ Custom("VU 1", "../img/user1.png"), Custom("VU 2", "../img/user1.png")]
    

    with Cluster("Usuarios virtuale21", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        grupo2 = [ User("VU 1"), User("VU 2"), User("VU 3"), User("VU 4")]

    
    with Cluster("Usuarios virtuales3", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        grupo3 = [ Custom("VU 1", "../img/user3.png")]
    

    with Cluster("Tiempo", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        time1 = Custom("Intervalo 10s", "../img/time.jpg")

    with Cluster("Tiempo", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        time2 = Custom("Intervalo 5m", "../img/time.jpg")

    with Cluster("Tiempo", graph_attr= {"style": "dashed", "bgcolor": "transparent"}):
        time3 = Custom("Intervalo 20s", "../img/time.jpg")


    load_balancer >> time1 >> grupo1
    load_balancer >> time2 >> grupo2
    load_balancer >> time3 >> grupo3