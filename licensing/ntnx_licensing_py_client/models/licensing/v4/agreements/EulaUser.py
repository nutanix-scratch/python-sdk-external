# coding: utf-8


"""
IGNORE:
    Nutanix Licensing Versioned APIs

    licensing desc placeholder  # noqa: E501

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
from ntnx_licensing_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_licensing_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501

class EulaUser(ExternalizableAbstractModel):

    """Model containing the EULA User Details attributes.

    :param user_name: (:attr:`user_name`) User name of the user accepting the EULA
    :type user_name: required
    :param login_id: (:attr:`login_id`) Login ID of the user accepting the EULA
    :type login_id: required
    :param job_title: (:attr:`job_title`) Job title of the user accepting the EULA
    :type job_title: required
    :param company_name: (:attr:`company_name`) Company name of the user accepting the EULA
    :type company_name: required
    :param accepted_time: (:attr:`accepted_time`) Date-time at which EULA was accepted. Date-Time in epoch seconds in ISO date time
    :type accepted_time: 

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
        'user_name': 'str',
        'login_id': 'str',
        'job_title': 'str',
        'company_name': 'str',
        'accepted_time': 'datetime',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'user_name': 'userName',
        'login_id': 'loginId',
        'job_title': 'jobTitle',
        'company_name': 'companyName',
        'accepted_time': 'acceptedTime',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, user_name=None, login_id=None, job_title=None, company_name=None, accepted_time=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__user_name = None
        self.__login_id = None
        self.__job_title = None
        self.__company_name = None
        self.__accepted_time = None
        self.discriminator = None
        self.__user_name = user_name
        self.__login_id = login_id
        self.__job_title = job_title
        self.__company_name = company_name
        if accepted_time is not None:
            self.__accepted_time = accepted_time

    def _initialize_object_type(self):
        return 'licensing.v4.agreements.EulaUser'

    def _initialize_object_version(self):
        return 'v4.r0.a1'


    @property
    def user_name(self):
        """
        User name of the user accepting the EULA

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501
        if user_name is not None and len(user_name) > 50:
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `50`")  # noqa: E501

        self.__user_name = user_name

    @property
    def login_id(self):
        """
        Login ID of the user accepting the EULA

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__login_id

    @login_id.setter
    def login_id(self, login_id):
        if login_id is None:
            raise ValueError("Invalid value for `login_id`, must not be `None`")  # noqa: E501
        if login_id is not None and len(login_id) > 50:
            raise ValueError("Invalid value for `login_id`, length must be less than or equal to `50`")  # noqa: E501

        self.__login_id = login_id

    @property
    def job_title(self):
        """
        Job title of the user accepting the EULA

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__job_title

    @job_title.setter
    def job_title(self, job_title):
        if job_title is None:
            raise ValueError("Invalid value for `job_title`, must not be `None`")  # noqa: E501
        if job_title is not None and len(job_title) > 50:
            raise ValueError("Invalid value for `job_title`, length must be less than or equal to `50`")  # noqa: E501

        self.__job_title = job_title

    @property
    def company_name(self):
        """
        Company name of the user accepting the EULA

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501
        if company_name is not None and len(company_name) > 100:
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `100`")  # noqa: E501

        self.__company_name = company_name

    @property
    def accepted_time(self):
        """
        Date-time at which EULA was accepted. Date-Time in epoch seconds in ISO date time

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__accepted_time

    @accepted_time.setter
    def accepted_time(self, accepted_time):

        self.__accepted_time = accepted_time

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
        if issubclass(EulaUser, dict):
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
        if not isinstance(other, EulaUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

