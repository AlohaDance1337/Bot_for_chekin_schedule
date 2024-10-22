import pandas as pd
from datetime import datetime
from .universal_logger import UniversalLogger

logger = UniversalLogger('excel')


class ExcelReader:
    def __init__(self, file: str = None):
        self.file = file
        self.sheet_to_remove = "Справка"
        self.first_sheet_removed = False
        self._output_file = 'filtered_file.xlsx'

    @staticmethod
    def get_week_from_september():
        """
        :return: Returns the number of the week
        """
        start_of_september = datetime(datetime.now().year, 9, 1)
        days_since_september = (datetime.now() - start_of_september).days
        return days_since_september // 7 + 1

    def write_to_excel(self, day_of_week=None):
        sheets = pd.read_excel(self.file, sheet_name=None)  # Load all sheets
        current_week = self.get_week_from_september()
        sheet_names = list(sheets.keys())

        days_of_week = {
            'Monday': 'Понедельник',
            'Tuesday': 'Вторник',
            'Wednesday': 'Среда',
            'Thursday': 'Четверг',
            'Friday': 'Пятница',
            'Saturday': 'Суббота',
            'Sunday': 'Воскресенье'
        }

        day_of_week = day_of_week or datetime.now().strftime('%A')
        current_day = days_of_week[day_of_week]

        # Remove the first sheet if not done yet
        if not self.first_sheet_removed and self.sheet_to_remove in sheet_names:
            del sheets[self.sheet_to_remove]
            self.first_sheet_removed = True

        if 0 <= current_week - 1 < len(sheet_names):
            current_sheet_name = sheet_names[current_week - 1]
            df_filtered = sheets[current_sheet_name].iloc[2:49, 2:16]

            days_of_week_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
            day_data = {
                day: df_filtered.iloc[i * 8:(i + 1) * 8] for i, day in enumerate(days_of_week_list) if
                i * 8 < df_filtered.shape[0]
            }

            # Save current day's data to filtered_file.xlsx
            if current_day in day_data:
                df_current_day = day_data[current_day]
                with pd.ExcelWriter(self._output_file, mode='w') as writer:
                    df_current_day.to_excel(writer, sheet_name=current_day, index=False)
                    logger.info("Successful writing to a file", extra="excel")

        else:
            logger.warning(f"No sheet available for week {current_week}", extra="excel")
