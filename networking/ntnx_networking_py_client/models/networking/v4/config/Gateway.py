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
from ntnx_networking_py_client.models.OneOfnetworking.v4.config.Gatewayservices import Gatewayservices  # noqa: F401,E501
from ntnx_networking_py_client.models.common.v1.config.Metadata import Metadata  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.GatewayDeployment import GatewayDeployment  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.NetworkingBaseModel import NetworkingBaseModel  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.Status import Status  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.Vm import Vm  # noqa: F401,E501
from ntnx_networking_py_client.models.networking.v4.config.Vpc import Vpc  # noqa: F401,E501

class Gateway(NetworkingBaseModel):

    """Network gateway

    :param name: (:attr:`name`) Name of the gateway
    :type name: 
    :param description: (:attr:`description`) Description of the gateway
    :type description: 
    :param vpc_reference: (:attr:`vpc_reference`) VPC
    :type vpc_reference: 
    :param cloud_network_reference: (:attr:`cloud_network_reference`) Cloud network on which network gateway is deployed
    :type cloud_network_reference: 
    :param installed_software_version: (:attr:`installed_software_version`) Software version installed on the gateway appliance
    :type installed_software_version: 
    :param supported_software_version: (:attr:`supported_software_version`) Supported gateway appliance version
    :type supported_software_version: 
    :param vm_reference: (:attr:`vm_reference`) Reference to a dedicated VM on which a local gateway is deployed 
    :type vm_reference: 
    :param deployment: (:attr:`deployment`) 
    :type deployment: 
    :param gateway_device_vendor: (:attr:`gateway_device_vendor`) Third-party gateway vendor
    :type gateway_device_vendor: 
    :param services: (:attr:`services`) 
    :type services: 
    :param status: (:attr:`status`) 
    :type status: 
    :param vpc: (:attr:`vpc`) 
    :type vpc: 
    :param vm: (:attr:`vm`) 
    :type vm: 

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
        'vpc_reference': 'str',
        'cloud_network_reference': 'str',
        'installed_software_version': 'str',
        'supported_software_version': 'str',
        'vm_reference': 'str',
        'deployment': 'networking.v4.config.GatewayDeployment',
        'gateway_device_vendor': 'str',
        'services': 'OneOfnetworking.v4.config.Gatewayservices',
        'status': 'networking.v4.config.Status',
        'vpc': 'networking.v4.config.Vpc',
        'vm': 'networking.v4.config.Vm',
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
        'vpc_reference': 'vpcReference',
        'cloud_network_reference': 'cloudNetworkReference',
        'installed_software_version': 'installedSoftwareVersion',
        'supported_software_version': 'supportedSoftwareVersion',
        'vm_reference': 'vmReference',
        'deployment': 'deployment',
        'gateway_device_vendor': 'gatewayDeviceVendor',
        'services': 'services',
        'status': 'status',
        'vpc': 'vpc',
        'vm': 'vm',
        'metadata': 'metadata',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, name=None, description=None, vpc_reference=None, cloud_network_reference=None, installed_software_version=None, supported_software_version=None, vm_reference=None, deployment=None, gateway_device_vendor=None, services=None, status=None, vpc=None, vm=None, metadata=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        NetworkingBaseModel.__init__(self, metadata, ext_id, links, tenant_id, *args, **kwargs)
        self.__name = None
        self.__description = None
        self.__vpc_reference = None
        self.__cloud_network_reference = None
        self.__installed_software_version = None
        self.__supported_software_version = None
        self.__vm_reference = None
        self.__deployment = None
        self.__gateway_device_vendor = None
        self.__services = None
        self.__status = None
        self.__vpc = None
        self.__vm = None
        self.discriminator = None
        if name is not None:
            self.__name = name
        if description is not None:
            self.__description = description
        if vpc_reference is not None:
            self.__vpc_reference = vpc_reference
        if cloud_network_reference is not None:
            self.__cloud_network_reference = cloud_network_reference
        if installed_software_version is not None:
            self.__installed_software_version = installed_software_version
        if supported_software_version is not None:
            self.__supported_software_version = supported_software_version
        if vm_reference is not None:
            self.__vm_reference = vm_reference
        if deployment is not None:
            self.__deployment = deployment
        if gateway_device_vendor is not None:
            self.__gateway_device_vendor = gateway_device_vendor
        if services is not None:
            self.__services = services
        if status is not None:
            self.__status = status
        if vpc is not None:
            self.__vpc = vpc
        if vm is not None:
            self.__vm = vm

    def _initialize_object_type(self):
        return 'networking.v4.config.Gateway'

    def _initialize_object_version(self):
        return 'v4.r0.b1'


    @property
    def name(self):
        """
        Name of the gateway

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501

        self.__name = name

    @property
    def description(self):
        """
        Description of the gateway

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
    def vpc_reference(self):
        """
        VPC

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
    def cloud_network_reference(self):
        """
        Cloud network on which network gateway is deployed

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__cloud_network_reference

    @cloud_network_reference.setter
    def cloud_network_reference(self, cloud_network_reference):
        if cloud_network_reference is not None and not re.search('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', cloud_network_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `cloud_network_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self.__cloud_network_reference = cloud_network_reference

    @property
    def installed_software_version(self):
        """
        Software version installed on the gateway appliance

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__installed_software_version

    @installed_software_version.setter
    def installed_software_version(self, installed_software_version):

        self.__installed_software_version = installed_software_version

    @property
    def supported_software_version(self):
        """
        Supported gateway appliance version

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__supported_software_version

    @supported_software_version.setter
    def supported_software_version(self, supported_software_version):

        self.__supported_software_version = supported_software_version

    @property
    def vm_reference(self):
        """
        Reference to a dedicated VM on which a local gateway is deployed 

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__vm_reference

    @vm_reference.setter
    def vm_reference(self, vm_reference):

        self.__vm_reference = vm_reference

    @property
    def deployment(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.GatewayDeployment`
        """  # noqa: E501
        return self.__deployment

    @deployment.setter
    def deployment(self, deployment):

        self.__deployment = deployment

    @property
    def gateway_device_vendor(self):
        """
        Third-party gateway vendor

        :type:

                :class:`~str`
        """  # noqa: E501
        return self.__gateway_device_vendor

    @gateway_device_vendor.setter
    def gateway_device_vendor(self, gateway_device_vendor):

        self.__gateway_device_vendor = gateway_device_vendor

    @property
    def services(self):
        """
        

        :type:
                :class:`~ntnx_networking_py_client.models.networking.v4.config.LocalNetworkServices` | 
                :class:`~ntnx_networking_py_client.models.networking.v4.config.RemoteNetworkServices`
                    """  # noqa: E501
        return self.__services

    @services.setter
    def services(self, services):

        self.__services = services

    @property
    def status(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.Status`
        """  # noqa: E501
        return self.__status

    @status.setter
    def status(self, status):

        self.__status = status

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
    def vm(self):
        """
        

        :type:
            :class:`~ntnx_networking_py_client.models.networking.v4.config.Vm`
        """  # noqa: E501
        return self.__vm

    @vm.setter
    def vm(self, vm):

        self.__vm = vm

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
        if issubclass(Gateway, dict):
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
        if not isinstance(other, Gateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
