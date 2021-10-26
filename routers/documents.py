from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core import crud, models, schemas
from core.database import SessionLocal, engine
from core.utils.summarize import summarize_text

# Create database tables if not yet created
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/documents"
)

# GET /documents
@router.get("", response_model=List[schemas.Document])
def read_documents(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    documents = crud.get_documents(db, skip=skip, limit=limit)
    return documents

# GET /documents/{document_id}
@router.get("/{document_id}", response_model=schemas.Document)
def read_document(document_id: int, db: Session=Depends(get_db)):
    db_document = crud.get_document(db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

# POST /documents
@router.post("", response_model=schemas.Document)
def create_document(document: schemas.DocumentCreate, db: Session=Depends(get_db)):
    return crud.create_document(db=db, document=document)

# POST /documents/summarize/{document_id}
@router.post("/summarize/{document_id}")
def summarize_document(document_id: int, db: Session=Depends(get_db)):
    db_document = crud.get_document(db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"document_id": document_id, "summary": summarize_text(db_document.text)}
