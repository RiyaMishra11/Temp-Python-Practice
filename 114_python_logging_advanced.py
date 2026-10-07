# 114 Advanced Logging
import logging
import time
from io import StringIO

logger = logging.getLogger("practice114")
logger.setLevel(logging.DEBUG)
logger.handlers.clear()

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)

# 1 Basic logging
logger.info("1. Application started")

# 2 Log levels
logger.debug("2. Debug")
logger.info("2. Info")
logger.warning("2. Warning")
logger.error("2. Error")

# 3 Custom formatting
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.info("3. Custom formatted log")

# 4 Capture logs in memory
stream = StringIO()
memory_handler = logging.StreamHandler(stream)
logger.addHandler(memory_handler)
logger.warning("4. Captured warning")
logger.removeHandler(memory_handler)
print("4.", stream.getvalue().strip())

# 5 Exception logging
try:
    10 / 0
except ZeroDivisionError:
    logger.exception("5. Division failed")

# 6 File logging
log_file = "/mnt/data/practice_114.log"
file_handler = logging.FileHandler(log_file, encoding="utf-8")
logger.addHandler(file_handler)
logger.info("6. Message written to file")
logger.removeHandler(file_handler)
file_handler.close()
print("6. Log file:", log_file)

# 7 Logger helper
def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    if not log.handlers:
        log.addHandler(logging.StreamHandler())
    return log

get_logger("helper114").info("7. Helper logger works")

# 8 Logging function arguments
def add(a, b):
    logger.info("8. Adding %s and %s", a, b)
    return a + b

print("8.", add(5, 7))

# 9 Filter sensitive words
class PasswordFilter(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage().lower()

filtered = logging.StreamHandler()
filtered.addFilter(PasswordFilter())
logger.addHandler(filtered)
logger.info("9. Normal message")
logger.info("9. password should be hidden")
logger.removeHandler(filtered)

# 10 Timed operation
start = time.perf_counter()
total = sum(range(100000))
logger.info("10. Operation took %.6f seconds", time.perf_counter() - start)
print("10.", total)

# 11 Application logger
class Application:
    def __init__(self):
        self.logger = get_logger("application114")

    def run(self):
        self.logger.info("11. Application running")
        return "success"

print("11.", Application().run())
