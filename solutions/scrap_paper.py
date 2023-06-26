# x = 5

# x %= 3

# print(x) answer 2


x = 5

x =% 3

print(x)

# Traceback (most recent call last):
#   File "/usr/lib/python3.8/py_compile.py", line 144, in compile
#     code = loader.source_to_code(source_bytes, dfile or file,
#   File "<frozen importlib._bootstrap_external>", line 846, in source_to_code
#   File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
#   File "./prog.py", line 10
#     x =% 3
#        ^
# SyntaxError: invalid syntax

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "/usr/lib/python3.8/py_compile.py", line 150, in compile
#     raise py_exc
# py_compile.PyCompileError:   File "./prog.py", line 10
#     x =% 3
#        ^
# SyntaxError: invalid syntax