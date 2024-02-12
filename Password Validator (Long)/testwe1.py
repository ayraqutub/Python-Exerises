# Python Intro Labs covers import
from passwordvalidate import validate

print(validate("HACKING"))
# Add your own tests and calls to validate() and generate() here
print(validate("Passw0rd!"))
print(validate("helloworld!"))
print(validate("Hello w0rld!"))

from passwordvalidate import generate
print(generate(10))