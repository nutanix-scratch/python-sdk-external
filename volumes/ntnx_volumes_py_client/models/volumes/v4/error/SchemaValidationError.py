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
from ntnx_volumes_py_client.models.volumes.v4.error.SchemaValidationErrorMessage import SchemaValidationErrorMessage  # noqa: F401,E501

class SchemaValidationError(object):

    """This schema is generated from SchemaValidationError.java

    :param timestamp: (:attr:`timestamp`) Timestamp of the response.
    :type timestamp: 
    :param status_code: (:attr:`status_code`) The HTTP status code of the response.
    :type status_code: 
    :param error: (:attr:`error`) The generic error message for the response.
    :type error: 
    :param path: (:attr:`path`) API path on which the request was made.
    :type path: 
    :param validation_error_messages: (:attr:`validation_error_messages`) List of validation error messages
    :type validation_error_messages: 

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
        'timestamp': 'str',
        'status_code': 'int',
        'error': 'str',
        'path': 'str',
        'validation_error_messages': 'list[volumes.v4.error.SchemaValidationErrorMessage]',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'status_code': 'statusCode',
        'error': 'error',
        'path': 'path',
        'validation_error_messages': 'validationErrorMessages',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, timestamp=None, status_code=None, error=None, path=None, validation_error_messages=None, *args, **kwargs):  # noqa: E501
        self.__timestamp = None
        self.__status_code = None
        self.__error = None
        self.__path = None
        self.__validation_error_messages = None
        self.discriminator = None
        if timestamp is not None:
            self.__timestamp = timestamp
        if status_code is not None:
            self.__status_code = status_code
        if error is not None:
            self.__error = error
        if path is not None:
            self.__path = path
        if validation_error_messages is not None:
            self.__validation_error_messages = validation_error_messages
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'volumes.v4.error.SchemaValidationError'

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
    def timestamp(self):
        """
        Timestamp of the response.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):

        self.__timestamp = timestamp

    @property
    def status_code(self):
        """
        The HTTP status code of the response.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__status_code

    @status_code.setter
    def status_code(self, status_code):

        self.__status_code = status_code

    @property
    def error(self):
        """
        The generic error message for the response.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__error

    @error.setter
    def error(self, error):

        self.__error = error

    @property
    def path(self):
        """
        API path on which the request was made.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__path

    @path.setter
    def path(self, path):

        self.__path = path

    @property
    def validation_error_messages(self):
        """
        List of validation error messages

        :type:
             list[ :class:`~ntnx_volumes_py_client.models.volumes.v4.error.SchemaValidationErrorMessage` ]
        """  # noqa: E501
        return self.__validation_error_messages

    @validation_error_messages.setter
    def validation_error_messages(self, validation_error_messages):

        self.__validation_error_messages = validation_error_messages

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
        if issubclass(SchemaValidationError, dict):
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
        if not isinstance(other, SchemaValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

