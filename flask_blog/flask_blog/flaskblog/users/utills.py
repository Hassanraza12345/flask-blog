from flaskblog import app
import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail





# here _ repersents that we want to through away that file name
def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(app.root_path,'static/profilepic',picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token= user.get_reset_token()
    msg=Message('Password Reset Request',sender='hr11302000@gmail.com',recipients=[user.email])
    msg_body=f''' To Reset Your Password Please Visit the Following Link {url_for('users.reset_token',token=token, _external=True)}
If you did not made this request then ignore this message and no change is made
'''
    mail.send(msg)