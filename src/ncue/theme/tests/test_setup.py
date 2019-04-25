# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ncue.theme.testing import NCUE_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ncue.theme is properly installed."""

    layer = NCUE_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ncue.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ncue.theme'))

    def test_browserlayer(self):
        """Test that INcueThemeLayer is registered."""
        from ncue.theme.interfaces import (
            INcueThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(INcueThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NCUE_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ncue.theme'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ncue.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ncue.theme'))

    def test_browserlayer_removed(self):
        """Test that INcueThemeLayer is removed."""
        from ncue.theme.interfaces import \
            INcueThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            INcueThemeLayer,
            utils.registered_layers(),
        )
