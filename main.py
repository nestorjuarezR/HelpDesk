from fastapi import FastAPI
from routers import tickets, users

app = FastAPI()


@app.get("/")
def get_root():
    return {'Hola'}


#Loas Routers
app.include_router(tickets.router)
app.include_router(users.router)