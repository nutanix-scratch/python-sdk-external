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
from ntnx_lifecycle_py_client.models.lifecycle.v4.common.CheckSumType import CheckSumType  # noqa: F401,E501

class ImageFile(object):

    """Description of LCM image file.

    :param file_location_id: (:attr:`file_location_id`) Image file global catalog item UUID.
    :type file_location_id: 
    :param name: (:attr:`name`) LCM image file name.
    :type name: 
    :param size_bytes: (:attr:`size_bytes`) LCM image file size.
    :type size_bytes: required
    :param file_path: (:attr:`file_path`) File path for the LCM image.
    :type file_path: 
    :param checksum_type: (:attr:`checksum_type`) 
    :type checksum_type: required
    :param checksum: (:attr:`checksum`) LCM image checksum.
    :type checksum: required

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
        'file_location_id': 'str',
        'name': 'str',
        'size_bytes': 'int',
        'file_path': 'str',
        'checksum_type': 'lifecycle.v4.common.CheckSumType',
        'checksum': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'file_location_id': 'fileLocationId',
        'name': 'name',
        'size_bytes': 'sizeBytes',
        'file_path': 'filePath',
        'checksum_type': 'checksumType',
        'checksum': 'checksum',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, file_location_id=None, name=None, size_bytes=None, file_path=None, checksum_type=None, checksum=None, *args, **kwargs):  # noqa: E501
        self.__file_location_id = None
        self.__name = None
        self.__size_bytes = None
        self.__file_path = None
        self.__checksum_type = None
        self.__checksum = None
        self.discriminator = None
        if file_location_id is not None:
            self.__file_location_id = file_location_id
        if name is not None:
            self.__name = name
        self.__size_bytes = size_bytes
        if file_path is not None:
            self.__file_path = file_path
        self.__checksum_type = checksum_type
        self.__checksum = checksum
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'lifecycle.v4.resources.ImageFile'

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
    def file_location_id(self):
        """
        Image file global catalog item UUID.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__file_location_id

    @file_location_id.setter
    def file_location_id(self, file_location_id):
        if file_location_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', file_location_id):  # noqa: E501
            raise ValueError(r"Invalid value for `file_location_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__file_location_id = file_location_id

    @property
    def name(self):
        """
        LCM image file name.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501

        self.__name = name

    @property
    def size_bytes(self):
        """
        LCM image file size.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        if size_bytes is None:
            raise ValueError("Invalid value for `size_bytes`, must not be `None`")  # noqa: E501

        self.__size_bytes = size_bytes

    @property
    def file_path(self):
        """
        File path for the LCM image.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        if file_path is not None and len(file_path) > 256:
            raise ValueError("Invalid value for `file_path`, length must be less than or equal to `256`")  # noqa: E501

        self.__file_path = file_path

    @property
    def checksum_type(self):
        """
        

        :type:
            :class:`~ntnx_lifecycle_py_client.models.lifecycle.v4.common.CheckSumType`
        """  # noqa: E501
        return self.__checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        if checksum_type is None:
            raise ValueError("Invalid value for `checksum_type`, must not be `None`")  # noqa: E501

        self.__checksum_type = checksum_type

    @property
    def checksum(self):
        """
        LCM image checksum.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__checksum

    @checksum.setter
    def checksum(self, checksum):
        if checksum is None:
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501
        if checksum is not None and len(checksum) > 128:
            raise ValueError("Invalid value for `checksum`, length must be less than or equal to `128`")  # noqa: E501

        self.__checksum = checksum

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
        if issubclass(ImageFile, dict):
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
        if not isinstance(other, ImageFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
