#Repository for smooth reading of English papers

## Enabling virtual environments.

```
python -m venv .venv
```

```
#Unix
source .venv/bin/activate
#Windows
source .venv/Scripts/activate
```

## Install libraries.

```
pip install -r requirements.txt
```

## How to run

Use the following command to use invoke.

```
inv run filename
```

Note that non-English print statements are garbled in Windows environment.
