# coding: utf-8


"""
IGNORE:
    Nutanix Microseg Versioned APIs

    Manage Network Security Policy configuration of Nutanix clusters.  # noqa: E501

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
from ntnx_microseg_py_client.models.common.v1.config.Flag import Flag  # noqa: F401,E501
from ntnx_microseg_py_client.models.common.v1.config.KVPair import KVPair  # noqa: F401,E501
from ntnx_microseg_py_client.models.common.v1.config.Message import Message  # noqa: F401,E501
from ntnx_microseg_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501

class ApiResponseMetadata(object):

    """The metadata associated with an API response. This value is always present and minimally contains the self-link for the API request that produced this response. It also contains pagination data for the paginated requests. 

    :param flags: (:attr:`flags`) An array of flags that may indicate the status of the response. For example, a flag with the name 'isPaginated' and value 'false', indicates that the response is not paginated. 
    :type flags: 
    :param links: (:attr:`links`) An array of HATEOAS style links for the response that may also include pagination links for list operations. 
    :type links: 
    :param total_available_results: (:attr:`total_available_results`) The total number of entities that are available on the server for this type. 
    :type total_available_results: 
    :param messages: (:attr:`messages`) Information, Warning or Error messages that might provide additional contextual information related to the operation. 
    :type messages: 
    :param extra_info: (:attr:`extra_info`) An array of entity-specific metadata 
    :type extra_info: 

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
        'flags': 'list[common.v1.config.Flag]',
        'links': 'list[common.v1.response.ApiLink]',
        'total_available_results': 'int',
        'messages': 'list[common.v1.config.Message]',
        'extra_info': 'list[common.v1.config.KVPair]',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'flags': 'flags',
        'links': 'links',
        'total_available_results': 'totalAvailableResults',
        'messages': 'messages',
        'extra_info': 'extraInfo',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, flags=None, links=None, total_available_results=None, messages=None, extra_info=None, *args, **kwargs):  # noqa: E501
        self.__flags = None
        self.__links = None
        self.__total_available_results = None
        self.__messages = None
        self.__extra_info = None
        self.discriminator = None
        if flags is not None:
            self.__flags = flags
        if links is not None:
            self.__links = links
        if total_available_results is not None:
            self.__total_available_results = total_available_results
        if messages is not None:
            self.__messages = messages
        if extra_info is not None:
            self.__extra_info = extra_info
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'common.v1.response.ApiResponseMetadata'

    def _initialize_object_version(self):
        return 'v1.r0.b1'

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
    def flags(self):
        """
        An array of flags that may indicate the status of the response. For example, a flag with the name 'isPaginated' and value 'false', indicates that the response is not paginated. 

        :type:
             list[ :class:`~ntnx_microseg_py_client.models.common.v1.config.Flag` ]
        """  # noqa: E501
        return self.__flags

    @flags.setter
    def flags(self, flags):

        self.__flags = flags

    @property
    def links(self):
        """
        An array of HATEOAS style links for the response that may also include pagination links for list operations. 

        :type:
             list[ :class:`~ntnx_microseg_py_client.models.common.v1.response.ApiLink` ]
        """  # noqa: E501
        return self.__links

    @links.setter
    def links(self, links):

        self.__links = links

    @property
    def total_available_results(self):
        """
        The total number of entities that are available on the server for this type. 

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__total_available_results

    @total_available_results.setter
    def total_available_results(self, total_available_results):

        self.__total_available_results = total_available_results

    @property
    def messages(self):
        """
        Information, Warning or Error messages that might provide additional contextual information related to the operation. 

        :type:
             list[ :class:`~ntnx_microseg_py_client.models.common.v1.config.Message` ]
        """  # noqa: E501
        return self.__messages

    @messages.setter
    def messages(self, messages):

        self.__messages = messages

    @property
    def extra_info(self):
        """
        An array of entity-specific metadata 

        :type:
             list[ :class:`~ntnx_microseg_py_client.models.common.v1.config.KVPair` ]
        """  # noqa: E501
        return self.__extra_info

    @extra_info.setter
    def extra_info(self, extra_info):

        self.__extra_info = extra_info

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
        if issubclass(ApiResponseMetadata, dict):
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
        if not isinstance(other, ApiResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

