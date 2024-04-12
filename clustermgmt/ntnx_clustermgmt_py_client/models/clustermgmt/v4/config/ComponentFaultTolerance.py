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
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.ComponentType import ComponentType  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.ToleranceMessage import ToleranceMessage  # noqa: F401,E501

class ComponentFaultTolerance(object):

    """Fault tolerance information of a component.

    :param type: (:attr:`type`) 
    :type type: 
    :param max_faults_tolerated: (:attr:`max_faults_tolerated`) Maximum fault tolerance.
    :type max_faults_tolerated: 
    :param last_updates_secs: (:attr:`last_updates_secs`) Time of last update.
    :type last_updates_secs: 
    :param under_computation: (:attr:`under_computation`) Indicates whether the tolerance computation is in progress or not.
    :type under_computation: 
    :param detail_message: (:attr:`detail_message`) 
    :type detail_message: 

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
        'type': 'clustermgmt.v4.config.ComponentType',
        'max_faults_tolerated': 'int',
        'last_updates_secs': 'datetime',
        'under_computation': 'bool',
        'detail_message': 'clustermgmt.v4.config.ToleranceMessage',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'type': 'type',
        'max_faults_tolerated': 'maxFaultsTolerated',
        'last_updates_secs': 'lastUpdatesSecs',
        'under_computation': 'underComputation',
        'detail_message': 'detailMessage',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, type=None, max_faults_tolerated=None, last_updates_secs=None, under_computation=None, detail_message=None, *args, **kwargs):  # noqa: E501
        self.__type = None
        self.__max_faults_tolerated = None
        self.__last_updates_secs = None
        self.__under_computation = None
        self.__detail_message = None
        self.discriminator = None
        if type is not None:
            self.__type = type
        if max_faults_tolerated is not None:
            self.__max_faults_tolerated = max_faults_tolerated
        if last_updates_secs is not None:
            self.__last_updates_secs = last_updates_secs
        if under_computation is not None:
            self.__under_computation = under_computation
        if detail_message is not None:
            self.__detail_message = detail_message
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.ComponentFaultTolerance'

    def _initialize_object_version(self):
        return 'v4.r0.b2'

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
    def type(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.ComponentType`
        """  # noqa: E501
        return self.__type

    @type.setter
    def type(self, type):

        self.__type = type

    @property
    def max_faults_tolerated(self):
        """
        Maximum fault tolerance.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__max_faults_tolerated

    @max_faults_tolerated.setter
    def max_faults_tolerated(self, max_faults_tolerated):

        self.__max_faults_tolerated = max_faults_tolerated

    @property
    def last_updates_secs(self):
        """
        Time of last update.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__last_updates_secs

    @last_updates_secs.setter
    def last_updates_secs(self, last_updates_secs):

        self.__last_updates_secs = last_updates_secs

    @property
    def under_computation(self):
        """
        Indicates whether the tolerance computation is in progress or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__under_computation

    @under_computation.setter
    def under_computation(self, under_computation):

        self.__under_computation = under_computation

    @property
    def detail_message(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.ToleranceMessage`
        """  # noqa: E501
        return self.__detail_message

    @detail_message.setter
    def detail_message(self, detail_message):

        self.__detail_message = detail_message

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
        if issubclass(ComponentFaultTolerance, dict):
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
        if not isinstance(other, ComponentFaultTolerance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

