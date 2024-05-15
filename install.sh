echo "Installing frontend"
# shellcheck disable=SC2164
cd frontend
pip install -r requirements.txt

echo "Installing backend"
# shellcheck disable=SC2164
cd ../backend
pip install -r requirements.txt
python create_database.py

cd ../
echo "Installation Done"