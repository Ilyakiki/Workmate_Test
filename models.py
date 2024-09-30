from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class Breed(Base):
    __tablename__ = 'Breed'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Cat(Base):
    __tablename__ = 'Cat'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, comment='Имя котенка')
    age = Column(Integer, nullable=False, comment='Возраст котенка')
    gender = Column(String, nullable=True, comment='Пол котенка')
    breed = Column(ForeignKey(Breed.id, onupdate='CASCADE', ondelete='SET NULL'), nullable=False, index=True,
                   comment='{Breed.id} Порода котенка')
