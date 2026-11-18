"""The document types exported by python-sbom."""

from __future__ import annotations

__lazy_modules__ = [
    f"{__spec__.parent}._content",  # ty: ignore[missing-union-attribute]  # imported modules have a spec
    f"{__spec__.parent}._identity",  # ty: ignore[missing-union-attribute]  # imported modules have a spec
    f"{__spec__.parent}._inputs",  # ty: ignore[missing-union-attribute]  # imported modules have a spec
    f"{__spec__.parent}._types",  # ty: ignore[missing-union-attribute]  # imported modules have a spec
]

from ._content import BundledWheelInfo, ContentProvider, Contributions, ProviderContext
from ._identity import ProjectIdentity
from ._inputs import Revision, Settings
from ._types import (
    Component,
    Contact,
    Dependency,
    Evidence,
    ExternalReference,
    Hash,
    Identity,
    IdentityMethod,
    License,
    LicenseInfo,
    OrganizationalEntity,
    Property,
)

__all__ = [
    "BundledWheelInfo",
    "Component",
    "Contact",
    "ContentProvider",
    "Contributions",
    "Dependency",
    "Evidence",
    "ExternalReference",
    "Hash",
    "Identity",
    "IdentityMethod",
    "License",
    "LicenseInfo",
    "OrganizationalEntity",
    "ProjectIdentity",
    "Property",
    "ProviderContext",
    "Revision",
    "Settings",
]
