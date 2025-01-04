import logging

logger1 = logging.getLogger("logger1")
logger1.setLevel(logging.INFO)

logger2 = logging.getLogger("logger2")
logger2.setLevel(logging.WARNING)


handler = logging.FileHandler("common_log.txt")
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger1.addHandler(handler)

logger2.addHandler(handler)

logger1.info("This is an info message from logger1")

logger2.warning("This is a warning message from logger2")

logger1.debug("This is a debug message from logger")

logger2.error("This is an error message from logger2")

handler.close()
