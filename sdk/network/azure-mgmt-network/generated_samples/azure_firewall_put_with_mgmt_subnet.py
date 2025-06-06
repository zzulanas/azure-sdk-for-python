# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python azure_firewall_put_with_mgmt_subnet.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.azure_firewalls.begin_create_or_update(
        resource_group_name="rg1",
        azure_firewall_name="azurefirewall",
        parameters={
            "location": "West US",
            "properties": {
                "applicationRuleCollections": [
                    {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/azureFirewalls/azurefirewall/applicationRuleCollections/apprulecoll",
                        "name": "apprulecoll",
                        "properties": {
                            "action": {"type": "Deny"},
                            "priority": 110,
                            "rules": [
                                {
                                    "description": "Deny inbound rule",
                                    "name": "rule1",
                                    "protocols": [{"port": 443, "protocolType": "Https"}],
                                    "sourceAddresses": ["216.58.216.164", "10.0.0.0/24"],
                                    "targetFqdns": ["www.test.com"],
                                }
                            ],
                        },
                    }
                ],
                "ipConfigurations": [
                    {
                        "name": "azureFirewallIpConfiguration",
                        "properties": {
                            "publicIPAddress": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/pipName"
                            },
                            "subnet": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/vnet2/subnets/AzureFirewallSubnet"
                            },
                        },
                    }
                ],
                "managementIpConfiguration": {
                    "name": "azureFirewallMgmtIpConfiguration",
                    "properties": {
                        "publicIPAddress": {
                            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/managementPipName"
                        },
                        "subnet": {
                            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/vnet2/subnets/AzureFirewallManagementSubnet"
                        },
                    },
                },
                "natRuleCollections": [
                    {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/azureFirewalls/azurefirewall/natRuleCollections/natrulecoll",
                        "name": "natrulecoll",
                        "properties": {
                            "action": {"type": "Dnat"},
                            "priority": 112,
                            "rules": [
                                {
                                    "description": "D-NAT all outbound web traffic for inspection",
                                    "destinationAddresses": ["1.2.3.4"],
                                    "destinationPorts": ["443"],
                                    "name": "DNAT-HTTPS-traffic",
                                    "protocols": ["TCP"],
                                    "sourceAddresses": ["*"],
                                    "translatedAddress": "1.2.3.5",
                                    "translatedPort": "8443",
                                },
                                {
                                    "description": "D-NAT all inbound web traffic for inspection",
                                    "destinationAddresses": ["1.2.3.4"],
                                    "destinationPorts": ["80"],
                                    "name": "DNAT-HTTP-traffic-With-FQDN",
                                    "protocols": ["TCP"],
                                    "sourceAddresses": ["*"],
                                    "translatedFqdn": "internalhttpserver",
                                    "translatedPort": "880",
                                },
                            ],
                        },
                    }
                ],
                "networkRuleCollections": [
                    {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/azureFirewalls/azurefirewall/networkRuleCollections/netrulecoll",
                        "name": "netrulecoll",
                        "properties": {
                            "action": {"type": "Deny"},
                            "priority": 112,
                            "rules": [
                                {
                                    "description": "Block traffic based on source IPs and ports",
                                    "destinationAddresses": ["*"],
                                    "destinationPorts": ["443-444", "8443"],
                                    "name": "L4-traffic",
                                    "protocols": ["TCP"],
                                    "sourceAddresses": ["192.168.1.1-192.168.1.12", "10.1.4.12-10.1.4.255"],
                                },
                                {
                                    "description": "Block traffic based on source IPs and ports to amazon",
                                    "destinationFqdns": ["www.amazon.com"],
                                    "destinationPorts": ["443-444", "8443"],
                                    "name": "L4-traffic-with-FQDN",
                                    "protocols": ["TCP"],
                                    "sourceAddresses": ["10.2.4.12-10.2.4.255"],
                                },
                            ],
                        },
                    }
                ],
                "sku": {"name": "AZFW_VNet", "tier": "Standard"},
                "threatIntelMode": "Alert",
            },
            "tags": {"key1": "value1"},
            "zones": [],
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-05-01/examples/AzureFirewallPutWithMgmtSubnet.json
if __name__ == "__main__":
    main()
