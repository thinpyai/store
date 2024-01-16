"""
Server's API definition

Author: Thin Pyai Win
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
        title='Url Shortener',
        version='0.1.0',
        description='Schema for url shortener service',
        routes=api.routes,
    )
    api.openapi_schema = openapi_schema
    return api.openapi_schema


api.openapi = custom_openapi
