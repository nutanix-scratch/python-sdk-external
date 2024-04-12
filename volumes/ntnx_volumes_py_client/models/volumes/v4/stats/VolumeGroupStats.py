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
from ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair import TimeValuePair  # noqa: F401,E501

class VolumeGroupStats(object):

    """A model that stores the Volume group stats.

    :param volume_group_ext_id: (:attr:`volume_group_ext_id`) Uuid of the Volume Group.
    :type volume_group_ext_id: 
    :param controller_user_bytes: (:attr:`controller_user_bytes`) Controller user bytes.
    :type controller_user_bytes: 
    :param controller_num_iops: (:attr:`controller_num_iops`) Controller I/O rate measured in iops.
    :type controller_num_iops: 
    :param controller_num_read_iops: (:attr:`controller_num_read_iops`) Controller read I/O measured in iops.
    :type controller_num_read_iops: 
    :param controller_num_write_iops: (:attr:`controller_num_write_iops`) Controller write I/O measured in iops.
    :type controller_num_write_iops: 
    :param controller_io_bandwidth_k_bps: (:attr:`controller_io_bandwidth_k_bps`) Controller I/O bandwidth measured in Kbps.
    :type controller_io_bandwidth_k_bps: 
    :param controller_read_io_bandwidth_k_bps: (:attr:`controller_read_io_bandwidth_k_bps`) Controller read I/O bandwidth measured in Kbps.
    :type controller_read_io_bandwidth_k_bps: 
    :param controller_write_io_bandwidth_k_bps: (:attr:`controller_write_io_bandwidth_k_bps`) Controller write I/O bandwidth measured in Kbps.
    :type controller_write_io_bandwidth_k_bps: 
    :param controller_avg_io_latency_usecs: (:attr:`controller_avg_io_latency_usecs`) Controller average I/O latency measured in microseconds.
    :type controller_avg_io_latency_usecs: 
    :param controller_avg_read_io_latency_usecs: (:attr:`controller_avg_read_io_latency_usecs`) Controller average read I/O latency measured in microseconds.
    :type controller_avg_read_io_latency_usecs: 
    :param controller_avg_write_io_latency_usecs: (:attr:`controller_avg_write_io_latency_usecs`) Controller average write I/O latency measured in microseconds.
    :type controller_avg_write_io_latency_usecs: 

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
        'volume_group_ext_id': 'str',
        'controller_user_bytes': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_num_iops': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_num_read_iops': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_num_write_iops': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_io_bandwidth_k_bps': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_read_io_bandwidth_k_bps': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_write_io_bandwidth_k_bps': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_avg_io_latency_usecs': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_avg_read_io_latency_usecs': 'list[volumes.v4.stats.TimeValuePair]',
        'controller_avg_write_io_latency_usecs': 'list[volumes.v4.stats.TimeValuePair]',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'volume_group_ext_id': 'volumeGroupExtId',
        'controller_user_bytes': 'controllerUserBytes',
        'controller_num_iops': 'controllerNumIOPS',
        'controller_num_read_iops': 'controllerNumReadIOPS',
        'controller_num_write_iops': 'controllerNumWriteIOPS',
        'controller_io_bandwidth_k_bps': 'controllerIOBandwidthKBps',
        'controller_read_io_bandwidth_k_bps': 'controllerReadIOBandwidthKBps',
        'controller_write_io_bandwidth_k_bps': 'controllerWriteIOBandwidthKBps',
        'controller_avg_io_latency_usecs': 'controllerAvgIOLatencyUsecs',
        'controller_avg_read_io_latency_usecs': 'controllerAvgReadIOLatencyUsecs',
        'controller_avg_write_io_latency_usecs': 'controllerAvgWriteIOLatencyUsecs',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, volume_group_ext_id=None, controller_user_bytes=None, controller_num_iops=None, controller_num_read_iops=None, controller_num_write_iops=None, controller_io_bandwidth_k_bps=None, controller_read_io_bandwidth_k_bps=None, controller_write_io_bandwidth_k_bps=None, controller_avg_io_latency_usecs=None, controller_avg_read_io_latency_usecs=None, controller_avg_write_io_latency_usecs=None, *args, **kwargs):  # noqa: E501
        self.__volume_group_ext_id = None
        self.__controller_user_bytes = None
        self.__controller_num_iops = None
        self.__controller_num_read_iops = None
        self.__controller_num_write_iops = None
        self.__controller_io_bandwidth_k_bps = None
        self.__controller_read_io_bandwidth_k_bps = None
        self.__controller_write_io_bandwidth_k_bps = None
        self.__controller_avg_io_latency_usecs = None
        self.__controller_avg_read_io_latency_usecs = None
        self.__controller_avg_write_io_latency_usecs = None
        self.discriminator = None
        if volume_group_ext_id is not None:
            self.__volume_group_ext_id = volume_group_ext_id
        if controller_user_bytes is not None:
            self.__controller_user_bytes = controller_user_bytes
        if controller_num_iops is not None:
            self.__controller_num_iops = controller_num_iops
        if controller_num_read_iops is not None:
            self.__controller_num_read_iops = controller_num_read_iops
        if controller_num_write_iops is not None:
            self.__controller_num_write_iops = controller_num_write_iops
        if controller_io_bandwidth_k_bps is not None:
            self.__controller_io_bandwidth_k_bps = controller_io_bandwidth_k_bps
        if controller_read_io_bandwidth_k_bps is not None:
            self.__controller_read_io_bandwidth_k_bps = controller_read_io_bandwidth_k_bps
        if controller_write_io_bandwidth_k_bps is not None:
            self.__controller_write_io_bandwidth_k_bps = controller_write_io_bandwidth_k_bps
        if controller_avg_io_latency_usecs is not None:
            self.__controller_avg_io_latency_usecs = controller_avg_io_latency_usecs
        if controller_avg_read_io_latency_usecs is not None:
            self.__controller_avg_read_io_latency_usecs = controller_avg_read_io_latency_usecs
        if controller_avg_write_io_latency_usecs is not None:
            self.__controller_avg_write_io_latency_usecs = controller_avg_write_io_latency_usecs
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'volumes.v4.stats.VolumeGroupStats'

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
    def volume_group_ext_id(self):
        """
        Uuid of the Volume Group.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__volume_group_ext_id

    @volume_group_ext_id.setter
    def volume_group_ext_id(self, volume_group_ext_id):
        if volume_group_ext_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', volume_group_ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `volume_group_ext_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__volume_group_ext_id = volume_group_ext_id

    @property
    def controller_user_bytes(self):
        """
        Controller user bytes.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_user_bytes

    @controller_user_bytes.setter
    def controller_user_bytes(self, controller_user_bytes):

        self.__controller_user_bytes = controller_user_bytes

    @property
    def controller_num_iops(self):
        """
        Controller I/O rate measured in iops.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_num_iops

    @controller_num_iops.setter
    def controller_num_iops(self, controller_num_iops):

        self.__controller_num_iops = controller_num_iops

    @property
    def controller_num_read_iops(self):
        """
        Controller read I/O measured in iops.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_num_read_iops

    @controller_num_read_iops.setter
    def controller_num_read_iops(self, controller_num_read_iops):

        self.__controller_num_read_iops = controller_num_read_iops

    @property
    def controller_num_write_iops(self):
        """
        Controller write I/O measured in iops.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_num_write_iops

    @controller_num_write_iops.setter
    def controller_num_write_iops(self, controller_num_write_iops):

        self.__controller_num_write_iops = controller_num_write_iops

    @property
    def controller_io_bandwidth_k_bps(self):
        """
        Controller I/O bandwidth measured in Kbps.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_io_bandwidth_k_bps

    @controller_io_bandwidth_k_bps.setter
    def controller_io_bandwidth_k_bps(self, controller_io_bandwidth_k_bps):

        self.__controller_io_bandwidth_k_bps = controller_io_bandwidth_k_bps

    @property
    def controller_read_io_bandwidth_k_bps(self):
        """
        Controller read I/O bandwidth measured in Kbps.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_read_io_bandwidth_k_bps

    @controller_read_io_bandwidth_k_bps.setter
    def controller_read_io_bandwidth_k_bps(self, controller_read_io_bandwidth_k_bps):

        self.__controller_read_io_bandwidth_k_bps = controller_read_io_bandwidth_k_bps

    @property
    def controller_write_io_bandwidth_k_bps(self):
        """
        Controller write I/O bandwidth measured in Kbps.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_write_io_bandwidth_k_bps

    @controller_write_io_bandwidth_k_bps.setter
    def controller_write_io_bandwidth_k_bps(self, controller_write_io_bandwidth_k_bps):

        self.__controller_write_io_bandwidth_k_bps = controller_write_io_bandwidth_k_bps

    @property
    def controller_avg_io_latency_usecs(self):
        """
        Controller average I/O latency measured in microseconds.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_avg_io_latency_usecs

    @controller_avg_io_latency_usecs.setter
    def controller_avg_io_latency_usecs(self, controller_avg_io_latency_usecs):

        self.__controller_avg_io_latency_usecs = controller_avg_io_latency_usecs

    @property
    def controller_avg_read_io_latency_usecs(self):
        """
        Controller average read I/O latency measured in microseconds.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_avg_read_io_latency_usecs

    @controller_avg_read_io_latency_usecs.setter
    def controller_avg_read_io_latency_usecs(self, controller_avg_read_io_latency_usecs):

        self.__controller_avg_read_io_latency_usecs = controller_avg_read_io_latency_usecs

    @property
    def controller_avg_write_io_latency_usecs(self):
        """
        Controller average write I/O latency measured in microseconds.

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.stats.TimeValuePair` ]
        """  # noqa: E501
        return self.__controller_avg_write_io_latency_usecs

    @controller_avg_write_io_latency_usecs.setter
    def controller_avg_write_io_latency_usecs(self, controller_avg_write_io_latency_usecs):

        self.__controller_avg_write_io_latency_usecs = controller_avg_write_io_latency_usecs

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
        if issubclass(VolumeGroupStats, dict):
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
        if not isinstance(other, VolumeGroupStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

