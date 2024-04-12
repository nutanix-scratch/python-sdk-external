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

class RsyslogModuleName(object):

    """RSYSLOG module name.


    Allowed enum values:

        - _UNKNOWN
        - _REDACTED
        - CASSANDRA: Cassandra module.
        - CEREBRO: Cerebro module.
        - CURATOR: Curator module.
        - GENESIS: Genesis module.
        - PRISM: Prism module.
        - STARGATE
        - SYSLOG_MODULE: Syslog module.
        - ZOOKEEPER: Zookeeper module.
        - UHARA: Uhara module.
        - LAZAN: Lazan module.
        - API_AUDIT: API audit module.
        - AUDIT: Audit module.
        - CALM: Calm module.
        - EPSILON: Epsilon module.
        - ACROPOLIS: Acropolis module.
        - MINERVA_CVM: Minerva module.
        - FLOW: Flow module.
        - FLOW_SERVICE_LOGS: Flow service module.
        - LCM: LCM module.
        - APLOS: Aplos module.
    """
    _UNKNOWN = "$UNKNOWN"
    _REDACTED = "$REDACTED"
    CASSANDRA = "CASSANDRA"
    CEREBRO = "CEREBRO"
    CURATOR = "CURATOR"
    GENESIS = "GENESIS"
    PRISM = "PRISM"
    STARGATE = "STARGATE"
    SYSLOG_MODULE = "SYSLOG_MODULE"
    ZOOKEEPER = "ZOOKEEPER"
    UHARA = "UHARA"
    LAZAN = "LAZAN"
    API_AUDIT = "API_AUDIT"
    AUDIT = "AUDIT"
    CALM = "CALM"
    EPSILON = "EPSILON"
    ACROPOLIS = "ACROPOLIS"
    MINERVA_CVM = "MINERVA_CVM"
    FLOW = "FLOW"
    FLOW_SERVICE_LOGS = "FLOW_SERVICE_LOGS"
    LCM = "LCM"
    APLOS = "APLOS"


    def __init__(self, *args, **kwargs):  # noqa: E501
        self.discriminator = None
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'clustermgmt.v4.config.RsyslogModuleName'

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

    def _to_dict(self, sanitize):
        """Returns the model properties as a dict. Omits None properties based on the provided "sanitize" parameter.

        :param sanitize: A flag to omit None properties if set to True
        :type sanitize: bool
        """

        result = {}

        for attr in vars(self):
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
        if issubclass(RsyslogModuleName, dict):
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
        if not isinstance(other, RsyslogModuleName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

