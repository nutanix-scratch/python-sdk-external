# coding: utf-8


"""
IGNORE:
    Nutanix Networking Versioned APIs

    Manage networking configuration on Nutanix clusters, including AHV and advanced networking.  # noqa: E501

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
from ntnx_networking_py_client.models.networking.v4.config.BondModeType import BondModeType  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.Cluster import Cluster  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.VirtualSwitch import VirtualSwitch  # noqa: F401,E501

class VirtualSwitchProjection(VirtualSwitch):

    """

    :param name: (:attr:`name`) User-visible Virtual Switch name
    :type name: required
    :param description: (:attr:`description`) Input body to configure a Virtual Switch
    :type description: 
    :param is_default: (:attr:`is_default`) Indicates whether it is a default Virtual Switch which cannot be deleted (**Default** False)
    :type is_default: 
    :param is_quick_mode: (:attr:`is_quick_mode`) When true, the node is not put in maintenance mode during the create/update operation. (**Default** False)
    :type is_quick_mode: 
    :param has_deployment_error: (:attr:`has_deployment_error`) When true, virtual switch configuration is not deployed on every node.
    :type has_deployment_error: 
    :param mtu: (:attr:`mtu`) MTU
    :type mtu: 
    :param bond_mode: (:attr:`bond_mode`) 
    :type bond_mode: required
    :param clusters: (:attr:`clusters`) Cluster configuration list
    :type clusters: required
    :param metadata: (:attr:`metadata`) 
    :type metadata: 
    :param ext_id: (:attr:`ext_id`) A globally unique identifier of an instance that is suitable for external consumption. 
    :type ext_id: 
    :param links: (:attr:`links`) A HATEOAS style link for the response.  Each link contains a user-friendly name identifying the link and an address for retrieving the particular resource. 
    :type links: 
    :param tenant_id: (:attr:`tenant_id`) A globally unique identifier that represents the tenant that owns this entity. The system automatically assigns it, and it and is immutable from an API consumer perspective (some use cases may cause this Id to change - For instance, a use case may require the transfer of ownership of the entity, but these cases are handled automatically on the server). 
    :type tenant_id: 

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
        'description': 'str',
        'is_default': 'bool',
        'is_quick_mode': 'bool',
        'has_deployment_error': 'bool',
        'mtu': 'int',
        'bond_mode': 'networking.v4.config.BondModeType',
        'clusters': 'list[networking.v4.config.Cluster]',
        'metadata': 'common.v1.config.Metadata',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_default': 'isDefault',
        'is_quick_mode': 'isQuickMode',
        'has_deployment_error': 'hasDeploymentError',
        'mtu': 'mtu',
        'bond_mode': 'bondMode',
        'clusters': 'clusters',
        'metadata': 'metadata',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, description=None, is_default=False, is_quick_mode=False, has_deployment_error=None, mtu=None, bond_mode=None, clusters=None, metadata=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        VirtualSwitch.__init__(self, name, description, is_default, is_quick_mode, has_deployment_error, mtu, bond_mode, clusters, metadata, ext_id, links, tenant_id, *args, **kwargs)
        self.discriminator = None

    def _initialize_object_type(self):
        return 'networking.v4.config.VirtualSwitchProjection'

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
        if issubclass(VirtualSwitchProjection, dict):
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
        if not isinstance(other, VirtualSwitchProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

