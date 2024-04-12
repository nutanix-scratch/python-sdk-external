# coding: utf-8


"""
IGNORE:
    Nutanix Volumes Versioned APIs

    Configure volumes.  # noqa: E501

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

class EntityType(object):

    """


    Allowed enum values:

        - _UNKNOWN
        - _REDACTED
        - CLUSTER
        - VM
        - STORAGE_CONTAINER
        - VOLUME_GROUP
        - TASK
        - IMAGE
        - CATEGORY
        - NODE
        - VPC
        - SUBNET
        - ROUTING_POLICY
        - FLOATING_IP
        - VPN_GATEWAY
        - VPN_CONNECTION
        - DIRECT_CONNECT
        - DIRECT_CONNECT_VIF
        - VIRTUAL_NIC
        - VIRTUAL_SWITCH
        - VM_DISK
        - VOLUME_DISK
        - DISK_RECOVERY_POINT
        - VTEP_GATEWAY
    """
    _UNKNOWN = "$UNKNOWN"
    _REDACTED = "$REDACTED"
    CLUSTER = "CLUSTER"
    VM = "VM"
    STORAGE_CONTAINER = "STORAGE_CONTAINER"
    VOLUME_GROUP = "VOLUME_GROUP"
    TASK = "TASK"
    IMAGE = "IMAGE"
    CATEGORY = "CATEGORY"
    NODE = "NODE"
    VPC = "VPC"
    SUBNET = "SUBNET"
    ROUTING_POLICY = "ROUTING_POLICY"
    FLOATING_IP = "FLOATING_IP"
    VPN_GATEWAY = "VPN_GATEWAY"
    VPN_CONNECTION = "VPN_CONNECTION"
    DIRECT_CONNECT = "DIRECT_CONNECT"
    DIRECT_CONNECT_VIF = "DIRECT_CONNECT_VIF"
    VIRTUAL_NIC = "VIRTUAL_NIC"
    VIRTUAL_SWITCH = "VIRTUAL_SWITCH"
    VM_DISK = "VM_DISK"
    VOLUME_DISK = "VOLUME_DISK"
    DISK_RECOVERY_POINT = "DISK_RECOVERY_POINT"
    VTEP_GATEWAY = "VTEP_GATEWAY"


    def __init__(self, *args, **kwargs):  # noqa: E501
        self.discriminator = None
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'common.v1.config.EntityType'

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

    def _to_dict(self, sanitize):
        """Returns the model properties as a dict. Omits None properties based on the provided "sanitize" parameter.

        :param sanitize: A flag to omit None properties if set to True
        :type sanitize: bool
        """

        result = {}

        for attr in vars(self):
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
        if issubclass(EntityType, dict):
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
        if not isinstance(other, EntityType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

