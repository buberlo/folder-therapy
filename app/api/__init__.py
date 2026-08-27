"""API layer for Folder Therapy.

This package contains the FastAPI router and endpoint definitions used by
``app.main`` to expose the Folder Therapy service.
"""

from . import routes  # noqa: F401

__all__ = ["routes"]