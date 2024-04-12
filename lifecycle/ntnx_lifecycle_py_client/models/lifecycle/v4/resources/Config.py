# coding: utf-8


"""
IGNORE:
    Nutanix Lifecycle Versioned APIs

    Manage Infrastructure, Software and Firmware Upgrades.  # noqa: E501

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
from ntnx_lifecycle_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_lifecycle_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from ntnx_lifecycle_py_client.models.lifecycle.v4.resources.ConnectivityType import ConnectivityType  # noqa: F401,E501

class Config(ExternalizableAbstractModel):

    """LCM configuration on the cluster.

    :param url: (:attr:`url`) URL of the LCM repository.
    :type url: 
    :param is_auto_inventory_enabled: (:attr:`is_auto_inventory_enabled`) Indicates if the auto inventory operation is enabled. The default value is set to False. (**Default** False)
    :type is_auto_inventory_enabled: 
    :param auto_inventory_schedule: (:attr:`auto_inventory_schedule`) The scheduled time in \"%H:%M\" 24-hour format of the next inventory execution. Used when auto_inventory_enabled is set to True. The default schedule time is 03:00(AM).
    :type auto_inventory_schedule: 
    :param version: (:attr:`version`) LCM version installed on the cluster.
    :type version: 
    :param display_version: (:attr:`display_version`) User friendly display version of LCM installed on the cluster.
    :type display_version: 
    :param connectivity_type: (:attr:`connectivity_type`) 
    :type connectivity_type: 
    :param is_https_enabled: (:attr:`is_https_enabled`) Indicates if the LCM URL has HTTPS enabled. The default value is True. (**Default** False)
    :type is_https_enabled: 
    :param supported_software_entities: (:attr:`supported_software_entities`) List of entities for which One-Click upgrades are supported.
    :type supported_software_entities: 
    :param deprecated_software_entities: (:attr:`deprecated_software_entities`) List of entities for which One-Click upgrades are not available.
    :type deprecated_software_entities: 
    :param is_framework_bundle_uploaded: (:attr:`is_framework_bundle_uploaded`) Indicates if the bundle is uploaded or not. (**Default** False)
    :type is_framework_bundle_uploaded: 
    :param has_module_auto_upgrade_enabled: (:attr:`has_module_auto_upgrade_enabled`) Indicates if LCM is enabled to auto-upgrade products. The default value is False. (**Default** False)
    :type has_module_auto_upgrade_enabled: 

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
        'url': 'str',
        'is_auto_inventory_enabled': 'bool',
        'auto_inventory_schedule': 'str',
        'version': 'str',
        'display_version': 'str',
        'connectivity_type': 'lifecycle.v4.resources.ConnectivityType',
        'is_https_enabled': 'bool',
        'supported_software_entities': 'list[str]',
        'deprecated_software_entities': 'list[str]',
        'is_framework_bundle_uploaded': 'bool',
        'has_module_auto_upgrade_enabled': 'bool',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'url': 'url',
        'is_auto_inventory_enabled': 'isAutoInventoryEnabled',
        'auto_inventory_schedule': 'autoInventorySchedule',
        'version': 'version',
        'display_version': 'displayVersion',
        'connectivity_type': 'connectivityType',
        'is_https_enabled': 'isHttpsEnabled',
        'supported_software_entities': 'supportedSoftwareEntities',
        'deprecated_software_entities': 'deprecatedSoftwareEntities',
        'is_framework_bundle_uploaded': 'isFrameworkBundleUploaded',
        'has_module_auto_upgrade_enabled': 'hasModuleAutoUpgradeEnabled',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, url=None, is_auto_inventory_enabled=False, auto_inventory_schedule=None, version=None, display_version=None, connectivity_type=None, is_https_enabled=False, supported_software_entities=None, deprecated_software_entities=None, is_framework_bundle_uploaded=False, has_module_auto_upgrade_enabled=False, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__url = None
        self.__is_auto_inventory_enabled = None
        self.__auto_inventory_schedule = None
        self.__version = None
        self.__display_version = None
        self.__connectivity_type = None
        self.__is_https_enabled = None
        self.__supported_software_entities = None
        self.__deprecated_software_entities = None
        self.__is_framework_bundle_uploaded = None
        self.__has_module_auto_upgrade_enabled = None
        self.discriminator = None
        if url is not None:
            self.__url = url
        if is_auto_inventory_enabled is not None:
            self.__is_auto_inventory_enabled = is_auto_inventory_enabled
        if auto_inventory_schedule is not None:
            self.__auto_inventory_schedule = auto_inventory_schedule
        if version is not None:
            self.__version = version
        if display_version is not None:
            self.__display_version = display_version
        if connectivity_type is not None:
            self.__connectivity_type = connectivity_type
        if is_https_enabled is not None:
            self.__is_https_enabled = is_https_enabled
        if supported_software_entities is not None:
            self.__supported_software_entities = supported_software_entities
        if deprecated_software_entities is not None:
            self.__deprecated_software_entities = deprecated_software_entities
        if is_framework_bundle_uploaded is not None:
            self.__is_framework_bundle_uploaded = is_framework_bundle_uploaded
        if has_module_auto_upgrade_enabled is not None:
            self.__has_module_auto_upgrade_enabled = has_module_auto_upgrade_enabled

    def _initialize_object_type(self):
        return 'lifecycle.v4.resources.Config'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def url(self):
        """
        URL of the LCM repository.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__url

    @url.setter
    def url(self, url):
        if url is not None and not re.search('^((http[s]?|nfs):\/)?\/?([^:\/\\s]*)((\/\\w+)*(:[0-9]+)*?\/)([\\w\\-\\.]+[^#?\\s]+)(.*)?(#[\\w\\-]+)?$', url):  # noqa: E501
            raise ValueError(r"Invalid value for `url`, must be a follow pattern or equal to `/^((http[s]?|nfs):\/)?\/?([^:\/\\s]*)((\/\\w+)*(:[0-9]+)*?\/)([\\w\\-\\.]+[^#?\\s]+)(.*)?(#[\\w\\-]+)?$/`")  # noqa: E501

        self.__url = url

    @property
    def is_auto_inventory_enabled(self):
        """
        Indicates if the auto inventory operation is enabled. The default value is set to False.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_auto_inventory_enabled

    @is_auto_inventory_enabled.setter
    def is_auto_inventory_enabled(self, is_auto_inventory_enabled):

        self.__is_auto_inventory_enabled = is_auto_inventory_enabled

    @property
    def auto_inventory_schedule(self):
        """
        The scheduled time in \"%H:%M\" 24-hour format of the next inventory execution. Used when auto_inventory_enabled is set to True. The default schedule time is 03:00(AM).

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__auto_inventory_schedule

    @auto_inventory_schedule.setter
    def auto_inventory_schedule(self, auto_inventory_schedule):
        if auto_inventory_schedule is not None and not re.search('^([01]\\d|2[0-3]):([0-5]\\d)$', auto_inventory_schedule):  # noqa: E501
            raise ValueError(r"Invalid value for `auto_inventory_schedule`, must be a follow pattern or equal to `/^([01]\\d|2[0-3]):([0-5]\\d)$/`")  # noqa: E501

        self.__auto_inventory_schedule = auto_inventory_schedule

    @property
    def version(self):
        """
        LCM version installed on the cluster.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__version

    @version.setter
    def version(self, version):
        if version is not None and len(version) > 128:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `128`")  # noqa: E501

        self.__version = version

    @property
    def display_version(self):
        """
        User friendly display version of LCM installed on the cluster.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__display_version

    @display_version.setter
    def display_version(self, display_version):
        if display_version is not None and len(display_version) > 128:
            raise ValueError("Invalid value for `display_version`, length must be less than or equal to `128`")  # noqa: E501

        self.__display_version = display_version

    @property
    def connectivity_type(self):
        """
        

        :type:
            :class:`~ntnx_lifecycle_py_client.models.lifecycle.v4.resources.ConnectivityType`
        """  # noqa: E501
        return self.__connectivity_type

    @connectivity_type.setter
    def connectivity_type(self, connectivity_type):

        self.__connectivity_type = connectivity_type

    @property
    def is_https_enabled(self):
        """
        Indicates if the LCM URL has HTTPS enabled. The default value is True.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_https_enabled

    @is_https_enabled.setter
    def is_https_enabled(self, is_https_enabled):

        self.__is_https_enabled = is_https_enabled

    @property
    def supported_software_entities(self):
        """
        List of entities for which One-Click upgrades are supported.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__supported_software_entities

    @supported_software_entities.setter
    def supported_software_entities(self, supported_software_entities):

        self.__supported_software_entities = supported_software_entities

    @property
    def deprecated_software_entities(self):
        """
        List of entities for which One-Click upgrades are not available.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__deprecated_software_entities

    @deprecated_software_entities.setter
    def deprecated_software_entities(self, deprecated_software_entities):

        self.__deprecated_software_entities = deprecated_software_entities

    @property
    def is_framework_bundle_uploaded(self):
        """
        Indicates if the bundle is uploaded or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_framework_bundle_uploaded

    @is_framework_bundle_uploaded.setter
    def is_framework_bundle_uploaded(self, is_framework_bundle_uploaded):

        self.__is_framework_bundle_uploaded = is_framework_bundle_uploaded

    @property
    def has_module_auto_upgrade_enabled(self):
        """
        Indicates if LCM is enabled to auto-upgrade products. The default value is False.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__has_module_auto_upgrade_enabled

    @has_module_auto_upgrade_enabled.setter
    def has_module_auto_upgrade_enabled(self, has_module_auto_upgrade_enabled):

        self.__has_module_auto_upgrade_enabled = has_module_auto_upgrade_enabled

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
        if issubclass(Config, dict):
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
        if not isinstance(other, Config):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
