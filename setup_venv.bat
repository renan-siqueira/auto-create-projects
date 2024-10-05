
@echo off
SET VENV_DIR=.venv

IF NOT EXIST %VENV_DIR% (
    python -m venv %VENV_DIR%
    echo Virtual environment created.
)

call %VENV_DIR%\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Virtual environment setup complete.
