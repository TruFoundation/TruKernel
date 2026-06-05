from __future__ import annotations

import os
from pathlib import Path
from platformdirs import user_data_dir

KERNEL_NAME = os.getenv("TRUKERNEL_APP_NAME", "TruKernel")
KERNEL_AUTHOR = os.getenv("TRUKERNEL_APP_AUTHOR", "TruFoundation")


def get_data_dir() -> Path:
    """Return the platform-specific data directory for the kernel."""
    return Path(user_data_dir(KERNEL_NAME, KERNEL_AUTHOR))


def get_db_path() -> Path:
    """Return the internal kernel database path.

    The file is created lazily when a caller explicitly needs it.
    """
    return get_data_dir() / "kernel_state.db"
