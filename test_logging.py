import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("User logged in")