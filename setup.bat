@echo off

REM create a virtual environment
python -m venv integration

REM install prerequisites
pip install -r requirements.txt

git clone https://github.com/wondergo2017/DHGAS
pip install -e DHGAS

git clone https://github.com/charleshsc/CommFormer
cd CommFormer
pip install -r requirments.txt


REM Get the absolute path of the current directory
for %%I in (.) do set "absolute_path=%%~fI"

REM Create a file and write the absolute path into it

echo %absolute_path%\CommFormer.pth > CommFormer.pth

cd ..

REM copy data folder
robocopy "DHGAS data\ecomm" "DHGAS\data\ecomm"

REM activate virtual environment
integration/Scripts/activate

python normalize.py
