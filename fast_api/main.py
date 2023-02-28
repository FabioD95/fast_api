import fastapi
import uvicorn
from typing import Optional

api = fastapi.FastAPI()


@api.get('/')
def index():
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to: PythonBiellaGroup FastCash Server App</h1>"
        "</body>"
        "</html>"
    )
    # return {'message': 'hello world'}
    return fastapi.responses.HTMLResponse(content=body)


@api.get('/default')
def default():
    '''
        return default
    '''
    return {'messagaggio': 'trullalero'}


@api.get('/api/test/{x}')
def calcola(x: int, y: int = 50, z: Optional[int] = None):
    if x == 0:
        return fastapi.responses.JSONResponse(
            content={'errore': 'per 0 è na somma scema'},
            status_code=400
        )
    return {
        'x': x,
        'y': y,
        'z': z,
        'somma': x + y
    }


if __name__ == '__main__':
    uvicorn.run(api, port='8000', host='127.0.0.1')     # local host
