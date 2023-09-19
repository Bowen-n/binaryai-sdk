# Generated by ariadne-codegen on 2023-09-18 11:53
# Source: https://api.binaryai.cn/v1/endpoint

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import FileType, SearchBinaryStatisticKey, SymbolType


class BindiffMatchInput(BaseModel):
    sha256: str


class CreateFileInput(BaseModel):
    ownership_po_s: Optional[str] = Field(alias="ownershipPoS", default=None)
    ticket_i_d: str = Field(alias="ticketID")


class CreateMatchInput(BaseModel):
    sha256: str
    target: "MatchTargetInput"


class CreateUploadTicketInput(BaseModel):
    captcha_random_string: Optional[str] = Field(alias="captchaRandomString", default=None)
    captcha_ticket: Optional[str] = Field(alias="captchaTicket", default=None)
    md5: Optional[str] = None
    name: Optional[str] = None
    sha256: Optional[str] = None


class MatchTargetInput(BaseModel):
    bindiff: Optional["BindiffMatchInput"] = None
    oss: Optional["OSSMatchInput"] = None


class OSSMatchInput(BaseModel):
    repo_u_r_ls: Optional[List[str]] = Field(alias="repoURLs", default=None)


class ReanalyzeInput(BaseModel):
    sha256: str
    skip_version_check: Optional[bool] = Field(alias="skipVersionCheck", default=None)


class SearchBinaryInput(BaseModel):
    include_type: Optional[List[FileType]] = Field(alias="includeType", default=None)
    keyword: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    statistic: Optional[List["SearchBinaryStatisticInput"]] = None
    third_lib: Optional[List["SearchThirdLib"]] = Field(alias="thirdLib", default=None)


class SearchBinaryStatisticInput(BaseModel):
    keys: List[SearchBinaryStatisticKey]


class SearchCVESec(BaseModel):
    name: str


class SearchFileInput(BaseModel):
    md5: Optional[str] = None
    sha256: Optional[str] = None


class SearchThirdLib(BaseModel):
    cves: Optional[List["SearchCVESec"]] = None
    name: Optional[str] = None
    version: Optional[List[str]] = None


class SymbolTableFilter(BaseModel):
    symbol_type: Optional[List[SymbolType]] = Field(alias="symbolType", default=None)


BindiffMatchInput.model_rebuild()
CreateFileInput.model_rebuild()
CreateMatchInput.model_rebuild()
CreateUploadTicketInput.model_rebuild()
MatchTargetInput.model_rebuild()
OSSMatchInput.model_rebuild()
ReanalyzeInput.model_rebuild()
SearchBinaryInput.model_rebuild()
SearchBinaryStatisticInput.model_rebuild()
SearchCVESec.model_rebuild()
SearchFileInput.model_rebuild()
SearchThirdLib.model_rebuild()
SymbolTableFilter.model_rebuild()
