from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Model(DeclarativeBase):
    ...


class URLModel(Model):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(primary_key=True)
    url_target: Mapped[str]
    url_key: Mapped[str]
    