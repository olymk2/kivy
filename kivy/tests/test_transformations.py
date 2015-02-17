import unittest
import numpy

from kivy.graphics.transformation import Matrix


class TransformationsTestCase(unittest.TestCase):
    def test_dot(self):
        """ Placeholder we probably should have tests, currently need
        get and set methods merging to test but then we can do
        something like the test below but this is nonsense currently"""

        result = Matrix().dot(
            Matrix().set([
                [2.08721089, 0.0, 0.0, 0.0],
                [0.0, 2.14450693, 0.0, 0.0],
                [0.0, 0.0, -1.66666663, -1.0],
                [0.0, 0.0, -53.33333206, 0.0]]))

        numpy.testing.assert_almost_equal(result.get(), numpy.array([
            [0.0, 2.96439387505e-323, 4.78268193255e-317, 4.78268193255e-317],
            [3.1201653622e-317, 1.58101006669e-322, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [2.87482174972e-317, 0.0, 0.0, 0.0]]))
