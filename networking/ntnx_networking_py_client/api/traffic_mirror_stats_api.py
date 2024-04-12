# coding: utf-8


"""
IGNORE:
    Nutanix Networking Versioned APIs

    Manage networking configuration on Nutanix clusters, including AHV and advanced networking.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ntnx_networking_py_client.api_client import ApiClient


class TrafficMirrorStatsApi(object):
    """IGNORE:
    NOTE: A placeholder for class level description
    IGNORE
    """  # noqa: E501

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()

        self.api_client = api_client
        self.__headers_to_skip = { 'authorization', 'cookie', 'host', 'user-agent' }

    def get_traffic_mirror_stats(self, extId, _startTime, _endTime, _samplingInterval=None, _statType=None, _select=None, **kwargs):  # noqa: E501
        """Get Traffic mirror session statistics.

        >>> response = api.get_traffic_mirror_stats(extId, _startTime, _endTime, (optional) _samplingInterval, (optional) _statType, (optional) _select)

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_traffic_mirror_stats(extId, _startTime, _endTime, async_req=True)
        >>> result = thread.get()

        :param extId: UUID of the session.
        :type extId:

            :class:`str`, required
        :param _startTime: The start time of the period for which stats should be reported. The value should be in extended ISO-8601 format. For example, start time of 2022-04-23T01:23:45.678+09:00 would consider all stats starting at 1:23:45.678 on the 23rd of April 2022. Details around ISO-8601 format can be found at https://www.iso.org/standard/70907.html 
        :type _startTime:

            :class:`str`, required
        :param _endTime: The end time of the period for which stats should be reported. The value should be in extended ISO-8601 format. For example, end time of 2022-04-23T013:23:45.678+09:00 would consider all stats till 13:23:45 .678 on the 23rd of April 2022. Details around ISO-8601 format can be found at https://www.iso.org/standard/70907.html 
        :type _endTime:

            :class:`str`, required
        :param _samplingInterval: The sampling interval in seconds at which statistical data should be collected. For example, if you want performance statistics every 30 seconds, then provide the value as 30. 
        :type _samplingInterval:

            :class:`int`
        :param _statType: 
        :type _statType:

            :class:`common.v1.stats.DownSamplingOperator`
        :param _select: A URL query parameter that allows clients to request a specific set of properties for each entity or complex type. Expression specified with the $select must conform to the [OData V4.01](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html) URL conventions. If a $select expression consists of a single select item that is an asterisk (i.e., *), then all properties on the matching resource will be returned. - entityUuid - extId - links - name - statType - state - stateMessage - statsData - tenantId 
        :type _select:

            :class:`str`
        :param kwargs: kwargs for the method.
                       The following can be passed for an asynchronous HTTP call::

                           async_req=True
        :return: An instance of class :class:`~ntnx_networking_py_client.models.networking.v4.stats.GetTrafficMirrorStatsApiResponse`.

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
            raise ValueError("Missing the required parameter `extId` when calling `get_traffic_mirror_stats`")  # noqa: E501
        # verify the required parameter '_startTime' is set
        if ('_startTime' not in params or params['_startTime'] is None):
            raise ValueError("Missing the required parameter `_startTime` when calling `get_traffic_mirror_stats`")  # noqa: E501
        # verify the required parameter '_endTime' is set
        if ('_endTime' not in params or params['_endTime'] is None):
            raise ValueError("Missing the required parameter `_endTime` when calling `get_traffic_mirror_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extId' in params and params['extId'] is not None:
            path_params['extId'] = params['extId']  # noqa: E501

        query_params = []
        if '_startTime' in params and params['_startTime'] is not None:
            query_params.append(('$startTime', params['_startTime']))  # noqa: E501
        if '_endTime' in params and params['_endTime'] is not None:
            query_params.append(('$endTime', params['_endTime']))  # noqa: E501
        if '_samplingInterval' in params and params['_samplingInterval'] is not None:
            query_params.append(('$samplingInterval', params['_samplingInterval']))  # noqa: E501
        if '_statType' in params and params['_statType'] is not None:
            query_params.append(('$statType', params['_statType']))  # noqa: E501
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
        all_params = set(['extId', '_startTime', '_endTime', '_samplingInterval', '_statType', '_select'])
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
                    '/api/networking/v4.0.b1/stats/traffic-mirrors/{extId}', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='networking.v4.stats.GetTrafficMirrorStatsApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
            else:
                (data) = self.api_client._call_api(
                    '/api/networking/v4.0.b1/stats/traffic-mirrors/{extId}', 'GET',
                    path_params,
                    query_params,
                    header_params,
                    body=body_params,
                    post_params=form_params,
                    files=local_var_files,
                    response_type='networking.v4.stats.GetTrafficMirrorStatsApiResponse',  # noqa: E501
                    auth_settings=auth_settings,
                    async_req=params.get('async_req'),
                    _return_http_data_only=params.get('_return_http_data_only'),
                    _preload_content=params.get('_preload_content', True),
                    _request_timeout=params.get('_request_timeout'),
                    collection_formats=collection_formats)
                return data
        finally:
            pass
