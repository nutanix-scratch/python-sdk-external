# coding: utf-8


"""
IGNORE:
    Nutanix Lifecycle Versioned APIs

    Manage Infrastructure, Software and Firmware Upgrades.  # noqa: E501

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

class FrameworkVersionInfo(object):

    """LCM framework version information.

    :param current_version: (:attr:`current_version`) Current LCM Version.
    :type current_version: 
    :param available_version: (:attr:`available_version`) LCM framework version present in the LCM URL.
    :type available_version: 
    :param is_update_needed: (:attr:`is_update_needed`) Boolean that indicates if LCM framework update is needed. (**Default** False)
    :type is_update_needed: 

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
        'current_version': 'str',
        'available_version': 'str',
        'is_update_needed': 'bool',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'current_version': 'currentVersion',
        'available_version': 'availableVersion',
        'is_update_needed': 'isUpdateNeeded',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, current_version=None, available_version=None, is_update_needed=False, *args, **kwargs):  # noqa: E501
        self.__current_version = None
        self.__available_version = None
        self.__is_update_needed = None
        self.discriminator = None
        if current_version is not None:
            self.__current_version = current_version
        if available_version is not None:
            self.__available_version = available_version
        if is_update_needed is not None:
            self.__is_update_needed = is_update_needed
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'lifecycle.v4.resources.FrameworkVersionInfo'

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
    def current_version(self):
        """
        Current LCM Version.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__current_version

    @current_version.setter
    def current_version(self, current_version):
        if current_version is not None and len(current_version) > 128:
            raise ValueError("Invalid value for `current_version`, length must be less than or equal to `128`")  # noqa: E501

        self.__current_version = current_version

    @property
    def available_version(self):
        """
        LCM framework version present in the LCM URL.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__available_version

    @available_version.setter
    def available_version(self, available_version):
        if available_version is not None and len(available_version) > 128:
            raise ValueError("Invalid value for `available_version`, length must be less than or equal to `128`")  # noqa: E501

        self.__available_version = available_version

    @property
    def is_update_needed(self):
        """
        Boolean that indicates if LCM framework update is needed.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_update_needed

    @is_update_needed.setter
    def is_update_needed(self, is_update_needed):

        self.__is_update_needed = is_update_needed

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
        if issubclass(FrameworkVersionInfo, dict):
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
        if not isinstance(other, FrameworkVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
