:: Set the path to your folder containing .whl files
set PACKAGE_DIR=offline_packages
py -m pip download -r requirements.txt -d offline_packages --only-binary=:all:
py -m pip install --no-index --find-links="%PACKAGE_DIR%" pip setuptools wheel

py -m pip install --no-index --find-links="%PACKAGE_DIR%" -r requirements.txt
echo Installation Complete
:: Option 1: Install all packages in the folder
:: py -m pip install --no-index --find-links="%PACKAGE_DIR%"

:: Option 2: Install specific packages from that folder
:: pip install --no-index --find-links="%PACKAGE_DIR%" package_name

pause