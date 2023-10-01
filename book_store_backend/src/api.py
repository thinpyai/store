"""
Book store server's API definition

Author: Thin Pyai Win
Date:  27 August 2023
"""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

logger = logging.getLogger(__name__)

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def custom_openapi():
    """
    To display the customized API documentation

    Returns:
        dict: OpenAPI schema
    """
    if api.openapi_schema:
        return api.openapi_schema
    openapi_schema = get_openapi(
        title='Book system',
        version='0.1.0',
        description='Schema for Book Store System',
        routes=api.routes,
    )
    api.openapi_schema = openapi_schema
    return api.openapi_schema


api.openapi = custom_openapi
