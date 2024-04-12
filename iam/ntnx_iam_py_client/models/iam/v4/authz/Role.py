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

class Role(ExternalizableAbstractModel):

    """A Role to group the Operations.

    :param display_name: (:attr:`display_name`) The display name for the Role.
    :type display_name: 
    :param description: (:attr:`description`) Description of the Role.
    :type description: 
    :param client_name: (:attr:`client_name`) Client that created the entity.
    :type client_name: 
    :param operations: (:attr:`operations`) List of Operations for the Role.
    :type operations: 
    :param accessible_clients: (:attr:`accessible_clients`) List of Accessible Clients for the Role.
    :type accessible_clients: 
    :param accessible_entity_types: (:attr:`accessible_entity_types`) List of Accessible EntityTypes for the Role.
    :type accessible_entity_types: 
    :param assigned_users_count: (:attr:`assigned_users_count`) Number of Users assigned to given Role.
    :type assigned_users_count: 
    :param assigned_user_groups_count: (:attr:`assigned_user_groups_count`) Number of User Groups assigned to given Role.
    :type assigned_user_groups_count: 
    :param created_time: (:attr:`created_time`) The creation time of the Role.
    :type created_time: 
    :param last_updated_time: (:attr:`last_updated_time`) The time when the Role was last updated.
    :type last_updated_time: 
    :param created_by: (:attr:`created_by`) User or Service Name that created the Role.
    :type created_by: 
    :param is_system_defined: (:attr:`is_system_defined`) Flag identifying if the Role is system defined or not. (**Default** True)
    :type is_system_defined: 

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
        'display_name': 'str',
        'description': 'str',
        'client_name': 'str',
        'operations': 'list[str]',
        'accessible_clients': 'list[str]',
        'accessible_entity_types': 'list[str]',
        'assigned_users_count': 'int',
        'assigned_user_groups_count': 'int',
        'created_time': 'datetime',
        'last_updated_time': 'datetime',
        'created_by': 'str',
        'is_system_defined': 'bool',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'client_name': 'clientName',
        'operations': 'operations',
        'accessible_clients': 'accessibleClients',
        'accessible_entity_types': 'accessibleEntityTypes',
        'assigned_users_count': 'assignedUsersCount',
        'assigned_user_groups_count': 'assignedUserGroupsCount',
        'created_time': 'createdTime',
        'last_updated_time': 'lastUpdatedTime',
        'created_by': 'createdBy',
        'is_system_defined': 'isSystemDefined',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, display_name=None, description=None, client_name=None, operations=None, accessible_clients=None, accessible_entity_types=None, assigned_users_count=None, assigned_user_groups_count=None, created_time=None, last_updated_time=None, created_by=None, is_system_defined=True, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)
        self.__display_name = None
        self.__description = None
        self.__client_name = None
        self.__operations = None
        self.__accessible_clients = None
        self.__accessible_entity_types = None
        self.__assigned_users_count = None
        self.__assigned_user_groups_count = None
        self.__created_time = None
        self.__last_updated_time = None
        self.__created_by = None
        self.__is_system_defined = None
        self.discriminator = None
        if display_name is not None:
            self.__display_name = display_name
        if description is not None:
            self.__description = description
        if client_name is not None:
            self.__client_name = client_name
        if operations is not None:
            self.__operations = operations
        if accessible_clients is not None:
            self.__accessible_clients = accessible_clients
        if accessible_entity_types is not None:
            self.__accessible_entity_types = accessible_entity_types
        if assigned_users_count is not None:
            self.__assigned_users_count = assigned_users_count
        if assigned_user_groups_count is not None:
            self.__assigned_user_groups_count = assigned_user_groups_count
        if created_time is not None:
            self.__created_time = created_time
        if last_updated_time is not None:
            self.__last_updated_time = last_updated_time
        if created_by is not None:
            self.__created_by = created_by
        if is_system_defined is not None:
            self.__is_system_defined = is_system_defined

    def _initialize_object_type(self):
        return 'iam.v4.authz.Role'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def display_name(self):
        """
        The display name for the Role.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__display_name

    @display_name.setter
    def display_name(self, display_name):
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if display_name is not None and not re.search('^[^<>;\'()&+%\/\\\\\"`]*$', display_name):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[^<>;'()&+%\/\\\\\"`]*$/`")  # noqa: E501

        self.__display_name = display_name

    @property
    def description(self):
        """
        Description of the Role.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__description

    @description.setter
    def description(self, description):
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if description is not None and not re.search('^[^<>;()&+%\/\\\\\"`]*$', description):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[^<>;()&+%\/\\\\\"`]*$/`")  # noqa: E501

        self.__description = description

    @property
    def client_name(self):
        """
        Client that created the entity.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__client_name

    @client_name.setter
    def client_name(self, client_name):
        if client_name is not None and len(client_name) > 255:
            raise ValueError("Invalid value for `client_name`, length must be less than or equal to `255`")  # noqa: E501
        if client_name is not None and not re.search('^[^<>;\'()&+%\/\\\\\"`]*$', client_name):  # noqa: E501
            raise ValueError(r"Invalid value for `client_name`, must be a follow pattern or equal to `/^[^<>;'()&+%\/\\\\\"`]*$/`")  # noqa: E501

        self.__client_name = client_name

    @property
    def operations(self):
        """
        List of Operations for the Role.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__operations

    @operations.setter
    def operations(self, operations):

        self.__operations = operations

    @property
    def accessible_clients(self):
        """
        List of Accessible Clients for the Role.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__accessible_clients

    @accessible_clients.setter
    def accessible_clients(self, accessible_clients):

        self.__accessible_clients = accessible_clients

    @property
    def accessible_entity_types(self):
        """
        List of Accessible EntityTypes for the Role.

        :type:
            list[ :class:`~str` ]
        """  # noqa: E501
        return self.__accessible_entity_types

    @accessible_entity_types.setter
    def accessible_entity_types(self, accessible_entity_types):

        self.__accessible_entity_types = accessible_entity_types

    @property
    def assigned_users_count(self):
        """
        Number of Users assigned to given Role.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__assigned_users_count

    @assigned_users_count.setter
    def assigned_users_count(self, assigned_users_count):

        self.__assigned_users_count = assigned_users_count

    @property
    def assigned_user_groups_count(self):
        """
        Number of User Groups assigned to given Role.

        :type:

                :class:`~int`
        """  # noqa: E501
        return self.__assigned_user_groups_count

    @assigned_user_groups_count.setter
    def assigned_user_groups_count(self, assigned_user_groups_count):

        self.__assigned_user_groups_count = assigned_user_groups_count

    @property
    def created_time(self):
        """
        The creation time of the Role.

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
        The time when the Role was last updated.

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
        User or Service Name that created the Role.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__created_by

    @created_by.setter
    def created_by(self, created_by):

        self.__created_by = created_by

    @property
    def is_system_defined(self):
        """
        Flag identifying if the Role is system defined or not.

        :type:

                :class:`~bool`
        """  # noqa: E501
        return self.__is_system_defined

    @is_system_defined.setter
    def is_system_defined(self, is_system_defined):

        self.__is_system_defined = is_system_defined

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

