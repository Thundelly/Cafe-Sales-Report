import datetime
import pytz

class TimeConverter:
    def get_time(self):

        today = datetime.datetime.now(pytz.timezone('US/Pacific')).isoformat()
        tmrw = (datetime.datetime.now(pytz.timezone('US/Pacific')) + datetime.timedelta(1)).isoformat()
        # today = (datetime.datetime.now(pytz.timezone('US/Pacific')) - datetime.timedelta(3)).isoformat()
        # tmrw = (datetime.datetime.now(pytz.timezone('US/Pacific')) - datetime.timedelta(2)).isoformat()

        self.begin_time = today[:11] + "07:00:00Z"
        self.end_time = tmrw[:11] + "07:00:00Z"

        return self.begin_time, self.end_time