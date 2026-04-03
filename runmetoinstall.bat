@echo off
:: Set the path to your folder containing .whl files
set PACKAGE_DIR=\offline_packages

python -m pip install --no-index --find-links=./offline_packages pip setuptools wheel

:: Option 1: Install all packages in the folder
pip install --no-index --find-links="%PACKAGE_DIR%" "%PACKAGE_DIR%\*.whl"

:: Option 2: Install specific packages from that folder
:: pip install --no-index --find-links="%PACKAGE_DIR%" package_name

pause