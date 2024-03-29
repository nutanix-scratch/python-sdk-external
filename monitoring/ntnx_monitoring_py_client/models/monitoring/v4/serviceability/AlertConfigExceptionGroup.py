# coding: utf-8


"""
IGNORE:
    Nutanix Monitoring Versioned APIs

    Manage Alerts, Alert policies, Events and Audits  # noqa: E501

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
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.AutoResolve import AutoResolve  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.SeverityThresholdInfo import SeverityThresholdInfo  # noqa: F401,E501

class AlertConfigExceptionGroup(object):

    """

    :param auto_resolve: (:attr:`auto_resolve`) 
    :type auto_resolve: 
    :param cluster_uuids: (:attr:`cluster_uuids`) List of cluster UUIDs on which the exceptions can be set.
    :type cluster_uuids: 
    :param severity_threshold_infos: (:attr:`severity_threshold_infos`) Enable/Disable for each severity information.
    :type severity_threshold_infos: 

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
        'auto_resolve': 'monitoring.v4.serviceability.AutoResolve',
        'cluster_uuids': 'list[str]',
        'severity_threshold_infos': 'list[monitoring.v4.serviceability.SeverityThresholdInfo]',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'auto_resolve': 'autoResolve',
        'cluster_uuids': 'clusterUuids',
        'severity_threshold_infos': 'severityThresholdInfos',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, auto_resolve=None, cluster_uuids=None, severity_threshold_infos=None, *args, **kwargs):  # noqa: E501
        self.__auto_resolve = None
        self.__cluster_uuids = None
        self.__severity_threshold_infos = None
        self.discriminator = None
        if auto_resolve is not None:
            self.__auto_resolve = auto_resolve
        if cluster_uuids is not None:
            self.__cluster_uuids = cluster_uuids
        if severity_threshold_infos is not None:
            self.__severity_threshold_infos = severity_threshold_infos
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'monitoring.v4.serviceability.AlertConfigExceptionGroup'

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
    def auto_resolve(self):
        """
        

        :type:
            :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.AutoResolve`
        """  # noqa: E501
        return self.__auto_resolve

    @auto_resolve.setter
    def auto_resolve(self, auto_resolve):

        self.__auto_resolve = auto_resolve

    @property
    def cluster_uuids(self):
        """
        List of cluster UUIDs on which the exceptions can be set.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__cluster_uuids

    @cluster_uuids.setter
    def cluster_uuids(self, cluster_uuids):

        self.__cluster_uuids = cluster_uuids

    @property
    def severity_threshold_infos(self):
        """
        Enable/Disable for each severity information.

        :type:
             list[ :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.SeverityThresholdInfo` ]
        """  # noqa: E501
        return self.__severity_threshold_infos

    @severity_threshold_infos.setter
    def severity_threshold_infos(self, severity_threshold_infos):

        self.__severity_threshold_infos = severity_threshold_infos

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
        if issubclass(AlertConfigExceptionGroup, dict):
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
        if not isinstance(other, AlertConfigExceptionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

