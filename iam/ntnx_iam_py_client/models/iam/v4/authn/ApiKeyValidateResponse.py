# coding: utf-8


"""
IGNORE:
    Nutanix Iam Versioned APIs

    Manage Identity and Access Management of Nutanix clusters.  # noqa: E501

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
from ntnx_iam_py_client.models.iam.v4.authn.ApiKey import ApiKey  # noqa: F401,E501
from ntnx_iam_py_client.models.iam.v4.authn.ApiKeyCustomOptions import ApiKeyCustomOptions  # noqa: F401,E501
from ntnx_iam_py_client.models.iam.v4.authn.ApiKeyStatusType import ApiKeyStatusType  # noqa: F401,E501

class ApiKeyValidateResponse(ApiKey):

    """Response of the validate request, consists of the API key details and the Service Account ID.

    :param service_account_id: (:attr:`service_account_id`) 
    :type service_account_id: 

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
        'service_account_id': 'str',
        'name': 'str',
        'description': 'str',
        'scope': 'list[str]',
        'custom_options': 'iam.v4.authn.ApiKeyCustomOptions',
        'api_key': 'str',
        'status': 'iam.v4.authn.ApiKeyStatusType',
        'created_time': 'datetime',
        'created_by': 'str',
        'last_used_time': 'datetime',
        'expiry_time': 'datetime',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'service_account_id': 'serviceAccountId',
        'name': 'name',
        'description': 'description',
        'scope': 'scope',
        'custom_options': 'customOptions',
        'api_key': 'apiKey',
        'status': 'status',
        'created_time': 'createdTime',
        'created_by': 'createdBy',
        'last_used_time': 'lastUsedTime',
        'expiry_time': 'expiryTime',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, service_account_id=None, name=None, description=None, scope=None, custom_options=None, api_key=None, status=None, created_time=None, created_by=None, last_used_time=None, expiry_time=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ApiKey.__init__(self, name, description, scope, custom_options, api_key, status, created_time, created_by, last_used_time, expiry_time, ext_id, links, tenant_id, *args, **kwargs)
        self.__service_account_id = None
        self.discriminator = None
        if service_account_id is not None:
            self.__service_account_id = service_account_id

    def _initialize_object_type(self):
        return 'iam.v4.authn.ApiKeyValidateResponse'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def service_account_id(self):
        """
        

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__service_account_id

    @service_account_id.setter
    def service_account_id(self, service_account_id):
        if service_account_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', service_account_id):  # noqa: E501
            raise ValueError(r"Invalid value for `service_account_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__service_account_id = service_account_id

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
        if issubclass(ApiKeyValidateResponse, dict):
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
        if not isinstance(other, ApiKeyValidateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

