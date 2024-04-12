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
from ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.HypervisorType import HypervisorType  # noqa: F401,E501

class UploadInfoNodeItem(object):

    """Upload information for a node.

    :param hypervisor_upload_required: (:attr:`hypervisor_upload_required`) Provides information on whether hypervisor ISO upload is required or not. This API is not supported for XEN hypervisor type.
    :type hypervisor_upload_required: 
    :param is_imaging_mandatory: (:attr:`is_imaging_mandatory`) Indicates if imaging is required or not.
    :type is_imaging_mandatory: 
    :param node_uuid: (:attr:`node_uuid`) UUID of the host.
    :type node_uuid: 
    :param available_hypervisor_iso_error: (:attr:`available_hypervisor_iso_error`) Error message if any, for available hypervisor ISO.
    :type available_hypervisor_iso_error: 
    :param required_hypervisor_type: (:attr:`required_hypervisor_type`) 
    :type required_hypervisor_type: 
    :param is_node_compatible: (:attr:`is_node_compatible`) Indicates if node is compatible or not.
    :type is_node_compatible: 
    :param md5_sum: (:attr:`md5_sum`) Md5sum of ISO.
    :type md5_sum: 
    :param bundle_name: (:attr:`bundle_name`) Name of the hypervisor bundle.
    :type bundle_name: 

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
        'hypervisor_upload_required': 'bool',
        'is_imaging_mandatory': 'bool',
        'node_uuid': 'str',
        'available_hypervisor_iso_error': 'str',
        'required_hypervisor_type': 'clustermgmt.v4.config.HypervisorType',
        'is_node_compatible': 'bool',
        'md5_sum': 'str',
        'bundle_name': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'hypervisor_upload_required': 'hypervisorUploadRequired',
        'is_imaging_mandatory': 'isImagingMandatory',
        'node_uuid': 'nodeUuid',
        'available_hypervisor_iso_error': 'availableHypervisorIsoError',
        'required_hypervisor_type': 'requiredHypervisorType',
        'is_node_compatible': 'isNodeCompatible',
        'md5_sum': 'md5Sum',
        'bundle_name': 'bundleName',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, hypervisor_upload_required=None, is_imaging_mandatory=None, node_uuid=None, available_hypervisor_iso_error=None, required_hypervisor_type=None, is_node_compatible=None, md5_sum=None, bundle_name=None, *args, **kwargs):  # noqa: E501
        self.__hypervisor_upload_required = None
        self.__is_imaging_mandatory = None
        self.__node_uuid = None
        self.__available_hypervisor_iso_error = None
        self.__required_hypervisor_type = None
        self.__is_node_compatible = None
        self.__md5_sum = None
        self.__bundle_name = None
        self.discriminator = None
        if hypervisor_upload_required is not None:
            self.__hypervisor_upload_required = hypervisor_upload_required
        if is_imaging_mandatory is not None:
            self.__is_imaging_mandatory = is_imaging_mandatory
        if node_uuid is not None:
            self.__node_uuid = node_uuid
        if available_hypervisor_iso_error is not None:
            self.__available_hypervisor_iso_error = available_hypervisor_iso_error
        if required_hypervisor_type is not None:
            self.__required_hypervisor_type = required_hypervisor_type
        if is_node_compatible is not None:
            self.__is_node_compatible = is_node_compatible
        if md5_sum is not None:
            self.__md5_sum = md5_sum
        if bundle_name is not None:
            self.__bundle_name = bundle_name
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.UploadInfoNodeItem'

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
    def hypervisor_upload_required(self):
        """
        Provides information on whether hypervisor ISO upload is required or not. This API is not supported for XEN hypervisor type.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__hypervisor_upload_required

    @hypervisor_upload_required.setter
    def hypervisor_upload_required(self, hypervisor_upload_required):

        self.__hypervisor_upload_required = hypervisor_upload_required

    @property
    def is_imaging_mandatory(self):
        """
        Indicates if imaging is required or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_imaging_mandatory

    @is_imaging_mandatory.setter
    def is_imaging_mandatory(self, is_imaging_mandatory):

        self.__is_imaging_mandatory = is_imaging_mandatory

    @property
    def node_uuid(self):
        """
        UUID of the host.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__node_uuid

    @node_uuid.setter
    def node_uuid(self, node_uuid):
        if node_uuid is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', node_uuid):  # noqa: E501
            raise ValueError(r"Invalid value for `node_uuid`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__node_uuid = node_uuid

    @property
    def available_hypervisor_iso_error(self):
        """
        Error message if any, for available hypervisor ISO.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__available_hypervisor_iso_error

    @available_hypervisor_iso_error.setter
    def available_hypervisor_iso_error(self, available_hypervisor_iso_error):

        self.__available_hypervisor_iso_error = available_hypervisor_iso_error

    @property
    def required_hypervisor_type(self):
        """
        

        :type:
            :class:`~ntnx_clustermgmt_py_client.models.clustermgmt.v4.config.HypervisorType`
        """  # noqa: E501
        return self.__required_hypervisor_type

    @required_hypervisor_type.setter
    def required_hypervisor_type(self, required_hypervisor_type):

        self.__required_hypervisor_type = required_hypervisor_type

    @property
    def is_node_compatible(self):
        """
        Indicates if node is compatible or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_node_compatible

    @is_node_compatible.setter
    def is_node_compatible(self, is_node_compatible):

        self.__is_node_compatible = is_node_compatible

    @property
    def md5_sum(self):
        """
        Md5sum of ISO.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__md5_sum

    @md5_sum.setter
    def md5_sum(self, md5_sum):
        if md5_sum is not None and not re.search('^[a-fA-F0-9]{32}$', md5_sum):  # noqa: E501
            raise ValueError(r"Invalid value for `md5_sum`, must be a follow pattern or equal to `/^[a-fA-F0-9]{32}$/`")  # noqa: E501

        self.__md5_sum = md5_sum

    @property
    def bundle_name(self):
        """
        Name of the hypervisor bundle.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__bundle_name

    @bundle_name.setter
    def bundle_name(self, bundle_name):

        self.__bundle_name = bundle_name

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
        if issubclass(UploadInfoNodeItem, dict):
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
        if not isinstance(other, UploadInfoNodeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

