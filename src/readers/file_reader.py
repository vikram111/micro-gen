import logging

logging.basicConfig(level=logging.INFO)


def read_definition(def_name: str) -> str:
    try:
        if def_name is not None:
            with open(def_name, "r") as f:
                content = f.read()
        return content
    except RuntimeError as re:
        logging.error("File %s reading failed with error %s", def_name, re)
