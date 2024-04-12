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
from ntnx_microseg_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_microseg_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from ntnx_microseg_py_client.models.microseg.v4.config.IcmpTypeCodeSpec import IcmpTypeCodeSpec  # noqa: F401,E501
from ntnx_microseg_py_client.models.microseg.v4.config.TcpPortRangeSpec import TcpPortRangeSpec  # noqa: F401,E501
from ntnx_microseg_py_client.models.microseg.v4.config.UdpPortRangeSpec import UdpPortRangeSpec  # noqa: F401,E501

class ServiceGroup(ExternalizableAbstractModel):

    """

    :param name: (:attr:`name`) A short identifier for a Service Group.
    :type name: required
    :param description: (:attr:`description`) A user defined annotation for a Service Group.
    :type description: 
    :param is_system_defined: (:attr:`is_system_defined`) Service Group is system defined or not.
    :type is_system_defined: 
    :param tcp_services: (:attr:`tcp_services`) List of TCP ports in the service.
    :type tcp_services: 
    :param udp_services: (:attr:`udp_services`) List of UDP ports in the service.
    :type udp_services: 
    :param icmp_services: (:attr:`icmp_services`) Icmp Type Code List.
    :type icmp_services: 
    :param policy_references: (:attr:`policy_references`) Reference to policy associated with Service Group.
    :type policy_references: 
    :param created_by: (:attr:`created_by`) 
    :type created_by: 

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
        'name': 'str',
        'description': 'str',
        'is_system_defined': 'bool',
        'tcp_services': 'list[microseg.v4.config.TcpPortRangeSpec]',
        'udp_services': 'list[microseg.v4.config.UdpPortRangeSpec]',
        'icmp_services': 'list[microseg.v4.config.IcmpTypeCodeSpec]',
        'policy_references': 'list[str]',
        'created_by': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_system_defined': 'isSystemDefined',
        'tcp_services': 'tcpServices',
        'udp_services': 'udpServices',
        'icmp_services': 'icmpServices',
        'policy_references': 'policyReferences',
        'created_by': 'createdBy',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, description=None, is_system_defined=None, tcp_services=None, udp_services=None, icmp_services=None, policy_references=None, created_by=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__name = None
        self.__description = None
        self.__is_system_defined = None
        self.__tcp_services = None
        self.__udp_services = None
        self.__icmp_services = None
        self.__policy_references = None
        self.__created_by = None
        self.discriminator = None
        self.__name = name
        if description is not None:
            self.__description = description
        if is_system_defined is not None:
            self.__is_system_defined = is_system_defined
        if tcp_services is not None:
            self.__tcp_services = tcp_services
        if udp_services is not None:
            self.__udp_services = udp_services
        if icmp_services is not None:
            self.__icmp_services = icmp_services
        if policy_references is not None:
            self.__policy_references = policy_references
        if created_by is not None:
            self.__created_by = created_by

    def _initialize_object_type(self):
        return 'microseg.v4.config.ServiceGroup'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def name(self):
        """
        A short identifier for a Service Group.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501

        self.__name = name

    @property
    def description(self):
        """
        A user defined annotation for a Service Group.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__description

    @description.setter
    def description(self, description):
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501

        self.__description = description

    @property
    def is_system_defined(self):
        """
        Service Group is system defined or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_system_defined

    @is_system_defined.setter
    def is_system_defined(self, is_system_defined):

        self.__is_system_defined = is_system_defined

    @property
    def tcp_services(self):
        """
        List of TCP ports in the service.

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
        List of UDP ports in the service.

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
    def policy_references(self):
        """
        Reference to policy associated with Service Group.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__policy_references

    @policy_references.setter
    def policy_references(self, policy_references):

        self.__policy_references = policy_references

    @property
    def created_by(self):
        """
        

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__created_by

    @created_by.setter
    def created_by(self, created_by):
        if created_by is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', created_by):  # noqa: E501
            raise ValueError(r"Invalid value for `created_by`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__created_by = created_by

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
        if issubclass(ServiceGroup, dict):
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
        if not isinstance(other, ServiceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
