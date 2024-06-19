# python flask application with mongodb and istio on AKS cluster

Database configuration details
-------------------------------
demo microservice applicationsdsd
mongosh
use microserviceDB
db.createCollection('data')


Cluster configuration
-------------------------------
Step 1: Create a AKS cluster and enable istio addon

Step 2: Enable external ingress gateway

Step 3: Create a namespace

kubectl create namespace pyapp-istio-test

Step 4: enable automatic sidecar injection

kubectl label namespace pyapp-istio-test istio-injection=enabled

you can also enable it form UI 

Kubernetes Service -> Settings -> Service mesh - Istio -> Automatic sidecar injection -> Add -> select the namespace

Step 5: enable ingress gateway external for accessing the application from outside the cluster

az aks mesh enable-ingress-gateway --resource-group $RESOURCE_GROUP --name $CLUSTER --ingress-gateway-type external

kubectl get svc aks-istio-ingressgateway-external -n aks-istio-ingress

You can also enable internal ingress gateway by using the following command, if needed:

az aks mesh enable-ingress-gateway --resource-group $RESOURCE_GROUP --name $CLUSTER --ingress-gateway-type internal

https://learn.microsoft.com/en-in/azure/aks/istio-deploy-ingress#enable-external-ingress-gateway