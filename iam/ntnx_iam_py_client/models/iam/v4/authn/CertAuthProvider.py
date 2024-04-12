# coding: utf-8


"""
IGNORE:
    Nutanix Iam Versioned APIs

    Manage Identity and Access Management of Nutanix clusters.  # noqa: E501

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
from ntnx_iam_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_iam_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from ntnx_iam_py_client.models.iam.v4.authn.CertRevocationInfo import CertRevocationInfo  # noqa: F401,E501

class CertAuthProvider(ExternalizableAbstractModel):

    """A Certificate based Authentication provider.

    :param name: (:attr:`name`) Unique name of the Certificate based Authentication provider.
    :type name: 
    :param client_ca_chain: (:attr:`client_ca_chain`) CA chain file.
    :type client_ca_chain: 
    :param is_cert_auth_enabled: (:attr:`is_cert_auth_enabled`) Flag to enable/disable CAC for the current Certificate based Authentication provider.
    :type is_cert_auth_enabled: 
    :param is_cac_enabled: (:attr:`is_cac_enabled`) Flag to enable/disable Certificate Authentication for the current certificate based authentication provider.
    :type is_cac_enabled: 
    :param dir_svc_ext_id: (:attr:`dir_svc_ext_id`) UUID of an existing Directory Service.
    :type dir_svc_ext_id: 
    :param ca_cert_file_name: (:attr:`ca_cert_file_name`) Name of the uploaded CA chain file.
    :type ca_cert_file_name: 
    :param cert_revocation_info: (:attr:`cert_revocation_info`) 
    :type cert_revocation_info: 
    :param created_time: (:attr:`created_time`) Creation time of the Certificate Authentication Provider.
    :type created_time: 
    :param last_updated_time: (:attr:`last_updated_time`) Last updated time of the Certificate Authentication Provider.
    :type last_updated_time: 
    :param created_by: (:attr:`created_by`) User or Service who created the Certificate Authentication Provider.
    :type created_by: 

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
        'name': 'str',
        'client_ca_chain': 'str',
        'is_cert_auth_enabled': 'bool',
        'is_cac_enabled': 'bool',
        'dir_svc_ext_id': 'str',
        'ca_cert_file_name': 'str',
        'cert_revocation_info': 'iam.v4.authn.CertRevocationInfo',
        'created_time': 'datetime',
        'last_updated_time': 'datetime',
        'created_by': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'client_ca_chain': 'clientCaChain',
        'is_cert_auth_enabled': 'isCertAuthEnabled',
        'is_cac_enabled': 'isCacEnabled',
        'dir_svc_ext_id': 'dirSvcExtID',
        'ca_cert_file_name': 'caCertFileName',
        'cert_revocation_info': 'certRevocationInfo',
        'created_time': 'createdTime',
        'last_updated_time': 'lastUpdatedTime',
        'created_by': 'createdBy',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, client_ca_chain=None, is_cert_auth_enabled=None, is_cac_enabled=None, dir_svc_ext_id=None, ca_cert_file_name=None, cert_revocation_info=None, created_time=None, last_updated_time=None, created_by=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__name = None
        self.__client_ca_chain = None
        self.__is_cert_auth_enabled = None
        self.__is_cac_enabled = None
        self.__dir_svc_ext_id = None
        self.__ca_cert_file_name = None
        self.__cert_revocation_info = None
        self.__created_time = None
        self.__last_updated_time = None
        self.__created_by = None
        self.discriminator = None
        if name is not None:
            self.__name = name
        if client_ca_chain is not None:
            self.__client_ca_chain = client_ca_chain
        if is_cert_auth_enabled is not None:
            self.__is_cert_auth_enabled = is_cert_auth_enabled
        if is_cac_enabled is not None:
            self.__is_cac_enabled = is_cac_enabled
        if dir_svc_ext_id is not None:
            self.__dir_svc_ext_id = dir_svc_ext_id
        if ca_cert_file_name is not None:
            self.__ca_cert_file_name = ca_cert_file_name
        if cert_revocation_info is not None:
            self.__cert_revocation_info = cert_revocation_info
        if created_time is not None:
            self.__created_time = created_time
        if last_updated_time is not None:
            self.__last_updated_time = last_updated_time
        if created_by is not None:
            self.__created_by = created_by

    def _initialize_object_type(self):
        return 'iam.v4.authn.CertAuthProvider'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def name(self):
        """
        Unique name of the Certificate based Authentication provider.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search('^[^<>;\'()&+%\/\\\\\"`]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^<>;'()&+%\/\\\\\"`]*$/`")  # noqa: E501

        self.__name = name

    @property
    def client_ca_chain(self):
        """
        CA chain file.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__client_ca_chain

    @client_ca_chain.setter
    def client_ca_chain(self, client_ca_chain):
        if client_ca_chain is not None and len(client_ca_chain) < 64:
            raise ValueError("Invalid value for `client_ca_chain`, length must be greater than or equal to `64`")  # noqa: E501

        self.__client_ca_chain = client_ca_chain

    @property
    def is_cert_auth_enabled(self):
        """
        Flag to enable/disable CAC for the current Certificate based Authentication provider.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_cert_auth_enabled

    @is_cert_auth_enabled.setter
    def is_cert_auth_enabled(self, is_cert_auth_enabled):

        self.__is_cert_auth_enabled = is_cert_auth_enabled

    @property
    def is_cac_enabled(self):
        """
        Flag to enable/disable Certificate Authentication for the current certificate based authentication provider.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_cac_enabled

    @is_cac_enabled.setter
    def is_cac_enabled(self, is_cac_enabled):

        self.__is_cac_enabled = is_cac_enabled

    @property
    def dir_svc_ext_id(self):
        """
        UUID of an existing Directory Service.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__dir_svc_ext_id

    @dir_svc_ext_id.setter
    def dir_svc_ext_id(self, dir_svc_ext_id):
        if dir_svc_ext_id is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', dir_svc_ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `dir_svc_ext_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__dir_svc_ext_id = dir_svc_ext_id

    @property
    def ca_cert_file_name(self):
        """
        Name of the uploaded CA chain file.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__ca_cert_file_name

    @ca_cert_file_name.setter
    def ca_cert_file_name(self, ca_cert_file_name):
        if ca_cert_file_name is not None and len(ca_cert_file_name) > 255:
            raise ValueError("Invalid value for `ca_cert_file_name`, length must be less than or equal to `255`")  # noqa: E501
        if ca_cert_file_name is not None and len(ca_cert_file_name) < 1:
            raise ValueError("Invalid value for `ca_cert_file_name`, length must be greater than or equal to `1`")  # noqa: E501

        self.__ca_cert_file_name = ca_cert_file_name

    @property
    def cert_revocation_info(self):
        """
        

        :type:
            :class:`~ntnx_iam_py_client.models.iam.v4.authn.CertRevocationInfo`
        """  # noqa: E501
        return self.__cert_revocation_info

    @cert_revocation_info.setter
    def cert_revocation_info(self, cert_revocation_info):

        self.__cert_revocation_info = cert_revocation_info

    @property
    def created_time(self):
        """
        Creation time of the Certificate Authentication Provider.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__created_time

    @created_time.setter
    def created_time(self, created_time):

        self.__created_time = created_time

    @property
    def last_updated_time(self):
        """
        Last updated time of the Certificate Authentication Provider.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):

        self.__last_updated_time = last_updated_time

    @property
    def created_by(self):
        """
        User or Service who created the Certificate Authentication Provider.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__created_by

    @created_by.setter
    def created_by(self, created_by):

        self.__created_by = created_by

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
        if issubclass(CertAuthProvider, dict):
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
        if not isinstance(other, CertAuthProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

