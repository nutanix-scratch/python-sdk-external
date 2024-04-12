# coding: utf-8


"""
IGNORE:
    Nutanix Microseg Versioned APIs

    Manage Network Security Policy configuration of Nutanix clusters.  # noqa: E501

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
from ntnx_microseg_py_client.models.common.v1.config.IPv4Address import IPv4Address  # noqa: F401,E501
from ntnx_microseg_py_client.models.microseg.v4.config.AllowType import AllowType  # noqa: F401,E501
from ntnx_microseg_py_client.models.microseg.v4.config.IcmpTypeCodeSpec import IcmpTypeCodeSpec  # noqa: F401,E501
from ntnx_microseg_py_client.models.microseg.v4.config.TcpPortRangeSpec import TcpPortRangeSpec  # noqa: F401,E501
from ntnx_microseg_py_client.models.microseg.v4.config.UdpPortRangeSpec import UdpPortRangeSpec  # noqa: F401,E501

class ApplicationRuleSpec(object):

    """A rule for specifying allowed traffic for an application.

    :param secured_group_category_references: (:attr:`secured_group_category_references`) A set of network endpoints which is protected by a Network Security Policy and defined as a list of categories.
    :type secured_group_category_references: required
    :param src_allow_spec: (:attr:`src_allow_spec`) 
    :type src_allow_spec: 
    :param dest_allow_spec: (:attr:`dest_allow_spec`) 
    :type dest_allow_spec: 
    :param src_category_references: (:attr:`src_category_references`) List of categories that define a set of network endpoints as inbound.
    :type src_category_references: 
    :param dest_category_references: (:attr:`dest_category_references`) List of categories that define a set of network endpoints as outbound.
    :type dest_category_references: 
    :param src_subnet: (:attr:`src_subnet`) 
    :type src_subnet: 
    :param dest_subnet: (:attr:`dest_subnet`) 
    :type dest_subnet: 
    :param src_address_group_references: (:attr:`src_address_group_references`) A list of address group references.
    :type src_address_group_references: 
    :param dest_address_group_references: (:attr:`dest_address_group_references`) A list of address group references.
    :type dest_address_group_references: 
    :param service_group_references: (:attr:`service_group_references`) 
    :type service_group_references: 
    :param is_all_protocol_allowed: (:attr:`is_all_protocol_allowed`) Denotes if rule allows traffic for all protocol.
    :type is_all_protocol_allowed: 
    :param tcp_services: (:attr:`tcp_services`) 
    :type tcp_services: 
    :param udp_services: (:attr:`udp_services`) 
    :type udp_services: 
    :param icmp_services: (:attr:`icmp_services`) Icmp Type Code List.
    :type icmp_services: 
    :param network_function_chain_reference: (:attr:`network_function_chain_reference`) A reference to the network function chain in the rule.
    :type network_function_chain_reference: 

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
        'secured_group_category_references': 'list[str]',
        'src_allow_spec': 'microseg.v4.config.AllowType',
        'dest_allow_spec': 'microseg.v4.config.AllowType',
        'src_category_references': 'list[str]',
        'dest_category_references': 'list[str]',
        'src_subnet': 'common.v1.config.IPv4Address',
        'dest_subnet': 'common.v1.config.IPv4Address',
        'src_address_group_references': 'list[str]',
        'dest_address_group_references': 'list[str]',
        'service_group_references': 'list[str]',
        'is_all_protocol_allowed': 'bool',
        'tcp_services': 'list[microseg.v4.config.TcpPortRangeSpec]',
        'udp_services': 'list[microseg.v4.config.UdpPortRangeSpec]',
        'icmp_services': 'list[microseg.v4.config.IcmpTypeCodeSpec]',
        'network_function_chain_reference': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'secured_group_category_references': 'securedGroupCategoryReferences',
        'src_allow_spec': 'srcAllowSpec',
        'dest_allow_spec': 'destAllowSpec',
        'src_category_references': 'srcCategoryReferences',
        'dest_category_references': 'destCategoryReferences',
        'src_subnet': 'srcSubnet',
        'dest_subnet': 'destSubnet',
        'src_address_group_references': 'srcAddressGroupReferences',
        'dest_address_group_references': 'destAddressGroupReferences',
        'service_group_references': 'serviceGroupReferences',
        'is_all_protocol_allowed': 'isAllProtocolAllowed',
        'tcp_services': 'tcpServices',
        'udp_services': 'udpServices',
        'icmp_services': 'icmpServices',
        'network_function_chain_reference': 'networkFunctionChainReference',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, secured_group_category_references=None, src_allow_spec=None, dest_allow_spec=None, src_category_references=None, dest_category_references=None, src_subnet=None, dest_subnet=None, src_address_group_references=None, dest_address_group_references=None, service_group_references=None, is_all_protocol_allowed=None, tcp_services=None, udp_services=None, icmp_services=None, network_function_chain_reference=None, *args, **kwargs):  # noqa: E501
        self.__secured_group_category_references = None
        self.__src_allow_spec = None
        self.__dest_allow_spec = None
        self.__src_category_references = None
        self.__dest_category_references = None
        self.__src_subnet = None
        self.__dest_subnet = None
        self.__src_address_group_references = None
        self.__dest_address_group_references = None
        self.__service_group_references = None
        self.__is_all_protocol_allowed = None
        self.__tcp_services = None
        self.__udp_services = None
        self.__icmp_services = None
        self.__network_function_chain_reference = None
        self.discriminator = None
        self.__secured_group_category_references = secured_group_category_references
        if src_allow_spec is not None:
            self.__src_allow_spec = src_allow_spec
        if dest_allow_spec is not None:
            self.__dest_allow_spec = dest_allow_spec
        if src_category_references is not None:
            self.__src_category_references = src_category_references
        if dest_category_references is not None:
            self.__dest_category_references = dest_category_references
        if src_subnet is not None:
            self.__src_subnet = src_subnet
        if dest_subnet is not None:
            self.__dest_subnet = dest_subnet
        if src_address_group_references is not None:
            self.__src_address_group_references = src_address_group_references
        if dest_address_group_references is not None:
            self.__dest_address_group_references = dest_address_group_references
        if service_group_references is not None:
            self.__service_group_references = service_group_references
        if is_all_protocol_allowed is not None:
            self.__is_all_protocol_allowed = is_all_protocol_allowed
        if tcp_services is not None:
            self.__tcp_services = tcp_services
        if udp_services is not None:
            self.__udp_services = udp_services
        if icmp_services is not None:
            self.__icmp_services = icmp_services
        if network_function_chain_reference is not None:
            self.__network_function_chain_reference = network_function_chain_reference
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'microseg.v4.config.ApplicationRuleSpec'

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
    def secured_group_category_references(self):
        """
        A set of network endpoints which is protected by a Network Security Policy and defined as a list of categories.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__secured_group_category_references

    @secured_group_category_references.setter
    def secured_group_category_references(self, secured_group_category_references):
        if secured_group_category_references is None:
            raise ValueError("Invalid value for `secured_group_category_references`, must not be `None`")  # noqa: E501

        self.__secured_group_category_references = secured_group_category_references

    @property
    def src_allow_spec(self):
        """
        

        :type:
            :class:`~ntnx_microseg_py_client.models.microseg.v4.config.AllowType`
        """  # noqa: E501
        return self.__src_allow_spec

    @src_allow_spec.setter
    def src_allow_spec(self, src_allow_spec):

        self.__src_allow_spec = src_allow_spec

    @property
    def dest_allow_spec(self):
        """
        

        :type:
            :class:`~ntnx_microseg_py_client.models.microseg.v4.config.AllowType`
        """  # noqa: E501
        return self.__dest_allow_spec

    @dest_allow_spec.setter
    def dest_allow_spec(self, dest_allow_spec):

        self.__dest_allow_spec = dest_allow_spec

    @property
    def src_category_references(self):
        """
        List of categories that define a set of network endpoints as inbound.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__src_category_references

    @src_category_references.setter
    def src_category_references(self, src_category_references):

        self.__src_category_references = src_category_references

    @property
    def dest_category_references(self):
        """
        List of categories that define a set of network endpoints as outbound.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__dest_category_references

    @dest_category_references.setter
    def dest_category_references(self, dest_category_references):

        self.__dest_category_references = dest_category_references

    @property
    def src_subnet(self):
        """
        

        :type:
            :class:`~ntnx_microseg_py_client.models.common.v1.config.IPv4Address`
        """  # noqa: E501
        return self.__src_subnet

    @src_subnet.setter
    def src_subnet(self, src_subnet):

        self.__src_subnet = src_subnet

    @property
    def dest_subnet(self):
        """
        

        :type:
            :class:`~ntnx_microseg_py_client.models.common.v1.config.IPv4Address`
        """  # noqa: E501
        return self.__dest_subnet

    @dest_subnet.setter
    def dest_subnet(self, dest_subnet):

        self.__dest_subnet = dest_subnet

    @property
    def src_address_group_references(self):
        """
        A list of address group references.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__src_address_group_references

    @src_address_group_references.setter
    def src_address_group_references(self, src_address_group_references):

        self.__src_address_group_references = src_address_group_references

    @property
    def dest_address_group_references(self):
        """
        A list of address group references.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__dest_address_group_references

    @dest_address_group_references.setter
    def dest_address_group_references(self, dest_address_group_references):

        self.__dest_address_group_references = dest_address_group_references

    @property
    def service_group_references(self):
        """
        

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__service_group_references

    @service_group_references.setter
    def service_group_references(self, service_group_references):

        self.__service_group_references = service_group_references

    @property
    def is_all_protocol_allowed(self):
        """
        Denotes if rule allows traffic for all protocol.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_all_protocol_allowed

    @is_all_protocol_allowed.setter
    def is_all_protocol_allowed(self, is_all_protocol_allowed):

        self.__is_all_protocol_allowed = is_all_protocol_allowed

    @property
    def tcp_services(self):
        """
        

        :type:
             list[ :class:`~ntnx_microseg_py_client.models.microseg.v4.config.TcpPortRangeSpec` ]
        """  # noqa: E501
        return self.__tcp_services

    @tcp_services.setter
    def tcp_services(self, tcp_services):

        self.__tcp_services = tcp_services

    @property
    def udp_services(self):
        """
        

        :type:
             list[ :class:`~ntnx_microseg_py_client.models.microseg.v4.config.UdpPortRangeSpec` ]
        """  # noqa: E501
        return self.__udp_services

    @udp_services.setter
    def udp_services(self, udp_services):

        self.__udp_services = udp_services

    @property
    def icmp_services(self):
        """
        Icmp Type Code List.

        :type:
             list[ :class:`~ntnx_microseg_py_client.models.microseg.v4.config.IcmpTypeCodeSpec` ]
        """  # noqa: E501
        return self.__icmp_services

    @icmp_services.setter
    def icmp_services(self, icmp_services):

        self.__icmp_services = icmp_services

    @property
    def network_function_chain_reference(self):
        """
        A reference to the network function chain in the rule.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__network_function_chain_reference

    @network_function_chain_reference.setter
    def network_function_chain_reference(self, network_function_chain_reference):
        if network_function_chain_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', network_function_chain_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `network_function_chain_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__network_function_chain_reference = network_function_chain_reference

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
        if issubclass(ApplicationRuleSpec, dict):
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
        if not isinstance(other, ApplicationRuleSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

