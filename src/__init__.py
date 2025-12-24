"""Password Generator package."""

# Versioning program
from pathlib import Path

_version_file = Path(__file__).resolve().parent.parent / "VERSION"
__version__ = _version_file.read_text(encoding="utf-8").strip()

__all__ = ["__version__"]
