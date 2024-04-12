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
from ntnx_networking_py_client.models.common.v1.config.Metadata import Metadata  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.ExportScope import ExportScope  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.ExporterProtocol import ExporterProtocol  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.NetworkingBaseModel import NetworkingBaseModel  # noqa: F401,E501

class IPFIXExporter(NetworkingBaseModel):

    """

    :param name: (:attr:`name`) Name of the IPFIX Exporter.
    :type name: required
    :param collector_ip: (:attr:`collector_ip`) The IP address of the IPFIX collector.
    :type collector_ip: required
    :param protocol: (:attr:`protocol`) 
    :type protocol: required
    :param collector_port: (:attr:`collector_port`) The port number of the IPFIX collector.
    :type collector_port: required
    :param export_rate_limit_per_node: (:attr:`export_rate_limit_per_node`) The maximum export rate in bits per second(bps) at which the exporter should try to export data.
    :type export_rate_limit_per_node: 
    :param export_scopes: (:attr:`export_scopes`) List of IPFIX exporter scopes.
    :type export_scopes: required
    :param description: (:attr:`description`) IPFIX exporter description.
    :type description: 

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
        'collector_ip': 'str',
        'protocol': 'networking.v4.config.ExporterProtocol',
        'collector_port': 'int',
        'export_rate_limit_per_node': 'int',
        'export_scopes': 'list[networking.v4.config.ExportScope]',
        'description': 'str',
        'metadata': 'common.v1.config.Metadata',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'collector_ip': 'collectorIp',
        'protocol': 'protocol',
        'collector_port': 'collectorPort',
        'export_rate_limit_per_node': 'exportRateLimitPerNode',
        'export_scopes': 'exportScopes',
        'description': 'description',
        'metadata': 'metadata',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, collector_ip=None, protocol=None, collector_port=None, export_rate_limit_per_node=None, export_scopes=None, description=None, metadata=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        NetworkingBaseModel.__init__(self, metadata, ext_id, links, tenant_id, *args, **kwargs)
        self.__name = None
        self.__collector_ip = None
        self.__protocol = None
        self.__collector_port = None
        self.__export_rate_limit_per_node = None
        self.__export_scopes = None
        self.__description = None
        self.discriminator = None
        self.__name = name
        self.__collector_ip = collector_ip
        self.__protocol = protocol
        self.__collector_port = collector_port
        if export_rate_limit_per_node is not None:
            self.__export_rate_limit_per_node = export_rate_limit_per_node
        self.__export_scopes = export_scopes
        if description is not None:
            self.__description = description

    def _initialize_object_type(self):
        return 'networking.v4.config.IPFIXExporter'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def name(self):
        """
        Name of the IPFIX Exporter.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501

        self.__name = name

    @property
    def collector_ip(self):
        """
        The IP address of the IPFIX collector.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__collector_ip

    @collector_ip.setter
    def collector_ip(self, collector_ip):
        if collector_ip is None:
            raise ValueError("Invalid value for `collector_ip`, must not be `None`")  # noqa: E501
        if collector_ip is not None and not re.search('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', collector_ip):  # noqa: E501
            raise ValueError(r"Invalid value for `collector_ip`, must be a follow pattern or equal to `/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/`")  # noqa: E501

        self.__collector_ip = collector_ip

    @property
    def protocol(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.ExporterProtocol`
        """  # noqa: E501
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol):
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self.__protocol = protocol

    @property
    def collector_port(self):
        """
        The port number of the IPFIX collector.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__collector_port

    @collector_port.setter
    def collector_port(self, collector_port):
        if collector_port is None:
            raise ValueError("Invalid value for `collector_port`, must not be `None`")  # noqa: E501

        self.__collector_port = collector_port

    @property
    def export_rate_limit_per_node(self):
        """
        The maximum export rate in bits per second(bps) at which the exporter should try to export data.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__export_rate_limit_per_node

    @export_rate_limit_per_node.setter
    def export_rate_limit_per_node(self, export_rate_limit_per_node):

        self.__export_rate_limit_per_node = export_rate_limit_per_node

    @property
    def export_scopes(self):
        """
        List of IPFIX exporter scopes.

        :type:
             list[ :class:`~ntnx_networking_py_client.models.networking.v4.config.ExportScope` ]
        """  # noqa: E501
        return self.__export_scopes

    @export_scopes.setter
    def export_scopes(self, export_scopes):
        if export_scopes is None:
            raise ValueError("Invalid value for `export_scopes`, must not be `None`")  # noqa: E501

        self.__export_scopes = export_scopes

    @property
    def description(self):
        """
        IPFIX exporter description.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__description

    @description.setter
    def description(self, description):

        self.__description = description

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
        if issubclass(IPFIXExporter, dict):
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
        if not isinstance(other, IPFIXExporter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

