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

  def get(self, owner, project_name):
    self.render('project_browse.html')

class UpdateProjectHandler(AppHandler):

  #@auth_only
  @tornado.web.asynchronous
  @tornado.gen.engine
  def get(self, owner=None, project_name=None):
    Project = ProjectModel()
    uploads = []
    if _id is not None:
      project = yield Op(self.db.projects.find_one,
        {'$and': 
          {'_id': _id, 
          #'owner': self.current_user.email}} )
          'owner': "charles.paul@gmail.com"}} )
      if project is not None:
        Project = ProjectModel(project)
        uploads = project.uploads

    project_form = model_form(Project)
    self.render('project_create.html', project = project_form(), uploads=uploads )

  #@auth_only
  @tornado.web.asynchronous
  @tornado.gen.coroutine
  def post(self, owner=None, project_name=None):
    _id = self.get_argument('_id', False) 
    errors = {}
    if _id:
      project = yield self.db.projects.find_one(
        {'$and': 
          {'_id': _id, 
          #'owner': self.current_user['email']}} )
          'owner': "charles.paul@gmail.com"}} )
      if not project:
        # sneaky monkey, you shouldn't get this
        raise tornado.web.HTTPError(404)

    args = self._args
    # schematics only recognizes True False  
    args['public'] = True if args['public'] == 'y' else False
    Project = ProjectModel(args)
    uploads = self.request.arguments['uploads[]']

    if not isinstance(uploads, list):  # has to be a list or mongo pukes
      uploads = [uploads,]
    uploads = [uuid.UUID(x) for x in uploads]

    # check to see if owner alread has project with name
    exists = yield self.db.projects.find_one({
      '$and': [
        #{'owner': self.current_user['email']},
        {'owner': "charles.paul@gmail.com"},
        {'name' : Project.name } ]})
    if exists is not None:
      errors['name'] = "Project name already used" 

    if len(uploads) > 0 and len(errors) == 0:
      cursor =  self.db.files.find(
        {'$and': [
          {'public_id':  {'$in': uploads}},
          #{'owner': self.current_user['email']} ] },
          {'owner': "charles.paul@gmail.com"} ] },
        fields=['filename']) 
      count = yield  cursor.count()
      files = yield cursor.to_list(count)

      stl = False
      for f in files:
        if f['filename'].split('.')[1].lower() == 'stl':
          stl = True # if at least 1 file is STL, proceed

      if stl:
        try:
          Project.owner = "charles.paul@gmail.com"
          Project.timestamp = datetime.datetime.now()
          Project.validate()
        except ValidationError,e:
          print e
        else:
          #Project.owner = self.current_user['email']
          # [XXX] Need to fix ormwtf's ListType conversion to
          # avoid doing this 
          project_with_uploads = {'uploads': uploads} 
          project_with_uploads.update(Project._data)
          if not _id: 
            project_with_uploads.pop('_id') 
          yield self.db.projects.save( project_with_uploads)
          self.redirect('/user/%s/%s' %  (
            #urlescape(self.current_user.username), 
            url_escape("chrrrles"), 
            url_escape(project_with_uploads['name'])))
          return

    form = model_form(Project)
    project_form = form()
    project_form.validate() #[XXX] this is gettin' redumbdumb
    for field in errors:
      project_form[field].errors.append (errors[field])
    self.render('project_create.html', project = project_form, uploads = uploads)
    return

