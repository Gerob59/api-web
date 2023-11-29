from sqlalchemy import String, DateTime, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Ouvrage(Base):
    __tablename__ = 'ouvrage'

    id_ouvrage: Mapped[int] = mapped_column(primary_key=True)
    nom_ouvrage: Mapped[str] = mapped_column(String(30))
    prenom_auteur: Mapped[str] = mapped_column(String(30))
    nom_auteur: Mapped[str] = mapped_column(String(30))
    isbn_ouvrage: Mapped[str] = mapped_column(String(20))
    langue_ouvrage: Mapped[str] = mapped_column(String(20))
    prix_ouvrage: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=True)
    date_parution_ouvrage: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    categorie_ouvrage: Mapped[str] = mapped_column(String(255))
    date_disponibilite_librairie_ouvrage: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    date_disponibilite_particulier: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    image_ouvrage: Mapped[str] = mapped_column(String(255))
    table_des_matieres: Mapped[str] = mapped_column(String(255))
    mot_cle_ouvrage: Mapped[str] = mapped_column(String(255))
    description_ouvrage: Mapped[str] = mapped_column(String(255))
