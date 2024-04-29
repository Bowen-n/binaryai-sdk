# Generated by ariadne-codegen
# Source: ./src/binaryai/query.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class DownloadLink(BaseModel):
    file: Optional["DownloadLinkFile"]


class DownloadLinkFile(BaseModel):
    download_link: Optional[str] = Field(alias="downloadLink")


DownloadLink.model_rebuild()
