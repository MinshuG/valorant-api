# valorant-api
A Python wrapper for valorant-api.com

[![pypi](https://img.shields.io/pypi/v/valorant-api.svg)](https://pypi.python.org/pypi/valorant-api/)
[![Downloads](https://static.pepy.tech/personalized-badge/valorant-api?period=total&units=international_system&left_color=green&right_color=blue&left_text=Downloads)](https://pepy.tech/project/valorant-api)

# Installation
<!-- `pip install git+https://github.com/MinshuG/valorant-api` \
or \ -->
`pip install valorant-api`

# Usages
```py
# this code is just for reference

from valorant_api import SyncValorantApi, AsyncValorantApi

#sync
api = SyncValorantApi(language="ru-RU")
agents = api.get_agents()

#Async
api = AsyncValorantApi(language="ru-Ru")
agents = await api.get_agents()

# searching
agent = agents.find_where(displayname="Raze", developerName="Gumshoe")
agent = agents.find_first(displayname="Raze")

# agents image generation
from valorant_api import generators

font_file = r"valorant_api\fonts\Valorant Font.ttf"
# initialize class
generator = generators.AgentImageGenerator(font_file)
# generator actual image
image = await generator.generate(agent)
# save the image
image.save("image.png", "PNG")
```
# Agents Image Example
<img src="./example.png" alt="KAY/O" width="250"/>
<!-- ![KAY/O](/example.png) -->

# Requirements

* python-dateutil
* aiohttp
* requests
* Pillow