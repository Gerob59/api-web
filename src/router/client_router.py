from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from models.client import Client
from config.connexion import  get_db
from schema.client_schema import ClientSchemaOut, ClientSchema

router = APIRouter(
    tags=["client"],
    prefix="/client"
)

@router.get("/", response_model=list[ClientSchemaOut], status_code=status.HTTP_200_OK)
def get_all_clients(db : Session = Depends(get_db)):
    stmt = select(Client)
    result = db.scalars(stmt).all()
    return result

@router.get("/{id_client}", response_model=ClientSchemaOut, status_code=status.HTTP_200_OK)
def get_client(id_client: int, db : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id_client)
    result = db.scalars(stmt).one()
    return result

@router.post("/", response_model=ClientSchemaOut, status_code=status.HTTP_201_CREATED)
def add_client(client: ClientSchema, db : Session = Depends(get_db)):
    client_db = Client(**client.dict())
    db.add(client_db)
    db.commit()
    return ClientSchemaOut.from_orm(client_db)

@router.patch("/{id_client}", response_model=ClientSchemaOut, status_code=status.HTTP_200_OK)
def update_client(id_client: int, client: ClientSchema, db : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id_client)
    result = db.scalars(stmt).first()
    if result:
        for key, value in client.dict().items():
            setattr(result, key, value)
        db.commit()
        return result
    raise HTTPException(status_code=404, detail="client not found")

@router.put("/{id_client}", response_model=ClientSchemaOut, status_code=status.HTTP_200_OK)
def replace_client(id_client: int, client: ClientSchema, db : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id_client)
    result = db.scalars(stmt).first()
    if result:
        for key, value in client.dict().items():
            setattr(result, key, value)
        db.commit()
        return result

@router.delete("/{id_client}", status_code=status.HTTP_200_OK)
def delete_client(id_client: int, db : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id_client)
    result = db.scalars(stmt).first()
    if result:
        db.delete(result)
        db.commit()
        return {"message": "client deleted"}
    raise HTTPException(status_code=404, detail="client not found")