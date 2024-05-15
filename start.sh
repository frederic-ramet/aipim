echo "Start backend"
# shellcheck disable=SC2164
cd backend
python main.py &
P1=$!


echo "Start frontend"
# shellcheck disable=SC2164
cd ../frontend
streamlit run streamlit_app.py &
P2=$!

cd ../
echo "Application started"

wait $P1 $P2