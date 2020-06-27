# Azure Website

Django website to display azure Virtual Machine information.

A .env file contains the secrets and is set like so.

```bash
AZURE_TENANT_ID=
AZURE_CLIENT_ID=
AZURE_CLIENT_SECRET=
AZURE_SUBSCRIPTION_ID=
SECRET_KEY=
```

## display images

Displays the virtual machine images and offers from publishers.

## Create an Azure VM

Export the azure credentials to environment variables:

```bash
export AZURE_CLIENT_ID=
export AZURE_SECRET=
export AZURE_SUBSCRIPTION_ID=
export AZURE_TENANT=
```

Run the playbook.

```bash
ansible-playbook -i localhost playbook.yml
```

## Update DNS record

Update the DNS record with the IP address of the server. This can be seen in the Output public IP address. task

## Deployment

Requires the geerlingguy.certbot ansible role for let's encrypt.
The domain name must resolve to the public IP of the VM.

```bash
ansible-playbook playbook.yml -i ../azure_vm/inventory
```

## Resources used

https://www.ansiblefordevops.com/
https://www.digitalocean.com/community/tutorials/how-to-display-data-from-the-digitalocean-api-with-django
https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/
https://github.com/Azure-Samples/virtual-machines-python-manage/blob/master/example.py
https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-samples-list-images