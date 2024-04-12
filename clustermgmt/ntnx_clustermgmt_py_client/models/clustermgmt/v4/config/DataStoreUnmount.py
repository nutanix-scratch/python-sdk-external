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

class DataStoreUnmount(ExternalizableAbstractModel):

    """

    :param datastore_name: (:attr:`datastore_name`) Name of the Data Store.
    :type datastore_name: required
    :param node_ext_ids: (:attr:`node_ext_ids`) The UUIDs of the nodes where the NFS Data Store has to be created.
    :type node_ext_ids: 

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
        'datastore_name': 'str',
        'node_ext_ids': 'list[str]',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'datastore_name': 'datastoreName',
        'node_ext_ids': 'nodeExtIds',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, datastore_name=None, node_ext_ids=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__datastore_name = None
        self.__node_ext_ids = None
        self.discriminator = None
        self.__datastore_name = datastore_name
        if node_ext_ids is not None:
            self.__node_ext_ids = node_ext_ids

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.DataStoreUnmount'

    def _initialize_object_version(self):
        return 'v4.r0.b2'


    @property
    def datastore_name(self):
        """
        Name of the Data Store.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        if datastore_name is None:
            raise ValueError("Invalid value for `datastore_name`, must not be `None`")  # noqa: E501
        if datastore_name is not None and len(datastore_name) > 255:
            raise ValueError("Invalid value for `datastore_name`, length must be less than or equal to `255`")  # noqa: E501

        self.__datastore_name = datastore_name

    @property
    def node_ext_ids(self):
        """
        The UUIDs of the nodes where the NFS Data Store has to be created.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__node_ext_ids

    @node_ext_ids.setter
    def node_ext_ids(self, node_ext_ids):

        self.__node_ext_ids = node_ext_ids

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
        if issubclass(DataStoreUnmount, dict):
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
        if not isinstance(other, DataStoreUnmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
