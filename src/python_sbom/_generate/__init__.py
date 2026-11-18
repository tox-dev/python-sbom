"""The pipelines that build a wheel's and an archive's SBOM from what _collect gathers, and write it."""

from __future__ import annotations

__lazy_modules__ = [f"{__spec__.parent}._embed"]  # ty: ignore[missing-union-attribute]  # imported modules have a spec

from ._embed import embed_built

__all__ = [
    "embed_built",
]
