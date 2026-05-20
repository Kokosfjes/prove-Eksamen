from openpyxl import load_workbook
from werkzeug.security import generate_password_hash
from app import app, db, User

# Leser users.xlsx, lager brukernavn (4 første bokstaver av fornavn)
# og passord <brukernavn>123. Kjøres én gang.
wb = load_workbook("../../users.xlsx")
ws = wb.active

with app.app_context():
    db.create_all()
    for row in ws.iter_rows(values_only=True):
        if not row[0]:
            continue
        # Fjern nummer foran navnet, hent fornavn
        navn = row[0].strip().split(" ", 1)[1].strip()
        fornavn = navn.split()[0]
        username = fornavn[:4].lower()
        password = username + "123"

        if not User.query.filter_by(username=username).first():
            db.session.add(User(
                username=username,
                password_hash=generate_password_hash(password),
            ))
            print(f"Lagt til: {username} / {password}")
    db.session.commit()
print("Ferdig.")
