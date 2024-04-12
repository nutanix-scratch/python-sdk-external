# coding: utf-8


"""
IGNORE:
    Nutanix VMM APIs

    Manage the life-cycle of virtual machines hosted on Nutanix  # noqa: E501

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

class CompleteGuestUpdateSpec(object):

    """Input to Template Complete Guest OS Update.

    :param version_name: (:attr:`version_name`) The user defined name of a Template Version.
    :type version_name: required
    :param version_description: (:attr:`version_description`) The user defined description of a Template Version.
    :type version_description: required
    :param is_active_version: (:attr:`is_active_version`) Specify whether to mark the Template Version as active or not. The newly created Version during Template Creation, Updation or Guest OS Updation is set to Active by default unless specified otherwise.  (**Default** True)
    :type is_active_version: 

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
        'version_name': 'str',
        'version_description': 'str',
        'is_active_version': 'bool',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'version_name': 'versionName',
        'version_description': 'versionDescription',
        'is_active_version': 'isActiveVersion',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, version_name=None, version_description=None, is_active_version=True, *args, **kwargs):  # noqa: E501
        self.__version_name = None
        self.__version_description = None
        self.__is_active_version = None
        self.discriminator = None
        self.__version_name = version_name
        self.__version_description = version_description
        if is_active_version is not None:
            self.__is_active_version = is_active_version
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'vmm.v4.content.CompleteGuestUpdateSpec'

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
    def version_name(self):
        """
        The user defined name of a Template Version.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__version_name

    @version_name.setter
    def version_name(self, version_name):
        if version_name is None:
            raise ValueError("Invalid value for `version_name`, must not be `None`")  # noqa: E501
        if version_name is not None and len(version_name) > 256:
            raise ValueError("Invalid value for `version_name`, length must be less than or equal to `256`")  # noqa: E501

        self.__version_name = version_name

    @property
    def version_description(self):
        """
        The user defined description of a Template Version.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__version_description

    @version_description.setter
    def version_description(self, version_description):
        if version_description is None:
            raise ValueError("Invalid value for `version_description`, must not be `None`")  # noqa: E501
        if version_description is not None and len(version_description) > 1000:
            raise ValueError("Invalid value for `version_description`, length must be less than or equal to `1000`")  # noqa: E501

        self.__version_description = version_description

    @property
    def is_active_version(self):
        """
        Specify whether to mark the Template Version as active or not. The newly created Version during Template Creation, Updation or Guest OS Updation is set to Active by default unless specified otherwise. 

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_active_version

    @is_active_version.setter
    def is_active_version(self, is_active_version):

        self.__is_active_version = is_active_version

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
        if issubclass(CompleteGuestUpdateSpec, dict):
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
        if not isinstance(other, CompleteGuestUpdateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
