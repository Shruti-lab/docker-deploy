import logging
import os
import sys
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    """
    Configure logging: stream to CLI (stdout) and rotate to file at /logs/app.log.
    Called this from create_app() after app.config is loaded.
    """

    log_level_name = app.config.get('LOG_LEVEL','INFO').upper()
    log_level = getattr(logging,log_level_name,logging.INFO)

    fmt = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt)

    log_file_path = app.config.get("LOG_FILE", "logs/app.log")
    if not isinstance(log_file_path, str):
        log_file_path = "logs/app.log"

    project_root = os.path.dirname(app.root_path)
    full_log_path = os.path.join(project_root, log_file_path)
    
    log_dir = os.path.dirname(full_log_path)
    os.makedirs(log_dir, exist_ok=True)

    # File handler (rotating) - 5MB max, keep 5 backup files
    file_handler = RotatingFileHandler(full_log_path, maxBytes=5 * 1024 * 1024, backupCount=5)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # Stream handler to CLI (stdout)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    root_logger.handlers.clear()

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)

    logging.getLogger('werkzeug').propagate = False

    app.logger.info("Logging setup complete - logs will be written to CLI and file")
