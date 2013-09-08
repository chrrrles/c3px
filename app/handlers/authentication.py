# -*- coding: utf-8 *-*
# Copyright (c) 2013 - The C3PX authors.
#
# This file is part of C3PX.
#
# C3PX is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as 
# published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
#
# C3PX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public 
# License along with C3PX.  If not, see <http://www.gnu.org/licenses/>.

from app import *

class RegisterHandler(AppHandler):
  @auth_redir
  def get(self):  
    form = model_form ( UserModel() )
    user_form = form()
    self.render('register.html', form = user_form)

  @auth_redir
  @tornado.gen.coroutine
  @tornado.web.asynchronous
  def post(self):
    user = UserModel(self._args)
    try:
      user.validate()
      email_user = yield Op (self.db.users.find_one,{'email': user.email})
      if email_user:
        raise ValidationError('email_exists')
    except ValidationError, e: 
      form = model_form(user)
      user_form = form()
      user_form.validate()
      if  'email_exists' in e.messages:
        user_form.email.errors = ['Email address is not available']
      self.render('register.html', form = user_form)
      return
    else:
      user.activated = True # [XXX] Just for testing till smtp is up
      user.password = bcrypt.hashpw(user.password, bcrypt.gensalt()) 
      user.date_create = datetime.datetime.now()
      user.join_hash = helpers.generate_md5()  
      yield Op (self.db.users.insert, user._data)
      #self.smtp.send('Confirm your new account', 'confirm.html', 
      #  user.email, {'user':user._data})
      self.redirect('/login')
      return


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
    _next = self.get_argument('_next', '/')
    form = model_form(UserModel(),only=['email','password'])
    login_form = form()
    self.render('login.html',form=login_form, message=None, _next=_next)

  @auth_redir
  @tornado.gen.coroutine
  @tornado.web.asynchronous
  def post(self):
    message = None
    luser = UserModel(self._args)  # the 'login' user
    _next = self.get_argument('_next', '/')
    user = yield Op( self.db.users.find_one, {'email': luser.email})
    if user:
      if user['activated']:
        hashpw = bcrypt.hashpw(luser.password, user['password'])
        if hashpw == user['password']:
          self.set_secure_cookie('current_user', user['email'])
          self.redirect(_next)
          return
        else:
          message = "Invalid email or password combination"
      else:
        message = "User not yet confirmed"
    else:
      message = "Invalid email or password combination"

    form = model_form(luser, only=['email','password'])
    login_form = form()
    # [XXX] wish we didn't have to validate form here, seems redundant
    login_form.validate() 
    self.render('login.html', form=login_form, message=message, _next=_next)


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
            'enabled' : True  },
          '$unset' : {'join_hash' : 1}},
        new = True)
      self.smtp.send( 'Reset password', 'reset_password.html', 
        user.email, {'user':user._data})

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
          user.email, {'user' : user._data})
        return self.redirect('/login')
    return self.render('authentication/new_password.html',
      message = "Invalid Arguments", reset_hash = '' )


class LogoutHandler(AppHandler):

#  @tornado.gen.coroutine
  @auth_only
  @tornado.web.asynchronous
  def post(self): 
    self.clear_cookie('current_user')
    return self.redirect('/')
 

        
