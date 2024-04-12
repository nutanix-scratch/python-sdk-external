# coding: utf-8


"""
IGNORE:
    Nutanix Prism Versioned APIs

    Manage Tasks, Category Associations and Submit Batch Operations.  # noqa: E501

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

class ResourceType(object):

    """An enum denoting the associated resource types.<br> Resource types are further grouped into 2 types - entity or a policy. 


    Allowed enum values:

        - _UNKNOWN
        - _REDACTED
        - VM: A resource of type Virtual Machine.
        - MH_VM: A resource of type Virtual Machine.
        - IMAGE: A resource of type Image.
        - SUBNET: A resource of type network subnets.
        - CLUSTER: A resource of type cluster, usually refers to a PE cluster.
        - HOST: A resource representing the underlying host, the machine hosting the hypervisors and vms.
        - REPORT: A resource of type report.
        - MARKETPLACE_ITEM: A resource of type marketplace item.
        - BLUEPRINT: A resource of type blueprint.
        - APP: A resource of type app.
        - VOLUMEGROUP: A resource of type volume group.
        - IMAGE_PLACEMENT_POLICY: A policy of type 'image placement'.
        - NETWORK_SECURITY_POLICY: A policy of type 'network security'.
        - NETWORK_SECURITY_RULE: A rule of type 'network security'.
        - VM_HOST_AFFINITY_POLICY: A policy of type 'vm host affinity'; this policy decides if 2 vms should belong to the same host.
        - QOS_POLICY: A policy or rule of type 'qos policy'.
        - NGT_POLICY: A policy or rule of type 'ngt policy'.
        - PROTECTION_RULE: A policy or rule of type 'protection rule'.
        - ACCESS_CONTROL_POLICY: A policy or rule of type 'access control policy' or ACP; the rules that decide authorization of users to access an api.
        - STORAGE_POLICY: A policy or rule of type 'storage policy'.
        - IMAGE_RATE_LIMIT: A resource of type 'rate limit'.
        - RECOVERY_PLAN: A policy or rule of type 'recovery plan'
        - BUNDLE: A resource of type 'bundle'.
        - POLICY_SCHEMA: Policies like user-defined-alerts, etc.
    """
    _UNKNOWN = "$UNKNOWN"
    _REDACTED = "$REDACTED"
    VM = "VM"
    MH_VM = "MH_VM"
    IMAGE = "IMAGE"
    SUBNET = "SUBNET"
    CLUSTER = "CLUSTER"
    HOST = "HOST"
    REPORT = "REPORT"
    MARKETPLACE_ITEM = "MARKETPLACE_ITEM"
    BLUEPRINT = "BLUEPRINT"
    APP = "APP"
    VOLUMEGROUP = "VOLUMEGROUP"
    IMAGE_PLACEMENT_POLICY = "IMAGE_PLACEMENT_POLICY"
    NETWORK_SECURITY_POLICY = "NETWORK_SECURITY_POLICY"
    NETWORK_SECURITY_RULE = "NETWORK_SECURITY_RULE"
    VM_HOST_AFFINITY_POLICY = "VM_HOST_AFFINITY_POLICY"
    QOS_POLICY = "QOS_POLICY"
    NGT_POLICY = "NGT_POLICY"
    PROTECTION_RULE = "PROTECTION_RULE"
    ACCESS_CONTROL_POLICY = "ACCESS_CONTROL_POLICY"
    STORAGE_POLICY = "STORAGE_POLICY"
    IMAGE_RATE_LIMIT = "IMAGE_RATE_LIMIT"
    RECOVERY_PLAN = "RECOVERY_PLAN"
    BUNDLE = "BUNDLE"
    POLICY_SCHEMA = "POLICY_SCHEMA"


    def __init__(self, *args, **kwargs):  # noqa: E501
        self.discriminator = None
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'prism.v4.config.ResourceType'

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
        if issubclass(ResourceType, dict):
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
        if not isinstance(other, ResourceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
