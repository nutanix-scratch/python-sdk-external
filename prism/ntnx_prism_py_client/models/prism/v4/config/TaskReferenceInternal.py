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
from ntnx_prism_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501

class TaskReferenceInternal(ApiLink):

    """Reference to the parent task associated with the current task.

    :param ext_id: (:attr:`ext_id`) A globally unique identifier of the task.
    :type ext_id: 

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
        'ext_id': 'str',
        'href': 'str',
        'rel': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'ext_id': 'extId',
        'href': 'href',
        'rel': 'rel',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, ext_id=None, href=None, rel=None, *args, **kwargs):  # noqa: E501
        ApiLink.__init__(self, href, rel, *args, **kwargs)
        self.__ext_id = None
        self.discriminator = None
        if ext_id is not None:
            self.__ext_id = ext_id

    def _initialize_object_type(self):
        return 'prism.v4.config.TaskReferenceInternal'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def ext_id(self):
        """
        A globally unique identifier of the task.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__ext_id

    @ext_id.setter
    def ext_id(self, ext_id):
        if ext_id is not None and not re.search('^[a-zA-Z0-9\/+]*={0,2}:[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}', ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `ext_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\/+]*={0,2}:[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/`")  # noqa: E501

        self.__ext_id = ext_id

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
        if issubclass(TaskReferenceInternal, dict):
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
        if not isinstance(other, TaskReferenceInternal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
