"""Pure functions used by the Quantum Village QKD challenge solution."""

from __future__ import annotations

from collections.abc import Sequence


def reconcile_key(
    alice_bases: str,
    bob_bases: str,
    alice_bits: Sequence[int],
) -> list[int]:
    """Keep Alice's bits at positions where Alice and Bob used the same basis."""
    if len(alice_bases) != len(bob_bases) or len(alice_bases) != len(alice_bits):
        raise ValueError("basis strings and bit sequence must have equal lengths")
    if any(bit not in (0, 1) for bit in alice_bits):
        raise ValueError("alice_bits must contain only 0 and 1")
    return [
        bit
        for alice_basis, bob_basis, bit in zip(alice_bases, bob_bases, alice_bits)
        if alice_basis == bob_basis
    ]


def bits_to_bytes(bits: Sequence[int]) -> bytes:
    """Pack a whole number of bytes, most significant bit first."""
    if len(bits) % 8 != 0:
        raise ValueError("the number of bits must be divisible by eight")
    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("bits must contain only 0 and 1")
    return bytes(
        int("".join(str(bit) for bit in bits[offset : offset + 8]), 2)
        for offset in range(0, len(bits), 8)
    )


def decrypt_message(
    alice_bases: str,
    bob_bases: str,
    alice_bits: Sequence[int],
    ciphertext: bytes,
) -> bytes:
    """Reconcile the key and XOR it with ``ciphertext``."""
    shared_bits = reconcile_key(alice_bases, bob_bases, alice_bits)
    required_bits = 8 * len(ciphertext)
    if len(shared_bits) < required_bits:
        raise ValueError("the reconciled key is shorter than the ciphertext")
    key = bits_to_bytes(shared_bits[:required_bits])
    return bytes(key_byte ^ cipher_byte for key_byte, cipher_byte in zip(key, ciphertext))
