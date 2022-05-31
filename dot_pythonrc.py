# inspired by this post: https://dev.to/kenbellows/a-few-python-repl-config-tricks-3o6i

# Python does not load this file by default, unless you've set the env var PYTHONSTARTUP
# for example:
# export PYTHONSTARTUP=~/.pythonrc.py

print(f"Loading {__file__} because PYTHONSTARTUP is set to point to it.")
