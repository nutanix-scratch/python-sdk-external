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
from ntnx_networking_py_client.models.common.v1.config.IPAddress import IPAddress  # noqa: F401,E501

class SiteParams(object):

    """Site-specific stretch configuration parameters.

    :param pc_cluster_reference: (:attr:`pc_cluster_reference`) Prism Central cluster reference.
    :type pc_cluster_reference: 
    :param stretch_subnet_reference: (:attr:`stretch_subnet_reference`) Subnet reference.
    :type stretch_subnet_reference: 
    :param connection_reference: (:attr:`connection_reference`) The VPN connection or network gateway with VTEP service used for this Layer2 stretch.
    :type connection_reference: 
    :param stretch_interface_ip_address: (:attr:`stretch_interface_ip_address`) 
    :type stretch_interface_ip_address: 
    :param vpn_interface_ip_address: (:attr:`vpn_interface_ip_address`) 
    :type vpn_interface_ip_address: 
    :param default_gateway_ip_address: (:attr:`default_gateway_ip_address`) 
    :type default_gateway_ip_address: 

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
        'pc_cluster_reference': 'str',
        'stretch_subnet_reference': 'str',
        'connection_reference': 'str',
        'stretch_interface_ip_address': 'common.v1.config.IPAddress',
        'vpn_interface_ip_address': 'common.v1.config.IPAddress',
        'default_gateway_ip_address': 'common.v1.config.IPAddress',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'pc_cluster_reference': 'pcClusterReference',
        'stretch_subnet_reference': 'stretchSubnetReference',
        'connection_reference': 'connectionReference',
        'stretch_interface_ip_address': 'stretchInterfaceIpAddress',
        'vpn_interface_ip_address': 'vpnInterfaceIPAddress',
        'default_gateway_ip_address': 'defaultGatewayIPAddress',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, pc_cluster_reference=None, stretch_subnet_reference=None, connection_reference=None, stretch_interface_ip_address=None, vpn_interface_ip_address=None, default_gateway_ip_address=None, *args, **kwargs):  # noqa: E501
        self.__pc_cluster_reference = None
        self.__stretch_subnet_reference = None
        self.__connection_reference = None
        self.__stretch_interface_ip_address = None
        self.__vpn_interface_ip_address = None
        self.__default_gateway_ip_address = None
        self.discriminator = None
        if pc_cluster_reference is not None:
            self.__pc_cluster_reference = pc_cluster_reference
        if stretch_subnet_reference is not None:
            self.__stretch_subnet_reference = stretch_subnet_reference
        if connection_reference is not None:
            self.__connection_reference = connection_reference
        if stretch_interface_ip_address is not None:
            self.__stretch_interface_ip_address = stretch_interface_ip_address
        if vpn_interface_ip_address is not None:
            self.__vpn_interface_ip_address = vpn_interface_ip_address
        if default_gateway_ip_address is not None:
            self.__default_gateway_ip_address = default_gateway_ip_address
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'networking.v4.config.SiteParams'

    def _initialize_object_version(self):
        return 'v4.r0.b1'

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
    def pc_cluster_reference(self):
        """
        Prism Central cluster reference.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__pc_cluster_reference

    @pc_cluster_reference.setter
    def pc_cluster_reference(self, pc_cluster_reference):
        if pc_cluster_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', pc_cluster_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `pc_cluster_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__pc_cluster_reference = pc_cluster_reference

    @property
    def stretch_subnet_reference(self):
        """
        Subnet reference.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__stretch_subnet_reference

    @stretch_subnet_reference.setter
    def stretch_subnet_reference(self, stretch_subnet_reference):
        if stretch_subnet_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', stretch_subnet_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `stretch_subnet_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__stretch_subnet_reference = stretch_subnet_reference

    @property
    def connection_reference(self):
        """
        The VPN connection or network gateway with VTEP service used for this Layer2 stretch.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__connection_reference

    @connection_reference.setter
    def connection_reference(self, connection_reference):
        if connection_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', connection_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `connection_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__connection_reference = connection_reference

    @property
    def stretch_interface_ip_address(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.common.v1.config.IPAddress`
        """  # noqa: E501
        return self.__stretch_interface_ip_address

    @stretch_interface_ip_address.setter
    def stretch_interface_ip_address(self, stretch_interface_ip_address):

        self.__stretch_interface_ip_address = stretch_interface_ip_address

    @property
    def vpn_interface_ip_address(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.common.v1.config.IPAddress`
        """  # noqa: E501
        return self.__vpn_interface_ip_address

    @vpn_interface_ip_address.setter
    def vpn_interface_ip_address(self, vpn_interface_ip_address):

        self.__vpn_interface_ip_address = vpn_interface_ip_address

    @property
    def default_gateway_ip_address(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.common.v1.config.IPAddress`
        """  # noqa: E501
        return self.__default_gateway_ip_address

    @default_gateway_ip_address.setter
    def default_gateway_ip_address(self, default_gateway_ip_address):

        self.__default_gateway_ip_address = default_gateway_ip_address

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
        if issubclass(SiteParams, dict):
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
        if not isinstance(other, SiteParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

