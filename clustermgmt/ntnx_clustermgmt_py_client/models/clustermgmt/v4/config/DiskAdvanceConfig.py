# coding: utf-8


"""
IGNORE:
    Nutanix Clustermgmt Versioned APIs

    Manage Hosts, Clusters and other Infrastructure.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
import pprint
import json
import ast
import re  # noqa: F401

import six
from pathlib import Path
from ntnx_clustermgmt_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501

class DiskAdvanceConfig(ExternalizableAbstractModel):

    """A model that represents Disk advance config properties.

    :param is_self_encrypting_drive: (:attr:`is_self_encrypting_drive`) Indicates whether the Disk has self encryption enabled.
    :type is_self_encrypting_drive: 
    :param is_self_managed_nvme: (:attr:`is_self_managed_nvme`) Indicates if the NVMe Disk is self managed and no host/CVM reboot is required.
    :type is_self_managed_nvme: 
    :param is_password_protected: (:attr:`is_password_protected`) Indicates if the Disk is password protected.
    :type is_password_protected: 
    :param is_boot_disk: (:attr:`is_boot_disk`) Indicates if Disk is a boot Disk.
    :type is_boot_disk: 
    :param has_boot_partitions_only: (:attr:`has_boot_partitions_only`) Indicates if the Disk is boot only and no Disk operation to be run on it.
    :type has_boot_partitions_only: 
    :param is_spdk_managed: (:attr:`is_spdk_managed`) Indicates if NVMe device is managed by storage performance development kit(SPDK).
    :type is_spdk_managed: 
    :param is_online: (:attr:`is_online`) Indicates whether Disk is online or offline.
    :type is_online: 
    :param is_marked_for_removal: (:attr:`is_marked_for_removal`) Indicates if the Disk is marked for removal.
    :type is_marked_for_removal: 
    :param is_data_migrated: (:attr:`is_data_migrated`) Indicates if data migration is completed for the Disk.
    :type is_data_migrated: 
    :param is_unhealthy: (:attr:`is_unhealthy`) Indicates if the Disk is unhealthy.
    :type is_unhealthy: 
    :param is_suspected_unhealthy: (:attr:`is_suspected_unhealthy`) Indicates if the Disk is suspected to be unhealthy.
    :type is_suspected_unhealthy: 
    :param is_mounted: (:attr:`is_mounted`) Indicates if the Disk is mounted.
    :type is_mounted: 
    :param is_under_diagnosis: (:attr:`is_under_diagnosis`) Indicates if the Disk is under diagnosis.
    :type is_under_diagnosis: 
    :param is_diagnostic_info_available: (:attr:`is_diagnostic_info_available`) Indicates the Disk diagnostic info along with device related statics is present.
    :type is_diagnostic_info_available: 
    :param is_error_found_in_log: (:attr:`is_error_found_in_log`) Indicates Disk error is seen on the Disk in kernel logs or not.
    :type is_error_found_in_log: 
    :param is_planned_outage: (:attr:`is_planned_outage`) Indicates if diagnostics are running on the Disk.
    :type is_planned_outage: 

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
        'is_self_encrypting_drive': 'bool',
        'is_self_managed_nvme': 'bool',
        'is_password_protected': 'bool',
        'is_boot_disk': 'bool',
        'has_boot_partitions_only': 'bool',
        'is_spdk_managed': 'bool',
        'is_online': 'bool',
        'is_marked_for_removal': 'bool',
        'is_data_migrated': 'bool',
        'is_unhealthy': 'bool',
        'is_suspected_unhealthy': 'bool',
        'is_mounted': 'bool',
        'is_under_diagnosis': 'bool',
        'is_diagnostic_info_available': 'bool',
        'is_error_found_in_log': 'bool',
        'is_planned_outage': 'bool',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'is_self_encrypting_drive': 'isSelfEncryptingDrive',
        'is_self_managed_nvme': 'isSelfManagedNvme',
        'is_password_protected': 'isPasswordProtected',
        'is_boot_disk': 'isBootDisk',
        'has_boot_partitions_only': 'hasBootPartitionsOnly',
        'is_spdk_managed': 'isSpdkManaged',
        'is_online': 'isOnline',
        'is_marked_for_removal': 'isMarkedForRemoval',
        'is_data_migrated': 'isDataMigrated',
        'is_unhealthy': 'isUnhealthy',
        'is_suspected_unhealthy': 'isSuspectedUnhealthy',
        'is_mounted': 'isMounted',
        'is_under_diagnosis': 'isUnderDiagnosis',
        'is_diagnostic_info_available': 'isDiagnosticInfoAvailable',
        'is_error_found_in_log': 'isErrorFoundInLog',
        'is_planned_outage': 'isPlannedOutage',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, is_self_encrypting_drive=None, is_self_managed_nvme=None, is_password_protected=None, is_boot_disk=None, has_boot_partitions_only=None, is_spdk_managed=None, is_online=None, is_marked_for_removal=None, is_data_migrated=None, is_unhealthy=None, is_suspected_unhealthy=None, is_mounted=None, is_under_diagnosis=None, is_diagnostic_info_available=None, is_error_found_in_log=None, is_planned_outage=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__is_self_encrypting_drive = None
        self.__is_self_managed_nvme = None
        self.__is_password_protected = None
        self.__is_boot_disk = None
        self.__has_boot_partitions_only = None
        self.__is_spdk_managed = None
        self.__is_online = None
        self.__is_marked_for_removal = None
        self.__is_data_migrated = None
        self.__is_unhealthy = None
        self.__is_suspected_unhealthy = None
        self.__is_mounted = None
        self.__is_under_diagnosis = None
        self.__is_diagnostic_info_available = None
        self.__is_error_found_in_log = None
        self.__is_planned_outage = None
        self.discriminator = None
        if is_self_encrypting_drive is not None:
            self.__is_self_encrypting_drive = is_self_encrypting_drive
        if is_self_managed_nvme is not None:
            self.__is_self_managed_nvme = is_self_managed_nvme
        if is_password_protected is not None:
            self.__is_password_protected = is_password_protected
        if is_boot_disk is not None:
            self.__is_boot_disk = is_boot_disk
        if has_boot_partitions_only is not None:
            self.__has_boot_partitions_only = has_boot_partitions_only
        if is_spdk_managed is not None:
            self.__is_spdk_managed = is_spdk_managed
        if is_online is not None:
            self.__is_online = is_online
        if is_marked_for_removal is not None:
            self.__is_marked_for_removal = is_marked_for_removal
        if is_data_migrated is not None:
            self.__is_data_migrated = is_data_migrated
        if is_unhealthy is not None:
            self.__is_unhealthy = is_unhealthy
        if is_suspected_unhealthy is not None:
            self.__is_suspected_unhealthy = is_suspected_unhealthy
        if is_mounted is not None:
            self.__is_mounted = is_mounted
        if is_under_diagnosis is not None:
            self.__is_under_diagnosis = is_under_diagnosis
        if is_diagnostic_info_available is not None:
            self.__is_diagnostic_info_available = is_diagnostic_info_available
        if is_error_found_in_log is not None:
            self.__is_error_found_in_log = is_error_found_in_log
        if is_planned_outage is not None:
            self.__is_planned_outage = is_planned_outage

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.DiskAdvanceConfig'

    def _initialize_object_version(self):
        return 'v4.r0.b2'


    @property
    def is_self_encrypting_drive(self):
        """
        Indicates whether the Disk has self encryption enabled.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_self_encrypting_drive

    @is_self_encrypting_drive.setter
    def is_self_encrypting_drive(self, is_self_encrypting_drive):

        self.__is_self_encrypting_drive = is_self_encrypting_drive

    @property
    def is_self_managed_nvme(self):
        """
        Indicates if the NVMe Disk is self managed and no host/CVM reboot is required.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_self_managed_nvme

    @is_self_managed_nvme.setter
    def is_self_managed_nvme(self, is_self_managed_nvme):

        self.__is_self_managed_nvme = is_self_managed_nvme

    @property
    def is_password_protected(self):
        """
        Indicates if the Disk is password protected.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_password_protected

    @is_password_protected.setter
    def is_password_protected(self, is_password_protected):

        self.__is_password_protected = is_password_protected

    @property
    def is_boot_disk(self):
        """
        Indicates if Disk is a boot Disk.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_boot_disk

    @is_boot_disk.setter
    def is_boot_disk(self, is_boot_disk):

        self.__is_boot_disk = is_boot_disk

    @property
    def has_boot_partitions_only(self):
        """
        Indicates if the Disk is boot only and no Disk operation to be run on it.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__has_boot_partitions_only

    @has_boot_partitions_only.setter
    def has_boot_partitions_only(self, has_boot_partitions_only):

        self.__has_boot_partitions_only = has_boot_partitions_only

    @property
    def is_spdk_managed(self):
        """
        Indicates if NVMe device is managed by storage performance development kit(SPDK).

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_spdk_managed

    @is_spdk_managed.setter
    def is_spdk_managed(self, is_spdk_managed):

        self.__is_spdk_managed = is_spdk_managed

    @property
    def is_online(self):
        """
        Indicates whether Disk is online or offline.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_online

    @is_online.setter
    def is_online(self, is_online):

        self.__is_online = is_online

    @property
    def is_marked_for_removal(self):
        """
        Indicates if the Disk is marked for removal.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_marked_for_removal

    @is_marked_for_removal.setter
    def is_marked_for_removal(self, is_marked_for_removal):

        self.__is_marked_for_removal = is_marked_for_removal

    @property
    def is_data_migrated(self):
        """
        Indicates if data migration is completed for the Disk.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_data_migrated

    @is_data_migrated.setter
    def is_data_migrated(self, is_data_migrated):

        self.__is_data_migrated = is_data_migrated

    @property
    def is_unhealthy(self):
        """
        Indicates if the Disk is unhealthy.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_unhealthy

    @is_unhealthy.setter
    def is_unhealthy(self, is_unhealthy):

        self.__is_unhealthy = is_unhealthy

    @property
    def is_suspected_unhealthy(self):
        """
        Indicates if the Disk is suspected to be unhealthy.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_suspected_unhealthy

    @is_suspected_unhealthy.setter
    def is_suspected_unhealthy(self, is_suspected_unhealthy):

        self.__is_suspected_unhealthy = is_suspected_unhealthy

    @property
    def is_mounted(self):
        """
        Indicates if the Disk is mounted.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_mounted

    @is_mounted.setter
    def is_mounted(self, is_mounted):

        self.__is_mounted = is_mounted

    @property
    def is_under_diagnosis(self):
        """
        Indicates if the Disk is under diagnosis.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_under_diagnosis

    @is_under_diagnosis.setter
    def is_under_diagnosis(self, is_under_diagnosis):

        self.__is_under_diagnosis = is_under_diagnosis

    @property
    def is_diagnostic_info_available(self):
        """
        Indicates the Disk diagnostic info along with device related statics is present.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_diagnostic_info_available

    @is_diagnostic_info_available.setter
    def is_diagnostic_info_available(self, is_diagnostic_info_available):

        self.__is_diagnostic_info_available = is_diagnostic_info_available

    @property
    def is_error_found_in_log(self):
        """
        Indicates Disk error is seen on the Disk in kernel logs or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_error_found_in_log

    @is_error_found_in_log.setter
    def is_error_found_in_log(self, is_error_found_in_log):

        self.__is_error_found_in_log = is_error_found_in_log

    @property
    def is_planned_outage(self):
        """
        Indicates if diagnostics are running on the Disk.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_planned_outage

    @is_planned_outage.setter
    def is_planned_outage(self, is_planned_outage):

        self.__is_planned_outage = is_planned_outage

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
        if issubclass(DiskAdvanceConfig, dict):
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
        if not isinstance(other, DiskAdvanceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

