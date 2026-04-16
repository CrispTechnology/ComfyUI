import logging
import os

import folder_paths

logger = logging.getLogger(__name__)

_DEFAULT_DEPLOY_ENV = "local_git"
_ENV_FILENAME = ".comfy_environment"

_cached_value: str | None = None


def get_deploy_environment() -> str:
    global _cached_value
    if _cached_value is not None:
        return _cached_value

    env_file = os.path.join(folder_paths.base_path, _ENV_FILENAME)
    try:
        with open(env_file, encoding="utf-8") as f:
            value = f.read().strip()
            if value:
                _cached_value = value
                return _cached_value
    except FileNotFoundError:
        pass
    except Exception as e:
        logger.warning("Failed to read %s: %s", env_file, e)

    _cached_value = _DEFAULT_DEPLOY_ENV
    return _cached_value
