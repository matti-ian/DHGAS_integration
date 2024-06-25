@echo off

REM create a virtual environment
python -m venv integration

REM install prerequisites
pip install -r requirements.txt

git clone https://github.com/wondergo2017/DHGAS
pip install -e DHGAS

git clone https://github.com/charleshsc/CommFormer
cd CommFormer
pip install -r requierments.txt

REM python -m site --user-site  user_python_path.txt
cd integration\Lib\site-packages
echo ..\DHGAS\dhgas > dhgas.pth
echo ..\CommFormer\commfommer > CommFormer.pth

cd ..
cd ..
cd ..
python normalize.py
