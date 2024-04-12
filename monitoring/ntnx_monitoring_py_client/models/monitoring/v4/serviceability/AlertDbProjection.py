# coding: utf-8


"""
IGNORE:
    Nutanix Monitoring Versioned APIs

    Manage Alerts, Alert policies, Events and Audits  # noqa: E501

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
from ntnx_monitoring_py_client.models.monitoring.v4.common.AlertEntityReference import AlertEntityReference  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.common.ImpactType import ImpactType  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.common.Severity import Severity  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.AlertDb import AlertDb  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.RootCauseAnalysisProjection import RootCauseAnalysisProjection  # noqa: F401,E501

class AlertDbProjection(AlertDb):

    """

    :param root_cause_analysis_projection: (:attr:`root_cause_analysis_projection`) 
    :type root_cause_analysis_projection: 

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
        'root_cause_analysis_projection': 'monitoring.v4.serviceability.RootCauseAnalysisProjection',
        'protobuf': 'str',
        'is_acknowledged': 'bool',
        'service_name': 'str',
        'severity': 'monitoring.v4.common.Severity',
        'is_auto_resolved': 'bool',
        'is_resolved': 'bool',
        'alert_type': 'str',
        'classifications': 'list[str]',
        'originating_cluster_uuid': 'str',
        'creation_time': 'datetime',
        'impact_types': 'list[monitoring.v4.common.ImpactType]',
        'last_updated_time': 'datetime',
        'acknowledged_time': 'datetime',
        'resolved_time': 'datetime',
        'source_entity': 'monitoring.v4.common.AlertEntityReference',
        'cluster': 'list[str]',
        'is_user_defined': 'bool',
        'resolved_by_username': 'str',
        'acknowledged_by_username': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'root_cause_analysis_projection': 'rootCauseAnalysisProjection',
        'protobuf': 'protobuf',
        'is_acknowledged': 'isAcknowledged',
        'service_name': 'serviceName',
        'severity': 'severity',
        'is_auto_resolved': 'isAutoResolved',
        'is_resolved': 'isResolved',
        'alert_type': 'alertType',
        'classifications': 'classifications',
        'originating_cluster_uuid': 'originatingClusterUUID',
        'creation_time': 'creationTime',
        'impact_types': 'impactTypes',
        'last_updated_time': 'lastUpdatedTime',
        'acknowledged_time': 'acknowledgedTime',
        'resolved_time': 'resolvedTime',
        'source_entity': 'sourceEntity',
        'cluster': 'cluster',
        'is_user_defined': 'isUserDefined',
        'resolved_by_username': 'resolvedByUsername',
        'acknowledged_by_username': 'acknowledgedByUsername',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, root_cause_analysis_projection=None, protobuf=None, is_acknowledged=None, service_name=None, severity=None, is_auto_resolved=None, is_resolved=None, alert_type=None, classifications=None, originating_cluster_uuid=None, creation_time=None, impact_types=None, last_updated_time=None, acknowledged_time=None, resolved_time=None, source_entity=None, cluster=None, is_user_defined=None, resolved_by_username=None, acknowledged_by_username=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        AlertDb.__init__(self, protobuf, is_acknowledged, service_name, severity, is_auto_resolved, is_resolved, alert_type, classifications, originating_cluster_uuid, creation_time, impact_types, last_updated_time, acknowledged_time, resolved_time, source_entity, cluster, is_user_defined, resolved_by_username, acknowledged_by_username, ext_id, links, tenant_id, *args, **kwargs)
        self.__root_cause_analysis_projection = None
        self.discriminator = None
        if root_cause_analysis_projection is not None:
            self.__root_cause_analysis_projection = root_cause_analysis_projection

    def _initialize_object_type(self):
        return 'monitoring.v4.serviceability.AlertDbProjection'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def root_cause_analysis_projection(self):
        """
        

        :type:
            :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.RootCauseAnalysisProjection`
        """  # noqa: E501
        return self.__root_cause_analysis_projection

    @root_cause_analysis_projection.setter
    def root_cause_analysis_projection(self, root_cause_analysis_projection):

        self.__root_cause_analysis_projection = root_cause_analysis_projection

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
        if issubclass(AlertDbProjection, dict):
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
        if not isinstance(other, AlertDbProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
