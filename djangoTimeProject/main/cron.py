"""file: main/cron.py
    This module is for setting up cron job
        Function: change_time_zone()
        - Changes the time zone for all entries in the TimeModel database.
"""
import logging
from datetime import timedelta
import pytz
from django.utils import timezone

from main.models import TimeModel

logger = logging.getLogger('main')

def change_time_zone():
    """Changes the time_obj zone for all entries in the TimeModel database.
    Logging is used to record the start and end of the function, as well as any errors that occur
    during execution.
    Raises:
        - Exception: If any error occurs during the execution, it will be logged.
    :return:
    :rtype:
    """

    pkst = pytz.timezone('Asia/Karachi')
    est = pytz.timezone('America/New_York')

    threshold_time = timezone.now() - timedelta(minutes=10)
    try:
        time_data = TimeModel.objects.filter(updated_at__lte=threshold_time)
        for time_obj in time_data:

            current_time = time_obj.time

            if time_obj.time_zone == "PKST":
                localized_time = pkst.localize(current_time)
                new_time = localized_time.astimezone(est)
                time_obj.time_zone = "EST"
                time_obj.time = new_time.replace(tzinfo=None)
            else:
                localized_time = est.localize(current_time)
                new_time = localized_time.astimezone(pkst)
                time_obj.time_zone = "PKST"
                time_obj.time = new_time.replace(tzinfo=None)

            time_obj.save()

    except Exception as e:
        logger.error(f"Error occurred: {e}")

    logger.info("change_time_zone function ended.")
