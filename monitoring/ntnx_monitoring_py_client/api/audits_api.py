# coding: utf-8


"""
IGNORE:
    Nutanix Monitoring Versioned APIs

    Manage Alerts, Alert policies, Events and Audits  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ntnx_monitoring_py_client.api_client import ApiClient


class AuditsApi(object):
    """IGNORE:
    NOTE: A placeholder for class level description
    IGNORE
    """  # noqa: E501

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()

        self.api_client = api_client
        self.__headers_to_skip = { 'authorization', 'cookie', 'host', 'user-agent' }

    def get_audit_by_id(self, extId, **kwargs):  # noqa: E501
        """Get the audit details

        >>> response = api.get_audit_by_id(extId)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_audit_by_id(extId, async_req=True)
        >>> result = thread.get()

        :param extId: UUID of the generated audit.
        :type extId:

            :class:`str`, required
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.GetAuditApiResponse`.

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
            raise ValueError("Missing the required parameter `extId` when calling `get_audit_by_id`")  # noqa: E501

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
                    '/api/monitoring/v4.0.b1/serviceability/audits/{extId}', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='monitoring.v4.serviceability.GetAuditApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/monitoring/v4.0.b1/serviceability/audits/{extId}', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='monitoring.v4.serviceability.GetAuditApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass

    def list_audits(self, _page=None, _limit=None, _filter=None, _orderby=None, _select=None, **kwargs):  # noqa: E501
        """List all the audits

        >>> response = api.list_audits((optional) _page, (optional) _limit, (optional) _filter, (optional) _orderby, (optional) _select)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_audits(async_req=True)
        >>> result = thread.get()

        :param _page: A URL query parameter that specifies the page number of the result set. It must be a positive integer between 0 and the maximum number of pages that are available for that resource. Any number out of this range might lead to no results. 
        :type _page:

            :class:`int`
        :param _limit: A URL query parameter that specifies the total number of records returned in the result set.  Must be a positive integer between 1 and 100. Any number out of this range will lead to a validation error. If the limit is not provided, a default value of 50 records will be returned in the result set. 
        :type _limit:

            :class:`int`
        :param _filter: A URL query parameter that allows clients to filter a collection of resources. The expression specified with $filter is evaluated for each resource in the collection, and only items where the expression evaluates to true are included in the response. Expression specified with the $filter must conform to the [OData V4.01](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html) URL conventions. For example, filter '$filter=name eq 'karbon-ntnx-1.0' would filter the result on cluster name 'karbon-ntnx1.0', filter '$filter=startswith(name, 'C')' would filter on cluster name starting with 'C'. The filter can be applied to the following fields: - auditType - creationTime - extId - operationType - sourceEntity/extId - sourceEntity/name - sourceEntity/type - userReference/extId - userReference/ipAddress - userReference/name 
        :type _filter:

            :class:`str`
        :param _orderby: A URL query parameter that allows clients to specify the sort criteria for the returned list of objects. Resources can be sorted in ascending order using asc or descending order using desc. If asc or desc are not specified, the resources will be sorted in ascending order by default. For example, '$orderby=templateName desc' would get all templates sorted by templateName in descending order. The orderby can be applied to the following fields: - auditType - creationTime - operationType 
        :type _orderby:

            :class:`str`
        :param _select: A URL query parameter that allows clients to request a specific set of properties for each entity or complex type. Expression specified with the $select must conform to the [OData V4.01](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html) URL conventions. If a $select expression consists of a single select item that is an asterisk (i.e., *), then all properties on the matching resource will be returned. - affectedEntities - auditType - clusterReference - creationTime - extId - links - message - operationEndTime - operationStartTime - operationType - parameters - serviceName - sourceEntity/extId - sourceEntity/name - sourceEntity/type - status - tenantId - userReference/extId - userReference/ipAddress - userReference/name 
        :type _select:

            :class:`str`
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.ListAuditsApiResponse`.

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
        if '_page' in params and params['_page'] is not None:
            query_params.append(('$page', params['_page']))  # noqa: E501
        if '_limit' in params and params['_limit'] is not None:
            query_params.append(('$limit', params['_limit']))  # noqa: E501
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
        all_params = set(['_page', '_limit', '_filter', '_orderby', '_select'])
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
                    '/api/monitoring/v4.0.b1/serviceability/audits', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='monitoring.v4.serviceability.ListAuditsApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/monitoring/v4.0.b1/serviceability/audits', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='monitoring.v4.serviceability.ListAuditsApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass
