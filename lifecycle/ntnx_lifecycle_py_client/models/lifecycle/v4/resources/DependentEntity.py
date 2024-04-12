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
from ntnx_lifecycle_py_client.models.common.v1.config.KVPair import KVPair  # noqa: F401,E501
from ntnx_lifecycle_py_client.models.lifecycle.v4.common.EntityBaseModel import EntityBaseModel  # noqa: F401,E501
from ntnx_lifecycle_py_client.models.lifecycle.v4.common.EntityType import EntityType  # noqa: F401,E501

class DependentEntity(EntityBaseModel):

    """Dependency of an LCM entity available version.

    :param dependent_versions: (:attr:`dependent_versions`) Information of the dependent entity versions for this available entity.
    :type dependent_versions: 

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
        'dependent_versions': 'list[common.v1.config.KVPair]',
        'entity_class': 'str',
        'entity_model': 'str',
        'entity_type': 'lifecycle.v4.common.EntityType',
        'entity_version': 'str',
        'hardware_family': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'dependent_versions': 'dependentVersions',
        'entity_class': 'entityClass',
        'entity_model': 'entityModel',
        'entity_type': 'entityType',
        'entity_version': 'entityVersion',
        'hardware_family': 'hardwareFamily',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, dependent_versions=None, entity_class=None, entity_model=None, entity_type=None, entity_version=None, hardware_family=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        EntityBaseModel.__init__(self, entity_class, entity_model, entity_type, entity_version, hardware_family, ext_id, links, tenant_id, *args, **kwargs)
        self.__dependent_versions = None
        self.discriminator = None
        if dependent_versions is not None:
            self.__dependent_versions = dependent_versions

    def _initialize_object_type(self):
        return 'lifecycle.v4.resources.DependentEntity'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def dependent_versions(self):
        """
        Information of the dependent entity versions for this available entity.

        :type:
             list[ :class:`~ntnx_lifecycle_py_client.models.common.v1.config.KVPair` ]
        """  # noqa: E501
        return self.__dependent_versions

    @dependent_versions.setter
    def dependent_versions(self, dependent_versions):

        self.__dependent_versions = dependent_versions

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
        if issubclass(DependentEntity, dict):
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
        if not isinstance(other, DependentEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

