# coding: utf-8

# flake8: noqa


"""
IGNORE:
    Nutanix Licensing Versioned APIs

    licensing desc placeholder  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
from __future__ import absolute_import

# import apis into sdk package
from ntnx_licensing_py_client.api.end_user_license_agreements_api import EndUserLicenseAgreementsApi
from ntnx_licensing_py_client.api.licenses_api import LicensesApi
# import ApiClient
from ntnx_licensing_py_client.api_client import ApiClient
from ntnx_licensing_py_client.configuration import Configuration
# import models into sdk package
from ntnx_licensing_py_client.models.OneOfcommon.v1.config.KVPairvalue import KVPairvalue
from ntnx_licensing_py_client.models.OneOflicensing.v4.agreements.AddUserApiResponsedata import AddUserApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.agreements.GetEulaApiResponsedata import GetEulaApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.agreements.UpdateEulaApiResponsedata import UpdateEulaApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.GetClusterAllowanceApiResponsedata import GetClusterAllowanceApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.GetClusterEntitlementApiResponsedata import GetClusterEntitlementApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.GetClusterViolationApiResponsedata import GetClusterViolationApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.GetComplianceApiResponsedata import GetComplianceApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.GetLicenseApiResponsedata import GetLicenseApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.GetSettingApiResponsedata import GetSettingApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.ListClusterAllowancesApiResponsedata import ListClusterAllowancesApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.ListClusterEntitlementsApiResponsedata import ListClusterEntitlementsApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.ListClusterViolationsApiResponsedata import ListClusterViolationsApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.ListCompliancesApiResponsedata import ListCompliancesApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.ListFeaturesApiResponsedata import ListFeaturesApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.ListLicensesApiResponsedata import ListLicensesApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.config.ListSettingsApiResponsedata import ListSettingsApiResponsedata
from ntnx_licensing_py_client.models.OneOflicensing.v4.error.ErrorResponseerror import ErrorResponseerror
from ntnx_licensing_py_client.models.common.v1.config.Flag import Flag
from ntnx_licensing_py_client.models.common.v1.config.KVPair import KVPair
from ntnx_licensing_py_client.models.common.v1.config.Message import Message
from ntnx_licensing_py_client.models.common.v1.config.MessageSeverity import MessageSeverity
from ntnx_licensing_py_client.models.common.v1.config.TenantAwareModel import TenantAwareModel
from ntnx_licensing_py_client.models.common.v1.response.ApiLink import ApiLink
from ntnx_licensing_py_client.models.common.v1.response.ApiResponseMetadata import ApiResponseMetadata
from ntnx_licensing_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel
from ntnx_licensing_py_client.models.licensing.v4.agreements.AddUserApiResponse import AddUserApiResponse
from ntnx_licensing_py_client.models.licensing.v4.agreements.Eula import Eula
from ntnx_licensing_py_client.models.licensing.v4.agreements.EulaUser import EulaUser
from ntnx_licensing_py_client.models.licensing.v4.agreements.GetEulaApiResponse import GetEulaApiResponse
from ntnx_licensing_py_client.models.licensing.v4.agreements.UpdateEulaApiResponse import UpdateEulaApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.AllowanceDetail import AllowanceDetail
from ntnx_licensing_py_client.models.licensing.v4.config.AllowanceDetailProjection import AllowanceDetailProjection
from ntnx_licensing_py_client.models.licensing.v4.config.BaseClusterInfo import BaseClusterInfo
from ntnx_licensing_py_client.models.licensing.v4.config.BaseLicenseInfo import BaseLicenseInfo
from ntnx_licensing_py_client.models.licensing.v4.config.CapacityViolation import CapacityViolation
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterAllowance import ClusterAllowance
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterAllowanceProjection import ClusterAllowanceProjection
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterEntitlement import ClusterEntitlement
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterEntitlementProjection import ClusterEntitlementProjection
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterTypeEnum import ClusterTypeEnum
from ntnx_licensing_py_client.models.licensing.v4.config.ClusterViolation import ClusterViolation
from ntnx_licensing_py_client.models.licensing.v4.config.Compliance import Compliance
from ntnx_licensing_py_client.models.licensing.v4.config.ComplianceProjection import ComplianceProjection
from ntnx_licensing_py_client.models.licensing.v4.config.Consumption import Consumption
from ntnx_licensing_py_client.models.licensing.v4.config.ConsumptionProjection import ConsumptionProjection
from ntnx_licensing_py_client.models.licensing.v4.config.EnforcementActionsEnum import EnforcementActionsEnum
from ntnx_licensing_py_client.models.licensing.v4.config.EnforcementLevelEnum import EnforcementLevelEnum
from ntnx_licensing_py_client.models.licensing.v4.config.EnforcementPolicyEnum import EnforcementPolicyEnum
from ntnx_licensing_py_client.models.licensing.v4.config.EntitlementDetail import EntitlementDetail
from ntnx_licensing_py_client.models.licensing.v4.config.EntitlementDetailProjection import EntitlementDetailProjection
from ntnx_licensing_py_client.models.licensing.v4.config.ExpiredLicense import ExpiredLicense
from ntnx_licensing_py_client.models.licensing.v4.config.Feature import Feature
from ntnx_licensing_py_client.models.licensing.v4.config.FeatureDetail import FeatureDetail
from ntnx_licensing_py_client.models.licensing.v4.config.FeatureProjection import FeatureProjection
from ntnx_licensing_py_client.models.licensing.v4.config.FeatureViolation import FeatureViolation
from ntnx_licensing_py_client.models.licensing.v4.config.GetClusterAllowanceApiResponse import GetClusterAllowanceApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.GetClusterEntitlementApiResponse import GetClusterEntitlementApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.GetClusterViolationApiResponse import GetClusterViolationApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.GetComplianceApiResponse import GetComplianceApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.GetLicenseApiResponse import GetLicenseApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.GetSettingApiResponse import GetSettingApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.License import License
from ntnx_licensing_py_client.models.licensing.v4.config.LicenseCategoryEnum import LicenseCategoryEnum
from ntnx_licensing_py_client.models.licensing.v4.config.LicenseProjection import LicenseProjection
from ntnx_licensing_py_client.models.licensing.v4.config.LicenseTypeEnum import LicenseTypeEnum
from ntnx_licensing_py_client.models.licensing.v4.config.ListClusterAllowancesApiResponse import ListClusterAllowancesApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.ListClusterEntitlementsApiResponse import ListClusterEntitlementsApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.ListClusterViolationsApiResponse import ListClusterViolationsApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.ListCompliancesApiResponse import ListCompliancesApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.ListFeaturesApiResponse import ListFeaturesApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.ListLicensesApiResponse import ListLicensesApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.ListSettingsApiResponse import ListSettingsApiResponse
from ntnx_licensing_py_client.models.licensing.v4.config.LogicalVersion import LogicalVersion
from ntnx_licensing_py_client.models.licensing.v4.config.MeterEnum import MeterEnum
from ntnx_licensing_py_client.models.licensing.v4.config.NutanixClusterConfig import NutanixClusterConfig
from ntnx_licensing_py_client.models.licensing.v4.config.PostPaidCategoryEnum import PostPaidCategoryEnum
from ntnx_licensing_py_client.models.licensing.v4.config.PostPaidConfig import PostPaidConfig
from ntnx_licensing_py_client.models.licensing.v4.config.ProductNameEnum import ProductNameEnum
from ntnx_licensing_py_client.models.licensing.v4.config.ResetScopeEnum import ResetScopeEnum
from ntnx_licensing_py_client.models.licensing.v4.config.ScopeEnum import ScopeEnum
from ntnx_licensing_py_client.models.licensing.v4.config.Service import Service
from ntnx_licensing_py_client.models.licensing.v4.config.ServiceProjection import ServiceProjection
from ntnx_licensing_py_client.models.licensing.v4.config.ServiceViolation import ServiceViolation
from ntnx_licensing_py_client.models.licensing.v4.config.ServiceViolationEnum import ServiceViolationEnum
from ntnx_licensing_py_client.models.licensing.v4.config.Setting import Setting
from ntnx_licensing_py_client.models.licensing.v4.config.StatusEnum import StatusEnum
from ntnx_licensing_py_client.models.licensing.v4.config.SubCategoryEnum import SubCategoryEnum
from ntnx_licensing_py_client.models.licensing.v4.config.TypeEnum import TypeEnum
from ntnx_licensing_py_client.models.licensing.v4.error.AppMessage import AppMessage
from ntnx_licensing_py_client.models.licensing.v4.error.ErrorResponse import ErrorResponse
from ntnx_licensing_py_client.models.licensing.v4.error.SchemaValidationError import SchemaValidationError
from ntnx_licensing_py_client.models.licensing.v4.error.SchemaValidationErrorMessage import SchemaValidationErrorMessage