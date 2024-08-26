from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey, Boolean

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, unique=True, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, nullable=False, default=True),
    Column('is_superuser', Boolean, nullable=False, default=False),
    Column('is_verified', Boolean, nullable=False, default=False),

)

note = Table(
    'note',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('content', String, nullable=False),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
)
