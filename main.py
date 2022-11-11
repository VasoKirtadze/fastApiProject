from fastapi import FastAPI,  Depends, HTTPException
from pydantic import BaseModel, Field
import models
from models import Games, History
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Move(BaseModel):
    type: str = Field(min_length=1)
    position: int = Field(gt=-1, lt=9)


@app.get('/')
def read_api():

    return {'Name': 'Tic tac toe'}


@app.get('/start')
def start_game(db: Session = Depends(get_db)):
    game_model = Games()
    db.add(game_model)
    db.commit()
    return {'game_id': game_model.id}


@app.post('/move/{game_id}')
def move(game_id: int, move: Move,  db: Session = Depends(get_db)):
    game_model = db.query(Games).filter(Games.id == game_id).first()

    if not game_model:
        raise HTTPException(
            status_code=404,
            detail=f"ID does not exist"
        )
    if game_model.finished:
        return {"result": "error", "error_code": "Game Already finished"}

    if game_model.define_position(move.position, move.type) == False:
        return {"result": "error", "error_code": "invalid_position"}
    game_model.state()
    history = History(game_id=game_id, position=move.position, type=move.type)
    db.add(history)
    db.commit()
    db.close()
    return {"result": "success"}




@app.get('/check/{game_id}')
def check(game_id: int, db: Session = Depends(get_db)):
    game_model = db.query(Games).filter(Games.id == game_id).first()

    if not game_model:
        raise HTTPException(
            status_code=404,
            detail=f"ID does not exist"
        )

    if game_model.finished:
        return {'game': 'finished', 'winner': game_model.winner}

    if not game_model.finished:
        return {'game': 'in_progress'}


@app.get('/history')
def history(db: Session = Depends(get_db)):
    return db.query(models.History).all()
