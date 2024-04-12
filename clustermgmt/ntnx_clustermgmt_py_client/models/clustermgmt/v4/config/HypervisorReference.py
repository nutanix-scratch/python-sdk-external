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
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.AcropolisConnectionState import AcropolisConnectionState  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.HypervisorState import HypervisorState  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.HypervisorType import HypervisorType  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress import IPAddress  # noqa: F401,E501

class HypervisorReference(object):

    """Hypervisor details.

    :param external_address: (:attr:`external_address`) 
    :type external_address: 
    :param user_name: (:attr:`user_name`) Hypervisor user name.
    :type user_name: 
    :param full_name: (:attr:`full_name`) Hypervisor full name.
    :type full_name: 
    :param type: (:attr:`type`) 
    :type type: 
    :param number_of_vms: (:attr:`number_of_vms`) Number of VMs.
    :type number_of_vms: 
    :param state: (:attr:`state`) 
    :type state: 
    :param acropolis_connection_state: (:attr:`acropolis_connection_state`) 
    :type acropolis_connection_state: 

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
        'external_address': 'common.v1.config.IPAddress',
        'user_name': 'str',
        'full_name': 'str',
        'type': 'clustermgmt.v4.config.HypervisorType',
        'number_of_vms': 'int',
        'state': 'clustermgmt.v4.config.HypervisorState',
        'acropolis_connection_state': 'clustermgmt.v4.config.AcropolisConnectionState',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'external_address': 'externalAddress',
        'user_name': 'userName',
        'full_name': 'fullName',
        'type': 'type',
        'number_of_vms': 'numberOfVms',
        'state': 'state',
        'acropolis_connection_state': 'acropolisConnectionState',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, external_address=None, user_name=None, full_name=None, type=None, number_of_vms=None, state=None, acropolis_connection_state=None, *args, **kwargs):  # noqa: E501
        self.__external_address = None
        self.__user_name = None
        self.__full_name = None
        self.__type = None
        self.__number_of_vms = None
        self.__state = None
        self.__acropolis_connection_state = None
        self.discriminator = None
        if external_address is not None:
            self.__external_address = external_address
        if user_name is not None:
            self.__user_name = user_name
        if full_name is not None:
            self.__full_name = full_name
        if type is not None:
            self.__type = type
        if number_of_vms is not None:
            self.__number_of_vms = number_of_vms
        if state is not None:
            self.__state = state
        if acropolis_connection_state is not None:
            self.__acropolis_connection_state = acropolis_connection_state
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.HypervisorReference'

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
    def external_address(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress`
        """  # noqa: E501
        return self.__external_address

    @external_address.setter
    def external_address(self, external_address):

        self.__external_address = external_address

    @property
    def user_name(self):
        """
        Hypervisor user name.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):

        self.__user_name = user_name

    @property
    def full_name(self):
        """
        Hypervisor full name.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):

        self.__full_name = full_name

    @property
    def type(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.HypervisorType`
        """  # noqa: E501
        return self.__type

    @type.setter
    def type(self, type):

        self.__type = type

    @property
    def number_of_vms(self):
        """
        Number of VMs.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__number_of_vms

    @number_of_vms.setter
    def number_of_vms(self, number_of_vms):

        self.__number_of_vms = number_of_vms

    @property
    def state(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.HypervisorState`
        """  # noqa: E501
        return self.__state

    @state.setter
    def state(self, state):

        self.__state = state

    @property
    def acropolis_connection_state(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.AcropolisConnectionState`
        """  # noqa: E501
        return self.__acropolis_connection_state

    @acropolis_connection_state.setter
    def acropolis_connection_state(self, acropolis_connection_state):

        self.__acropolis_connection_state = acropolis_connection_state

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
        if issubclass(HypervisorReference, dict):
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
        if not isinstance(other, HypervisorReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
