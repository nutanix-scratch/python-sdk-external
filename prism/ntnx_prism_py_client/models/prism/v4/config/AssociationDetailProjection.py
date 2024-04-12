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
from ntnx_prism_py_client.models.prism.v4.config.AssociationDetail import AssociationDetail  # noqa: F401,E501
from ntnx_prism_py_client.models.prism.v4.config.ResourceGroup import ResourceGroup  # noqa: F401,E501
from ntnx_prism_py_client.models.prism.v4.config.ResourceType import ResourceType  # noqa: F401,E501

class AssociationDetailProjection(AssociationDetail):

    """

    :param category_id: (:attr:`category_id`) External identifier for the given category, used across all v4 apis/entities/resources where categories are referenced.<br> The field has UUID format.<br> A type 4 UUID is generated during category creation. 
    :type category_id: 
    :param resource_type: (:attr:`resource_type`) 
    :type resource_type: 
    :param resource_group: (:attr:`resource_group`) 
    :type resource_group: 
    :param resource_id: (:attr:`resource_id`) The UUID of the entity or policy associated with the particular category. 
    :type resource_id: 

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
        'category_id': 'str',
        'resource_type': 'prism.v4.config.ResourceType',
        'resource_group': 'prism.v4.config.ResourceGroup',
        'resource_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'category_id': 'categoryId',
        'resource_type': 'resourceType',
        'resource_group': 'resourceGroup',
        'resource_id': 'resourceId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, category_id=None, resource_type=None, resource_group=None, resource_id=None, *args, **kwargs):  # noqa: E501
        AssociationDetail.__init__(self, category_id, resource_type, resource_group, resource_id, *args, **kwargs)
        self.discriminator = None

    def _initialize_object_type(self):
        return 'prism.v4.config.AssociationDetailProjection'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


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
        if issubclass(AssociationDetailProjection, dict):
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
        if not isinstance(other, AssociationDetailProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
