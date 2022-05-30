"""Application entry point."""
#from routers import model_get
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
import uvicorn
from dash_flask import init_app

dash_app = init_app()

# if __name__ == "__main__":
#     app.run(host="127.0.0.1")


app = FastAPI()
app.mount("/dash", WSGIMiddleware(dash_app.server))
# app.include_router(model_get.router)


@app.get("/")
async def redirect_root():
    response = RedirectResponse("http://127.0.0.1:8888/dash")
    return response

# ----------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, port=8888)
