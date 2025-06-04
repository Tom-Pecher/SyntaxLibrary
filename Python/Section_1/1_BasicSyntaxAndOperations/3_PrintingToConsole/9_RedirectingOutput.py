
## Python: 1.1.3.9 - Redirecting Output

# We can redirect the output on the console to a file:
with open("log.txt", "w") as f:
    print("Logging info", file=f)

# Or to stderr (for error messages):
import sys
print("Error message", file=sys.stderr)
