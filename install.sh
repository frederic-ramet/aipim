echo "Installing frontend"
cd frontend
pip install -r requirements.txt

echo "Installing backend"
cd ../backend
pip install -r requirements.txt
python create_database.py

cd ../
echo "Installation Done"