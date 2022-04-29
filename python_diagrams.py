from diagrams import Cluster, Diagram
from diagrams.generic.network import Router
from diagrams.custom import Custom

with Diagram("Grouped Workers", show=False):
    with Cluster("AS-65001"):
        router1 = Custom('router1', 'my_resources/network-router-icon-1.jpeg')
        router2 = Custom('router2', 'my_resources/network-router-icon-1.jpeg')
        router3 = Custom('router3', 'my_resources/network-router-icon-1.jpeg')

    router1 >> router2 >> router3
