import sys
from pathlib import Path


def resource_path(relative_path: str) -> Path:
    """gets the resource path of the local path

    Args:
        local_path (str): path relative to this file

    Returns:
        str: resource file path
    """
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).parent / relative_path
