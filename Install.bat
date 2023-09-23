cd /D "%~dp0"
python -m venv venv
cd venv/Scripts
python -m pip install --upgrade pip
python -m pip install -r ..\..\requirements.txt
python pywin32_postinstall.py -install