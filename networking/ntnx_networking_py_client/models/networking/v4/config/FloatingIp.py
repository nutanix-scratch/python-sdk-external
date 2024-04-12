# coding: utf-8


"""
IGNORE:
    Nutanix Networking Versioned APIs

    Manage networking configuration on Nutanix clusters, including AHV and advanced networking.  # noqa: E501

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
import ntnx_networking_py_client.models
from ntnx_networking_py_client.models.OneOfnetworking.v4.config.FloatingIpassociation import FloatingIpassociation  # noqa: F401,E501
from ntnx_networking_py_client.models.common.v1.config.Metadata import Metadata  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.FloatingIPAddress import FloatingIPAddress  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.NetworkingBaseModel import NetworkingBaseModel  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.Subnet import Subnet  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.VmNic import VmNic  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.Vpc import Vpc  # noqa: F401,E501

class FloatingIp(NetworkingBaseModel):

    """Configure a floating IP.

    :param name: (:attr:`name`) Name of the floating IP.
    :type name: required
    :param description: (:attr:`description`) Description for the Floating IP.
    :type description: 
    :param association: (:attr:`association`) Association of the Floating IP with either NIC or Private IP
    :type association: 
    :param floating_ip: (:attr:`floating_ip`) 
    :type floating_ip: 
    :param external_subnet_reference: (:attr:`external_subnet_reference`) External subnet reference for the Floating IP to be allocated in on-prem only.
    :type external_subnet_reference: 
    :param external_subnet: (:attr:`external_subnet`) 
    :type external_subnet: 
    :param private_ip: (:attr:`private_ip`) Private IP value in string
    :type private_ip: 
    :param floating_ip_value: (:attr:`floating_ip_value`) Floating IP value in string
    :type floating_ip_value: 
    :param association_status: (:attr:`association_status`) Association status of floating IP.
    :type association_status: 
    :param vpc_reference: (:attr:`vpc_reference`) VPC reference UUID
    :type vpc_reference: 
    :param vm_nic_reference: (:attr:`vm_nic_reference`) VM NIC reference.
    :type vm_nic_reference: 
    :param vpc: (:attr:`vpc`) 
    :type vpc: 
    :param vm_nic: (:attr:`vm_nic`) 
    :type vm_nic: 

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
        'description': 'str',
        'association': 'OneOfnetworking.v4.config.FloatingIpassociation',
        'floating_ip': 'networking.v4.config.FloatingIPAddress',
        'external_subnet_reference': 'str',
        'external_subnet': 'networking.v4.config.Subnet',
        'private_ip': 'str',
        'floating_ip_value': 'str',
        'association_status': 'str',
        'vpc_reference': 'str',
        'vm_nic_reference': 'str',
        'vpc': 'networking.v4.config.Vpc',
        'vm_nic': 'networking.v4.config.VmNic',
        'metadata': 'common.v1.config.Metadata',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'association': 'association',
        'floating_ip': 'floatingIp',
        'external_subnet_reference': 'externalSubnetReference',
        'external_subnet': 'externalSubnet',
        'private_ip': 'privateIp',
        'floating_ip_value': 'floatingIpValue',
        'association_status': 'AssociationStatus',
        'vpc_reference': 'vpcReference',
        'vm_nic_reference': 'vmNicReference',
        'vpc': 'vpc',
        'vm_nic': 'vmNic',
        'metadata': 'metadata',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, description=None, association=None, floating_ip=None, external_subnet_reference=None, external_subnet=None, private_ip=None, floating_ip_value=None, association_status=None, vpc_reference=None, vm_nic_reference=None, vpc=None, vm_nic=None, metadata=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        NetworkingBaseModel.__init__(self, metadata, ext_id, links, tenant_id, *args, **kwargs)
        self.__name = None
        self.__description = None
        self.__association = None
        self.__floating_ip = None
        self.__external_subnet_reference = None
        self.__external_subnet = None
        self.__private_ip = None
        self.__floating_ip_value = None
        self.__association_status = None
        self.__vpc_reference = None
        self.__vm_nic_reference = None
        self.__vpc = None
        self.__vm_nic = None
        self.discriminator = None
        self.__name = name
        if description is not None:
            self.__description = description
        if association is not None:
            self.__association = association
        if floating_ip is not None:
            self.__floating_ip = floating_ip
        if external_subnet_reference is not None:
            self.__external_subnet_reference = external_subnet_reference
        if external_subnet is not None:
            self.__external_subnet = external_subnet
        if private_ip is not None:
            self.__private_ip = private_ip
        if floating_ip_value is not None:
            self.__floating_ip_value = floating_ip_value
        if association_status is not None:
            self.__association_status = association_status
        if vpc_reference is not None:
            self.__vpc_reference = vpc_reference
        if vm_nic_reference is not None:
            self.__vm_nic_reference = vm_nic_reference
        if vpc is not None:
            self.__vpc = vpc
        if vm_nic is not None:
            self.__vm_nic = vm_nic

    def _initialize_object_type(self):
        return 'networking.v4.config.FloatingIp'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def name(self):
        """
        Name of the floating IP.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501

        self.__name = name

    @property
    def description(self):
        """
        Description for the Floating IP.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__description

    @description.setter
    def description(self, description):
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501

        self.__description = description

    @property
    def association(self):
        """
        Association of the Floating IP with either NIC or Private IP

        :type:
                :class:`~ntnx_networking_py_client.models.networking.v4.config.VmNicAssociation` | 
                :class:`~ntnx_networking_py_client.models.networking.v4.config.PrivateIpAssociation`
                    """  # noqa: E501
        return self.__association

    @association.setter
    def association(self, association):

        self.__association = association

    @property
    def floating_ip(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.FloatingIPAddress`
        """  # noqa: E501
        return self.__floating_ip

    @floating_ip.setter
    def floating_ip(self, floating_ip):

        self.__floating_ip = floating_ip

    @property
    def external_subnet_reference(self):
        """
        External subnet reference for the Floating IP to be allocated in on-prem only.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__external_subnet_reference

    @external_subnet_reference.setter
    def external_subnet_reference(self, external_subnet_reference):
        if external_subnet_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', external_subnet_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `external_subnet_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__external_subnet_reference = external_subnet_reference

    @property
    def external_subnet(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.Subnet`
        """  # noqa: E501
        return self.__external_subnet

    @external_subnet.setter
    def external_subnet(self, external_subnet):

        self.__external_subnet = external_subnet

    @property
    def private_ip(self):
        """
        Private IP value in string

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__private_ip

    @private_ip.setter
    def private_ip(self, private_ip):

        self.__private_ip = private_ip

    @property
    def floating_ip_value(self):
        """
        Floating IP value in string

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__floating_ip_value

    @floating_ip_value.setter
    def floating_ip_value(self, floating_ip_value):

        self.__floating_ip_value = floating_ip_value

    @property
    def association_status(self):
        """
        Association status of floating IP.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__association_status

    @association_status.setter
    def association_status(self, association_status):

        self.__association_status = association_status

    @property
    def vpc_reference(self):
        """
        VPC reference UUID

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__vpc_reference

    @vpc_reference.setter
    def vpc_reference(self, vpc_reference):
        if vpc_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', vpc_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `vpc_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__vpc_reference = vpc_reference

    @property
    def vm_nic_reference(self):
        """
        VM NIC reference.

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__vm_nic_reference

    @vm_nic_reference.setter
    def vm_nic_reference(self, vm_nic_reference):
        if vm_nic_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', vm_nic_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `vm_nic_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__vm_nic_reference = vm_nic_reference

    @property
    def vpc(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.Vpc`
        """  # noqa: E501
        return self.__vpc

    @vpc.setter
    def vpc(self, vpc):

        self.__vpc = vpc

    @property
    def vm_nic(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.VmNic`
        """  # noqa: E501
        return self.__vm_nic

    @vm_nic.setter
    def vm_nic(self, vm_nic):

        self.__vm_nic = vm_nic

    def _to_dict(self, sanitize):
        """Returns the model properties as a dict. Omits None properties based on the provided "sanitize" parameter.

        :param sanitize: A flag to omit None properties if set to True
        :type sanitize: bool
        """

        result = {}
        for attr, attr_type in six.iteritems(self.swagger_types):
        
            value = getattr(self, attr)
            if attr_type.startswith('OneOf'):
                type = getattr(ntnx_networking_py_client.models, attr_type.split('.')[-1])
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
        if issubclass(FloatingIp, dict):
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
        if not isinstance(other, FloatingIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

