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
from ntnx_licensing_py_client.models.licensing.v4.config.AllowanceDetail import AllowanceDetail  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.AllowanceDetailProjection import AllowanceDetailProjection  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterAllowance import ClusterAllowance  # noqa: F401,E501
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterTypeEnum import ClusterTypeEnum  # noqa: F401,E501

class ClusterAllowanceProjection(ClusterAllowance):

    """

    :param allowance_detail_projection: (:attr:`allowance_detail_projection`) 
    :type allowance_detail_projection: 

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
        'allowance_detail_projection': 'licensing.v4.config.AllowanceDetailProjection',
        'name': 'str',
        'type': 'licensing.v4.config.ClusterTypeEnum',
        'allowance_details': 'list[licensing.v4.config.AllowanceDetail]',
        'is_multicluster': 'bool',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'allowance_detail_projection': 'allowanceDetailProjection',
        'name': 'name',
        'type': 'type',
        'allowance_details': 'allowanceDetails',
        'is_multicluster': 'isMulticluster',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, allowance_detail_projection=None, name=None, type=None, allowance_details=None, is_multicluster=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ClusterAllowance.__init__(self, name, type, allowance_details, is_multicluster, ext_id, links, tenant_id, *args, **kwargs)
        self.__allowance_detail_projection = None
        self.discriminator = None
        if allowance_detail_projection is not None:
            self.__allowance_detail_projection = allowance_detail_projection

    def _initialize_object_type(self):
        return 'licensing.v4.config.ClusterAllowanceProjection'

    def _initialize_object_version(self):
        return 'v4.r0.a1'


    @property
    def allowance_detail_projection(self):
        """
        

        :type:
            :class:`~ntnx_licensing_py_client.models.licensing.v4.config.AllowanceDetailProjection`
        """  # noqa: E501
        return self.__allowance_detail_projection

    @allowance_detail_projection.setter
    def allowance_detail_projection(self, allowance_detail_projection):

        self.__allowance_detail_projection = allowance_detail_projection

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
        if issubclass(ClusterAllowanceProjection, dict):
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
        if not isinstance(other, ClusterAllowanceProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
