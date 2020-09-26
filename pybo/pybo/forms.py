from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력하세요.')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('사용자이름을 입력하세요.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', 
                              validators=[DataRequired('비밀번호를 입력하세요'), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired('비밀번호 확인을 입력하세요.')])
    email = EmailField('이메일', [DataRequired('이메일을 입력하세요.'), Email('이메일주소가 아닙니다.')])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('사용자이름을 입력하세요.'), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력하세요.')])
