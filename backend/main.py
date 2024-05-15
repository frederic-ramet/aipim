import uvicorn
from core.apps import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8021, reload=True, log_level="debug")
