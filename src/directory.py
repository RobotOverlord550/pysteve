import os

# get global path from a path local to this module
def get_global_path(local_path: str) -> str:
    return os.path.join(
        os.path.dirname(__file__), 
        local_path
    )