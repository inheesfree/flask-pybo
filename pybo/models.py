from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 속성 = db.Column(속성의 데이터 타입, 속성을 기본키로 지정)
    subject = db.Column(db.String(200), nullable=False)
    # 속성 = db.Column(속성의 데이터 타입, 속성에 빈값을 허용하지 않는 옵션)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # 속성 = db.Column(속성의 데이터 타입, 기존 모델을 연결(연결한 기존 모델의 속성, 삭제 연동 설정)
    question = db.relationship('Question', backref=db.backref('answer_set',))
    # 속성 = db.relationship 기존 모델을 참조(참조할 모델-답변에서 질문을 참조, 역참조 설정-질문에서 답변을 참조)
    # 한 질문에 여러 개의 답변이 달릴 수 있기 때문에 질문에 역참조로 질문에서 달린 답변을 참조 할 수 있게 해준다.
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)