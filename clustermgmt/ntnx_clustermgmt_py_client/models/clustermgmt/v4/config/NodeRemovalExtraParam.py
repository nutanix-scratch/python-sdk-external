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

class NodeRemovalExtraParam(object):

    """Extra parameters for node addition.

    :param skip_upgrade_check: (:attr:`skip_upgrade_check`) Indicates if upgrade check needs to be skip or not.
    :type skip_upgrade_check: 
    :param skip_space_check: (:attr:`skip_space_check`) Indicates if space check needs to be skip or not.
    :type skip_space_check: 
    :param skip_add_check: (:attr:`skip_add_check`) Indicates if add node check need to be skip or not.
    :type skip_add_check: 

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
        'skip_upgrade_check': 'bool',
        'skip_space_check': 'bool',
        'skip_add_check': 'bool',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'skip_upgrade_check': 'skipUpgradeCheck',
        'skip_space_check': 'skipSpaceCheck',
        'skip_add_check': 'skipAddCheck',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, skip_upgrade_check=None, skip_space_check=None, skip_add_check=None, *args, **kwargs):  # noqa: E501
        self.__skip_upgrade_check = None
        self.__skip_space_check = None
        self.__skip_add_check = None
        self.discriminator = None
        if skip_upgrade_check is not None:
            self.__skip_upgrade_check = skip_upgrade_check
        if skip_space_check is not None:
            self.__skip_space_check = skip_space_check
        if skip_add_check is not None:
            self.__skip_add_check = skip_add_check
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.NodeRemovalExtraParam'

    def _initialize_object_version(self):
        return 'v4.r0.b2'

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
    def skip_upgrade_check(self):
        """
        Indicates if upgrade check needs to be skip or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__skip_upgrade_check

    @skip_upgrade_check.setter
    def skip_upgrade_check(self, skip_upgrade_check):

        self.__skip_upgrade_check = skip_upgrade_check

    @property
    def skip_space_check(self):
        """
        Indicates if space check needs to be skip or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__skip_space_check

    @skip_space_check.setter
    def skip_space_check(self, skip_space_check):

        self.__skip_space_check = skip_space_check

    @property
    def skip_add_check(self):
        """
        Indicates if add node check need to be skip or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__skip_add_check

    @skip_add_check.setter
    def skip_add_check(self, skip_add_check):

        self.__skip_add_check = skip_add_check

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
        if issubclass(NodeRemovalExtraParam, dict):
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
        if not isinstance(other, NodeRemovalExtraParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
