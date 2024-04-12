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
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.RsyslogModuleItem import RsyslogModuleItem  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.RsyslogNetworkProtocol import RsyslogNetworkProtocol  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress import IPAddress  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501

class RsyslogServer(ExternalizableAbstractModel):

    """

    :param server_name: (:attr:`server_name`) RSYSLOG server name.
    :type server_name: required
    :param ip_address: (:attr:`ip_address`) 
    :type ip_address: required
    :param port: (:attr:`port`) RSYSLOG server port.
    :type port: required
    :param network_protocol: (:attr:`network_protocol`) 
    :type network_protocol: required
    :param modules: (:attr:`modules`) List of modules registered to RSYSLOG server.
    :type modules: 

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
        'server_name': 'str',
        'ip_address': 'common.v1.config.IPAddress',
        'port': 'int',
        'network_protocol': 'clustermgmt.v4.config.RsyslogNetworkProtocol',
        'modules': 'list[clustermgmt.v4.config.RsyslogModuleItem]',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'server_name': 'serverName',
        'ip_address': 'ipAddress',
        'port': 'port',
        'network_protocol': 'networkProtocol',
        'modules': 'modules',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, server_name=None, ip_address=None, port=None, network_protocol=None, modules=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__server_name = None
        self.__ip_address = None
        self.__port = None
        self.__network_protocol = None
        self.__modules = None
        self.discriminator = None
        self.__server_name = server_name
        self.__ip_address = ip_address
        self.__port = port
        self.__network_protocol = network_protocol
        if modules is not None:
            self.__modules = modules

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.RsyslogServer'

    def _initialize_object_version(self):
        return 'v4.r0.b2'


    @property
    def server_name(self):
        """
        RSYSLOG server name.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__server_name

    @server_name.setter
    def server_name(self, server_name):
        if server_name is None:
            raise ValueError("Invalid value for `server_name`, must not be `None`")  # noqa: E501

        self.__server_name = server_name

    @property
    def ip_address(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress`
        """  # noqa: E501
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self.__ip_address = ip_address

    @property
    def port(self):
        """
        RSYSLOG server port.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__port

    @port.setter
    def port(self, port):
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self.__port = port

    @property
    def network_protocol(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.RsyslogNetworkProtocol`
        """  # noqa: E501
        return self.__network_protocol

    @network_protocol.setter
    def network_protocol(self, network_protocol):
        if network_protocol is None:
            raise ValueError("Invalid value for `network_protocol`, must not be `None`")  # noqa: E501

        self.__network_protocol = network_protocol

    @property
    def modules(self):
        """
        List of modules registered to RSYSLOG server.

        :type:
             list[ :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.RsyslogModuleItem` ]
        """  # noqa: E501
        return self.__modules

    @modules.setter
    def modules(self, modules):

        self.__modules = modules

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
        if issubclass(RsyslogServer, dict):
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
        if not isinstance(other, RsyslogServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
