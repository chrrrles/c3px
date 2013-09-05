from app import *
from .. lib.thumbnail import thumbnail 
import time

class AssetHandler(AppHandler):

  @tornado.web.asynchronous
  @tornado.gen.engine
  def get(self, public_id, thumbnail=False):  
    thumb = ""
    if thumbnail:
      thumb ="thumb_"
    File = yield Op (self.db.files.find_one, {
      'public_id' : uuid.UUID(public_id) } )
    if File:
      self.set_header("Content-Type", File["%scontent_type" % thumb])
      self.write(File["%scontent" % thumb])
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

      print "thumb size: %d" % len(thumb_content)
      # now we don't write to GridFS
      #fs = yield Op (MotorGridFS(self.db).open)
      #gridin = yield Op (fs.new_file)
      #yield Op (gridin.write, body)
      #yield Op (gridin.close)
      #object_id =  gridin._id       
      File = {
        'filename' : filename,
        'size' : size,
        'content_type' : content_type,
        'public_id' : public_id,
        'content' : Binary(content),
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
      
