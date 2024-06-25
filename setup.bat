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
setlocal

REM Specify the directory and file name
set "directory=CommFormer"
set "file_name=CommFormer.pth"

REM Check if the directory exists
if not exist "%directory%" (
    echo Directory does not exist: %directory%
    exit /b 1
)

REM Get the absolute path of the directory
for %%I in ("%directory%") do set "absolute_path=%%~fI"

REM Create the file and write the absolute path into it
set "file_path=%directory%\%file_name%"
echo %absolute_path% > "%file_path%"

REM copy data folder
robocopy "DHGAS_integration\DHGAS data\ecomm" "DHGAS_integration\DHGAS\data\ecomm"

REM activate virtual environment
integration/Scripts/activate

python normalize.py
