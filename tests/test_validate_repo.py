import unittest

from tools.validate_repo import validate


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_is_valid(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
