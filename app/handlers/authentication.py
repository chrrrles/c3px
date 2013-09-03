from app import *

class RegisterHandler(AppHandler):
  @auth_redir
  def get(self):  
    form = model_form ( UserModel() )
    user_form = form()
    self.render('register.html', form = user_form)

  @auth_redir
  def post(self):
    user = UserModel(self._args())
    try:
      user.validate()
      if self.db.users.find_one({'email': user.email}):
        raise ValidationError('email_exists')
    except ValidationError, e: 
      form = model_form(user)
      user_form = form()
      user_form.validate()
      if e == "email_exists":
        user_form.email.errors = 'Email address is already registered'
      return self.render('register.html', form = user_form)
    else:
      self.db.users.insert(user.serialize())
      self.smtp.send('Confirm your new account', 'confirm.html', 
        user.email, {'user':user.serialize()})
      return self.redirect('/login')


# thanks to Jorge Puente Sarrín for the code inspiration
# https://github.com/puentesarrin

class ConfirmAccountHandler(AppHandler):  
  @auth_redir
  def get(self, join_hash=None):
    self.db.users.find_and_modify(
      {'join_hash': join_hash},
      {'unset':{'join_hash':1},'$set':{'enabled':True}})
    self.render('confirm_account.html')


class LoginHandler(AppHandler):
  @auth_redir
  def get(self):
    form = model_form(UserModel(),only=['email','password'])
    self.render('login.html',form, message=None)

  @auth_redir
  @tornado.gen.engine
  @tornado.web.asynchronous
  def post(self):
    luser = UserModel(self._args())  # the 'login' user
    message = ''
    if user.validate(): 
      next_ = self.get_argument('next_', '/')
      user = yield Op( self.db.users.find_one, {'email': luser.email})
      if user:
        if user.activated:
          legit = bcrypt.hashpw(luser.password, user.password) == user.password
        if legit:
          self.set_secure_cookie('current_user', user.email)
          return self.redirect(next_)
      # user doesn't exist or pw incorrect so pass vague message
      message = "Invalid email or password combination"

    form = model_form(luser, only=['email','password'])
    login_form = form()
    # [XXX] wish we didn't have to validate form here, seems redundant
    form.validate() 
    self.render('login.html', form, message=message)


class RequestNewPasswordHandler(AppHandler):
  
  @auth_redir
  def get(self):
    self.render('request_password.html', message='')

  @auth_redir
  def post(self):
    email = self.get_argument('email', False)
    if not email:
      return self.render('request_password.html',  
        message='An email address is required')

    user = self.db.users.find_one({'email': email})
    if user:
      reset_hash = helpers.generate_md5()
      user = self.db.users_find_and_modify(
        {'email': email}, {
          '$set': {
            'reset_hash': reset_hash,
            'enabled' : True  }
          '$unset' : {'join_hash' : 1}},
        new = True)
      self.smtp.send( 'Reset password', 'reset_password.html', 
        user.email, {'user':user.serialize()})

    # Don't tell luser if an email exists or not
    self.redirect('/')


class ResetPasswordHandler(AppHandler):
  
  @auth_redir
  def get(self, reset_hash=''):
    self.render('authentication/reset_password.html', message='', 
      reset_hash = reset_hash)

  @auth_redir
  def post(self, reset_hash=None):
    message = "Invalid Arguments" # predefine message
    reset_hash = self.get_argument('hash', False)
    password = self.get_argument('password', False)
    if reset_hash and password:
      password = bcrypt.hashpw(password, bcrypt.gensalt())
      user = self.db.users.find_and_modify(
        {'reset_hash': reset_hash},
        {'$set': {'password': password}},
        new=True)
      if user:
        self.smtp.send( 'Updated Password', 'reset_password.html',
          user.email, {'user' : user.serialize()})
        return self.redirect('/login')
    return self.render('authentication/new_password.html',
      message = "Invalid Arguments", reset_hash = '' )


class LogoutHandler(AppHandler):
  @auth_only
  @tornado.gen.engine
  @tornado.web.asynchronous
  def post(self): 
    self.clear_cookie('current_user')
    self.redirect('/')
 

        
