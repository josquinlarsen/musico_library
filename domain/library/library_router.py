from fastapi import FastAPI, APIRouter, HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
from domain.library.library_schema import PieceCreate, PieceUpdate, PieceResponse
from database import get_db
from models import Piece


router = APIRouter()



@router.post("/library/", response_model=PieceResponse)
def create_piece(piece: PieceCreate, db: Session = Depends(get_db)):

    db_piece = Piece(
        title = piece.title,
        composer = piece.composer,
        instrumentation = piece.instrumentation,
        duration = piece.duration,
      
    )
    db.add(db_piece)
    db.commit()
    db.refresh(db_piece)

    return db_piece


@router.get("/library/", response_model=list[PieceResponse])
def read_pieces(db: Session = Depends(get_db)):
    #  can set a limit paramter and limit query. 
    pieces = db.query(Piece).all()
    return pieces


@router.get("/library/{piece_id}", response_model=PieceResponse)
def read_piece(piece_id: int, db: Session = Depends(get_db)):
    piece = db.query(Piece).filter(Piece.id == piece_id).first()
    if piece is None:
        raise HTTPException(status_code=404, detail="Piece not found")
    return piece


@router.put("/library/{piece_id}", response_model=PieceResponse)
def update_piece(piece_id: int, piece: PieceUpdate, db: Session = Depends(get_db)):
    db_piece = db.query(Piece).filter(Piece.id == piece_id).first()
    if db_piece is None:
        raise HTTPException(status_code=404, detail="Piece not found")
    

    db_piece.title = piece.title
    db_piece.composer = piece.composer
    db_piece.instrumentation = piece.instrumentation
    db_piece.duration = piece.duration
   
    db.commit()
    db.refresh(db_piece)
    return db_piece


@router.delete("/library/{piece_id}")
def delete_piece(piece_id: int, db: Session = Depends(get_db)):
    db_piece = db.query(Piece).filter(Piece.id == piece_id).first()
    if db_piece is None:
        raise HTTPException(status_code=404, detail="Piece not found")

    db.delete(db_piece)
    db.commit()
    return {"detail": "Piece deleted successfully"}
