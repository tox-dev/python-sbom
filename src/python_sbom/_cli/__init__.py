"""The command line: parsing options and running one command per subcommand."""

from __future__ import annotations

__lazy_modules__ = [f"{__spec__.parent}._main"]  # ty: ignore[missing-union-attribute]  # imported modules have a spec

from ._main import main

__all__ = [
    "main",
]
