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
from ntnx_licensing_py_client.models.licensing.v4.config.LicenseCategoryEnum import LicenseCategoryEnum  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.LicenseTypeEnum import LicenseTypeEnum  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.MeterEnum import MeterEnum  # noqa: F401,E501

class CapacityViolation(object):

    """Model for capturing capacity violation. Capacity violations are thrown when user has not applied licenses to extended capacity.

    :param type: (:attr:`type`) 
    :type type: 
    :param category: (:attr:`category`) 
    :type category: 
    :param meter: (:attr:`meter`) 
    :type meter: 
    :param insufficient_quantity: (:attr:`insufficient_quantity`) Indicates the insufficient quantity of a license.License of given quantity should be applied for a cluster to function properly
    :type insufficient_quantity: 

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
        'type': 'licensing.v4.config.LicenseTypeEnum',
        'category': 'licensing.v4.config.LicenseCategoryEnum',
        'meter': 'licensing.v4.config.MeterEnum',
        'insufficient_quantity': 'float',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'type': 'type',
        'category': 'category',
        'meter': 'meter',
        'insufficient_quantity': 'insufficientQuantity',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, type=None, category=None, meter=None, insufficient_quantity=None, *args, **kwargs):  # noqa: E501
        self.__type = None
        self.__category = None
        self.__meter = None
        self.__insufficient_quantity = None
        self.discriminator = None
        if type is not None:
            self.__type = type
        if category is not None:
            self.__category = category
        if meter is not None:
            self.__meter = meter
        if insufficient_quantity is not None:
            self.__insufficient_quantity = insufficient_quantity
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'licensing.v4.config.CapacityViolation'

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
    def type(self):
        """
        

        :type:
            :class:`~ntnx_licensing_py_client.models.licensing.v4.config.LicenseTypeEnum`
        """  # noqa: E501
        return self.__type

    @type.setter
    def type(self, type):

        self.__type = type

    @property
    def category(self):
        """
        

        :type:
            :class:`~ntnx_licensing_py_client.models.licensing.v4.config.LicenseCategoryEnum`
        """  # noqa: E501
        return self.__category

    @category.setter
    def category(self, category):

        self.__category = category

    @property
    def meter(self):
        """
        

        :type:
            :class:`~ntnx_licensing_py_client.models.licensing.v4.config.MeterEnum`
        """  # noqa: E501
        return self.__meter

    @meter.setter
    def meter(self, meter):

        self.__meter = meter

    @property
    def insufficient_quantity(self):
        """
        Indicates the insufficient quantity of a license.License of given quantity should be applied for a cluster to function properly

        :type:

                :class:`~float`
        """  # noqa: E501
        return self.__insufficient_quantity

    @insufficient_quantity.setter
    def insufficient_quantity(self, insufficient_quantity):

        self.__insufficient_quantity = insufficient_quantity

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
        if issubclass(CapacityViolation, dict):
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
        if not isinstance(other, CapacityViolation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

