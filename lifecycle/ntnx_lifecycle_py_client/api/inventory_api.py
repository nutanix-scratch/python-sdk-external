# coding: utf-8


"""
IGNORE:
    Nutanix Lifecycle Versioned APIs

    Manage Infrastructure, Software and Firmware Upgrades.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ntnx_lifecycle_py_client.api_client import ApiClient


class InventoryApi(object):
    """IGNORE:
    NOTE: A placeholder for class level description
    IGNORE
    """  # noqa: E501

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()

        self.api_client = api_client
        self.__headers_to_skip = { 'authorization', 'cookie', 'host', 'user-agent' }

    def perform_inventory(self, X_Cluster_Id=None, **kwargs):  # noqa: E501
        """Perform an inventory operation to identify/scan entities on the cluster that can be updated through LCM.

        >>> response = api.perform_inventory((optional) X_Cluster_Id)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.perform_inventory(async_req=True)
        >>> result = thread.get()

        :param X_Cluster_Id: Cluster uuid on which the resource is present or operation is being performed.
        :type X_Cluster_Id:

            :class:`str`
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_lifecycle_py_client.models.lifecycle.v4.operations.InventoryApiResponse`.

                 If the method is called asynchronously, returns the request thread.
        """ # noqa: E501
        kwargs['_return_http_data_only'] = True

        params = dict(locals())
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        del params['self']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'X_Cluster_Id' in params and params['X_Cluster_Id'] is not None:
            header_params['X-Cluster-Id'] = params['X_Cluster_Id']  # noqa: E501
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client._select_header_accept(
            ['application/json'])  # noqa: E501
        if 'Accept' in params and params.get('Accept') is not None:
            header_params['Accept'] = params.get('Accept')

        # Process operation specific headers
        extra_params = []
        extra_params.append('async_req')
        extra_params.append('_return_http_data_only')
        extra_params.append('_preload_content')
        extra_params.append('_request_timeout')
        all_params = set(['X_Cluster_Id'])
        all_params.update(extra_params)
        for key, val in six.iteritems(params):
            if val is not None and key.lower() not in self.__headers_to_skip and key not in all_params:
                if key.lower() == 'if_match'.lower():
                    key = 'If-Match'
                elif key.lower() == 'if_none_match'.lower():
                    key = 'If-None-Match'
                header_params[key] = val

        form_params = []
        local_var_files = {}

        # Authentication setting
        auth_settings = ['basicAuthScheme']  # noqa: E501

        body_params = None

        try:
            if kwargs.get('async_req'):
                return self.api_client._call_api(
                    '/api/lifecycle/v4.0.b1/operations/$actions/inventory', 'POST',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='lifecycle.v4.operations.InventoryApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/lifecycle/v4.0.b1/operations/$actions/inventory', 'POST',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='lifecycle.v4.operations.InventoryApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass
