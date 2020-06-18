import os
from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials


# Retrieve the IDs and secret to use with ServicePrincipalCredentials
subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
tenant_id = os.getenv('AZURE_TENANT_ID')
client_id = os.getenv('AZURE_CLIENT_ID')
client_secret = os.getenv('AZURE_CLIENT_SECRET')

credential = ServicePrincipalCredentials(
    tenant=tenant_id, client_id=client_id, secret=client_secret)

compute_client = ComputeManagementClient(credential, subscription_id)

REGION = 'eastus'

def get_publishers():
    region_list_publishers = compute_client.virtual_machine_images.list_publishers(
        REGION,)
    publisher_list = []
    for publisher in region_list_publishers:
        publisher_list.append(publisher.name)
    return publisher_list


def get_offers(publisher):
    region_offer_list = compute_client.virtual_machine_images.list_offers(
        REGION, publisher)
    offer_list = []
    for offer in region_offer_list:
        offer_list.append(offer.name)
    offer_dictionary = {
        'publisher': publisher,
        'offers': offer_list
    }
    return offer_dictionary


def get_skus(publisher, offer):
    region_sku_list = compute_client.virtual_machine_images.list_skus(
        REGION, publisher, offer)
    sku_list = []
    for sku in region_sku_list:
        sku_list.append(sku.name)
    sku_dictionary = {
        'publisher': publisher,
        'offer': offer,
        'skus': sku_list
    }
    return sku_dictionary

def get_versions(publisher, offer, sku):
    region_version_list = compute_client.virtual_machine_images.list(REGION, publisher, offer, sku)
    version_list = []
    for version in region_version_list:
        version_list.append(version.name)
    version_dictionary = {
        'publisher': publisher,
        'offer': offer,
        'sku': sku,
        'versions': version_list 
    }
    return version_dictionary

def get_image(publisher, offer, sku, version):
    result_image = compute_client.virtual_machine_images.get(REGION, publisher, offer, sku, version)
    res_dict = result_image.as_dict()

    # check for hyperv return as it is not always returned
    if('hyper_vgeneration' in res_dict.keys()):
        hyper_v_value = res_dict['hyper_vgeneration']
    else:
        hyper_v_value = 'Not found'

    image_dictionary = {
        'publisher': publisher,
        'offer': offer,
        'sku': sku,
        'version': res_dict['name'],
        'location': REGION,
        'os': res_dict['os_disk_image']['operating_system'],
        'hyperv': hyper_v_value
    }
    return image_dictionary
    
