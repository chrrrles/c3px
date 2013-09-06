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

from skeinforge.skeinforge_application.skeinforge_plugins.analyze_plugins.statistic import StatisticRepository
from skeinforge.skeinforge_application.skeinforge_plugins.analyze_plugins.statistic import StatisticSkein
from skeinforge.skeinforge_application.skeinforge_plugins.craft_plugins.export import writeOutput
from skeinforge.skeinforge_application.skeinforge_plugins.craft_plugins.export import ExportRepository
from skeinforge.skeinforge_application.skeinforge_utilities import skeinforge_craft
from skeinforge.fabmetheus_utilities import settings

#from lib.skeinforge.fabmetheus_utilities import writeOutput
repository = StatisticRepository()
repository.density = 930.0
repository.material = 20.0

def skein(data):
  # [XXX] for now we are exec'ing these python scripts  -- we should be doing this using the library
  pass
  


