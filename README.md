# valorant_api
python wrapper for valorant-api.com

# Installation
`pip install git+https://github.com/MinshuG/valorant-api`

# Usages
```py
from valorant_api import SyncValorantApi, AsyncValorantApi

#sync
api = SyncValorantApi(language="ru-RU")
agents = api.get_agents()

#Async
api = AsyncValorantApi(language="ru-Ru")
agents = await api.get_agents()
```

# Requirements

* python-dateutil==2.8.1
* aiohttp==3.7.3
* requests==2.25.1