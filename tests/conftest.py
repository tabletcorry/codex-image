import os
import sys

# Ensure src/ is on sys.path for imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "src"))
)
