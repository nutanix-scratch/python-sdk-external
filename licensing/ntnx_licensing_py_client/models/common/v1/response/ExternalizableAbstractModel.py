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
from ntnx_licensing_py_client.models.common.v1.config.TenantAwareModel import TenantAwareModel  # noqa: F401,E501
from ntnx_licensing_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501

class ExternalizableAbstractModel(TenantAwareModel):

    """A model that represents an object instance that is accessible through an API endpoint.  Instances of this type get an extId field that contains the globally unique identifier for that instance.  Externally accessible instances are always tenant aware and, therefore, extend the TenantAwareModel 

    :param ext_id: (:attr:`ext_id`) A globally unique identifier of an instance that is suitable for external consumption. 
    :type ext_id: 
    :param links: (:attr:`links`) A HATEOAS style link for the response.  Each link contains a user-friendly name identifying the link and an address for retrieving the particular resource. 
    :type links: 

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
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        TenantAwareModel.__init__(self, tenant_id, *args, **kwargs)
        self.__ext_id = None
        self.__links = None
        self.discriminator = None
        if ext_id is not None:
            self.__ext_id = ext_id
        if links is not None:
            self.__links = links

    def _initialize_object_type(self):
        return 'common.v1.response.ExternalizableAbstractModel'

    def _initialize_object_version(self):
        return 'v1.r0.b1'


    @property
    def ext_id(self):
        """
        A globally unique identifier of an instance that is suitable for external consumption. 

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__ext_id

    @ext_id.setter
    def ext_id(self, ext_id):
        if ext_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `ext_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__ext_id = ext_id

    @property
    def links(self):
        """
        A HATEOAS style link for the response.  Each link contains a user-friendly name identifying the link and an address for retrieving the particular resource. 

        :type:
             list[ :class:`~ntnx_licensing_py_client.models.common.v1.response.ApiLink` ]
        """  # noqa: E501
        return self.__links

    @links.setter
    def links(self, links):

        self.__links = links

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
        if issubclass(ExternalizableAbstractModel, dict):
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
        if not isinstance(other, ExternalizableAbstractModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

