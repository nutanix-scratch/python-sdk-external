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
from ntnx_dataprotection_py_client.models.dataprotection.v4.config.DiskRecoveryPoint import DiskRecoveryPoint  # noqa: F401,E501

class VmRecoveryPoint(object):

    """A model that represents VM recovery point properties.

    :param vm_recovery_point_ext_id: (:attr:`vm_recovery_point_ext_id`) The external identifier that can be used to retrieve the VM recovery point using its URL.
    :type vm_recovery_point_ext_id: 
    :param consistency_group_ext_id: (:attr:`consistency_group_ext_id`) External identifier of the Consistency group which the entity was part of at the time of recovery point creation.
    :type consistency_group_ext_id: 
    :param location_agnostic_id: (:attr:`location_agnostic_id`) Location agnostic identifier of the recovery point. This identifier is used to identify the same instances of a recovery point across different sites.
    :type location_agnostic_id: 
    :param vm_ext_id: (:attr:`vm_ext_id`) VM external identifier which is captured as part of this recovery point.
    :type vm_ext_id: required
    :param vm_categories: (:attr:`vm_categories`) Category key-value pairs associated with the VM at the time of recovery point creation. The category key and value are separated by '/'. For example, a category with key 'dept' and value 'hr' will be represented as 'dept/hr'.
    :type vm_categories: 
    :param disk_recovery_points: (:attr:`disk_recovery_points`) 
    :type disk_recovery_points: 

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
        'vm_recovery_point_ext_id': 'str',
        'consistency_group_ext_id': 'str',
        'location_agnostic_id': 'str',
        'vm_ext_id': 'str',
        'vm_categories': 'list[str]',
        'disk_recovery_points': 'list[dataprotection.v4.config.DiskRecoveryPoint]',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'vm_recovery_point_ext_id': 'vmRecoveryPointExtId',
        'consistency_group_ext_id': 'consistencyGroupExtId',
        'location_agnostic_id': 'locationAgnosticId',
        'vm_ext_id': 'vmExtId',
        'vm_categories': 'vmCategories',
        'disk_recovery_points': 'diskRecoveryPoints',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, vm_recovery_point_ext_id=None, consistency_group_ext_id=None, location_agnostic_id=None, vm_ext_id=None, vm_categories=None, disk_recovery_points=None, *args, **kwargs):  # noqa: E501
        self.__vm_recovery_point_ext_id = None
        self.__consistency_group_ext_id = None
        self.__location_agnostic_id = None
        self.__vm_ext_id = None
        self.__vm_categories = None
        self.__disk_recovery_points = None
        self.discriminator = None
        if vm_recovery_point_ext_id is not None:
            self.__vm_recovery_point_ext_id = vm_recovery_point_ext_id
        if consistency_group_ext_id is not None:
            self.__consistency_group_ext_id = consistency_group_ext_id
        if location_agnostic_id is not None:
            self.__location_agnostic_id = location_agnostic_id
        self.__vm_ext_id = vm_ext_id
        if vm_categories is not None:
            self.__vm_categories = vm_categories
        if disk_recovery_points is not None:
            self.__disk_recovery_points = disk_recovery_points
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'dataprotection.v4.config.VmRecoveryPoint'

    def _initialize_object_version(self):
        return 'v4.r0.b1'

    def _populate_hidden_vars(self, kwargs):
        if "_reserved" in kwargs and kwargs["_reserved"] is not None:
            self.__dollar_reserved = kwargs["_reserved"]
        elif hasattr(self, "attribute_map") and "_reserved" in self.attribute_map and self.attribute_map["_reserved"] in kwargs and kwargs[self.attribute_map["_reserved"]] is not None:
            self.__dollar_reserved = kwargs[self.attribute_map["_reserved"]]
        else :
            self.__dollar_reserved = {"$fv": self._initialize_object_version()}
        if "_unknown_fields" in kwargs and kwargs["_unknown_fields"] is not None:
            self.__dollar_unknown_fields = kwargs["_unknown_fields"]
        elif hasattr(self, "attribute_map") and "_unknown_fields" in self.attribute_map and self.attribute_map["_unknown_fields"] in kwargs and kwargs[self.attribute_map["_unknown_fields"]] is not None:
            self.__dollar_unknown_fields = kwargs[self.attribute_map["_unknown_fields"]]
        else :
            self.__dollar_unknown_fields = {}
        if "_object_type" in kwargs and kwargs["_object_type"] is not None:
            self.__dollar_object_type = kwargs["_object_type"]
        elif hasattr(self, "attribute_map") and "_object_type" in self.attribute_map and self.attribute_map["_object_type"] in kwargs and kwargs[self.attribute_map["_object_type"]] is not None:
            self.__dollar_object_type = kwargs[self.attribute_map["_object_type"]]
        else:
            self.__dollar_object_type = self._initialize_object_type()

    def get_object_type(self):
        return self.__dollar_object_type

    def get_reserved(self):
        return self.__dollar_reserved

    def get_unknown_fields(self):
        return self.__dollar_unknown_fields

    @property
    def vm_recovery_point_ext_id(self):
        """
        The external identifier that can be used to retrieve the VM recovery point using its URL.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__vm_recovery_point_ext_id

    @vm_recovery_point_ext_id.setter
    def vm_recovery_point_ext_id(self, vm_recovery_point_ext_id):
        if vm_recovery_point_ext_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', vm_recovery_point_ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `vm_recovery_point_ext_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__vm_recovery_point_ext_id = vm_recovery_point_ext_id

    @property
    def consistency_group_ext_id(self):
        """
        External identifier of the Consistency group which the entity was part of at the time of recovery point creation.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__consistency_group_ext_id

    @consistency_group_ext_id.setter
    def consistency_group_ext_id(self, consistency_group_ext_id):
        if consistency_group_ext_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', consistency_group_ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `consistency_group_ext_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__consistency_group_ext_id = consistency_group_ext_id

    @property
    def location_agnostic_id(self):
        """
        Location agnostic identifier of the recovery point. This identifier is used to identify the same instances of a recovery point across different sites.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__location_agnostic_id

    @location_agnostic_id.setter
    def location_agnostic_id(self, location_agnostic_id):
        if location_agnostic_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', location_agnostic_id):  # noqa: E501
            raise ValueError(r"Invalid value for `location_agnostic_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__location_agnostic_id = location_agnostic_id

    @property
    def vm_ext_id(self):
        """
        VM external identifier which is captured as part of this recovery point.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__vm_ext_id

    @vm_ext_id.setter
    def vm_ext_id(self, vm_ext_id):
        if vm_ext_id is None:
            raise ValueError("Invalid value for `vm_ext_id`, must not be `None`")  # noqa: E501
        if vm_ext_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', vm_ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `vm_ext_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__vm_ext_id = vm_ext_id

    @property
    def vm_categories(self):
        """
        Category key-value pairs associated with the VM at the time of recovery point creation. The category key and value are separated by '/'. For example, a category with key 'dept' and value 'hr' will be represented as 'dept/hr'.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__vm_categories

    @vm_categories.setter
    def vm_categories(self, vm_categories):

        self.__vm_categories = vm_categories

    @property
    def disk_recovery_points(self):
        """
        

        :type:
             list[ :class:`~ntnx_dataprotection_py_client.models.dataprotection.v4.config.DiskRecoveryPoint` ]
        """  # noqa: E501
        return self.__disk_recovery_points

    @disk_recovery_points.setter
    def disk_recovery_points(self, disk_recovery_points):

        self.__disk_recovery_points = disk_recovery_points

    @property
    def _reserved(self):
        """
        

        :type:
            dict(str, :class:`~object`)
        """  # noqa: E501
        return self.__dollar_reserved

    @property
    def _object_type(self):
        """
        

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__dollar_object_type

    @property
    def _unknown_fields(self):
        """
        

        :type:
            dict(str, :class:`~object`)
        """  # noqa: E501
        return self.__dollar_unknown_fields

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
        if issubclass(VmRecoveryPoint, dict):
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
        if not isinstance(other, VmRecoveryPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
