# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ncue.theme


class NcueThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ncue.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ncue.theme:default')


NCUE_THEME_FIXTURE = NcueThemeLayer()


NCUE_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NCUE_THEME_FIXTURE,),
    name='NcueThemeLayer:IntegrationTesting'
)


NCUE_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NCUE_THEME_FIXTURE,),
    name='NcueThemeLayer:FunctionalTesting'
)


NCUE_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NCUE_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='NcueThemeLayer:AcceptanceTesting'
)
