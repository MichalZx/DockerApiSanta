from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect('santa.db')
cursor = conn.cursor()

def is_table_exists(table_name):
    cursor.execute("PRAGMA table_info({})".format(table_name))
    return cursor.fetchall()

@app.post("/gift")
async def post_gift(giftName: str, idElf: int):
    if is_table_exists('Gifts'):
        cursor.execute('INSERT INTO Gifts (giftName, idElf) VALUES (?, ?)', (giftName, idElf))
        conn.commit()
        return {"message": "Gift created"}
    else:
        return {"message": "Gifts table not found"}

@app.get("/gift")
async def get_gift(idGifts: int):
    if is_table_exists('Gifts'):
        result = cursor.execute("SELECT * FROM Gifts WHERE idGifts = ?", (idGifts,))
        data = result.fetchall()
        conn.commit()
        if data:
            return {"message": data}
        else:
            return {"message": "selected gift not found"}
    else:
        return {"message": "Gifts table not found"}

@app.delete("/gift")
async def delete_gift(idGifts: int):
    if is_table_exists('Gifts'):
        cursor.execute("DELETE FROM Gifts WHERE idGifts = ?", (idGifts,))
        conn.commit()
        return {"message": "Gift deleted"}
    else:
        return {"message": "Gifts table not found"}

@app.post("/elf")
async def post_elf(name: str):
    if is_table_exists('Elves'):
        cursor.execute('INSERT INTO Elves (name) VALUES (?)', (name,))
        conn.commit()
        return {"message": "Elf created"}
    else:
        return {"message": "Elves table not found"}

@app.get("/elf")
async def get_elf(idElf: int):
    if is_table_exists('Elves'):
        result = cursor.execute("SELECT * FROM Elves WHERE idElf = ?", (idElf,))
        data = result.fetchall()
        conn.commit()
        if data:
            return {"message": data}
        else:
            return {"message": "selected elf not found"}
    else:
        return {"message": "Elves table not found"}

@app.delete("/elf")
async def delete_elf(idElf: int):
    if is_table_exists('Elves'):
        cursor.execute("DELETE FROM Elves WHERE idElf = ?", (idElf,))
        conn.commit()
        return {"message": "You just removed elf from the world"}
    else:
        return {"message": "Elves table not found"}