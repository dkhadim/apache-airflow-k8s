## Déployer Apache airflow sur Kubernetes

Bienvenue sur ce tutoriel qui met en avant le déploiement d'apache airflow sur k8s. 
<!-- TODO: continue -->

### Prérequis

- Concepts de base sur k8s 
Parler ici de k8s

    - Pods 
    - Namespace
    - ServiceAccount
    - ...
- Python
- Git

### Technogolies utilisées

- **Apache airflow** [Outils d'orchestration de taches]
- **Helm** [Gestionnaire de package d'application sur k8s]
- **Kubernetes** [Orchestrateur de conteneurs]
- **Python** [Langage de programmation]
- **Git** [Outil de gestion de code source]

### Get Started 

#### Préparation de l'environnement [Installations nécessaires]

- Docker Desktop
    - Activer Kubernetes
- Kubectl

```bash
    brew install kubectl
```

Quelques commandes pour tester et vérifier l'etat du cluster

```bash
    # La version de kubectl
    kubectl version

    # Infos sur le cluster
    kubectl cluster-info

    # Le context utilisé
    kubectl config get-contexts

    # Tous les pods dans les differents namespaces
    kubectl get pods -A
```

- Helm

```bash
    brew install helm
```

```bash
    helm version
```

#### Configuration du dashboard

Téléchargement du fichier yaml recommandé pour la ressource dashboard

```bash
curl https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml -o recommended-dashboard.yaml
```

```bash
    kubectl apply -f recommendded-dashboard.yaml
```

Ajouter les fichiers suivants: 
- dashboard-clusterrole.yaml
- dashboard-adminuser.yaml
- dashboard-secret.yaml

```bash
    kubectl apply -f k8s/
```

URL Dashboard: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

Créer un token

```bash
    kubectl get secret admin-user -n kubernetes-dashboard -o jsonpath={".data.token"} | base64 -d
```

Utiliser le token pour se connecter au dashboard.

#### Utilisation du chart 

```bash
    helm repo add apache-airflow https://airflow.apache.org

    helm install airflow apache-airflow/airflow --namespace airflow --create-namespace
```


```bash

    kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow

```

```bash
    helm show values apache-airflow/airflow > values.yaml
```

Générer de nouvelles clés avec la commande pour plus de sécurité ...

```bash
echo Fernet Key: $(kubectl get secret --namespace airflow airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)
```

```bash
    helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace -f values.yaml
```

### Au final ?

### References 

- Kubernetes documentation
- Docker Desktop
- CodeWithYu