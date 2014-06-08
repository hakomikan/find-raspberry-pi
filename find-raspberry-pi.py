import subprocess
import re
import platform
import sys

if __name__ == "__main__":
    if "CYGWIN" in platform.system():
        for x in subprocess.check_output(["arp", "-a"]).split("\n"):
            m = re.match(".*\s+([0-9]+(?:\\.[0-9]+){3})\s+(b8-27-eb(?:-[0-9a-z]{2}){3})\s+.*", x)
            if m:
                print "%s\t%s" % (m.group(1), m.group(2))
    else:
        print >>sys.stderr, "unsupported"
        sys.exit(1)
