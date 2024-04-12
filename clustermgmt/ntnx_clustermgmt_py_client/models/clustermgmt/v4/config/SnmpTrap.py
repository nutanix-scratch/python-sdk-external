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
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.SnmpProtocol import SnmpProtocol  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.SnmpTrapVersion import SnmpTrapVersion  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress import IPAddress  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_clustermgmt_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501

class SnmpTrap(ExternalizableAbstractModel):

    """

    :param address: (:attr:`address`) 
    :type address: required
    :param username: (:attr:`username`) SNMP username. For SNMP trap v3 version, SNMP username is required parameter.
    :type username: 
    :param protocol: (:attr:`protocol`) 
    :type protocol: 
    :param port: (:attr:`port`) SNMP port.
    :type port: 
    :param inform: (:attr:`inform`) SNMP information status.
    :type inform: 
    :param engine_id: (:attr:`engine_id`) SNMP engine Id.
    :type engine_id: 
    :param version: (:attr:`version`) 
    :type version: required
    :param reciever_name: (:attr:`reciever_name`) SNMP receiver name.
    :type reciever_name: 
    :param community_string: (:attr:`community_string`) Community string(plaintext) for SNMP version 2.0.
    :type community_string: 

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
        'address': 'common.v1.config.IPAddress',
        'username': 'str',
        'protocol': 'clustermgmt.v4.config.SnmpProtocol',
        'port': 'int',
        'inform': 'bool',
        'engine_id': 'str',
        'version': 'clustermgmt.v4.config.SnmpTrapVersion',
        'reciever_name': 'str',
        'community_string': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'address': 'address',
        'username': 'username',
        'protocol': 'protocol',
        'port': 'port',
        'inform': 'inform',
        'engine_id': 'engineId',
        'version': 'version',
        'reciever_name': 'recieverName',
        'community_string': 'communityString',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, address=None, username=None, protocol=None, port=None, inform=None, engine_id=None, version=None, reciever_name=None, community_string=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__address = None
        self.__username = None
        self.__protocol = None
        self.__port = None
        self.__inform = None
        self.__engine_id = None
        self.__version = None
        self.__reciever_name = None
        self.__community_string = None
        self.discriminator = None
        self.__address = address
        if username is not None:
            self.__username = username
        if protocol is not None:
            self.__protocol = protocol
        if port is not None:
            self.__port = port
        if inform is not None:
            self.__inform = inform
        if engine_id is not None:
            self.__engine_id = engine_id
        self.__version = version
        if reciever_name is not None:
            self.__reciever_name = reciever_name
        if community_string is not None:
            self.__community_string = community_string

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.SnmpTrap'

    def _initialize_object_version(self):
        return 'v4.r0.b2'


    @property
    def address(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.common.v1.config.IPAddress`
        """  # noqa: E501
        return self.__address

    @address.setter
    def address(self, address):
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self.__address = address

    @property
    def username(self):
        """
        SNMP username. For SNMP trap v3 version, SNMP username is required parameter.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__username

    @username.setter
    def username(self, username):

        self.__username = username

    @property
    def protocol(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.SnmpProtocol`
        """  # noqa: E501
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol):

        self.__protocol = protocol

    @property
    def port(self):
        """
        SNMP port.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__port

    @port.setter
    def port(self, port):

        self.__port = port

    @property
    def inform(self):
        """
        SNMP information status.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__inform

    @inform.setter
    def inform(self, inform):

        self.__inform = inform

    @property
    def engine_id(self):
        """
        SNMP engine Id.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        if engine_id is not None and not re.search('^(?:0[xX])?[0-9a-fA-F]+$', engine_id):  # noqa: E501
            raise ValueError(r"Invalid value for `engine_id`, must be a follow pattern or equal to `/^(?:0[xX])?[0-9a-fA-F]+$/`")  # noqa: E501

        self.__engine_id = engine_id

    @property
    def version(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.SnmpTrapVersion`
        """  # noqa: E501
        return self.__version

    @version.setter
    def version(self, version):
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self.__version = version

    @property
    def reciever_name(self):
        """
        SNMP receiver name.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__reciever_name

    @reciever_name.setter
    def reciever_name(self, reciever_name):

        self.__reciever_name = reciever_name

    @property
    def community_string(self):
        """
        Community string(plaintext) for SNMP version 2.0.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__community_string

    @community_string.setter
    def community_string(self, community_string):

        self.__community_string = community_string

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
        if issubclass(SnmpTrap, dict):
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
        if not isinstance(other, SnmpTrap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
