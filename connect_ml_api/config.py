import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="connect_ml_api",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="connect_ml_api_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from connect_ml_api.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export connect_ml_api_KEY=value
export connect_ml_api_KEY="@int 42"
export connect_ml_api_KEY="@jinja {{ this.db.uri }}"
export connect_ml_api_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
connect_ml_api_ENV=production connect_ml_api run
```

Read more on https://dynaconf.com
"""
