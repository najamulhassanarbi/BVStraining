"""file: main/cron.py
    This module is for setting up cron job
        Function: change_time_zone()
        - Changes the time zone for all entries in the TimeModel database.
"""
import logging
from datetime import timedelta
from django.utils import timezone

from main.models import TimeModel

logger = logging.getLogger('main')

def change_time_zone():
    """Changes the time zone for all entries in the TimeModel database.
    Logging is used to record the start and end of the function, as well as any errors that occur
    during execution.
    Raises:
        - Exception: If any error occurs during the execution, it will be logged.
    :return:
    :rtype:
    """
    # logger.info("change_time_zone function started.")

    threshold_time = timezone.localtime(timezone.now()) - timedelta(minutes=10)
    try:
        logger.info(f"minutes are {threshold_time}")
        time_data = TimeModel.objects.filter(updated_at__lte=threshold_time)
        for time in time_data:
            logger.info(f"time is {time}")

            current_time = time.time

            if time.time_zone == "PKST":
                time.time_zone = "EST"
                time.time = current_time.replace(hour=(current_time.hour - 10) % 24)
            else:
                time.time_zone = "PKST"
                time.time = current_time.replace(hour=(current_time.hour + 10) % 24)

            time.save()

    except Exception as e:
        logger.error(f"Error occurred: {e}")

    logger.info("change_time_zone function ended.")
