# -*- coding: utf-8 *-*

from app import *


class UserProfileHandler(AppHandler):

  @auth_only
  def get(self):
    return self.render('user_profile.html')


class UserSettingsHandler(AppHandler):

  @auth_only
  def get(self):
    return self.render('user_profile.html')
