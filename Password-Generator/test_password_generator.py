
import string
from password_generator import generate_password

# Test 1: Generate 1000 passwords with all character types
for i in range(1000):
    password = generate_password(
        length=12,
        use_upper=True,
        use_lower=True,
        use_digits=True,
        use_symbols=True
    )

    assert len(password) == 12, f"Wrong length at test {i + 1}"
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)

print("PASS: 1000 passwords passed all character-type tests.")

# Test 2: Minimum length with all four types
password = generate_password(4, True, True, True, True)

assert len(password) == 4
assert any(c in string.ascii_uppercase for c in password)
assert any(c in string.ascii_lowercase for c in password)
assert any(c in string.digits for c in password)
assert any(c in string.punctuation for c in password)

print("PASS: Length 4 with all four character types.")

# Test 3: Digits only
for i in range(1000):
    password = generate_password(8, False, False, True, False)

    assert len(password) == 8
    assert all(c in string.digits for c in password)

print("PASS: 1000 digits-only passwords.")

# Test 4: Exclude look-alike characters
password = generate_password(
    20, True, True, True, True,
    exclude_lookalikes=True
)

for char in "0Ol1I":
    assert char not in password

print("PASS: Look-alike characters excluded.")
print("\nAll tests completed successfully!")
