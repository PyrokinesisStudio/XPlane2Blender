import bpy
import os
import sys
from io_xplane2blender.tests import *
from io_xplane2blender import xplane_config

__dirname__ = os.path.dirname(__file__)

class TestCase2(XPlaneAnimationTestCase):
    def test_TestCase2(self):
        self.runAnimationTestCase('TestCase2', __dirname__)


runTestCases([TestCase2])