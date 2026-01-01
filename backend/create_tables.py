from app.database import engine, Base
from app.models import user, company, company_account_balance, request, request_received

# This will create all tables in the database
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
