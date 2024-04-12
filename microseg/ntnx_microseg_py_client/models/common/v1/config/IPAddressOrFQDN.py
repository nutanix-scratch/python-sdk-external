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
from ntnx_microseg_py_client.models.common.v1.config.FQDN import FQDN  # noqa: F401,E501
from ntnx_microseg_py_client.models.common.v1.config.IPv4Address import IPv4Address  # noqa: F401,E501
from ntnx_microseg_py_client.models.common.v1.config.IPv6Address import IPv6Address  # noqa: F401,E501

class IPAddressOrFQDN(object):

    """An unique address that identifies a device on the internet or a local network in IPv4/IPv6 format or a Fully Qualified Domain Name. 

    :param ipv4: (:attr:`ipv4`) 
    :type ipv4: 
    :param ipv6: (:attr:`ipv6`) 
    :type ipv6: 
    :param fqdn: (:attr:`fqdn`) 
    :type fqdn: 

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
        'ipv4': 'common.v1.config.IPv4Address',
        'ipv6': 'common.v1.config.IPv6Address',
        'fqdn': 'common.v1.config.FQDN',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'ipv4': 'ipv4',
        'ipv6': 'ipv6',
        'fqdn': 'fqdn',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, ipv4=None, ipv6=None, fqdn=None, *args, **kwargs):  # noqa: E501
        self.__ipv4 = None
        self.__ipv6 = None
        self.__fqdn = None
        self.discriminator = None
        if ipv4 is not None:
            self.__ipv4 = ipv4
        if ipv6 is not None:
            self.__ipv6 = ipv6
        if fqdn is not None:
            self.__fqdn = fqdn
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'common.v1.config.IPAddressOrFQDN'

    def _initialize_object_version(self):
        return 'v1.r0.b1'

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
    def ipv4(self):
        """
        

        :type:
            :class:`~ntnx_microseg_py_client.models.common.v1.config.IPv4Address`
        """  # noqa: E501
        return self.__ipv4

    @ipv4.setter
    def ipv4(self, ipv4):

        self.__ipv4 = ipv4

    @property
    def ipv6(self):
        """
        

        :type:
            :class:`~ntnx_microseg_py_client.models.common.v1.config.IPv6Address`
        """  # noqa: E501
        return self.__ipv6

    @ipv6.setter
    def ipv6(self, ipv6):

        self.__ipv6 = ipv6

    @property
    def fqdn(self):
        """
        

        :type:
            :class:`~ntnx_microseg_py_client.models.common.v1.config.FQDN`
        """  # noqa: E501
        return self.__fqdn

    @fqdn.setter
    def fqdn(self, fqdn):

        self.__fqdn = fqdn

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
        if issubclass(IPAddressOrFQDN, dict):
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
        if not isinstance(other, IPAddressOrFQDN):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    def has_ipv4(self):
        """Returns true if `ipv4` has non-none value"""
        return self._ipv4 is None
    def has_ipv6(self):
        """Returns true if `ipv6` has non-none value"""
        return self._ipv6 is None
    def has_fqdn(self):
        """Returns true if `fqdn` has non-none value"""
        return self._fqdn is None
    def is_valid(self):
        """Returns true if any one of the attributes has non-none value"""
        return self.has_ipv4() or self.has_ipv6() or self.has_fqdn()
