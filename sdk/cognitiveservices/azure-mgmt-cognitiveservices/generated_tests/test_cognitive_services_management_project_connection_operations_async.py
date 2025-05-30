# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cognitiveservices.aio import CognitiveServicesManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCognitiveServicesManagementProjectConnectionOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CognitiveServicesManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_project_connection_delete(self, resource_group):
        response = await self.client.project_connection.delete(
            resource_group_name=resource_group.name,
            account_name="str",
            project_name="str",
            connection_name="str",
            api_version="2025-04-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_project_connection_get(self, resource_group):
        response = await self.client.project_connection.get(
            resource_group_name=resource_group.name,
            account_name="str",
            project_name="str",
            connection_name="str",
            api_version="2025-04-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_project_connection_update(self, resource_group):
        response = await self.client.project_connection.update(
            resource_group_name=resource_group.name,
            account_name="str",
            project_name="str",
            connection_name="str",
            api_version="2025-04-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_project_connection_create(self, resource_group):
        response = await self.client.project_connection.create(
            resource_group_name=resource_group.name,
            account_name="str",
            project_name="str",
            connection_name="str",
            api_version="2025-04-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_project_connection_list(self, resource_group):
        response = self.client.project_connection.list(
            resource_group_name=resource_group.name,
            account_name="str",
            project_name="str",
            api_version="2025-04-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
