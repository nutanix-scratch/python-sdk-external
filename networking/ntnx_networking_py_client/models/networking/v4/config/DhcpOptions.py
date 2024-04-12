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

class DhcpOptions(object):

    """List of DHCP options to be configured.

    :param domain_name_servers: (:attr:`domain_name_servers`) List of Domain Name Server addresses (option 6).
    :type domain_name_servers: 
    :param domain_name: (:attr:`domain_name`) The DNS domain name of the client (option 15).
    :type domain_name: 
    :param search_domains: (:attr:`search_domains`) The DNS domain search list (option 119).
    :type search_domains: 
    :param tftp_server_name: (:attr:`tftp_server_name`) TFTP server name (option 66).
    :type tftp_server_name: 
    :param boot_file_name: (:attr:`boot_file_name`) Boot file name (option 67).
    :type boot_file_name: 
    :param ntp_servers: (:attr:`ntp_servers`) List of NTP server addresses (option 42).
    :type ntp_servers: 

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
        'domain_name_servers': 'list[common.v1.config.IPAddress]',
        'domain_name': 'str',
        'search_domains': 'list[str]',
        'tftp_server_name': 'str',
        'boot_file_name': 'str',
        'ntp_servers': 'list[common.v1.config.IPAddress]',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'domain_name_servers': 'domainNameServers',
        'domain_name': 'domainName',
        'search_domains': 'searchDomains',
        'tftp_server_name': 'tftpServerName',
        'boot_file_name': 'bootFileName',
        'ntp_servers': 'ntpServers',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, domain_name_servers=None, domain_name=None, search_domains=None, tftp_server_name=None, boot_file_name=None, ntp_servers=None, *args, **kwargs):  # noqa: E501
        self.__domain_name_servers = None
        self.__domain_name = None
        self.__search_domains = None
        self.__tftp_server_name = None
        self.__boot_file_name = None
        self.__ntp_servers = None
        self.discriminator = None
        if domain_name_servers is not None:
            self.__domain_name_servers = domain_name_servers
        if domain_name is not None:
            self.__domain_name = domain_name
        if search_domains is not None:
            self.__search_domains = search_domains
        if tftp_server_name is not None:
            self.__tftp_server_name = tftp_server_name
        if boot_file_name is not None:
            self.__boot_file_name = boot_file_name
        if ntp_servers is not None:
            self.__ntp_servers = ntp_servers
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'networking.v4.config.DhcpOptions'

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
    def domain_name_servers(self):
        """
        List of Domain Name Server addresses (option 6).

        :type:
             list[ :class:`~ntnx_networking_py_client.models.common.v1.config.IPAddress` ]
        """  # noqa: E501
        return self.__domain_name_servers

    @domain_name_servers.setter
    def domain_name_servers(self, domain_name_servers):

        self.__domain_name_servers = domain_name_servers

    @property
    def domain_name(self):
        """
        The DNS domain name of the client (option 15).

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        if domain_name is not None and not re.search('^(?:[a-z0-9][\\w\\-]*[a-z0-9]*\\.)*(?:(?:(?:[a-z0-9][\\w\\-]*[a-z0-9]*)(?:\\.[a-z0-9]+)?))$', domain_name):  # noqa: E501
            raise ValueError(r"Invalid value for `domain_name`, must be a follow pattern or equal to `/^(?:[a-z0-9][\\w\\-]*[a-z0-9]*\\.)*(?:(?:(?:[a-z0-9][\\w\\-]*[a-z0-9]*)(?:\\.[a-z0-9]+)?))$/`")  # noqa: E501

        self.__domain_name = domain_name

    @property
    def search_domains(self):
        """
        The DNS domain search list (option 119).

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__search_domains

    @search_domains.setter
    def search_domains(self, search_domains):

        self.__search_domains = search_domains

    @property
    def tftp_server_name(self):
        """
        TFTP server name (option 66).

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__tftp_server_name

    @tftp_server_name.setter
    def tftp_server_name(self, tftp_server_name):

        self.__tftp_server_name = tftp_server_name

    @property
    def boot_file_name(self):
        """
        Boot file name (option 67).

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__boot_file_name

    @boot_file_name.setter
    def boot_file_name(self, boot_file_name):

        self.__boot_file_name = boot_file_name

    @property
    def ntp_servers(self):
        """
        List of NTP server addresses (option 42).

        :type:
             list[ :class:`~ntnx_networking_py_client.models.common.v1.config.IPAddress` ]
        """  # noqa: E501
        return self.__ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):

        self.__ntp_servers = ntp_servers

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
        if issubclass(DhcpOptions, dict):
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
        if not isinstance(other, DhcpOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

