import os
import logging
import datetime as dt
from dotenv import load_dotenv

from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)

# Configure debug logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Example dates
startDate = dt.date.today() - dt.timedelta(days=7)
endDate = dt.date.today()

# Load Garmin Connect credentials from environment variables
load_dotenv()

try:
    # API

    ## Initialize Garmin api with your credentials using environement variables,
    # instead of hardcoded sensitive data.
    api = Garmin(os.getenv("EMAIL"), os.getenv("PASSWORD"))

    ## Login to Garmin Connect portal
    api.login()

    # Get mass values
    massValues = api.get_body_composition(startDate, endDate)

    #zip([x['calendarDate'] for x in weightValues['dateWeightList']], [x['weight'] for x in weightValues['dateWeightList']])

    api.logout()

except (
        GarminConnectConnectionError,
        GarminConnectAuthenticationError,
        GarminConnectTooManyRequestsError,
    ) as err:
    logger.error("Error occurred during Garmin Connect communication: %s", err)