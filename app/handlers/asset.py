from app import *
from .. lib.thumbnail import thumbnail 
from .. lib.render import render_stl
import time

class AssetHandler(AppHandler):

  @tornado.web.asynchronous
  @tornado.gen.engine
  def get(self, public_id, ftype=False):  
    prefix=''
    if ftype == "thumbnail":
      prefix ="thumb_"
    elif ftype == "stl":
      prefix = "stl_"
      
    File = yield Op (self.db.files.find_one, {
      'public_id' : uuid.UUID(public_id) } )
    if File:
      self.set_header("Content-Type", File["%scontent_type" % prefix])
      self.write(File["%scontent" % prefix])
      self.finish()

  @auth_only
  @tornado.web.asynchronous
  @tornado.gen.engine
  def post(self):
    # We do NOT use these user-generated values anywhere, here just 
    # for reference -- only supporting fineuploader atm
    qquuid = self.get_argument('qquuid', False)
    qqtotalfilesize = self.get_argument('qqtotalfilesize', None)

    if qquuid:
      upload =  self.request.files['qqfile'][0]
      content = upload['body']
      size =  len(content)
      filename = self.get_argument('qqfilename', upload['filename'])
      if filename.count('.') == 0:
        self.write({
          'error' : 'filename is missing filetype extension' } )
        self.finish()
        return
      content_type = upload['content_type']
      public_id = uuid.uuid1() 
      stl_content = None
      stl_content_type = None

      # Render STL file
      if filename.split('.')[-1].lower() == 'stl':
        stl_content = content
        stl_content_type = content_type 
        job = self.q.enqueue( render_stl, stl_content )
        io = IOLoop.instance()
        while True:
          yield tornado.gen.Task(
            io.add_timeout,
            time.time() + .5 )  # this job takes a while...
          if job.result is not None:
            content = job.result
            content_type = 'image/jpeg'
            break
        if not content:
          self.write({ 'error' : 'Render Failed' })
          self.finish()
          return 

      # we need to create a thumbnail now...
      job = self.q.enqueue( thumbnail, content )
      io = IOLoop.instance()
      while True:
        yield tornado.gen.Task(
          io.add_timeout,
          time.time() + .25 )  # .25 seems like a healthy number)
        if job.result is not None:
          thumb_content = job.result
          break

      File = {
        'filename' : filename,
        'size' : size,
        'content_type' : content_type,
        'public_id' : public_id,
        'content' : Binary(content),
        'stl_content' : Binary(stl_content) if stl_content else None,
        'stl_content_type' : stl_content_type,
        'thumb_content' : Binary(thumb_content),
        'thumb_content_type' : "image/jpeg",  # hardcoding for now
        'owner' : self.current_user['email'] }

      file_object = yield Op (self.db.files.insert, File )

      self.write({
        'success' : True,
        'newUuid' : str(public_id) })

      self.finish()

  @auth_only
  @tornado.web.asynchronous
  @tornado.gen.engine
  def delete(self, public_id):
    File = yield Op (self.db.files.find_one, {
      'public_id' : uuid.UUID(public_id) } )
    if File:
      if File['owner'] == self.current_user['email']:
        model_delete = yield Op (self.db.files.remove, File['_id'])
        print "\n\n\nFileObject Deleted: \n%s" % model_delete

        if model_delete:
          self.set_status(204)  # non-authoritative response
          self.finish()
          return

    # Then FAILURE
    self.set_status(500) # generic error
    self.write({'success': 'false'})  
    self.finish()
      
