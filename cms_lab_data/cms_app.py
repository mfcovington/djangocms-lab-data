from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class DataApp(CMSApp):
    name = 'Data App'
    urls = ['cms_lab_data.urls']
    app_name = 'cms_lab_data'

apphook_pool.register(DataApp)
