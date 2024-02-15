from fastapi import FastAPI
from schemas import Book

app = FastAPI()

@app.get('/')
def home():
    return {"key":"hello"}

@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {'key': pk, 'q': q}

@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}

@app.post('/book')
def create_book(item: Book):
    return item


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
