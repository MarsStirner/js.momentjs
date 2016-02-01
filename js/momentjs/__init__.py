from fanstatic import Library
from fanstatic import Resource

library = Library('momentjs', 'resources')

moment = Resource(
    library, 'moment.js'
)
moment_with_locales = Resource(
    library, 'moment-with-locales.js',
)
moment_timezone = Resource(
    library, 'moment-timezone.js',
    depends=[moment]
)
moment_timezone_with_data = Resource(
    library, 'moment-timezone-with-data.js',
    depends=[moment]
)
moment_timezone_with_data_periodic = Resource(
    library, 'moment-timezone-with-data-2010-2020.js',
    depends=[moment]
)
moment_timezone_with_data_2010_2020 = Resource(
    library, 'moment-timezone-with-data-2010-2020.js',
    depends=[moment]
)