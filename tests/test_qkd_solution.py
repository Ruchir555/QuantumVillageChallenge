import unittest

from qkd_solution import bits_to_bytes, decrypt_message, reconcile_key


class QKDSolutionTests(unittest.TestCase):
    def test_basis_reconciliation_keeps_only_matches(self):
        bits = reconcile_key("+X+X", "+XXX", [1, 0, 1, 1])
        self.assertEqual(bits, [1, 0, 1])

    def test_bits_are_packed_most_significant_first(self):
        self.assertEqual(bits_to_bytes([0, 1, 0, 0, 0, 0, 0, 1]), b"A")

    def test_known_challenge_key_decrypts_flag(self):
        key = bytes.fromhex("3663a8d3f6af49316e0e5521c09df2a414d893")
        ciphertext = bytes.fromhex("500fc9b48dfe6462077a300192e89e976ef9ee")
        key_bits = [int(bit) for byte in key for bit in f"{byte:08b}"]
        bases = "+" * len(key_bits)
        plaintext = decrypt_message(bases, bases, key_bits, ciphertext)
        self.assertEqual(plaintext, b"flag{Q-Site Rul3z!}")

    def test_decrypt_message_rejects_short_key(self):
        with self.assertRaises(ValueError):
            decrypt_message("++++++++", "++++++++", [0] * 8, b"two bytes")

    def test_invalid_input_is_rejected(self):
        with self.assertRaises(ValueError):
            reconcile_key("+X", "+", [0, 1])
        with self.assertRaises(ValueError):
            bits_to_bytes([0, 1, 0])
        with self.assertRaises(ValueError):
            bits_to_bytes([0, 1, 2, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
