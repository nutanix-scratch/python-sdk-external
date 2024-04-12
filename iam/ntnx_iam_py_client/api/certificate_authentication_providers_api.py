# coding: utf-8


"""
IGNORE:
    Nutanix Iam Versioned APIs

    Manage Identity and Access Management of Nutanix clusters.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ntnx_iam_py_client.api_client import ApiClient


class CertificateAuthenticationProvidersApi(object):
    """IGNORE:
    NOTE: A placeholder for class level description
    IGNORE
    """  # noqa: E501

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()

        self.api_client = api_client
        self.__headers_to_skip = { 'authorization', 'cookie', 'host', 'user-agent' }

    def create_cert_auth_provider(self, clientCaChain, caCertFileName, isCertAuthEnabled, name, isCacEnabled, dirSvcExtID=None, certRevocationInfo=None, createdBy=None, tenantId=None, createdTime=None, links=None, lastUpdatedTime=None, extId=None, **kwargs):  # noqa: E501
        """Create Certificate based Authentication provider

        >>> response = api.create_cert_auth_provider(clientCaChain, caCertFileName, isCertAuthEnabled, name, isCacEnabled, (optional) dirSvcExtID, (optional) certRevocationInfo, (optional) createdBy, (optional) tenantId, (optional) createdTime, (optional) links, (optional) lastUpdatedTime, (optional) extId)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_cert_auth_provider(clientCaChain, caCertFileName, isCertAuthEnabled, name, isCacEnabled, async_req=True)
        >>> result = thread.get()

        :param clientCaChain: 
        :type clientCaChain:

            :class:`str`, required
        :param caCertFileName: 
        :type caCertFileName:

            :class:`str`, required
        :param isCertAuthEnabled: 
        :type isCertAuthEnabled:

            :class:`bool`, required
        :param name: 
        :type name:

            :class:`str`, required
        :param isCacEnabled: 
        :type isCacEnabled:

            :class:`bool`, required
        :param dirSvcExtID: 
        :type dirSvcExtID:

            :class:`str`
        :param certRevocationInfo: 
        :type certRevocationInfo:

            :class:`iam.v4.authn.CertRevocationInfo`
        :param createdBy: 
        :type createdBy:

            :class:`str`
        :param tenantId: 
        :type tenantId:

            :class:`str`
        :param createdTime: 
        :type createdTime:

            :class:`datetime`
        :param links: 
        :type links:

                :param lastUpdatedTime: 
        :type lastUpdatedTime:

            :class:`datetime`
        :param extId: 
        :type extId:

            :class:`str`
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_iam_py_client.models.iam.v4.authn.CreateCertAuthProviderApiResponse`.

                 If the method is called asynchronously, returns the request thread.
        """ # noqa: E501
        kwargs['_return_http_data_only'] = True

        params = dict(locals())
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        del params['self']

        # verify the required parameter 'clientCaChain' is set
        if ('clientCaChain' not in params or params['clientCaChain'] is None):
            raise ValueError("Missing the required parameter `clientCaChain` when calling `create_cert_auth_provider`")  # noqa: E501
        # verify the required parameter 'caCertFileName' is set
        if ('caCertFileName' not in params or params['caCertFileName'] is None):
            raise ValueError("Missing the required parameter `caCertFileName` when calling `create_cert_auth_provider`")  # noqa: E501
        # verify the required parameter 'isCertAuthEnabled' is set
        if ('isCertAuthEnabled' not in params or params['isCertAuthEnabled'] is None):
            raise ValueError("Missing the required parameter `isCertAuthEnabled` when calling `create_cert_auth_provider`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_cert_auth_provider`")  # noqa: E501
        # verify the required parameter 'isCacEnabled' is set
        if ('isCacEnabled' not in params or params['isCacEnabled'] is None):
            raise ValueError("Missing the required parameter `isCacEnabled` when calling `create_cert_auth_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client._select_header_accept(
            ['application/json'])  # noqa: E501
        if 'Accept' in params and params.get('Accept') is not None:
            header_params['Accept'] = params.get('Accept')

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client._select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501
        if 'Content-Type' in params and params.get('Content-Type') is not None:
            header_params['Content-Type'] = params.get('Content-Type')

        # Process operation specific headers
        extra_params = []
        extra_params.append('async_req')
        extra_params.append('_return_http_data_only')
        extra_params.append('_preload_content')
        extra_params.append('_request_timeout')
        all_params = set(['clientCaChain', 'caCertFileName', 'isCertAuthEnabled', 'name', 'isCacEnabled', 'dirSvcExtID', 'certRevocationInfo', 'createdBy', 'tenantId', 'createdTime', 'links', 'lastUpdatedTime', 'extId'])
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
        if 'clientCaChain' in params and params['clientCaChain'] is not None:
            form_params.append(('clientCaChain', params['clientCaChain']))  # noqa: E501
        if 'dirSvcExtID' in params and params['dirSvcExtID'] is not None:
            form_params.append(('dirSvcExtID', params['dirSvcExtID']))  # noqa: E501
        if 'certRevocationInfo' in params and params['certRevocationInfo'] is not None:
            form_params.append(('certRevocationInfo', params['certRevocationInfo']))  # noqa: E501
        if 'caCertFileName' in params and params['caCertFileName'] is not None:
            form_params.append(('caCertFileName', params['caCertFileName']))  # noqa: E501
        if 'isCertAuthEnabled' in params and params['isCertAuthEnabled'] is not None:
            form_params.append(('isCertAuthEnabled', params['isCertAuthEnabled']))  # noqa: E501
        if 'createdBy' in params and params['createdBy'] is not None:
            form_params.append(('createdBy', params['createdBy']))  # noqa: E501
        if 'tenantId' in params and params['tenantId'] is not None:
            form_params.append(('tenantId', params['tenantId']))  # noqa: E501
        if 'name' in params and params['name'] is not None:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'createdTime' in params and params['createdTime'] is not None:
            form_params.append(('createdTime', params['createdTime']))  # noqa: E501
        if 'links' in params and params['links'] is not None:
            form_params.append(('links', params['links']))  # noqa: E501
            collection_formats['links'] = 'multi'  # noqa: E501
        if 'isCacEnabled' in params and params['isCacEnabled'] is not None:
            form_params.append(('isCacEnabled', params['isCacEnabled']))  # noqa: E501
        if 'lastUpdatedTime' in params and params['lastUpdatedTime'] is not None:
            form_params.append(('lastUpdatedTime', params['lastUpdatedTime']))  # noqa: E501
        if 'extId' in params and params['extId'] is not None:
            form_params.append(('extId', params['extId']))  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuthScheme']  # noqa: E501

        body_params = None

        try:
            if kwargs.get('async_req'):
                return self.api_client._call_api(
                    '/api/iam/v4.0.b1/authn/cert-auth-providers', 'POST',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.CreateCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/iam/v4.0.b1/authn/cert-auth-providers', 'POST',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.CreateCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass

    def delete_cert_auth_provider_by_id(self, extId, **kwargs):  # noqa: E501
        """Delete Certificate based Authentication provider

        >>> response = api.delete_cert_auth_provider_by_id(extId)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_cert_auth_provider_by_id(extId, async_req=True)
        >>> result = thread.get()

        :param extId: 
        :type extId:

            :class:`str`, required
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_iam_py_client.models.iam.v4.authn.DeleteCertAuthProviderApiResponse`.

                 If the method is called asynchronously, returns the request thread.
        """ # noqa: E501
        kwargs['_return_http_data_only'] = True

        params = dict(locals())
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        del params['self']

        # verify the required parameter 'extId' is set
        if ('extId' not in params or params['extId'] is None):
            raise ValueError("Missing the required parameter `extId` when calling `delete_cert_auth_provider_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extId' in params and params['extId'] is not None:
            path_params['extId'] = params['extId']  # noqa: E501

        query_params = []

        header_params = {}
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
        all_params = set(['extId'])
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
                    '/api/iam/v4.0.b1/authn/cert-auth-providers/{extId}', 'DELETE',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.DeleteCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/iam/v4.0.b1/authn/cert-auth-providers/{extId}', 'DELETE',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.DeleteCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass

    def get_cert_auth_provider_by_id(self, extId, **kwargs):  # noqa: E501
        """Get Certificate based Authentication provider

        >>> response = api.get_cert_auth_provider_by_id(extId)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_cert_auth_provider_by_id(extId, async_req=True)
        >>> result = thread.get()

        :param extId: 
        :type extId:

            :class:`str`, required
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_iam_py_client.models.iam.v4.authn.GetCertAuthProviderApiResponse`.

                 If the method is called asynchronously, returns the request thread.
        """ # noqa: E501
        kwargs['_return_http_data_only'] = True

        params = dict(locals())
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        del params['self']

        # verify the required parameter 'extId' is set
        if ('extId' not in params or params['extId'] is None):
            raise ValueError("Missing the required parameter `extId` when calling `get_cert_auth_provider_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extId' in params and params['extId'] is not None:
            path_params['extId'] = params['extId']  # noqa: E501

        query_params = []

        header_params = {}
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
        all_params = set(['extId'])
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
                    '/api/iam/v4.0.b1/authn/cert-auth-providers/{extId}', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.GetCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/iam/v4.0.b1/authn/cert-auth-providers/{extId}', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.GetCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass

    def list_cert_auth_providers(self, _filter=None, _orderby=None, _select=None, **kwargs):  # noqa: E501
        """List Certificate based Authentication provider(s)

        >>> response = api.list_cert_auth_providers((optional) _filter, (optional) _orderby, (optional) _select)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_cert_auth_providers(async_req=True)
        >>> result = thread.get()

        :param _filter: A URL query parameter that allows clients to filter a collection of resources. The expression specified with $filter is evaluated for each resource in the collection, and only items where the expression evaluates to true are included in the response. Expression specified with the $filter must conform to the [OData V4.01](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html) URL conventions. For example, filter '$filter=name eq 'karbon-ntnx-1.0' would filter the result on cluster name 'karbon-ntnx1.0', filter '$filter=startswith(name, 'C')' would filter on cluster name starting with 'C'. The filter can be applied to the following fields: - createdBy - extId - name 
        :type _filter:

            :class:`str`
        :param _orderby: A URL query parameter that allows clients to specify the sort criteria for the returned list of objects. Resources can be sorted in ascending order using asc or descending order using desc. If asc or desc are not specified, the resources will be sorted in ascending order by default. For example, '$orderby=templateName desc' would get all templates sorted by templateName in descending order. The orderby can be applied to the following fields: - createdTime - lastUpdatedTime - name 
        :type _orderby:

            :class:`str`
        :param _select: A URL query parameter that allows clients to request a specific set of properties for each entity or complex type. Expression specified with the $select must conform to the [OData V4.01](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html) URL conventions. If a $select expression consists of a single select item that is an asterisk (i.e., *), then all properties on the matching resource will be returned. - caCertFileName - certRevocationInfo/crlDps - certRevocationInfo/globalCrlRefreshInterval - certRevocationInfo/isCrlEnabled - certRevocationInfo/isOcspEnabled - certRevocationInfo/ocspResponder - clientCaChain - createdBy - createdTime - dirSvcExtID - extId - isCacEnabled - isCertAuthEnabled - lastUpdatedTime - links - name - tenantId 
        :type _select:

            :class:`str`
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_iam_py_client.models.iam.v4.authn.ListCertAuthProvidersApiResponse`.

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
        if '_filter' in params and params['_filter'] is not None:
            query_params.append(('$filter', params['_filter']))  # noqa: E501
        if '_orderby' in params and params['_orderby'] is not None:
            query_params.append(('$orderby', params['_orderby']))  # noqa: E501
        if '_select' in params and params['_select'] is not None:
            query_params.append(('$select', params['_select']))  # noqa: E501

        header_params = {}
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
        all_params = set(['_filter', '_orderby', '_select'])
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
                    '/api/iam/v4.0.b1/authn/cert-auth-providers', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.ListCertAuthProvidersApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/iam/v4.0.b1/authn/cert-auth-providers', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.ListCertAuthProvidersApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass

    def update_cert_auth_provider_by_id(self, extId, clientCaChain=None, dirSvcExtID=None, certRevocationInfo=None, caCertFileName=None, isCertAuthEnabled=None, createdBy=None, tenantId=None, name=None, createdTime=None, links=None, isCacEnabled=None, lastUpdatedTime=None, extId2=None, **kwargs):  # noqa: E501
        """Update Certificate based Authentication provider

        >>> response = api.update_cert_auth_provider_by_id(extId, (optional) clientCaChain, (optional) dirSvcExtID, (optional) certRevocationInfo, (optional) caCertFileName, (optional) isCertAuthEnabled, (optional) createdBy, (optional) tenantId, (optional) name, (optional) createdTime, (optional) links, (optional) isCacEnabled, (optional) lastUpdatedTime, (optional) extId2)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_cert_auth_provider_by_id(extId, async_req=True)
        >>> result = thread.get()

        :param extId: 
        :type extId:

            :class:`str`, required
        :param clientCaChain: 
        :type clientCaChain:

            :class:`str`
        :param dirSvcExtID: 
        :type dirSvcExtID:

            :class:`str`
        :param certRevocationInfo: 
        :type certRevocationInfo:

            :class:`iam.v4.authn.CertRevocationInfo`
        :param caCertFileName: 
        :type caCertFileName:

            :class:`str`
        :param isCertAuthEnabled: 
        :type isCertAuthEnabled:

            :class:`bool`
        :param createdBy: 
        :type createdBy:

            :class:`str`
        :param tenantId: 
        :type tenantId:

            :class:`str`
        :param name: 
        :type name:

            :class:`str`
        :param createdTime: 
        :type createdTime:

            :class:`datetime`
        :param links: 
        :type links:

                :param isCacEnabled: 
        :type isCacEnabled:

            :class:`bool`
        :param lastUpdatedTime: 
        :type lastUpdatedTime:

            :class:`datetime`
        :param extId2: 
        :type extId2:

            :class:`str`
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_iam_py_client.models.iam.v4.authn.UpdateCertAuthProviderApiResponse`.

                 If the method is called asynchronously, returns the request thread.
        """ # noqa: E501
        kwargs['_return_http_data_only'] = True

        params = dict(locals())
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        del params['self']

        # verify the required parameter 'extId' is set
        if ('extId' not in params or params['extId'] is None):
            raise ValueError("Missing the required parameter `extId` when calling `update_cert_auth_provider_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extId' in params and params['extId'] is not None:
            path_params['extId'] = params['extId']  # noqa: E501

        query_params = []

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client._select_header_accept(
            ['application/json'])  # noqa: E501
        if 'Accept' in params and params.get('Accept') is not None:
            header_params['Accept'] = params.get('Accept')

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client._select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501
        if 'Content-Type' in params and params.get('Content-Type') is not None:
            header_params['Content-Type'] = params.get('Content-Type')

        # Process operation specific headers
        extra_params = []
        extra_params.append('async_req')
        extra_params.append('_return_http_data_only')
        extra_params.append('_preload_content')
        extra_params.append('_request_timeout')
        all_params = set(['extId', 'clientCaChain', 'dirSvcExtID', 'certRevocationInfo', 'caCertFileName', 'isCertAuthEnabled', 'createdBy', 'tenantId', 'name', 'createdTime', 'links', 'isCacEnabled', 'lastUpdatedTime', 'extId2'])
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
        if 'clientCaChain' in params and params['clientCaChain'] is not None:
            form_params.append(('clientCaChain', params['clientCaChain']))  # noqa: E501
        if 'dirSvcExtID' in params and params['dirSvcExtID'] is not None:
            form_params.append(('dirSvcExtID', params['dirSvcExtID']))  # noqa: E501
        if 'certRevocationInfo' in params and params['certRevocationInfo'] is not None:
            form_params.append(('certRevocationInfo', params['certRevocationInfo']))  # noqa: E501
        if 'caCertFileName' in params and params['caCertFileName'] is not None:
            form_params.append(('caCertFileName', params['caCertFileName']))  # noqa: E501
        if 'isCertAuthEnabled' in params and params['isCertAuthEnabled'] is not None:
            form_params.append(('isCertAuthEnabled', params['isCertAuthEnabled']))  # noqa: E501
        if 'createdBy' in params and params['createdBy'] is not None:
            form_params.append(('createdBy', params['createdBy']))  # noqa: E501
        if 'tenantId' in params and params['tenantId'] is not None:
            form_params.append(('tenantId', params['tenantId']))  # noqa: E501
        if 'name' in params and params['name'] is not None:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'createdTime' in params and params['createdTime'] is not None:
            form_params.append(('createdTime', params['createdTime']))  # noqa: E501
        if 'links' in params and params['links'] is not None:
            form_params.append(('links', params['links']))  # noqa: E501
            collection_formats['links'] = 'multi'  # noqa: E501
        if 'isCacEnabled' in params and params['isCacEnabled'] is not None:
            form_params.append(('isCacEnabled', params['isCacEnabled']))  # noqa: E501
        if 'lastUpdatedTime' in params and params['lastUpdatedTime'] is not None:
            form_params.append(('lastUpdatedTime', params['lastUpdatedTime']))  # noqa: E501
        if 'extId2' in params and params['extId2'] is not None:
            form_params.append(('extId', params['extId2']))  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuthScheme']  # noqa: E501

        body_params = None

        try:
            if kwargs.get('async_req'):
                return self.api_client._call_api(
                    '/api/iam/v4.0.b1/authn/cert-auth-providers/{extId}', 'PUT',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.UpdateCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/iam/v4.0.b1/authn/cert-auth-providers/{extId}', 'PUT',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='iam.v4.authn.UpdateCertAuthProviderApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass
