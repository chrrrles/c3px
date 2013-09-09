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

class BrowseProjectHandler(AppHandler):

  def get(self):
    self.render('project_browse.html')

class ViewProjectHandler(AppHandler):

  @tornado.web.asynchronous
  @tornado.gen.coroutine
  def get(self, username, name):
    user = yield self.db.users.find_one(
      {'username' : url_unescape(username)})

    if user:
      project = yield self.db.projects.find_one(
        {'$and':[
          {'owner': user['email']},
          {'name' : url_unescape(name)} ]})

      if project:
        if not project['public']:
          if not self.current_user:
            self.redirect(self.get_login_url() + '?' + 
              urllib.urlescape({'_next': self.request.uri}))
            return

        project['owner'] = user # stash owner info 
        cr = self.db.files.find(
          {'public_id':  {'$in': project['uploads']}},
          fields=['filename','size','public_id'])
        project['assets'] = []
        while (yield cr.fetch_next):
          asset = cr.next_object()
          asset['public_id'] = str(asset['public_id'])
          project['assets'].append(asset)
        self.render('project_view.html', project=project)
        return

    #raise tornado.web.HTTPError(404)
    self.redirect('/')
         

class ViewUserProjectHandler(AppHandler):

  def get(self, user):
    self.render('project_user.html')

class UpdateProjectHandler(AppHandler):

  @auth_only
  @tornado.web.asynchronous
  @tornado.gen.coroutine
  def get(self, project_name=None):
    Project = ProjectModel()
    uploads = []
    if project_name is not None:
      project = self.db.projects.find_one( {
        '$and': [
          {'name': url_unescape(project_name)}, 
          {'owner': self.current_user['email']}]} )
      if project is not None:
        Project = ProjectModel(project)
        print Project._data
        uploads = project['uploads']
        uploads = [str(x) for x in uploads]

    project_form = model_form(Project)
    self.render('project_create.html', project = project_form(), uploads=uploads )

  @auth_only
  @tornado.web.asynchronous
  @tornado.gen.coroutine
  def post(self, project_name=None):
    errors = {}

    # we are editing an existing project
    if project_name is not None:
      project = yield self.db.projects.find_one({
        '$and': [
          {'name': url_unescape(project_name)}, 
          {'owner': self.current_user['email']} ] } )
      if not project:
        # cheeky monkey, you shouldn't get this
        raise tornado.web.HTTPError(404)

    args = self._args
    # schematics only recognizes True False  
    args['public'] = True if args['public'] == 'y' else False
    Project = ProjectModel(args)

    # We don't let user's change project names 
    if project_name is not None:
      Project.name = project_name 
    uploads = self.request.arguments['uploads[]']

    # has to be a list or mongo pukes
    if not isinstance(uploads, list):  
      uploads = [uploads,]
    uploads = [uuid.UUID(x) for x in uploads]

    # check to see if owner alread has project with name
    if project_name is None:
      exists = yield self.db.projects.find_one({
        '$and': [
          {'owner': self.current_user['email']},
          {'name' : Project.name } ]})

      if exists:
        errors['name'] = "Project name already used" 

    # we check for uploads w/ javascript, but can't trust dem users
    if len(uploads) > 0 and len(errors) == 0:
      cr =  self.db.files.find(
        {'$and': [
          {'public_id':  {'$in': uploads}},
          {'owner': self.current_user['email']} ] },
        fields=['filename']) 
      cnt = yield  cr.count()
      files = yield cr.to_list(cnt)

      stl = False
      for f in files:
        if f['filename'].split('.')[1].lower() == 'stl':
          stl = True # if at least 1 file is STL, proceed

      # we have an STL file, we can proceed
      if stl:
        try:
          Project.owner = self.current_user['email']
          Project.timestamp = datetime.datetime.now()
          Project.validate()
        except ValidationError,e:
          print e
        else:
          # [XXX] Need to fix ormwtf's ListType conversion to
          # avoid doing this 
          project_with_uploads = {'uploads': uploads} 
          project_with_uploads.update(Project._data)
          if not project_name: # we are not updating a record 
            project_with_uploads.pop('_id') 
          yield self.db.projects.save( project_with_uploads)
          self.redirect('/user/%s/%s' %  (
            url_escape(self.current_user['username']), 
            url_escape(project_with_uploads['name'])))
          return

    form = model_form(Project)
    project_form = form()
    project_form.validate() #[XXX] this is gettin' redumbdumb
    for field in errors:
      project_form[field].errors.append (errors[field])
    self.render('project_create.html', project = project_form, uploads = uploads)
    return

