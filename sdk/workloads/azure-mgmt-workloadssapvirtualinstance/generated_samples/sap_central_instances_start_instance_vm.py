# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.workloadssapvirtualinstance import WorkloadsSapVirtualInstanceMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-workloadssapvirtualinstance
# USAGE
    python sap_central_instances_start_instance_vm.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = WorkloadsSapVirtualInstanceMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.sap_central_server_instances.begin_start(
        resource_group_name="test-rg",
        sap_virtual_instance_name="X00",
        central_instance_name="centralServer",
    ).result()
    print(response)


# x-ms-original-file: 2024-09-01/SapCentralInstances_StartInstanceVM.json
if __name__ == "__main__":
    main()
