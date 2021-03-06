"""Test Pure Python functionality"""

import os
import sys
import nose
import flaky.flaky_nose_plugin as flaky

if __name__ == "__main__":
    print("Initialising Maya..")
    from maya import standalone, cmds
    standalone.initialize()
    cmds.loadPlugin("matrixNodes", quiet=True)

    argv = sys.argv[:]
    argv.extend([
        "--verbose",
        "--with-doctest",

        "--with-flaky",
        "--with-coverage",
        "--cover-html",
        "--cover-package", "cmdx",
        "--cover-erase",
        "--cover-tests",

        "tests.py",
        "test_performance.py",
        "cmdx.py",
    ])

    nose.main(argv=argv, addplugins=[flaky.FlakyPlugin()])

    if os.getenv("TRAVIS_JOB_ID"):
        import coveralls
        coveralls.wear()
    else:
        sys.stdout.write("Skipping coveralls")
