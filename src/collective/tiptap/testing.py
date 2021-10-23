# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    PLONE_FIXTURE,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import collective.tiptap


class CollectiveTiptapLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.tiptap)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.tiptap:default")


COLLECTIVE_TIPTAP_FIXTURE = CollectiveTiptapLayer()


COLLECTIVE_TIPTAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_TIPTAP_FIXTURE,),
    name="CollectiveTiptapLayer:IntegrationTesting",
)


COLLECTIVE_TIPTAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_TIPTAP_FIXTURE,),
    name="CollectiveTiptapLayer:FunctionalTesting",
)


COLLECTIVE_TIPTAP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_TIPTAP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveTiptapLayer:AcceptanceTesting",
)
