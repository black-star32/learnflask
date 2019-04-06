from app import db, Note

# Create
# note1 = Note(body='remember Sammy Jankis')
# note2 = Note(body='SHAVE')
# note3 = Note(body='DON\'T BELIEVE HIS LIES, HE IS THE ONE, KILL HIM')
# db.session.add(note1)
# db.session.add(note2)
# db.session.add(note3)
# db.session.commit()

# Read
print(Note.query.all())
print('--------------')
note1 = Note.query.first()
print(note1)
print('--------------')
note2 = Note.query.get(2)
print(note2)
print('--------------')
print(Note.query.count())
print('--------------')
print(Note.query.filter(Note.body=='SHAVE').first())
print('--------------')
