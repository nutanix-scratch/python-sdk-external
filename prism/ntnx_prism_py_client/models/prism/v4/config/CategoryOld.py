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
from ntnx_prism_py_client.models.common.v1.config.KVPair import KVPair  # noqa: F401,E501
from ntnx_prism_py_client.models.prism.v4.config.CategoryAssociationSummaryOld import CategoryAssociationSummaryOld  # noqa: F401,E501
from ntnx_prism_py_client.models.prism.v4.config.CategorySummaryOld import CategorySummaryOld  # noqa: F401,E501
from ntnx_prism_py_client.models.prism.v4.config.CategoryType import CategoryType  # noqa: F401,E501

class CategoryOld(CategorySummaryOld):

    """Denotes the type of a category.<br> There are three types of categories: SYSTEM, INTERNAL, and USER.<br> This field is immutable. 

    :param metadata: (:attr:`metadata`) Opaque metadata which can be associated to a category.<br> It is a list of key-value pairs.<br> For example, for a category 'California/SanJose' we can associate a geographical coordinate based metadata like: {'latitude': '37.3382° N' , 'longitude': '121.8863° W'}.  The server does not validate this value nor does it enforce the uniqueness or any other constraints. It is the responsibility of the user to ensure that any semantic or syntactic constraints are retained when mutating this field. 
    :type metadata: 

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
        'metadata': 'list[common.v1.config.KVPair]',
        'fq_name': 'str',
        'name': 'str',
        'parent_ext_id': 'str',
        'user_specified_name': 'str',
        'type': 'prism.v4.config.CategoryType',
        'description': 'str',
        'associations': 'list[prism.v4.config.CategoryAssociationSummaryOld]',
        'child_categories': 'list[prism.v4.config.CategorySummaryOld]',
        'owner_uuid': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'metadata': 'metadata',
        'fq_name': 'fqName',
        'name': 'name',
        'parent_ext_id': 'parentExtId',
        'user_specified_name': 'userSpecifiedName',
        'type': 'type',
        'description': 'description',
        'associations': 'associations',
        'child_categories': 'childCategories',
        'owner_uuid': 'ownerUuid',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, metadata=None, fq_name=None, name=None, parent_ext_id=None, user_specified_name=None, type=None, description=None, associations=None, child_categories=None, owner_uuid=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        CategorySummaryOld.__init__(self, fq_name, name, parent_ext_id, user_specified_name, type, description, associations, child_categories, owner_uuid, ext_id, links, tenant_id, *args, **kwargs)
        self.__metadata = None
        self.discriminator = None
        if metadata is not None:
            self.__metadata = metadata

    def _initialize_object_type(self):
        return 'prism.v4.config.CategoryOld'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def metadata(self):
        """
        Opaque metadata which can be associated to a category.<br> It is a list of key-value pairs.<br> For example, for a category 'California/SanJose' we can associate a geographical coordinate based metadata like: {'latitude': '37.3382° N' , 'longitude': '121.8863° W'}.  The server does not validate this value nor does it enforce the uniqueness or any other constraints. It is the responsibility of the user to ensure that any semantic or syntactic constraints are retained when mutating this field. 

        :type:
             list[ :class:`~ntnx_prism_py_client.models.common.v1.config.KVPair` ]
        """  # noqa: E501
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata):

        self.__metadata = metadata

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
        if issubclass(CategoryOld, dict):
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
        if not isinstance(other, CategoryOld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

