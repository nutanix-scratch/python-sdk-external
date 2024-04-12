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
import ntnx_monitoring_py_client.models
from ntnx_monitoring_py_client.models.OneOfmonitoring.v4.serviceability.UserDefinedPolicyfilters import UserDefinedPolicyfilters  # noqa: F401,E501
from ntnx_monitoring_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_monitoring_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.common.ImpactType import ImpactType  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.RelatedPolicy import RelatedPolicy  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.TriggerCondition import TriggerCondition  # noqa: F401,E501

class UserDefinedPolicy(ExternalizableAbstractModel):

    """

    :param title: (:attr:`title`) Title of the policy.
    :type title: required
    :param description: (:attr:`description`) Description of the policy.
    :type description: 
    :param is_enabled: (:attr:`is_enabled`) Enable/Disable flag for the policy. (**Default** False)
    :type is_enabled: 
    :param is_auto_resolved: (:attr:`is_auto_resolved`) Indicates whether the auto resolve feature is enabled for this policy. (**Default** True)
    :type is_auto_resolved: 
    :param filters: (:attr:`filters`) Filter criteria for narrowing down the entities on which User-Defined Alert policies can be setup.
    :type filters: 
    :param trigger_conditions: (:attr:`trigger_conditions`) Trigger conditions for the policy. If there are multiple trigger conditions, all of them will be considered during the operation.
    :type trigger_conditions: required
    :param impact_types: (:attr:`impact_types`) Impact Types for the associated resulting alert.
    :type impact_types: 
    :param created_by: (:attr:`created_by`) Username of the user who created the policy.
    :type created_by: 
    :param last_updated_time: (:attr:`last_updated_time`) Last updated time of the policy in ISO 8601 format. This value will be used as the CAS value during updates.
    :type last_updated_time: 
    :param is_expected_to_error_on_conflict: (:attr:`is_expected_to_error_on_conflict`) Error if conflicting alert policies are found. (**Default** True)
    :type is_expected_to_error_on_conflict: 
    :param policies_to_override: (:attr:`policies_to_override`) List of IDs of the alert policies that should be overridden.
    :type policies_to_override: 
    :param trigger_wait_period: (:attr:`trigger_wait_period`) Waiting duration in seconds before triggering the alert, when the specified condition is met. It is set to 600s by default.
    :type trigger_wait_period: 
    :param related_policies: (:attr:`related_policies`) List of alert policies that are related to the entities of the current policy.
    :type related_policies: 
    :param entity_type: (:attr:`entity_type`) Entity type associated with the User-Defined Alert policy. Allowed values are VM, node and cluster.
    :type entity_type: required

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
        'title': 'str',
        'description': 'str',
        'is_enabled': 'bool',
        'is_auto_resolved': 'bool',
        'filters': 'OneOfmonitoring.v4.serviceability.UserDefinedPolicyfilters',
        'trigger_conditions': 'list[monitoring.v4.serviceability.TriggerCondition]',
        'impact_types': 'list[monitoring.v4.common.ImpactType]',
        'created_by': 'str',
        'last_updated_time': 'datetime',
        'is_expected_to_error_on_conflict': 'bool',
        'policies_to_override': 'list[str]',
        'trigger_wait_period': 'int',
        'related_policies': 'list[monitoring.v4.serviceability.RelatedPolicy]',
        'entity_type': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'is_enabled': 'isEnabled',
        'is_auto_resolved': 'isAutoResolved',
        'filters': 'filters',
        'trigger_conditions': 'triggerConditions',
        'impact_types': 'impactTypes',
        'created_by': 'createdBy',
        'last_updated_time': 'lastUpdatedTime',
        'is_expected_to_error_on_conflict': 'isExpectedToErrorOnConflict',
        'policies_to_override': 'policiesToOverride',
        'trigger_wait_period': 'triggerWaitPeriod',
        'related_policies': 'relatedPolicies',
        'entity_type': 'entityType',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, title=None, description=None, is_enabled=False, is_auto_resolved=True, filters=None, trigger_conditions=None, impact_types=None, created_by=None, last_updated_time=None, is_expected_to_error_on_conflict=True, policies_to_override=None, trigger_wait_period=None, related_policies=None, entity_type=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__title = None
        self.__description = None
        self.__is_enabled = None
        self.__is_auto_resolved = None
        self.__filters = None
        self.__trigger_conditions = None
        self.__impact_types = None
        self.__created_by = None
        self.__last_updated_time = None
        self.__is_expected_to_error_on_conflict = None
        self.__policies_to_override = None
        self.__trigger_wait_period = None
        self.__related_policies = None
        self.__entity_type = None
        self.discriminator = None
        self.__title = title
        if description is not None:
            self.__description = description
        if is_enabled is not None:
            self.__is_enabled = is_enabled
        if is_auto_resolved is not None:
            self.__is_auto_resolved = is_auto_resolved
        if filters is not None:
            self.__filters = filters
        self.__trigger_conditions = trigger_conditions
        if impact_types is not None:
            self.__impact_types = impact_types
        if created_by is not None:
            self.__created_by = created_by
        if last_updated_time is not None:
            self.__last_updated_time = last_updated_time
        if is_expected_to_error_on_conflict is not None:
            self.__is_expected_to_error_on_conflict = is_expected_to_error_on_conflict
        if policies_to_override is not None:
            self.__policies_to_override = policies_to_override
        if trigger_wait_period is not None:
            self.__trigger_wait_period = trigger_wait_period
        if related_policies is not None:
            self.__related_policies = related_policies
        self.__entity_type = entity_type

    def _initialize_object_type(self):
        return 'monitoring.v4.serviceability.UserDefinedPolicy'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def title(self):
        """
        Title of the policy.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__title

    @title.setter
    def title(self, title):
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) > 150:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `150`")  # noqa: E501
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self.__title = title

    @property
    def description(self):
        """
        Description of the policy.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__description

    @description.setter
    def description(self, description):
        if description is not None and len(description) > 500:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `500`")  # noqa: E501

        self.__description = description

    @property
    def is_enabled(self):
        """
        Enable/Disable flag for the policy.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):

        self.__is_enabled = is_enabled

    @property
    def is_auto_resolved(self):
        """
        Indicates whether the auto resolve feature is enabled for this policy.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_auto_resolved

    @is_auto_resolved.setter
    def is_auto_resolved(self, is_auto_resolved):

        self.__is_auto_resolved = is_auto_resolved

    @property
    def filters(self):
        """
        Filter criteria for narrowing down the entities on which User-Defined Alert policies can be setup.

        :type:
                :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.EntityFilter` | 
                :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.GroupFilter`
                    """  # noqa: E501
        return self.__filters

    @filters.setter
    def filters(self, filters):

        self.__filters = filters

    @property
    def trigger_conditions(self):
        """
        Trigger conditions for the policy. If there are multiple trigger conditions, all of them will be considered during the operation.

        :type:
             list[ :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.TriggerCondition` ]
        """  # noqa: E501
        return self.__trigger_conditions

    @trigger_conditions.setter
    def trigger_conditions(self, trigger_conditions):
        if trigger_conditions is None:
            raise ValueError("Invalid value for `trigger_conditions`, must not be `None`")  # noqa: E501

        self.__trigger_conditions = trigger_conditions

    @property
    def impact_types(self):
        """
        Impact Types for the associated resulting alert.

        :type:
             list[ :class:`~ntnx_monitoring_py_client.models.monitoring.v4.common.ImpactType` ]
        """  # noqa: E501
        return self.__impact_types

    @impact_types.setter
    def impact_types(self, impact_types):

        self.__impact_types = impact_types

    @property
    def created_by(self):
        """
        Username of the user who created the policy.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__created_by

    @created_by.setter
    def created_by(self, created_by):

        self.__created_by = created_by

    @property
    def last_updated_time(self):
        """
        Last updated time of the policy in ISO 8601 format. This value will be used as the CAS value during updates.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):

        self.__last_updated_time = last_updated_time

    @property
    def is_expected_to_error_on_conflict(self):
        """
        Error if conflicting alert policies are found.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_expected_to_error_on_conflict

    @is_expected_to_error_on_conflict.setter
    def is_expected_to_error_on_conflict(self, is_expected_to_error_on_conflict):

        self.__is_expected_to_error_on_conflict = is_expected_to_error_on_conflict

    @property
    def policies_to_override(self):
        """
        List of IDs of the alert policies that should be overridden.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__policies_to_override

    @policies_to_override.setter
    def policies_to_override(self, policies_to_override):

        self.__policies_to_override = policies_to_override

    @property
    def trigger_wait_period(self):
        """
        Waiting duration in seconds before triggering the alert, when the specified condition is met. It is set to 600s by default.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__trigger_wait_period

    @trigger_wait_period.setter
    def trigger_wait_period(self, trigger_wait_period):

        self.__trigger_wait_period = trigger_wait_period

    @property
    def related_policies(self):
        """
        List of alert policies that are related to the entities of the current policy.

        :type:
             list[ :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.RelatedPolicy` ]
        """  # noqa: E501
        return self.__related_policies

    @related_policies.setter
    def related_policies(self, related_policies):

        self.__related_policies = related_policies

    @property
    def entity_type(self):
        """
        Entity type associated with the User-Defined Alert policy. Allowed values are VM, node and cluster.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        if entity_type is not None and len(entity_type) > 10:
            raise ValueError("Invalid value for `entity_type`, length must be less than or equal to `10`")  # noqa: E501
        if entity_type is not None and len(entity_type) < 1:
            raise ValueError("Invalid value for `entity_type`, length must be greater than or equal to `1`")  # noqa: E501

        self.__entity_type = entity_type

    def _to_dict(self, sanitize):
        """Returns the model properties as a dict. Omits None properties based on the provided "sanitize" parameter.

        :param sanitize: A flag to omit None properties if set to True
        :type sanitize: bool
        """

        result = {}
        for attr, attr_type in six.iteritems(self.swagger_types):
        
            value = getattr(self, attr)
            if attr_type.startswith('OneOf'):
                type = getattr(ntnx_monitoring_py_client.models, attr_type.split('.')[-1])
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
        if issubclass(UserDefinedPolicy, dict):
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
        if not isinstance(other, UserDefinedPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
