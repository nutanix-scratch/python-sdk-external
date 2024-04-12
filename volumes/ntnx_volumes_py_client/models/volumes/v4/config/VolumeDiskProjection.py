# coding: utf-8


"""
IGNORE:
    Nutanix Volumes Versioned APIs

    Configure volumes.  # noqa: E501

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
from ntnx_volumes_py_client.models.common.v1.config.EntityReference import EntityReference  # noqa: F401,E501
from ntnx_volumes_py_client.models.volumes.v4.config.DiskStorageFeatures import DiskStorageFeatures  # noqa: F401,E501
from ntnx_volumes_py_client.models.volumes.v4.config.VolumeDisk import VolumeDisk  # noqa: F401,E501

class VolumeDiskProjection(VolumeDisk):

    """

    :param index: (:attr:`index`) Index of the disk in a Volume Group. This field is optional and immutable.
    :type index: 
    :param disk_size_bytes: (:attr:`disk_size_bytes`) Size of the disk in bytes. This field is mandatory during Volume Group creation if a new disk is being created on the storage container.
    :type disk_size_bytes: 
    :param storage_container_id: (:attr:`storage_container_id`) Storage container on which the disk must be created. This is a read-only field.
    :type storage_container_id: 
    :param description: (:attr:`description`) Volume Disk description. This is an optional field.
    :type description: 
    :param disk_data_source_reference: (:attr:`disk_data_source_reference`) 
    :type disk_data_source_reference: 
    :param disk_storage_features: (:attr:`disk_storage_features`) 
    :type disk_storage_features: 
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
        'index': 'int',
        'disk_size_bytes': 'int',
        'storage_container_id': 'str',
        'description': 'str',
        'disk_data_source_reference': 'common.v1.config.EntityReference',
        'disk_storage_features': 'volumes.v4.config.DiskStorageFeatures',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'index': 'index',
        'disk_size_bytes': 'diskSizeBytes',
        'storage_container_id': 'storageContainerId',
        'description': 'description',
        'disk_data_source_reference': 'diskDataSourceReference',
        'disk_storage_features': 'diskStorageFeatures',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, index=None, disk_size_bytes=None, storage_container_id=None, description=None, disk_data_source_reference=None, disk_storage_features=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        VolumeDisk.__init__(self, index, disk_size_bytes, storage_container_id, description, disk_data_source_reference, disk_storage_features, ext_id, links, tenant_id, *args, **kwargs)
        self.discriminator = None

    def _initialize_object_type(self):
        return 'volumes.v4.config.VolumeDiskProjection'

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
        if issubclass(VolumeDiskProjection, dict):
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
        if not isinstance(other, VolumeDiskProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
