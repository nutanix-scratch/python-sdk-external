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
from ntnx_networking_py_client.models.networking.v4.config.GatewayNodeReference import GatewayNodeReference  # noqa: F401,E501

class ExternalSubnet(object):

    """Information about the external subnet, SNAT IPs and the gateway nodes.

    :param subnet_reference: (:attr:`subnet_reference`) External subnet reference.
    :type subnet_reference: required
    :param external_ips: (:attr:`external_ips`) List of IP Addresses used for SNAT, if NAT is enabled on the external subnet. If NAT is not enabled, this specifies the IP address of the VPC port connected to the external gateway.
    :type external_ips: 
    :param gateway_nodes: (:attr:`gateway_nodes`) List of gateway nodes that can be used for external connectivity.
    :type gateway_nodes: 
    :param active_gateway_node: (:attr:`active_gateway_node`) 
    :type active_gateway_node: 
    :param active_gateway_nodes: (:attr:`active_gateway_nodes`) Currently active gateways node that are used for external connectivity. The singleton activeGateway attribute will be deprecated.
    :type active_gateway_nodes: 
    :param active_gateway_count: (:attr:`active_gateway_count`) Maximum number of active gateway nodes for the VPC external subnet association.
    :type active_gateway_count: 

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
        'subnet_reference': 'str',
        'external_ips': 'list[common.v1.config.IPAddress]',
        'gateway_nodes': 'list[str]',
        'active_gateway_node': 'networking.v4.config.GatewayNodeReference',
        'active_gateway_nodes': 'list[networking.v4.config.GatewayNodeReference]',
        'active_gateway_count': 'int',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'subnet_reference': 'subnetReference',
        'external_ips': 'externalIps',
        'gateway_nodes': 'gatewayNodes',
        'active_gateway_node': 'activeGatewayNode',
        'active_gateway_nodes': 'activeGatewayNodes',
        'active_gateway_count': 'activeGatewayCount',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, subnet_reference=None, external_ips=None, gateway_nodes=None, active_gateway_node=None, active_gateway_nodes=None, active_gateway_count=None, *args, **kwargs):  # noqa: E501
        self.__subnet_reference = None
        self.__external_ips = None
        self.__gateway_nodes = None
        self.__active_gateway_node = None
        self.__active_gateway_nodes = None
        self.__active_gateway_count = None
        self.discriminator = None
        self.__subnet_reference = subnet_reference
        if external_ips is not None:
            self.__external_ips = external_ips
        if gateway_nodes is not None:
            self.__gateway_nodes = gateway_nodes
        if active_gateway_node is not None:
            self.__active_gateway_node = active_gateway_node
        if active_gateway_nodes is not None:
            self.__active_gateway_nodes = active_gateway_nodes
        if active_gateway_count is not None:
            self.__active_gateway_count = active_gateway_count
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'networking.v4.config.ExternalSubnet'

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
    def subnet_reference(self):
        """
        External subnet reference.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__subnet_reference

    @subnet_reference.setter
    def subnet_reference(self, subnet_reference):
        if subnet_reference is None:
            raise ValueError("Invalid value for `subnet_reference`, must not be `None`")  # noqa: E501
        if subnet_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', subnet_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `subnet_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__subnet_reference = subnet_reference

    @property
    def external_ips(self):
        """
        List of IP Addresses used for SNAT, if NAT is enabled on the external subnet. If NAT is not enabled, this specifies the IP address of the VPC port connected to the external gateway.

        :type:
             list[ :class:`~ntnx_networking_py_client.models.common.v1.config.IPAddress` ]
        """  # noqa: E501
        return self.__external_ips

    @external_ips.setter
    def external_ips(self, external_ips):

        self.__external_ips = external_ips

    @property
    def gateway_nodes(self):
        """
        List of gateway nodes that can be used for external connectivity.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__gateway_nodes

    @gateway_nodes.setter
    def gateway_nodes(self, gateway_nodes):

        self.__gateway_nodes = gateway_nodes

    @property
    def active_gateway_node(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.GatewayNodeReference`
        """  # noqa: E501
        return self.__active_gateway_node

    @active_gateway_node.setter
    def active_gateway_node(self, active_gateway_node):

        self.__active_gateway_node = active_gateway_node

    @property
    def active_gateway_nodes(self):
        """
        Currently active gateways node that are used for external connectivity. The singleton activeGateway attribute will be deprecated.

        :type:
             list[ :class:`~ntnx_networking_py_client.models.networking.v4.config.GatewayNodeReference` ]
        """  # noqa: E501
        return self.__active_gateway_nodes

    @active_gateway_nodes.setter
    def active_gateway_nodes(self, active_gateway_nodes):

        self.__active_gateway_nodes = active_gateway_nodes

    @property
    def active_gateway_count(self):
        """
        Maximum number of active gateway nodes for the VPC external subnet association.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__active_gateway_count

    @active_gateway_count.setter
    def active_gateway_count(self, active_gateway_count):
        if active_gateway_count is not None and active_gateway_count > 4:  # noqa: E501
            raise ValueError("Invalid value for `active_gateway_count`, must be a value less than or equal to `4`")  # noqa: E501
        if active_gateway_count is not None and active_gateway_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `active_gateway_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self.__active_gateway_count = active_gateway_count

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
        if issubclass(ExternalSubnet, dict):
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
        if not isinstance(other, ExternalSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
