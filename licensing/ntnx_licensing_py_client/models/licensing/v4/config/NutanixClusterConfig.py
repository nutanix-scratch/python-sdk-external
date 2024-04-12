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

class NutanixClusterConfig(object):

    """Model for capturing nutanix cluster configuration

    :param id: (:attr:`id`) Attribute for nutanix cluster configuration identifier
    :type id: 
    :param category: (:attr:`category`) Attribute for nutanix cluster configuration category like nutanix_cluster
    :type category: 
    :param consumption: (:attr:`consumption`) Indicates consumption model like Subscription
    :type consumption: 
    :param billing_plan: (:attr:`billing_plan`) Attribute for capturing billing plan
    :type billing_plan: 
    :param is_pulse_required: (:attr:`is_pulse_required`) Indicates whether pulse data collection is required
    :type is_pulse_required: 

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
        'id': 'str',
        'category': 'str',
        'consumption': 'str',
        'billing_plan': 'str',
        'is_pulse_required': 'bool',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'consumption': 'consumption',
        'billing_plan': 'billingPlan',
        'is_pulse_required': 'isPulseRequired',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, id=None, category=None, consumption=None, billing_plan=None, is_pulse_required=None, *args, **kwargs):  # noqa: E501
        self.__id = None
        self.__category = None
        self.__consumption = None
        self.__billing_plan = None
        self.__is_pulse_required = None
        self.discriminator = None
        if id is not None:
            self.__id = id
        if category is not None:
            self.__category = category
        if consumption is not None:
            self.__consumption = consumption
        if billing_plan is not None:
            self.__billing_plan = billing_plan
        if is_pulse_required is not None:
            self.__is_pulse_required = is_pulse_required
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'licensing.v4.config.NutanixClusterConfig'

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
    def id(self):
        """
        Attribute for nutanix cluster configuration identifier

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__id

    @id.setter
    def id(self, id):
        if id is not None and len(id) > 100:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `100`")  # noqa: E501

        self.__id = id

    @property
    def category(self):
        """
        Attribute for nutanix cluster configuration category like nutanix_cluster

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__category

    @category.setter
    def category(self, category):
        if category is not None and len(category) > 50:
            raise ValueError("Invalid value for `category`, length must be less than or equal to `50`")  # noqa: E501

        self.__category = category

    @property
    def consumption(self):
        """
        Indicates consumption model like Subscription

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption):
        if consumption is not None and len(consumption) > 50:
            raise ValueError("Invalid value for `consumption`, length must be less than or equal to `50`")  # noqa: E501

        self.__consumption = consumption

    @property
    def billing_plan(self):
        """
        Attribute for capturing billing plan

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__billing_plan

    @billing_plan.setter
    def billing_plan(self, billing_plan):
        if billing_plan is not None and len(billing_plan) > 50:
            raise ValueError("Invalid value for `billing_plan`, length must be less than or equal to `50`")  # noqa: E501

        self.__billing_plan = billing_plan

    @property
    def is_pulse_required(self):
        """
        Indicates whether pulse data collection is required

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_pulse_required

    @is_pulse_required.setter
    def is_pulse_required(self, is_pulse_required):

        self.__is_pulse_required = is_pulse_required

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
        if issubclass(NutanixClusterConfig, dict):
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
        if not isinstance(other, NutanixClusterConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
