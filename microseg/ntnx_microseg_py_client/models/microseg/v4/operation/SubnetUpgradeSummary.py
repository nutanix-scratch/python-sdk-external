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

class SubnetUpgradeSummary(object):

    """Subnet information to be communicated for subnet upgrade as part of Flow upgrade to FNS Next-Gen.<br> The info includes vlanID, vlanName and subnetUuid. 

    :param vlan_name: (:attr:`vlan_name`) Vlan name in the upgrade.
    :type vlan_name: 
    :param vlan_id: (:attr:`vlan_id`) Vlan id used in the upgrade.
    :type vlan_id: required
    :param subnet_reference: (:attr:`subnet_reference`) Subnet ExtID used in upgrade.
    :type subnet_reference: 

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
        'vlan_name': 'str',
        'vlan_id': 'int',
        'subnet_reference': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'vlan_name': 'vlanName',
        'vlan_id': 'vlanID',
        'subnet_reference': 'subnetReference',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, vlan_name=None, vlan_id=None, subnet_reference=None, *args, **kwargs):  # noqa: E501
        self.__vlan_name = None
        self.__vlan_id = None
        self.__subnet_reference = None
        self.discriminator = None
        if vlan_name is not None:
            self.__vlan_name = vlan_name
        self.__vlan_id = vlan_id
        if subnet_reference is not None:
            self.__subnet_reference = subnet_reference
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'microseg.v4.operation.SubnetUpgradeSummary'

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
    def vlan_name(self):
        """
        Vlan name in the upgrade.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__vlan_name

    @vlan_name.setter
    def vlan_name(self, vlan_name):
        if vlan_name is not None and len(vlan_name) > 64:
            raise ValueError("Invalid value for `vlan_name`, length must be less than or equal to `64`")  # noqa: E501

        self.__vlan_name = vlan_name

    @property
    def vlan_id(self):
        """
        Vlan id used in the upgrade.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        if vlan_id is None:
            raise ValueError("Invalid value for `vlan_id`, must not be `None`")  # noqa: E501

        self.__vlan_id = vlan_id

    @property
    def subnet_reference(self):
        """
        Subnet ExtID used in upgrade.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__subnet_reference

    @subnet_reference.setter
    def subnet_reference(self, subnet_reference):
        if subnet_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', subnet_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `subnet_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__subnet_reference = subnet_reference

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
        if issubclass(SubnetUpgradeSummary, dict):
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
        if not isinstance(other, SubnetUpgradeSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

