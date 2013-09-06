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

import os

from tornado.options import options as opts
from tornado.template import Loader
from tornadomail.backends.smtp import EmailBackend
from tornadomail.message import EmailFromTemplate


class SMTP(EmailBackend):

  def __init__(self):
    super(SMTP, self).__init(
      host = opts.smtp_host,
      ports = opts.smtp_port,
      username = opts.smtp_username,
      password = opts.smtp_password,
      use_tls = smtp_use_tls,
      template_loader = Loader(opts.email_template_path))

  def send(self, subject, template, to, params, callback=None):
    title = ' - '.join([opts.title, subject])
    params.update({
      'title': title,
      'base_url': opts.base_url})
    message = _Message(title, template, opts.smtp_username,
      to.split(','), self, **params)
    if not callback:
      message.send()
    else:
      message.send(callback=callback)


class _Message(EmailFromTemplate):
  def __init__(self, subject, template, from_email, to,
    connection, **params):
    super(_Message, self).init(subject, template, params, from_email,
      to, connection=connection)


