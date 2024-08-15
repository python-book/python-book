"""Demo importing standard libaries"""
import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger("main_script")

logger.debug("Imported logging and finished setup")

var_1 = '10'
if isinstance(var_1, str):
    logger.warning(f"var_1 is a string, converting to int.")
    var_1 = int(var_1)
#WARNING - main_script(m6_1_3_I.py:12) - var_1 is a string, converting to int.

print("# Regular output: 5*10 =", 5 * var_1)
# Regular output: 5*10 = 50

logger.info("End program, exiting...")
#INFO - main_script(m6_1_3_I.py:18) - End program, exiting...
