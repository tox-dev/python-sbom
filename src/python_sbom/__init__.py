"""SBOMs for Python distributions: write PEP 770 CycloneDX SBOMs into wheels."""

from __future__ import annotations

__lazy_modules__ = [
    f"{__spec__.parent}._errors",  # ty: ignore[missing-union-attribute]  # imported modules have a spec
    f"{__spec__.parent}._model",  # ty: ignore[missing-union-attribute]  # imported modules have a spec
    f"{__spec__.parent}.version",  # ty: ignore[missing-union-attribute]  # imported modules have a spec
]

from ._errors import MissingExtraError, SbomError
from ._model import (
    BundledWheelInfo,
    Component,
    Contact,
    ContentProvider,
    Contributions,
    Dependency,
    Evidence,
    ExternalReference,
    Hash,
    Identity,
    IdentityMethod,
    License,
    LicenseInfo,
    OrganizationalEntity,
    ProjectIdentity,
    Property,
    ProviderContext,
    Settings,
)
from .version import __version__

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
    "MissingExtraError",
    "OrganizationalEntity",
    "ProjectIdentity",
    "Property",
    "ProviderContext",
    "SbomError",
    "Settings",
    "__version__",
]
