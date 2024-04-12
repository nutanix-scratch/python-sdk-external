# coding: utf-8


"""
IGNORE:
    Nutanix Dataprotection Versioned APIs

    Business Continuity with full spectrum of Disaster Recovery and Backup solution. Spanning across Single PC, Cross AZ, MultiSite. Configuration of Recovery points, Protection policies, Recovery Plans. Execution and monitoring of back up and recovery orchestrations on OnPrem as well as Cloud.  # noqa: E501

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
from ntnx_dataprotection_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.dataprotection.v4.config.HostType import HostType  # noqa: F401,E501

class HostReference(ExternalizableAbstractModel):

    """Information about the Witness host site.

    :param host_type: (:attr:`host_type`) 
    :type host_type: 
    :param name: (:attr:`name`) Name of the Witness host site.
    :type name: 

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
        'host_type': 'dataprotection.v4.config.HostType',
        'name': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'host_type': 'hostType',
        'name': 'name',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, host_type=None, name=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__host_type = None
        self.__name = None
        self.discriminator = None
        if host_type is not None:
            self.__host_type = host_type
        if name is not None:
            self.__name = name

    def _initialize_object_type(self):
        return 'dataprotection.v4.config.HostReference'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def host_type(self):
        """
        

        :type:
            :class:`~ntnx_dataprotection_py_client.models.dataprotection.v4.config.HostType`
        """  # noqa: E501
        return self.__host_type

    @host_type.setter
    def host_type(self, host_type):

        self.__host_type = host_type

    @property
    def name(self):
        """
        Name of the Witness host site.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501

        self.__name = name

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
        if issubclass(HostReference, dict):
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
        if not isinstance(other, HostReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

