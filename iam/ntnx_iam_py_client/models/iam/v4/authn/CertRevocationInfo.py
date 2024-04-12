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

class CertRevocationInfo(object):

    """Configuration details used for determining if the client certificate is revoked.

    :param is_ocsp_enabled: (:attr:`is_ocsp_enabled`) Flag to enable/disable OCSP revocation check.
    :type is_ocsp_enabled: 
    :param ocsp_responder: (:attr:`ocsp_responder`) URL of the OCSP responder used to override the url from AIA extension.
    :type ocsp_responder: 
    :param is_crl_enabled: (:attr:`is_crl_enabled`) Flag to enable/disable CRL revocation check.
    :type is_crl_enabled: 
    :param crl_dps: (:attr:`crl_dps`) List of the CRL distribution points which will be used to fetch the CRLs.
    :type crl_dps: 
    :param global_crl_refresh_interval: (:attr:`global_crl_refresh_interval`) Interval in seconds at which the CRL should be fetched from the CRLDP, default = 86400 seconds(1 day).
    :type global_crl_refresh_interval: 

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
        'is_ocsp_enabled': 'bool',
        'ocsp_responder': 'str',
        'is_crl_enabled': 'bool',
        'crl_dps': 'list[str]',
        'global_crl_refresh_interval': 'int',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'is_ocsp_enabled': 'isOcspEnabled',
        'ocsp_responder': 'ocspResponder',
        'is_crl_enabled': 'isCrlEnabled',
        'crl_dps': 'crlDps',
        'global_crl_refresh_interval': 'globalCrlRefreshInterval',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, is_ocsp_enabled=None, ocsp_responder=None, is_crl_enabled=None, crl_dps=None, global_crl_refresh_interval=None, *args, **kwargs):  # noqa: E501
        self.__is_ocsp_enabled = None
        self.__ocsp_responder = None
        self.__is_crl_enabled = None
        self.__crl_dps = None
        self.__global_crl_refresh_interval = None
        self.discriminator = None
        if is_ocsp_enabled is not None:
            self.__is_ocsp_enabled = is_ocsp_enabled
        if ocsp_responder is not None:
            self.__ocsp_responder = ocsp_responder
        if is_crl_enabled is not None:
            self.__is_crl_enabled = is_crl_enabled
        if crl_dps is not None:
            self.__crl_dps = crl_dps
        if global_crl_refresh_interval is not None:
            self.__global_crl_refresh_interval = global_crl_refresh_interval
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'iam.v4.authn.CertRevocationInfo'

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
    def is_ocsp_enabled(self):
        """
        Flag to enable/disable OCSP revocation check.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_ocsp_enabled

    @is_ocsp_enabled.setter
    def is_ocsp_enabled(self, is_ocsp_enabled):

        self.__is_ocsp_enabled = is_ocsp_enabled

    @property
    def ocsp_responder(self):
        """
        URL of the OCSP responder used to override the url from AIA extension.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__ocsp_responder

    @ocsp_responder.setter
    def ocsp_responder(self, ocsp_responder):
        if ocsp_responder is not None and not re.search('^((http[s]?|nfs):\/)?\/?([^:\/\\s]*)((\/\\w+)*(:[0-9]+)*?\/)([\\w\\-\\.]+[^#?\\s]+)(.*)?(#[\\w\\-]+)?$', ocsp_responder):  # noqa: E501
            raise ValueError(r"Invalid value for `ocsp_responder`, must be a follow pattern or equal to `/^((http[s]?|nfs):\/)?\/?([^:\/\\s]*)((\/\\w+)*(:[0-9]+)*?\/)([\\w\\-\\.]+[^#?\\s]+)(.*)?(#[\\w\\-]+)?$/`")  # noqa: E501

        self.__ocsp_responder = ocsp_responder

    @property
    def is_crl_enabled(self):
        """
        Flag to enable/disable CRL revocation check.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_crl_enabled

    @is_crl_enabled.setter
    def is_crl_enabled(self, is_crl_enabled):

        self.__is_crl_enabled = is_crl_enabled

    @property
    def crl_dps(self):
        """
        List of the CRL distribution points which will be used to fetch the CRLs.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__crl_dps

    @crl_dps.setter
    def crl_dps(self, crl_dps):

        self.__crl_dps = crl_dps

    @property
    def global_crl_refresh_interval(self):
        """
        Interval in seconds at which the CRL should be fetched from the CRLDP, default = 86400 seconds(1 day).

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__global_crl_refresh_interval

    @global_crl_refresh_interval.setter
    def global_crl_refresh_interval(self, global_crl_refresh_interval):

        self.__global_crl_refresh_interval = global_crl_refresh_interval

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
        if issubclass(CertRevocationInfo, dict):
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
        if not isinstance(other, CertRevocationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

