import sys
import re

assert(len(sys.argv) == 3)
_, meson, header_base = sys.argv
assert(meson.endswith("/meson.build") and header_base.endswith(".h.in"))

version_regex = r"project[ ]*\([\n\'\w\d\:\, \[\]\.\>\=]*[ ,]version[ ]*\:[ ]*['\"]([\d\.]*)['\"]"

ver_matches = re.search(version_regex, open(meson).read(), re.MULTILINE)
assert(ver_matches)
version = ver_matches.groups(0)[0]
ver_split = version.split(".")

vars = {
    "PIXMAN_VERSION_MAJOR": ver_split[0],
    "PIXMAN_VERSION_MINOR": ver_split[1],
    "PIXMAN_VERSION_MICRO": ver_split[2]
}

base = open(header_base).read()
for var in vars:
	base = base.replace("@"+var+"@", vars[var])
print(base)
