#!/bin/bash

#Gitlab Variables 
PROJECT_ID=<gitlab-project-id> # Project ID of the gitlab project
TOKEN=<gitlab-access-token> # Project ID of the gitlab project

#Azure Variables
RG_NAME=<azure-resource-group-name>
STORAGE_NAME=<azure-storage-account-name>
CONTAINER_NAME="data"
LOCATION="westeurope"

# Setup Deploy KEy
echo "./deploy_key" | ssh-keygen -t ed25519 -N ""

curl --request POST --header "PRIVATE-TOKEN: $TOKEN" --header "Content-Type: application/json" \
     --data "{'title': 'DEPLOY_KEY', 'key': $(cat deploy_key.pub), 'can_push': 'true'}" 
     "https://gitlab.com/api/v4/projects/$PROJECT_ID/deploy_keys"

curl --request POST --header "PRIVATE-TOKEN: $TOKEN" \
     "https://gitlab.com/api/v4/projects/$PROJECT_ID/variables" --form "key=DEPLOY_KEY" --form "value=$(cat deploy_key)\n" --form "variable_type=file"

rm ./deploy_key ./deploy_key.pub


# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Create a Azure Backing Store
az login

az group create \
    --location $LOCATION \
    --name $RG_NAME

az storage account create \
    --name $STORAGE_NAME \
    --resource-group $RG_NAME \
    --location $LOCATION \
    --sku "Standard_LRS"

az storage container create \
    --account-name $STORAGE_NAME \
    --name $CONTAINER_NAME

CONNECTION_STRING=$(az storage account show-connection-string -g $RG_NAME -n $STORAGE_NAME | \
python -c "import sys, json; print(json.load(sys.stdin)['connectionString'])")

# Set as DVC backing store locally
dvc remote add -d myremote "azure://$CONTAINER_NAME/backingstore"
dvc remote modify --local myremote connection_string "$CONNECTION_STRING"

# Track raw data
dvc add /app/data/base/01_raw
dvc push

# Set Connection String as CI variable so DVC can pull data.
curl --request POST --header "PRIVATE-TOKEN: $TOKEN" --header "Content-Type: application/json" \
     --data "{'key': 'AZURE_STORAGE_CONNECTION_STRING', 'value': $CONNECTION_STRING}" \
     "https://gitlab.com/api/v4/projects/$PROJECT_ID/variables"
