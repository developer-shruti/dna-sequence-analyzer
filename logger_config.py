import logging

log_directory = "logs/"
log_file = log_directory+ "dna_analyzer.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)