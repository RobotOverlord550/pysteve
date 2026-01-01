import os


def get_global_path(local_path: str) -> str:
    """sets the global path of the local path

    Args:
        local_path (str): path relative to this file

    Returns:
        str: global file path
    """
    return os.path.join(
        os.path.dirname(__file__), 
        local_path
    )