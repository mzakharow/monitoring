import pyqtgraph as pg
import datetime
import time


def read_file():
    # file = "C:\\Users\\m.zakharov\\Desktop\\file_log\\test.txt"
    file = "C:\\Users\\m.zakharov\\Desktop\\file_log\\20200225000000.lgp"

    list_events = [0, ]
    period = int(time.mktime(datetime.datetime.strptime('20200225000000', '%Y%m%d%H%M%S').timetuple()))
    list_times = [period, ]
    count_event = 0
    with open(file, 'r', encoding='utf-8') as file_handler:
        # print(' '.join(map(str, file_handler)).split('20200224'))
        brace = 0
        filled = False
        current_line = ""
        for line in file_handler:
            if line.find('{') != -1:
                filled = True
                brace += line.count('{')
            if line.find('}') != -1:
                brace -= line.count('}')
            if brace > 0:
                current_line = current_line + line.strip()
            else:
                if current_line:
                    if filled:
                        if current_line.split(',')[9] == "E":
                            # print('time:', current_line.split(',')[0].replace('{', ''), 'event:', current_line.split(',')[9])
                            str_time = current_line.split(',')[0].replace('{', '')[: 14]
                            str_time = int(time.mktime(datetime.datetime.strptime(str_time, '%Y%m%d%H%M%S').timetuple()))
                            # str_time = int(current_line.split(',')[0].replace('{', '')[8: 14])
                            # time = datetime.datetime.strptime(str_time, '%Y%m%d%H%M%S')
                            # print(time)
                            count_event += 1
                            if period < str_time - 6000:
                                list_events.append(count_event)
                                list_times.append(str_time)
                                count_event = 0
                                period = str_time
                        else:
                            # print('time:', current_line.split(',')[0].replace('{', ''), 'event:', current_line.split(',')[9])
                            # str_time = int(current_line.split(',')[0].replace('{', '')[8: 14])
                            # str_time = int(time.mktime(current_line.split(',')[0].replace('{', '')[8: 14]))
                            str_time = current_line.split(',')[0].replace('{', '')[: 14]
                            str_time = int(time.mktime(datetime.datetime.strptime(str_time, '%Y%m%d%H%M%S').timetuple()))
                            # time = datetime.datetime.strptime(str_time, '%Y%m%d%H%M%S')
                            # print(time)
                            #count_event += 1
                            # list_events.append(0)
                            # list_times.append(str_time)
                        current_line = ""
                        filled = False
    return list_events, list_times


def timestamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))


class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [datetime.datetime.fromtimestamp(value).strftime("%H:%M") for value in values]


if __name__ == '__main__':
    read_file()
