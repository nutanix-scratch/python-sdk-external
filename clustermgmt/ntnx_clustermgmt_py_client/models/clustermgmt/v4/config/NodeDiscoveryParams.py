# coding: utf-8


"""
IGNORE:
    Nutanix Clustermgmt Versioned APIs

    Manage Hosts, Clusters and other Infrastructure.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
import pprint
import json
import ast
import re  # noqa: F401

import six
from pathlib import Path
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.AddressType import AddressType  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress import IPAddress  # noqa: F401,E501

class NodeDiscoveryParams(object):

    """Discover unconfigured node details.

    :param address_type: (:attr:`address_type`) 
    :type address_type: 
    :param ip_filter_list: (:attr:`ip_filter_list`) IP addresses of the unconfigured nodes.
    :type ip_filter_list: 
    :param uuid_filter_list: (:attr:`uuid_filter_list`) Unconfigured node UUIDs.
    :type uuid_filter_list: 
    :param timeout: (:attr:`timeout`) Timeout for discovering nodes in seconds.
    :type timeout: 
    :param interface_filter_list: (:attr:`interface_filter_list`) Interface name that is used for packet broadcasting.
    :type interface_filter_list: 
    :param is_manual_discovery: (:attr:`is_manual_discovery`) Indicates if the discovery is manual or not.
    :type is_manual_discovery: 

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
        'address_type': 'clustermgmt.v4.config.AddressType',
        'ip_filter_list': 'list[common.v1.config.IPAddress]',
        'uuid_filter_list': 'list[str]',
        'timeout': 'int',
        'interface_filter_list': 'list[str]',
        'is_manual_discovery': 'bool',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'address_type': 'addressType',
        'ip_filter_list': 'ipFilterList',
        'uuid_filter_list': 'uuidFilterList',
        'timeout': 'timeout',
        'interface_filter_list': 'interfaceFilterList',
        'is_manual_discovery': 'isManualDiscovery',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, address_type=None, ip_filter_list=None, uuid_filter_list=None, timeout=None, interface_filter_list=None, is_manual_discovery=None, *args, **kwargs):  # noqa: E501
        self.__address_type = None
        self.__ip_filter_list = None
        self.__uuid_filter_list = None
        self.__timeout = None
        self.__interface_filter_list = None
        self.__is_manual_discovery = None
        self.discriminator = None
        if address_type is not None:
            self.__address_type = address_type
        if ip_filter_list is not None:
            self.__ip_filter_list = ip_filter_list
        if uuid_filter_list is not None:
            self.__uuid_filter_list = uuid_filter_list
        if timeout is not None:
            self.__timeout = timeout
        if interface_filter_list is not None:
            self.__interface_filter_list = interface_filter_list
        if is_manual_discovery is not None:
            self.__is_manual_discovery = is_manual_discovery
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.NodeDiscoveryParams'

    def _initialize_object_version(self):
        return 'v4.r0.b2'

    def _populate_hidden_vars(self, kwargs):
        if "_reserved" in kwargs and kwargs["_reserved"] is not None:
            self.__dollar_reserved = kwargs["_reserved"]
        elif hasattr(self, "attribute_map") and "_reserved" in self.attribute_map and self.attribute_map["_reserved"] in kwargs and kwargs[self.attribute_map["_reserved"]] is not None:
            self.__dollar_reserved = kwargs[self.attribute_map["_reserved"]]
        else :
            self.__dollar_reserved = {"$fv": self._initialize_object_version()}
        if "_unknown_fields" in kwargs and kwargs["_unknown_fields"] is not None:
            self.__dollar_unknown_fields = kwargs["_unknown_fields"]
        elif hasattr(self, "attribute_map") and "_unknown_fields" in self.attribute_map and self.attribute_map["_unknown_fields"] in kwargs and kwargs[self.attribute_map["_unknown_fields"]] is not None:
            self.__dollar_unknown_fields = kwargs[self.attribute_map["_unknown_fields"]]
        else :
            self.__dollar_unknown_fields = {}
        if "_object_type" in kwargs and kwargs["_object_type"] is not None:
            self.__dollar_object_type = kwargs["_object_type"]
        elif hasattr(self, "attribute_map") and "_object_type" in self.attribute_map and self.attribute_map["_object_type"] in kwargs and kwargs[self.attribute_map["_object_type"]] is not None:
            self.__dollar_object_type = kwargs[self.attribute_map["_object_type"]]
        else:
            self.__dollar_object_type = self._initialize_object_type()

    def get_object_type(self):
        return self.__dollar_object_type

    def get_reserved(self):
        return self.__dollar_reserved

    def get_unknown_fields(self):
        return self.__dollar_unknown_fields

    @property
    def address_type(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.AddressType`
        """  # noqa: E501
        return self.__address_type

    @address_type.setter
    def address_type(self, address_type):

        self.__address_type = address_type

    @property
    def ip_filter_list(self):
        """
        IP addresses of the unconfigured nodes.

        :type:
             list[ :class:`~ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress` ]
        """  # noqa: E501
        return self.__ip_filter_list

    @ip_filter_list.setter
    def ip_filter_list(self, ip_filter_list):

        self.__ip_filter_list = ip_filter_list

    @property
    def uuid_filter_list(self):
        """
        Unconfigured node UUIDs.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__uuid_filter_list

    @uuid_filter_list.setter
    def uuid_filter_list(self, uuid_filter_list):

        self.__uuid_filter_list = uuid_filter_list

    @property
    def timeout(self):
        """
        Timeout for discovering nodes in seconds.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout):

        self.__timeout = timeout

    @property
    def interface_filter_list(self):
        """
        Interface name that is used for packet broadcasting.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__interface_filter_list

    @interface_filter_list.setter
    def interface_filter_list(self, interface_filter_list):

        self.__interface_filter_list = interface_filter_list

    @property
    def is_manual_discovery(self):
        """
        Indicates if the discovery is manual or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_manual_discovery

    @is_manual_discovery.setter
    def is_manual_discovery(self, is_manual_discovery):

        self.__is_manual_discovery = is_manual_discovery

    @property
    def _reserved(self):
        """
        

        :type:
            dict(str, :class:`~object`)
        """  # noqa: E501
        return self.__dollar_reserved

    @property
    def _object_type(self):
        """
        

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__dollar_object_type

    @property
    def _unknown_fields(self):
        """
        

        :type:
            dict(str, :class:`~object`)
        """  # noqa: E501
        return self.__dollar_unknown_fields

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
        if issubclass(NodeDiscoveryParams, dict):
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
        if not isinstance(other, NodeDiscoveryParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

