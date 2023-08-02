set -x
set -e

virtualenv --python python3.10 env
source env/Scripts/activate

python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e