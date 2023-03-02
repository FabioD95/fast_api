import fastapi
import uvicorn
from typing import Optional
from pydantic import BaseModel

api = fastapi.FastAPI()


product_db = {
    1: {
        'id': 1,
        'name': 'kebab',
        'description': 'sarhwerhw54e',
        'price': 4.25,
        'avaible': True
    },
    2: {
        'id': 2,
        'name': 'name panino',
        'description': 'sarhwerhw54e',
        'price': 4.25,
        'avaible': True
    }
}


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    avaible: bool


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


@api.get('/products/')
def get_products():
    return product_db


@api.get('/products/{product_id}', response_model=Product)
def get_one_products(product_id: int):
    return product_db[product_id]


@api.post('/products/', response_model=Product)
def insert_product(product: Product):
    product_db[product.id] = product
    print(product_db)
    return product


@api.delete('/products/{product_id}', response_model=Product)
def delete_product(product_id: int):
    deleted_product = product_db[product_id]
    product_db.pop(product_id)
    print(product_db)
    return deleted_product


@api.put('/products/{product_id}', response_model=Product)
def modify_product(product_id: int, product: Product):
    product_db[product_id] = product
    print(product_db)
    return product


@api.get('/prova1/default')
def default():
    '''
        return default
    '''
    return {'messagaggio': 'trullalero'}


@api.get('/prova1/api/test/{x}')
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
