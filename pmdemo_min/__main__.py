"""This is executed by `python pmdemo` from the root,
or by `python -m pmdemo` for anywhere, if installed."""

import logging
import sys

import pmdemo_min


def main():
    """So that the main can be called after importing this module."""
    args = pmdemo_min.utils.parse_args(sys.argv[1:])
    conf = pmdemo_min.utils.parse_conf(args.Master_Config)
    pmdemo_min.utils.set_log(conf["outputs"]["log"])
    logging.info("Program ready to run, version %s", pmdemo_min.__version__)

    params = pmdemo_min.utils.parse_conf(conf["inputs"]["params"])
    factor = params.getfloat("top", "factor")
    pmdemo_min.my_mod.my_func(conf["inputs"]["tables"],
                              factor,
                              conf["outputs"]["res"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
