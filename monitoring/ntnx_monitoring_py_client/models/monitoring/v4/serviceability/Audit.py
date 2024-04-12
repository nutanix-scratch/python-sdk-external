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
from ntnx_monitoring_py_client.models.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from ntnx_monitoring_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.common.EntityReference import EntityReference  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.common.OperationType import OperationType  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.common.Parameter import Parameter  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.AuditEntityReference import AuditEntityReference  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.Status import Status  # noqa: F401,E501
from ntnx_monitoring_py_client.models.monitoring.v4.serviceability.UserReference import UserReference  # noqa: F401,E501

class Audit(ExternalizableAbstractModel):

    """

    :param source_entity: (:attr:`source_entity`) 
    :type source_entity: 
    :param cluster_reference: (:attr:`cluster_reference`) 
    :type cluster_reference: 
    :param affected_entities: (:attr:`affected_entities`) List of all entities that are affected by the event or audit.
    :type affected_entities: 
    :param operation_type: (:attr:`operation_type`) 
    :type operation_type: 
    :param message: (:attr:`message`) Additional message associated with the audit.
    :type message: 
    :param parameters: (:attr:`parameters`) Additional parameters associated with the audit. These parameters can be used to indicate custom key-value pairs for a given audit instance. For example, a service down audit in Prism Central can have the service name as a parameter.
    :type parameters: 
    :param operation_start_time: (:attr:`operation_start_time`) The audit operation start time in ISO 8601 format.
    :type operation_start_time: 
    :param operation_end_time: (:attr:`operation_end_time`) The audit operation end time in ISO 8601 format.
    :type operation_end_time: 
    :param user_reference: (:attr:`user_reference`) 
    :type user_reference: 
    :param service_name: (:attr:`service_name`) The service which raised the event or audit. For internal Nutanix services, this value is set to \"Nutanix\".
    :type service_name: 
    :param audit_type: (:attr:`audit_type`) The unique name for a given audit type. For example, VMCloneAudit, or VMDeleteAudit.
    :type audit_type: 
    :param status: (:attr:`status`) 
    :type status: 
    :param creation_time: (:attr:`creation_time`) The time in ISO 8601 format when the audit was created.
    :type creation_time: 

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
        'source_entity': 'monitoring.v4.serviceability.AuditEntityReference',
        'cluster_reference': 'monitoring.v4.common.EntityReference',
        'affected_entities': 'list[monitoring.v4.common.EntityReference]',
        'operation_type': 'monitoring.v4.common.OperationType',
        'message': 'str',
        'parameters': 'list[monitoring.v4.common.Parameter]',
        'operation_start_time': 'datetime',
        'operation_end_time': 'datetime',
        'user_reference': 'monitoring.v4.serviceability.UserReference',
        'service_name': 'str',
        'audit_type': 'str',
        'status': 'monitoring.v4.serviceability.Status',
        'creation_time': 'datetime',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'source_entity': 'sourceEntity',
        'cluster_reference': 'clusterReference',
        'affected_entities': 'affectedEntities',
        'operation_type': 'operationType',
        'message': 'message',
        'parameters': 'parameters',
        'operation_start_time': 'operationStartTime',
        'operation_end_time': 'operationEndTime',
        'user_reference': 'userReference',
        'service_name': 'serviceName',
        'audit_type': 'auditType',
        'status': 'status',
        'creation_time': 'creationTime',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, source_entity=None, cluster_reference=None, affected_entities=None, operation_type=None, message=None, parameters=None, operation_start_time=None, operation_end_time=None, user_reference=None, service_name=None, audit_type=None, status=None, creation_time=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__source_entity = None
        self.__cluster_reference = None
        self.__affected_entities = None
        self.__operation_type = None
        self.__message = None
        self.__parameters = None
        self.__operation_start_time = None
        self.__operation_end_time = None
        self.__user_reference = None
        self.__service_name = None
        self.__audit_type = None
        self.__status = None
        self.__creation_time = None
        self.discriminator = None
        if source_entity is not None:
            self.__source_entity = source_entity
        if cluster_reference is not None:
            self.__cluster_reference = cluster_reference
        if affected_entities is not None:
            self.__affected_entities = affected_entities
        if operation_type is not None:
            self.__operation_type = operation_type
        if message is not None:
            self.__message = message
        if parameters is not None:
            self.__parameters = parameters
        if operation_start_time is not None:
            self.__operation_start_time = operation_start_time
        if operation_end_time is not None:
            self.__operation_end_time = operation_end_time
        if user_reference is not None:
            self.__user_reference = user_reference
        if service_name is not None:
            self.__service_name = service_name
        if audit_type is not None:
            self.__audit_type = audit_type
        if status is not None:
            self.__status = status
        if creation_time is not None:
            self.__creation_time = creation_time

    def _initialize_object_type(self):
        return 'monitoring.v4.serviceability.Audit'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def source_entity(self):
        """
        

        :type:
            :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.AuditEntityReference`
        """  # noqa: E501
        return self.__source_entity

    @source_entity.setter
    def source_entity(self, source_entity):

        self.__source_entity = source_entity

    @property
    def cluster_reference(self):
        """
        

        :type:
            :class:`~ntnx_monitoring_py_client.models.monitoring.v4.common.EntityReference`
        """  # noqa: E501
        return self.__cluster_reference

    @cluster_reference.setter
    def cluster_reference(self, cluster_reference):

        self.__cluster_reference = cluster_reference

    @property
    def affected_entities(self):
        """
        List of all entities that are affected by the event or audit.

        :type:
             list[ :class:`~ntnx_monitoring_py_client.models.monitoring.v4.common.EntityReference` ]
        """  # noqa: E501
        return self.__affected_entities

    @affected_entities.setter
    def affected_entities(self, affected_entities):

        self.__affected_entities = affected_entities

    @property
    def operation_type(self):
        """
        

        :type:
            :class:`~ntnx_monitoring_py_client.models.monitoring.v4.common.OperationType`
        """  # noqa: E501
        return self.__operation_type

    @operation_type.setter
    def operation_type(self, operation_type):

        self.__operation_type = operation_type

    @property
    def message(self):
        """
        Additional message associated with the audit.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__message

    @message.setter
    def message(self, message):
        if message is not None and len(message) > 1024:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `1024`")  # noqa: E501

        self.__message = message

    @property
    def parameters(self):
        """
        Additional parameters associated with the audit. These parameters can be used to indicate custom key-value pairs for a given audit instance. For example, a service down audit in Prism Central can have the service name as a parameter.

        :type:
             list[ :class:`~ntnx_monitoring_py_client.models.monitoring.v4.common.Parameter` ]
        """  # noqa: E501
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters):

        self.__parameters = parameters

    @property
    def operation_start_time(self):
        """
        The audit operation start time in ISO 8601 format.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__operation_start_time

    @operation_start_time.setter
    def operation_start_time(self, operation_start_time):

        self.__operation_start_time = operation_start_time

    @property
    def operation_end_time(self):
        """
        The audit operation end time in ISO 8601 format.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__operation_end_time

    @operation_end_time.setter
    def operation_end_time(self, operation_end_time):

        self.__operation_end_time = operation_end_time

    @property
    def user_reference(self):
        """
        

        :type:
            :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.UserReference`
        """  # noqa: E501
        return self.__user_reference

    @user_reference.setter
    def user_reference(self, user_reference):

        self.__user_reference = user_reference

    @property
    def service_name(self):
        """
        The service which raised the event or audit. For internal Nutanix services, this value is set to \"Nutanix\".

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__service_name

    @service_name.setter
    def service_name(self, service_name):

        self.__service_name = service_name

    @property
    def audit_type(self):
        """
        The unique name for a given audit type. For example, VMCloneAudit, or VMDeleteAudit.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__audit_type

    @audit_type.setter
    def audit_type(self, audit_type):

        self.__audit_type = audit_type

    @property
    def status(self):
        """
        

        :type:
            :class:`~ntnx_monitoring_py_client.models.monitoring.v4.serviceability.Status`
        """  # noqa: E501
        return self.__status

    @status.setter
    def status(self, status):

        self.__status = status

    @property
    def creation_time(self):
        """
        The time in ISO 8601 format when the audit was created.

        :type:

                :class:`~datetime`
        """  # noqa: E501
        return self.__creation_time

    @creation_time.setter
    def creation_time(self, creation_time):

        self.__creation_time = creation_time

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
        if issubclass(Audit, dict):
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
        if not isinstance(other, Audit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
