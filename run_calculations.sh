#!/bin/bash
az vm start --name damir --resource-group MyResourceGroup
ssh -tt azureuser@104.45.150.12 python3 script.py
az vm deallocate --resource-group MyResourceGroup --name damir