from django.core.urlresolvers import reverse

def base_data_menu(menu):

    url_change = reverse('admin:cms_lab_data_datafile_changelist')
    url_addnew = reverse('admin:cms_lab_data_datafile_add')
    menu.add_sideframe_item('Edit Data Files', url=url_change)
    menu.add_modal_item('Add New Data File', url=url_addnew)
    menu.add_break()

    url_change = reverse('admin:cms_lab_data_datafileset_changelist')
    url_addnew = reverse('admin:cms_lab_data_datafileset_add')
    menu.add_sideframe_item('Edit Data File Sets', url=url_change)
    menu.add_modal_item('Add New Data File Set', url=url_addnew)

    return menu
