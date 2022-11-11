from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

#Modelo
class Item(BaseModel):
	name: str
	price: float = Field(None, gt=0, description="precio del producto")
	tax: float | None 
	description: str | None = Field(None, min_length=1)


app = FastAPI()

#Api en su forma mas simple
@app.get("/")
def home():
	return { "menssage": "Hola Mision TIC" }

#Path parametro
@app.get("/usuarios/{user_id}")
def read_user( user_id: int = Path( 

	gt=0,
	title="Id del usuario",
	description="Id del usuario en la base de datos"

	)):
	return {"user_id": user_id}

#Simulacion de base de datos
cursos = [
	{"cursos": "Fundamentos de programacion"},
	{"cursos": "Programacion basica"},
	{"cursos": "Desarrollo de software"},
	{"cursos": "Desarrollo Apps web"},
]

#Query parametros
@app.get("/cursos/")
def read_cursos(

	inicio: int | None = Query( 
		default=0, 
		gt=0, 
		lt=len(cursos), 
		title= "inicio de busqueda",
		description=f"Inicio de la busqueda de los cursos de mision Tic. Inicia en 0 y finaliza {len(cursos) - 1}"

		), 

	n: int = len(cursos)

):
	return cursos[inicio:inicio+n]


#Metodo post
@app.post("/nuevo_item/")
def new_item(
		item: Item = Body(...)
	):
	return dict( item )