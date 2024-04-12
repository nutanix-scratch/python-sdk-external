# coding: utf-8


"""
IGNORE:
    Nutanix Prism Versioned APIs

    Manage Tasks, Category Associations and Submit Batch Operations.  # noqa: E501

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
from ntnx_prism_py_client.models.prism.v4.operations.ActionType import ActionType  # noqa: F401,E501

class BatchSpecMetadata(object):

    """The metadata section on the input specification for performing the batch operation.

    :param action: (:attr:`action`) 
    :type action: required
    :param name: (:attr:`name`) An user friendly name of the batch.
    :type name: required
    :param uri: (:attr:`uri`) The absolute URI of the API operation on which batching will be performed.
    :type uri: required
    :param stop_on_error: (:attr:`stop_on_error`) A flag indicating whether the batch procession should halt or continue when an error response is received from the server during the execution of a batch chunk
    :type stop_on_error: 
    :param chunk_size: (:attr:`chunk_size`) The chunk size to use during the batching operation. If not specified a minimum value of 1 would be chosen. (**Default** 1)
    :type chunk_size: 

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
        'action': 'prism.v4.operations.ActionType',
        'name': 'str',
        'uri': 'str',
        'stop_on_error': 'bool',
        'chunk_size': 'int',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'action': 'action',
        'name': 'name',
        'uri': 'uri',
        'stop_on_error': 'stopOnError',
        'chunk_size': 'chunkSize',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, action=None, name=None, uri=None, stop_on_error=None, chunk_size=1, *args, **kwargs):  # noqa: E501
        self.__action = None
        self.__name = None
        self.__uri = None
        self.__stop_on_error = None
        self.__chunk_size = None
        self.discriminator = None
        self.__action = action
        self.__name = name
        self.__uri = uri
        if stop_on_error is not None:
            self.__stop_on_error = stop_on_error
        if chunk_size is not None:
            self.__chunk_size = chunk_size
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'prism.v4.operations.BatchSpecMetadata'

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
    def action(self):
        """
        

        :type:
            :class:`~ntnx_prism_py_client.models.prism.v4.operations.ActionType`
        """  # noqa: E501
        return self.__action

    @action.setter
    def action(self, action):
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self.__action = action

    @property
    def name(self):
        """
        An user friendly name of the batch.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501

        self.__name = name

    @property
    def uri(self):
        """
        The absolute URI of the API operation on which batching will be performed.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__uri

    @uri.setter
    def uri(self, uri):
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self.__uri = uri

    @property
    def stop_on_error(self):
        """
        A flag indicating whether the batch procession should halt or continue when an error response is received from the server during the execution of a batch chunk

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__stop_on_error

    @stop_on_error.setter
    def stop_on_error(self, stop_on_error):

        self.__stop_on_error = stop_on_error

    @property
    def chunk_size(self):
        """
        The chunk size to use during the batching operation. If not specified a minimum value of 1 would be chosen.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__chunk_size

    @chunk_size.setter
    def chunk_size(self, chunk_size):
        if chunk_size is not None and chunk_size < 1:  # noqa: E501
            raise ValueError("Invalid value for `chunk_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self.__chunk_size = chunk_size

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
        if issubclass(BatchSpecMetadata, dict):
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
        if not isinstance(other, BatchSpecMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
