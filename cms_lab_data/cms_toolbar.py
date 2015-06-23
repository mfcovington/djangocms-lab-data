from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar.items import Break, SubMenu
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


@toolbar_pool.register
class DataToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(
            ADMIN_MENU_IDENTIFIER, _('Apps')
        )

        position = admin_menu.get_alphabetical_insert_position(
            _('Data'),
            SubMenu
        )

        if not position:
            position = admin_menu.find_first(
                Break,
                identifier=ADMINISTRATION_BREAK
            ) + 1
            admin_menu.add_break('custom-break', position=position)

        data_menu = admin_menu.get_or_create_menu(
            'data-menu',
            _('Data ...'),
            position=position
        )

        url_change = reverse('admin:cms_lab_data_datafile_changelist')
        url_addnew = reverse('admin:cms_lab_data_datafile_add')
        data_menu.add_sideframe_item(_('Edit Data Files'), url=url_change)
        data_menu.add_modal_item(_('Add New Data File'), url=url_addnew)
        data_menu.add_break()

        url_change = reverse('admin:cms_lab_data_datafileset_changelist')
        url_addnew = reverse('admin:cms_lab_data_datafileset_add')
        data_menu.add_sideframe_item(_('Edit Data File Sets'), url=url_change)
        data_menu.add_modal_item(_('Add New Data File Set'), url=url_addnew)
