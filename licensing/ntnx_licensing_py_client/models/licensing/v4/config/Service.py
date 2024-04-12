# coding: utf-8


"""
IGNORE:
    Nutanix Licensing Versioned APIs

    licensing desc placeholder  # noqa: E501

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
from ntnx_licensing_py_client.models.licensing.v4.config.EnforcementActionsEnum import EnforcementActionsEnum  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.EnforcementLevelEnum import EnforcementLevelEnum  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.LicenseTypeEnum import LicenseTypeEnum  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.ProductNameEnum import ProductNameEnum  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.ServiceViolation import ServiceViolation  # noqa: F401,E501

class Service(object):

    """Model for capturing Service details.

    :param name: (:attr:`name`) 
    :type name: 
    :param license_type: (:attr:`license_type`) 
    :type license_type: 
    :param is_compliant: (:attr:`is_compliant`) Attribute for capturing the whether the service is compliant
    :type is_compliant: 
    :param enforcement_level: (:attr:`enforcement_level`) 
    :type enforcement_level: 
    :param enforcement_actions: (:attr:`enforcement_actions`) Attribute for capturing the list of enforcement actions corresponding to this service.
    :type enforcement_actions: 
    :param violations: (:attr:`violations`) Attribute for capturing the list of violations corresponding to this service.
    :type violations: 

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
        'name': 'licensing.v4.config.ProductNameEnum',
        'license_type': 'licensing.v4.config.LicenseTypeEnum',
        'is_compliant': 'bool',
        'enforcement_level': 'licensing.v4.config.EnforcementLevelEnum',
        'enforcement_actions': 'list[licensing.v4.config.EnforcementActionsEnum]',
        'violations': 'list[licensing.v4.config.ServiceViolation]',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'license_type': 'licenseType',
        'is_compliant': 'isCompliant',
        'enforcement_level': 'enforcementLevel',
        'enforcement_actions': 'enforcementActions',
        'violations': 'violations',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, license_type=None, is_compliant=None, enforcement_level=None, enforcement_actions=None, violations=None, *args, **kwargs):  # noqa: E501
        self.__name = None
        self.__license_type = None
        self.__is_compliant = None
        self.__enforcement_level = None
        self.__enforcement_actions = None
        self.__violations = None
        self.discriminator = None
        if name is not None:
            self.__name = name
        if license_type is not None:
            self.__license_type = license_type
        if is_compliant is not None:
            self.__is_compliant = is_compliant
        if enforcement_level is not None:
            self.__enforcement_level = enforcement_level
        if enforcement_actions is not None:
            self.__enforcement_actions = enforcement_actions
        if violations is not None:
            self.__violations = violations
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'licensing.v4.config.Service'

    def _initialize_object_version(self):
        return 'v4.r0.a1'

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
    def name(self):
        """
        

        :type:
            :class:`~ntnx_licensing_py_client.models.licensing.v4.config.ProductNameEnum`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):

        self.__name = name

    @property
    def license_type(self):
        """
        

        :type:
            :class:`~ntnx_licensing_py_client.models.licensing.v4.config.LicenseTypeEnum`
        """  # noqa: E501
        return self.__license_type

    @license_type.setter
    def license_type(self, license_type):

        self.__license_type = license_type

    @property
    def is_compliant(self):
        """
        Attribute for capturing the whether the service is compliant

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_compliant

    @is_compliant.setter
    def is_compliant(self, is_compliant):

        self.__is_compliant = is_compliant

    @property
    def enforcement_level(self):
        """
        

        :type:
            :class:`~ntnx_licensing_py_client.models.licensing.v4.config.EnforcementLevelEnum`
        """  # noqa: E501
        return self.__enforcement_level

    @enforcement_level.setter
    def enforcement_level(self, enforcement_level):

        self.__enforcement_level = enforcement_level

    @property
    def enforcement_actions(self):
        """
        Attribute for capturing the list of enforcement actions corresponding to this service.

        :type:
             list[ :class:`~ntnx_licensing_py_client.models.licensing.v4.config.EnforcementActionsEnum` ]
        """  # noqa: E501
        return self.__enforcement_actions

    @enforcement_actions.setter
    def enforcement_actions(self, enforcement_actions):

        self.__enforcement_actions = enforcement_actions

    @property
    def violations(self):
        """
        Attribute for capturing the list of violations corresponding to this service.

        :type:
             list[ :class:`~ntnx_licensing_py_client.models.licensing.v4.config.ServiceViolation` ]
        """  # noqa: E501
        return self.__violations

    @violations.setter
    def violations(self, violations):

        self.__violations = violations

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
        if issubclass(Service, dict):
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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
