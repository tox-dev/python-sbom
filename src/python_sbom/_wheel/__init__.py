"""Zip artifacts: one checked handle per build, verifying the wheels they bundle, and writing an SBOM in."""

from __future__ import annotations

__lazy_modules__ = [f"{__spec__.parent}._sdist"]  # ty: ignore[missing-union-attribute]  # imported modules have a spec

from ._sdist import add_to_sdist

__all__ = [
    "add_to_sdist",
]
