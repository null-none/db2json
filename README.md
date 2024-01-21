db2json
===================

This client dumps all* the tables in an sqlite database as json.

Installation
------------

```bash
pip install db2json
```

Usage
-----

```python
from db2json.client import Db2json

client = Db2json("database.db")
client.sqlite_to_json()
```