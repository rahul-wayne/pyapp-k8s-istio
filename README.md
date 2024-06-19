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

Step 6: Access the application from outside the cluster via external ip

kubectl get svc -n aks-istio-ingress


Setup custom buildx builder for multi-platform docker image building
+++++++++++++++++
On AMD64
-------
1. Install QEMU:
sudo apt-get install qemu-user-static

2. Enable Binfmt_misc:
Enable the binfmt_misc kernel module to allow the execution of binaries for foreign architectures:
sudo update-binfmts --enable qemu-arm
sudo update-binfmts --enable qemu-armeb
sudo update-binfmts --enable qemu-aarch64
sudo update-binfmts --enable qemu-aarch64_be


3. Restart Docker:
sudo systemctl restart docker

4. Create Buildx Builder:
docker buildx create --name mybuilder
docker buildx ls
docker buildx use mybuilder
docker buildx inspect --bootstrap
docker buildx inspect mybuilder

5. Build the Multi-Platform Image:
docker buildx build --platform linux/amd64,linux/arm64 -t your-image-name .

6. Push the Multi-Platform Image:
docker buildx build --platform linux/amd64,linux/arm64 -t your-registry/your-image-name:tag --push .



ON ARM64
-----
1. First, you need to install the qemu packages that include support for x86_64 emulation. On a Debian-based system like Ubuntu, you can install these packages as follows:

sudo apt update
sudo apt install qemu qemu-user qemu-user-static binfmt-support

2. Enable QEMU for amd64

sudo update-binfmts --enable qemu-x86_64

3. Verify the Registration

sudo update-binfmts --display qemu-x86_64

sudo update-binfmts --enable qemu-x86_64

4. List Existing Registered Binfmts

sudo update-binfmts --display

4. Create Buildx Builder:
docker buildx create --name mybuilder
docker buildx ls
docker buildx use mybuilder
docker buildx inspect --bootstrap
docker buildx inspect mybuilder

6. Push the Multi-Platform Image:
docker buildx build --platform linux/amd64,linux/arm64 -t your-registry/your-image-name:tag --push .



*   To enable mutual TLS (mTLS) across your entire Istio service mesh, you need to configure PeerAuthentication and DestinationRule
to achive this, apply ymls in mtls directory

Ensure that the PeerAuthentication policy is correctly applied:

kubectl describe peerauthentication default -n aks-istio-system

Ensure that the DestinationRule is correctly applied:

kubectl describe destinationrule default -n aks-istio-system


https://istio.io/latest/docs/setup/getting-started/#bookinfo

kubectl apply -f istio-1.22.1/samples/sleep/sleep.yaml
kubectl apply -f istio-1.22.1/samples/httpbin/httpbin.yaml

https://istio.io/latest/docs/tasks/security/tls-configuration/workload-min-tls-version/

kubectl exec -it <pod> -n <namespace> -- curl -v http://httpbin.default.svc.cluster.local:8000/ip


