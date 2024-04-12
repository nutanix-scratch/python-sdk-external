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
from ntnx_iam_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_iam_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501

class SystemConfig(ExternalizableAbstractModel):

    """System configuration resource.

    :param name: (:attr:`name`) Name of the system configuration.
    :type name: 
    :param value: (:attr:`value`) Value of the system configuration.
    :type value: 
    :param created_time: (:attr:`created_time`) Creation time of the system configuration.
    :type created_time: 
    :param last_updated_time: (:attr:`last_updated_time`) Last update time of the system configuration.
    :type last_updated_time: 

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
        'name': 'str',
        'value': 'str',
        'created_time': 'datetime',
        'last_updated_time': 'datetime',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'created_time': 'createdTime',
        'last_updated_time': 'lastUpdatedTime',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, value=None, created_time=None, last_updated_time=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__name = None
        self.__value = None
        self.__created_time = None
        self.__last_updated_time = None
        self.discriminator = None
        if name is not None:
            self.__name = name
        if value is not None:
            self.__value = value
        if created_time is not None:
            self.__created_time = created_time
        if last_updated_time is not None:
            self.__last_updated_time = last_updated_time

    def _initialize_object_type(self):
        return 'iam.v4.authn.SystemConfig'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def name(self):
        """
        Name of the system configuration.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search('^[^<>;\'()&+%\/\\\\\"`]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^<>;'()&+%\/\\\\\"`]*$/`")  # noqa: E501

        self.__name = name

    @property
    def value(self):
        """
        Value of the system configuration.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__value

    @value.setter
    def value(self, value):
        if value is not None and len(value) > 255:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `255`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self.__value = value

    @property
    def created_time(self):
        """
        Creation time of the system configuration.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__created_time

    @created_time.setter
    def created_time(self, created_time):

        self.__created_time = created_time

    @property
    def last_updated_time(self):
        """
        Last update time of the system configuration.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):

        self.__last_updated_time = last_updated_time

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
        if issubclass(SystemConfig, dict):
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
        if not isinstance(other, SystemConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

