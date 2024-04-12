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
from ntnx_dataprotection_py_client.models.dataprotection.v4.common.BaseRecoveryPoint import BaseRecoveryPoint  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.dataprotection.v4.common.RecoveryPointStatus import RecoveryPointStatus  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.dataprotection.v4.common.RecoveryPointType import RecoveryPointType  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.dataprotection.v4.common.VendorSpecificProperty import VendorSpecificProperty  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.dataprotection.v4.config.LocationReference import LocationReference  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.dataprotection.v4.config.VmRecoveryPoint import VmRecoveryPoint  # noqa: F401,E501
from ntnx_dataprotection_py_client.models.dataprotection.v4.config.VolumeGroupRecoveryPoint import VolumeGroupRecoveryPoint  # noqa: F401,E501

class RecoveryPoint(BaseRecoveryPoint):

    """Details about the recovery point along with all the captured VM and volume group recovery point(s).

    :param owner_ext_id: (:attr:`owner_ext_id`) A read only field inserted into recovery point at the time of recovery point creation, indicating the external identifier of the user who created this recovery point.
    :type owner_ext_id: 
    :param location_references: (:attr:`location_references`) List of location references where the VM or volume group recovery point are a part of the specified recovery point.
    :type location_references: 
    :param vm_recovery_points: (:attr:`vm_recovery_points`) List of VM recovery point that are a part of the specified top-level recovery point. Note that a recovery point can contain a maximum number of 30 entities. These entities can be a combination of VM(s) and volume group(s).
    :type vm_recovery_points: 
    :param volume_group_recovery_points: (:attr:`volume_group_recovery_points`) List of volume group recovery point that are a part of the specified top-level recovery point. Note that a recovery point can contain a maximum number of 30 entities. These entities can be a combination of VM(s) and volume group(s).
    :type volume_group_recovery_points: 

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
        'owner_ext_id': 'str',
        'location_references': 'list[dataprotection.v4.config.LocationReference]',
        'vm_recovery_points': 'list[dataprotection.v4.config.VmRecoveryPoint]',
        'volume_group_recovery_points': 'list[dataprotection.v4.config.VolumeGroupRecoveryPoint]',
        'location_agnostic_id': 'str',
        'name': 'str',
        'creation_time': 'datetime',
        'expiration_time': 'datetime',
        'status': 'dataprotection.v4.common.RecoveryPointStatus',
        'recovery_point_type': 'dataprotection.v4.common.RecoveryPointType',
        'vendor_specific_properties': 'list[dataprotection.v4.common.VendorSpecificProperty]',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'owner_ext_id': 'ownerExtId',
        'location_references': 'locationReferences',
        'vm_recovery_points': 'vmRecoveryPoints',
        'volume_group_recovery_points': 'volumeGroupRecoveryPoints',
        'location_agnostic_id': 'locationAgnosticId',
        'name': 'name',
        'creation_time': 'creationTime',
        'expiration_time': 'expirationTime',
        'status': 'status',
        'recovery_point_type': 'recoveryPointType',
        'vendor_specific_properties': 'vendorSpecificProperties',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, owner_ext_id=None, location_references=None, vm_recovery_points=None, volume_group_recovery_points=None, location_agnostic_id=None, name=None, creation_time=None, expiration_time=None, status=None, recovery_point_type=None, vendor_specific_properties=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        BaseRecoveryPoint.__init__(self, location_agnostic_id, name, creation_time, expiration_time, status, recovery_point_type, vendor_specific_properties, ext_id, links, tenant_id, *args, **kwargs)
        self.__owner_ext_id = None
        self.__location_references = None
        self.__vm_recovery_points = None
        self.__volume_group_recovery_points = None
        self.discriminator = None
        if owner_ext_id is not None:
            self.__owner_ext_id = owner_ext_id
        if location_references is not None:
            self.__location_references = location_references
        if vm_recovery_points is not None:
            self.__vm_recovery_points = vm_recovery_points
        if volume_group_recovery_points is not None:
            self.__volume_group_recovery_points = volume_group_recovery_points

    def _initialize_object_type(self):
        return 'dataprotection.v4.config.RecoveryPoint'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def owner_ext_id(self):
        """
        A read only field inserted into recovery point at the time of recovery point creation, indicating the external identifier of the user who created this recovery point.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__owner_ext_id

    @owner_ext_id.setter
    def owner_ext_id(self, owner_ext_id):
        if owner_ext_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', owner_ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `owner_ext_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__owner_ext_id = owner_ext_id

    @property
    def location_references(self):
        """
        List of location references where the VM or volume group recovery point are a part of the specified recovery point.

        :type:
             list[ :class:`~ntnx_dataprotection_py_client.models.dataprotection.v4.config.LocationReference` ]
        """  # noqa: E501
        return self.__location_references

    @location_references.setter
    def location_references(self, location_references):

        self.__location_references = location_references

    @property
    def vm_recovery_points(self):
        """
        List of VM recovery point that are a part of the specified top-level recovery point. Note that a recovery point can contain a maximum number of 30 entities. These entities can be a combination of VM(s) and volume group(s).

        :type:
             list[ :class:`~ntnx_dataprotection_py_client.models.dataprotection.v4.config.VmRecoveryPoint` ]
        """  # noqa: E501
        return self.__vm_recovery_points

    @vm_recovery_points.setter
    def vm_recovery_points(self, vm_recovery_points):

        self.__vm_recovery_points = vm_recovery_points

    @property
    def volume_group_recovery_points(self):
        """
        List of volume group recovery point that are a part of the specified top-level recovery point. Note that a recovery point can contain a maximum number of 30 entities. These entities can be a combination of VM(s) and volume group(s).

        :type:
             list[ :class:`~ntnx_dataprotection_py_client.models.dataprotection.v4.config.VolumeGroupRecoveryPoint` ]
        """  # noqa: E501
        return self.__volume_group_recovery_points

    @volume_group_recovery_points.setter
    def volume_group_recovery_points(self, volume_group_recovery_points):

        self.__volume_group_recovery_points = volume_group_recovery_points

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
        if issubclass(RecoveryPoint, dict):
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
        if not isinstance(other, RecoveryPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

