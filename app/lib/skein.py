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

def skein():
  pass

