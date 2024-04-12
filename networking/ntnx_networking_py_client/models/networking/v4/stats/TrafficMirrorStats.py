# coding: utf-8


"""
IGNORE:
    Nutanix Networking Versioned APIs

    Manage networking configuration on Nutanix clusters, including AHV and advanced networking.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
import pprint
import json
import ast
import re  # noqa: F401

import six
from pathlib import Path
from ntnx_networking_py_client.models.common.v1.stats.DownSamplingOperator import DownSamplingOperator  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.stats.StatsQueryResponseBase import StatsQueryResponseBase  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.stats.TrafficMirrorState import TrafficMirrorState  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.stats.TrafficMirrorStatsData import TrafficMirrorStatsData  # noqa: F401,E501

class TrafficMirrorStats(StatsQueryResponseBase):

    """Traffic mirror stats description.

    :param stats_data: (:attr:`stats_data`) 
    :type stats_data: 
    :param name: (:attr:`name`) Name of the session.
    :type name: 
    :param state: (:attr:`state`) 
    :type state: 
    :param state_message: (:attr:`state_message`) Traffic mirror stats state message.
    :type state_message: 

    """
    """
    IGNORE:
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    IGNORE
    """  # noqa: E501
    swagger_types = {
        'stats_data': 'networking.v4.stats.TrafficMirrorStatsData',
        'name': 'str',
        'state': 'networking.v4.stats.TrafficMirrorState',
        'state_message': 'str',
        'entity_uuid': 'str',
        'stat_type': 'common.v1.stats.DownSamplingOperator',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'stats_data': 'statsData',
        'name': 'name',
        'state': 'state',
        'state_message': 'stateMessage',
        'entity_uuid': 'entityUuid',
        'stat_type': 'statType',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, stats_data=None, name=None, state=None, state_message=None, entity_uuid=None, stat_type=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        StatsQueryResponseBase.__init__(self, entity_uuid, stat_type, ext_id, links, tenant_id, *args, **kwargs)
        self.__stats_data = None
        self.__name = None
        self.__state = None
        self.__state_message = None
        self.discriminator = None
        if stats_data is not None:
            self.__stats_data = stats_data
        if name is not None:
            self.__name = name
        if state is not None:
            self.__state = state
        if state_message is not None:
            self.__state_message = state_message

    def _initialize_object_type(self):
        return 'networking.v4.stats.TrafficMirrorStats'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def stats_data(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.stats.TrafficMirrorStatsData`
        """  # noqa: E501
        return self.__stats_data

    @stats_data.setter
    def stats_data(self, stats_data):

        self.__stats_data = stats_data

    @property
    def name(self):
        """
        Name of the session.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):

        self.__name = name

    @property
    def state(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.stats.TrafficMirrorState`
        """  # noqa: E501
        return self.__state

    @state.setter
    def state(self, state):

        self.__state = state

    @property
    def state_message(self):
        """
        Traffic mirror stats state message.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__state_message

    @state_message.setter
    def state_message(self, state_message):

        self.__state_message = state_message

    def _to_dict(self, sanitize):
        """Returns the model properties as a dict. Omits None properties based on the provided "sanitize" parameter.

        :param sanitize: A flag to omit None properties if set to True
        :type sanitize: bool
        """

        result = {}
        for attr, attr_type in six.iteritems(self.swagger_types):
        
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x._to_dict(sanitize) if hasattr(x, "_to_dict") else x,
                    value
                ))
            elif hasattr(value, "_to_dict"):
                result[attr] = value._to_dict(sanitize)
            elif isinstance(value, Path):
                result[attr] = str(value)
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1]._to_dict(sanitize)) if hasattr(item[1], "_to_dict")
                    else (
                        (item[0], str(item[1])) if item[0] == 'path' and '$objectType' in value and value['$objectType'] == 'pathlib.Path'
                        else item
                    ),
                    six.iteritems(value)
                ))
            else:
                if sanitize:
                    if value is not None:
                        result[attr] = value
                else:
                    result[attr] = value
        if issubclass(TrafficMirrorStats, dict):
            for key, value in six.iteritems(self):
                result[key] = value

        return result

    def to_dict(self):
        """Returns the model properties as a dictionary"""
        return self._to_dict(False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self._to_dict(True))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrafficMirrorStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

