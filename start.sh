echo "Start backend"
cd backend
python main.py &

echo "Start frontend"
cd ../frontend
streamlit run streamlit_app.py &

cd ../
echo "Application started"