# coding: utf-8

# flake8: noqa

"""
IGNORE:
    Nutanix Prism Versioned APIs

    Manage Tasks, Category Associations and Submit Batch Operations.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
from __future__ import absolute_import

# import models into model package
from ntnx_prism_py_client.models.OneOfcommon.v1.config.KVPairvalue import KVPairvalue
from ntnx_prism_py_client.models.OneOfprism.v4.config.CancelTaskApiResponsedata import CancelTaskApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.config.CreateCategoryApiResponsedata import CreateCategoryApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.config.DeleteCategoryApiResponsedata import DeleteCategoryApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.config.GetCategoryApiResponsedata import GetCategoryApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.config.GetTaskApiResponsedata import GetTaskApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.config.ListCategoriesApiResponsedata import ListCategoriesApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.config.ListTasksApiResponsedata import ListTasksApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.config.UpdateCategoryApiResponsedata import UpdateCategoryApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.error.ErrorResponseerror import ErrorResponseerror
from ntnx_prism_py_client.models.OneOfprism.v4.operations.GetBatchApiResponsedata import GetBatchApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.operations.ListBatchesApiResponsedata import ListBatchesApiResponsedata
from ntnx_prism_py_client.models.OneOfprism.v4.operations.SubmitBatchApiResponsedata import SubmitBatchApiResponsedata
from ntnx_prism_py_client.models.common.v1.config.Flag import Flag
from ntnx_prism_py_client.models.common.v1.config.KVPair import KVPair
from ntnx_prism_py_client.models.common.v1.config.Message import Message
from ntnx_prism_py_client.models.common.v1.config.MessageSeverity import MessageSeverity
from ntnx_prism_py_client.models.common.v1.config.TenantAwareModel import TenantAwareModel
from ntnx_prism_py_client.models.common.v1.response.ApiLink import ApiLink
from ntnx_prism_py_client.models.common.v1.response.ApiResponseMetadata import ApiResponseMetadata
from ntnx_prism_py_client.models.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel
from ntnx_prism_py_client.models.prism.v4.config.AssociationDetail import AssociationDetail
from ntnx_prism_py_client.models.prism.v4.config.AssociationDetailOld import AssociationDetailOld
from ntnx_prism_py_client.models.prism.v4.config.AssociationDetailOldProjection import AssociationDetailOldProjection
from ntnx_prism_py_client.models.prism.v4.config.AssociationDetailProjection import AssociationDetailProjection
from ntnx_prism_py_client.models.prism.v4.config.AssociationSummary import AssociationSummary
from ntnx_prism_py_client.models.prism.v4.config.AssociationSummaryProjection import AssociationSummaryProjection
from ntnx_prism_py_client.models.prism.v4.config.CancelTaskApiResponse import CancelTaskApiResponse
from ntnx_prism_py_client.models.prism.v4.config.Category import Category
from ntnx_prism_py_client.models.prism.v4.config.CategoryAssociationSummaryOld import CategoryAssociationSummaryOld
from ntnx_prism_py_client.models.prism.v4.config.CategoryAssociationSummaryOldProjection import CategoryAssociationSummaryOldProjection
from ntnx_prism_py_client.models.prism.v4.config.CategoryOld import CategoryOld
from ntnx_prism_py_client.models.prism.v4.config.CategoryOldProjection import CategoryOldProjection
from ntnx_prism_py_client.models.prism.v4.config.CategoryProjection import CategoryProjection
from ntnx_prism_py_client.models.prism.v4.config.CategorySummaryOld import CategorySummaryOld
from ntnx_prism_py_client.models.prism.v4.config.CategorySummaryOldProjection import CategorySummaryOldProjection
from ntnx_prism_py_client.models.prism.v4.config.CategoryType import CategoryType
from ntnx_prism_py_client.models.prism.v4.config.CreateCategoryApiResponse import CreateCategoryApiResponse
from ntnx_prism_py_client.models.prism.v4.config.DeleteCategoryApiResponse import DeleteCategoryApiResponse
from ntnx_prism_py_client.models.prism.v4.config.EntityReference import EntityReference
from ntnx_prism_py_client.models.prism.v4.config.GetCategoryApiResponse import GetCategoryApiResponse
from ntnx_prism_py_client.models.prism.v4.config.GetTaskApiResponse import GetTaskApiResponse
from ntnx_prism_py_client.models.prism.v4.config.ListCategoriesApiResponse import ListCategoriesApiResponse
from ntnx_prism_py_client.models.prism.v4.config.ListTasksApiResponse import ListTasksApiResponse
from ntnx_prism_py_client.models.prism.v4.config.OwnerReference import OwnerReference
from ntnx_prism_py_client.models.prism.v4.config.Reference import Reference
from ntnx_prism_py_client.models.prism.v4.config.ResourceGroup import ResourceGroup
from ntnx_prism_py_client.models.prism.v4.config.ResourceType import ResourceType
from ntnx_prism_py_client.models.prism.v4.config.Task import Task
from ntnx_prism_py_client.models.prism.v4.config.TaskReference import TaskReference
from ntnx_prism_py_client.models.prism.v4.config.TaskReferenceInternal import TaskReferenceInternal
from ntnx_prism_py_client.models.prism.v4.config.TaskStatus import TaskStatus
from ntnx_prism_py_client.models.prism.v4.config.TaskStep import TaskStep
from ntnx_prism_py_client.models.prism.v4.config.UpdateCategoryApiResponse import UpdateCategoryApiResponse
from ntnx_prism_py_client.models.prism.v4.error.AppMessage import AppMessage
from ntnx_prism_py_client.models.prism.v4.error.ErrorResponse import ErrorResponse
from ntnx_prism_py_client.models.prism.v4.error.SchemaValidationError import SchemaValidationError
from ntnx_prism_py_client.models.prism.v4.error.SchemaValidationErrorMessage import SchemaValidationErrorMessage
from ntnx_prism_py_client.models.prism.v4.operations.ActionType import ActionType
from ntnx_prism_py_client.models.prism.v4.operations.Batch import Batch
from ntnx_prism_py_client.models.prism.v4.operations.BatchCompletionStatus import BatchCompletionStatus
from ntnx_prism_py_client.models.prism.v4.operations.BatchExecutionStatus import BatchExecutionStatus
from ntnx_prism_py_client.models.prism.v4.operations.BatchSpec import BatchSpec
from ntnx_prism_py_client.models.prism.v4.operations.BatchSpecMetadata import BatchSpecMetadata
from ntnx_prism_py_client.models.prism.v4.operations.BatchSpecPayload import BatchSpecPayload
from ntnx_prism_py_client.models.prism.v4.operations.BatchSpecPayloadMetadata import BatchSpecPayloadMetadata
from ntnx_prism_py_client.models.prism.v4.operations.BatchSpecPayloadMetadataHeader import BatchSpecPayloadMetadataHeader
from ntnx_prism_py_client.models.prism.v4.operations.BatchSpecPayloadMetadataPath import BatchSpecPayloadMetadataPath
from ntnx_prism_py_client.models.prism.v4.operations.GetBatchApiResponse import GetBatchApiResponse
from ntnx_prism_py_client.models.prism.v4.operations.ListBatchesApiResponse import ListBatchesApiResponse
from ntnx_prism_py_client.models.prism.v4.operations.SubmitBatchApiResponse import SubmitBatchApiResponse
from ntnx_prism_py_client.api_response import ApiResponse
