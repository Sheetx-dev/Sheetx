import asyncio
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import text
from backend.database import engine

async def alter_table():
    async with engine.begin() as conn:
        try:
            await conn.execute(text("ALTER TABLE demo_requests ADD COLUMN scheduled_time VARCHAR;"))
            print("Successfully added scheduled_time to demo_requests table.")
        except Exception as e:
            if "already exists" in str(e).lower() or "duplicate column" in str(e).lower():
                print("Column scheduled_time already exists.")
            else:
                print(f"Error (or SQLite syntax difference): {e}")

if __name__ == "__main__":
    asyncio.run(alter_table())
