import unittest
from service import delete_user, User

class TestAuth(unittest.TestCase):

    def test_admin_can_delete(self):
        user = User(["admin", "editor"])
        result = delete_user(user, 123)
        self.assertEqual(result, "user 123 deleted")

    def test_non_admin_cannot_delete(self):
        user = User(["editor"])
        with self.assertRaises(PermissionError):
            delete_user(user, 123)

if __name__ == "__main__":
    unittest.main()
