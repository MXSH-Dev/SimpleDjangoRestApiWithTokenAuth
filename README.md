Create virtual environment on vagrant vm:
```
python3 -m venv ~/env
```

Activate virtual environment:
```
source ~/env/bin/activate
```

Deactivate virtual environment:
```
deactivate
```

Install python packages:
```
pip install -r requirements.txt
```

Add APPs to `settings.py`:
```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'profile_api'
]
```