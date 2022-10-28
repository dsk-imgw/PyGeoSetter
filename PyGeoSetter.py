import json
from pyexif import pyexif
from GPSPhoto import gpsphoto
import sys
import math
import shutil
import glob
from logging import Formatter, handlers, StreamHandler, getLogger, INFO

CONFIG_FILE = 'config.json'

class GPSData:
    
    # Members
    gps_datestamp = ''
    gps_timestamp = ''
    gps_latitude_ref = ''
    gps_longitude_ref = ''
    gps_latitude = ''
    gps_longitude = ''
    gps_altitude = ''
    gps_satellites = ''
    gps_map_datum = ''
    gps_status = ''
    gps_measure_mode = ''

    # Get
    def get_datestamp(self):
        return self.gps_datestamp

    def get_timestamp(self):
        return self.gps_timestamp

    def get_latitude_ref(self):
        return self.gps_latitude_ref

    def get_longitude_ref(self):
        return self.gps_longitude_ref

    def get_latitude(self):
        return self.gps_latitude

    def get_longitude(self):
        return self.gps_longitude

    def get_altitude(self):
        return self.gps_altitude

    def get_satellites(self):
        return self.gps_satellites

    def get_map_datum(self):
        return self.gps_map_datum

    def get_status(self):
        return self.gps_status

    def get_measure_mode(self):
        return self.gps_measure_mode

    # Set
    def set_datestamp(self, x):
        self.gps_datestamp = x

    def set_timestamp(self, x):
        self.gps_timestamp = x

    def set_latitude_ref(self, x):
        self.gps_latitude_ref = x

    def set_longitude_ref(self, x):
        self.gps_longitude_ref = x

    def set_latitude(self, x):
        self.gps_latitude = x

    def set_longitude(self, x):
        self.gps_longitude = x

    def set_altitude(self, x):
        self.gps_altitude = x

    def set_satellites(self, x):
        self.gps_satellites = x

    def set_map_datum(self, x):
        self.gps_map_datum = x

    def set_status(self, x):
        self.gps_status = x

    def set_measure_mode(self, x):
        self.gps_measure_mode = x

def CustomLogger():

    logger = getLogger()

    formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')

    handler = StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(INFO)

    return logger

def ParseConfig(gpsdata, configFile):

    try:
        json_file = open(configFile, 'r')
        json_obj  = json.load(json_file)
    
        gpsdata.set_datestamp(json_obj['gps']['DATESTAMP'])
        gpsdata.set_timestamp(json_obj['gps']['TIMESTAMP'])
        gpsdata.set_latitude_ref(json_obj['gps']['LATITUDE_REF'])
        gpsdata.set_longitude_ref(json_obj['gps']['LONGITUDE_REF'])
        gpsdata.set_latitude(json_obj['gps']['LATITUDE'])
        gpsdata.set_longitude(json_obj['gps']['LONGITUDE'])
        gpsdata.set_altitude(json_obj['gps']['ALTITUDE'])
        gpsdata.set_satellites(json_obj['gps']['SATELLITES'])
        gpsdata.set_map_datum(json_obj['gps']['MAP_DATUM'])
        gpsdata.set_status(json_obj['gps']['STATUS'])
        gpsdata.set_measure_mode(json_obj['gps']['MEASURE_MODE'])

    except FileNotFoundError as e:
        logger.error('設定ファイルが見つかりませんでした。')
        sys.exit(1)

def SetGPSTag(gpsdata, imgFile):

    shutil.copy2(imgFile, imgFile + '_bak')
    photo = gpsphoto.GPSPhoto(imgFile)

    try:
        info = gpsphoto.GPSInfo((float(gpsdata.get_latitude()), float(gpsdata.get_longitude())), alt=int(gpsdata.get_altitude()), timeStamp = gpsdata.get_datestamp() + ' ' + gpsdata.get_timestamp())
        photo.modGPSData(info, imgFile)
        logger.info('画像ファイル "' + imgFile + '" への GPS タグの付与に成功しました。')
    except Exception as e:
        logger.error(e)

def main():
    argc = len(sys.argv)
    if ( argc <= 1 ):
        print('')
        print('[説明] PyGeoSetter ～画像ファイルに GPS 情報を付与するツール～')
        print('[バージョン] 1.0.0 (2022/10/28)')
        print('[使用法] PyGetSetter.py <ファイル名>')
        print('　※「ファイル名」にはワイルドカード（例: *.jpg）が使用可能')
        sys.exit(1)
    else:
        gpsdata = GPSData()
        ParseConfig(gpsdata, CONFIG_FILE)
        for f in glob.glob(sys.argv[1]):
            SetGPSTag(gpsdata, f)

if __name__ == '__main__':
    logger = CustomLogger()
    main()