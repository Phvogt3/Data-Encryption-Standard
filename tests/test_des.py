import subprocess
import sys
import unittest
from pathlib import Path

from des import des_decrypt, des_encrypt, valid_hex


class TestDES(unittest.TestCase):
    def test_known_ciphertexts(self):
        cases = [
            ("133457799BBCDFF1", "0123456789ABCDEF", "85E813540F0AB405"),
            ("0000000000000000", "0000000000000000", "8CA64DE9C1B123A7"),
            ("FFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFF", "7359B2163E4EDC58"),
        ]

        for key, plaintext, expected_ciphertext in cases:
            with self.subTest(key=key, plaintext=plaintext):
                self.assertEqual(des_encrypt(plaintext, key), expected_ciphertext)
                self.assertEqual(des_decrypt(expected_ciphertext, key), plaintext)

    def test_lowercase_input(self):
        self.assertEqual(
            des_encrypt("0123456789abcdef", "133457799bbcdff1"),
            "85E813540F0AB405",
        )
        self.assertTrue(valid_hex("133457799bbcdff1"))

    def test_invalid_input(self):
        for value in ("Hello", "12345", "0123456789ABCDEG", " 0123456789ABCDEF"):
            with self.subTest(value=value):
                self.assertFalse(valid_hex(value))
                with self.assertRaises(ValueError):
                    des_encrypt(value, "133457799BBCDFF1")

    def test_command_line_output(self):
        program = Path(__file__).resolve().parents[1] / "des.py"
        result = subprocess.run(
            [sys.executable, str(program)],
            input="133457799BBCDFF1\n0123456789ABCDEF\n",
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Plaintext: 0123456789ABCDEF", result.stdout)
        self.assertIn("Ciphertext: 85E813540F0AB405", result.stdout)
        self.assertIn("Decrypted plaintext: 0123456789ABCDEF", result.stdout)


if __name__ == "__main__":
    unittest.main()
