import uvicorn
import sys

if __name__ == "__main__":
    sys.path.insert(0, '/')
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
