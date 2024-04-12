# coding: utf-8


"""
IGNORE:
    Nutanix VMM APIs

    Manage the life-cycle of virtual machines hosted on Nutanix  # noqa: E501

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
from ntnx_vmm_py_client.models.vmm.v4.ahv.config.Ipv4Config import Ipv4Config  # noqa: F401,E501
from ntnx_vmm_py_client.models.vmm.v4.ahv.config.Ipv4Info import Ipv4Info  # noqa: F401,E501
from ntnx_vmm_py_client.models.vmm.v4.ahv.config.NetworkFunctionChainReference import NetworkFunctionChainReference  # noqa: F401,E501
from ntnx_vmm_py_client.models.vmm.v4.ahv.config.NetworkFunctionNicType import NetworkFunctionNicType  # noqa: F401,E501
from ntnx_vmm_py_client.models.vmm.v4.ahv.config.NicType import NicType  # noqa: F401,E501
from ntnx_vmm_py_client.models.vmm.v4.ahv.config.SubnetReference import SubnetReference  # noqa: F401,E501
from ntnx_vmm_py_client.models.vmm.v4.ahv.config.VlanMode import VlanMode  # noqa: F401,E501

class NicNetworkInfo(object):

    """Network information for a NIC.

    :param nic_type: (:attr:`nic_type`) 
    :type nic_type: 
    :param network_function_chain: (:attr:`network_function_chain`) 
    :type network_function_chain: 
    :param network_function_nic_type: (:attr:`network_function_nic_type`) 
    :type network_function_nic_type: 
    :param subnet: (:attr:`subnet`) 
    :type subnet: 
    :param vlan_mode: (:attr:`vlan_mode`) 
    :type vlan_mode: 
    :param trunked_vlans: (:attr:`trunked_vlans`) List of networks to trunk if VLAN mode is marked as TRUNKED. If empty and VLAN mode is set to TRUNKED, all the VLANs are trunked.
    :type trunked_vlans: 
    :param should_allow_unknown_macs: (:attr:`should_allow_unknown_macs`) Indicates whether an unknown unicast traffic is forwarded to this NIC or not. This is applicable only for the NICs on the overlay subnets.
    :type should_allow_unknown_macs: 
    :param ipv4_config: (:attr:`ipv4_config`) 
    :type ipv4_config: 
    :param ipv4_info: (:attr:`ipv4_info`) 
    :type ipv4_info: 

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
        'nic_type': 'vmm.v4.ahv.config.NicType',
        'network_function_chain': 'vmm.v4.ahv.config.NetworkFunctionChainReference',
        'network_function_nic_type': 'vmm.v4.ahv.config.NetworkFunctionNicType',
        'subnet': 'vmm.v4.ahv.config.SubnetReference',
        'vlan_mode': 'vmm.v4.ahv.config.VlanMode',
        'trunked_vlans': 'list[int]',
        'should_allow_unknown_macs': 'bool',
        'ipv4_config': 'vmm.v4.ahv.config.Ipv4Config',
        'ipv4_info': 'vmm.v4.ahv.config.Ipv4Info',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'nic_type': 'nicType',
        'network_function_chain': 'networkFunctionChain',
        'network_function_nic_type': 'networkFunctionNicType',
        'subnet': 'subnet',
        'vlan_mode': 'vlanMode',
        'trunked_vlans': 'trunkedVlans',
        'should_allow_unknown_macs': 'shouldAllowUnknownMacs',
        'ipv4_config': 'ipv4Config',
        'ipv4_info': 'ipv4Info',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, nic_type=None, network_function_chain=None, network_function_nic_type=None, subnet=None, vlan_mode=None, trunked_vlans=None, should_allow_unknown_macs=None, ipv4_config=None, ipv4_info=None, *args, **kwargs):  # noqa: E501
        self.__nic_type = None
        self.__network_function_chain = None
        self.__network_function_nic_type = None
        self.__subnet = None
        self.__vlan_mode = None
        self.__trunked_vlans = None
        self.__should_allow_unknown_macs = None
        self.__ipv4_config = None
        self.__ipv4_info = None
        self.discriminator = None
        if nic_type is not None:
            self.__nic_type = nic_type
        if network_function_chain is not None:
            self.__network_function_chain = network_function_chain
        if network_function_nic_type is not None:
            self.__network_function_nic_type = network_function_nic_type
        if subnet is not None:
            self.__subnet = subnet
        if vlan_mode is not None:
            self.__vlan_mode = vlan_mode
        if trunked_vlans is not None:
            self.__trunked_vlans = trunked_vlans
        if should_allow_unknown_macs is not None:
            self.__should_allow_unknown_macs = should_allow_unknown_macs
        if ipv4_config is not None:
            self.__ipv4_config = ipv4_config
        if ipv4_info is not None:
            self.__ipv4_info = ipv4_info
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'vmm.v4.ahv.config.NicNetworkInfo'

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
    def nic_type(self):
        """
        

        :type:
            :class:`~ntnx_vmm_py_client.models.vmm.v4.ahv.config.NicType`
        """  # noqa: E501
        return self.__nic_type

    @nic_type.setter
    def nic_type(self, nic_type):

        self.__nic_type = nic_type

    @property
    def network_function_chain(self):
        """
        

        :type:
            :class:`~ntnx_vmm_py_client.models.vmm.v4.ahv.config.NetworkFunctionChainReference`
        """  # noqa: E501
        return self.__network_function_chain

    @network_function_chain.setter
    def network_function_chain(self, network_function_chain):

        self.__network_function_chain = network_function_chain

    @property
    def network_function_nic_type(self):
        """
        

        :type:
            :class:`~ntnx_vmm_py_client.models.vmm.v4.ahv.config.NetworkFunctionNicType`
        """  # noqa: E501
        return self.__network_function_nic_type

    @network_function_nic_type.setter
    def network_function_nic_type(self, network_function_nic_type):

        self.__network_function_nic_type = network_function_nic_type

    @property
    def subnet(self):
        """
        

        :type:
            :class:`~ntnx_vmm_py_client.models.vmm.v4.ahv.config.SubnetReference`
        """  # noqa: E501
        return self.__subnet

    @subnet.setter
    def subnet(self, subnet):

        self.__subnet = subnet

    @property
    def vlan_mode(self):
        """
        

        :type:
            :class:`~ntnx_vmm_py_client.models.vmm.v4.ahv.config.VlanMode`
        """  # noqa: E501
        return self.__vlan_mode

    @vlan_mode.setter
    def vlan_mode(self, vlan_mode):

        self.__vlan_mode = vlan_mode

    @property
    def trunked_vlans(self):
        """
        List of networks to trunk if VLAN mode is marked as TRUNKED. If empty and VLAN mode is set to TRUNKED, all the VLANs are trunked.

        :type:
            list[ :class:`~int` ]
        """  # noqa: E501
        return self.__trunked_vlans

    @trunked_vlans.setter
    def trunked_vlans(self, trunked_vlans):

        self.__trunked_vlans = trunked_vlans

    @property
    def should_allow_unknown_macs(self):
        """
        Indicates whether an unknown unicast traffic is forwarded to this NIC or not. This is applicable only for the NICs on the overlay subnets.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__should_allow_unknown_macs

    @should_allow_unknown_macs.setter
    def should_allow_unknown_macs(self, should_allow_unknown_macs):

        self.__should_allow_unknown_macs = should_allow_unknown_macs

    @property
    def ipv4_config(self):
        """
        

        :type:
            :class:`~ntnx_vmm_py_client.models.vmm.v4.ahv.config.Ipv4Config`
        """  # noqa: E501
        return self.__ipv4_config

    @ipv4_config.setter
    def ipv4_config(self, ipv4_config):

        self.__ipv4_config = ipv4_config

    @property
    def ipv4_info(self):
        """
        

        :type:
            :class:`~ntnx_vmm_py_client.models.vmm.v4.ahv.config.Ipv4Info`
        """  # noqa: E501
        return self.__ipv4_info

    @ipv4_info.setter
    def ipv4_info(self, ipv4_info):

        self.__ipv4_info = ipv4_info

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
        if issubclass(NicNetworkInfo, dict):
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
        if not isinstance(other, NicNetworkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

