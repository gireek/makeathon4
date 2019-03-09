from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, Numeric, orm
from config.utils import config

db = config()
port=5432
DATABASE_URI = 'postgres+psycopg2://{}:{}@{}:{}/{}'.format(db['user'], db['password'], db['host'], port ,db['database'])


Base = declarative_base()
class Flowline(Base):
    __tablename__ = 'flowline'
    timestamp = Column(DateTime, primary_key=True)
    COL_05_PT_28201_01_B2_Manifold_Pressure = Column(Numeric) #'05-PT-28201-01_B2_Manifold_Pressure (Psi)'
    COL_05_PT_28201_03_B2_Manifold_Pressure = Column(Numeric) #'05-PT-28201-03_B2_Manifold_Pressure (Psi)'
    COL_05_PT_29101_02_C1_Manifold_Pressure = Column(Numeric) #'05-PT-29101-02_C1_Manifold_Pressure (Psi)'
    COL_05_PT_29101_03_C1_Manifold_Pressure = Column(Numeric) #'05-PT-29101-03_C1_Manifold_Pressure (Psi)'
    COL_05_PT_33101_02_G1_Manifold_Pressure = Column(Numeric) #'05-PT-33101-02_G1_Manifold_Pressure (Psi)'
    COL_05_PT_33101_03_G1_Manifold_Pressure = Column(Numeric) #'05-PT-33101-03_G1_Manifold_Pressure (Psi)'
    COL_05_PT_34101_01_H1_Manifold_Pressure = Column(Numeric) #'05-PT-34101-01_H1_Manifold_Pressure (Psi)'
    COL_05_PT_34101_04_H1_Manifold_Pressure = Column(Numeric) #'05-PT-34101-04_H1_Manifold_Pressure (Psi)'
    COL_05_TT_28201_01_B2_Manifold_Temperature = Column(Numeric) #'05-TT-28201-01_B2_Manifold_Temperature (DegF)'
    COL_05_TT_28201_03_B2_Manifold_Temperature = Column(Numeric) #'05-TT-28201-03_B2_Manifold_Temperature (DegF)'
    COL_05_TT_29101_02_C1_Manifold_Temperature = Column(Numeric) #'05-TT-29101-02_C1_Manifold_Temperature (DegF)'
    COL_05_TT_29101_03_C1_Manifold_Temperature = Column(Numeric) #'05-TT-29101-03_C1_Manifold_Temperature (DegF)'
    COL_05_TT_33101_02_G1_Manifold_Temperature = Column(Numeric) #'05-TT-33101-02_G1_Manifold_Temperature (DegF)'
    COL_05_TT_33101_03_G1_Manifold_Temperature = Column(Numeric) #'05-TT-33101-03_G1_Manifold_Temperature (DegF)'
    COL_05_TT_34101_01_H1_Manifold_Temperature = Column(Numeric) #'05-TT-34101-01_H1_Manifold_Temperature (DegF)'
    COL_05_TT_34101_04_H1_Manifold_Temperature = Column(Numeric) #'05-TT-34101-04_H1_Manifold_Temperature (DegF)'
    COL_20_HX_10003_Status_Flowline_From_Drill_Center_C = Column(String) #'20-HX-10003.Status_Flowline_From_Drill_Center_C ( )'
    COL_20_HX_10004_Status_Flowline_From_Drill_Center_C = Column(String) #'20-HX-10004.Status_Flowline_From_Drill_Center_C ( )'
    COL_20_HX_20003_Status_Flowline_From_Drill_Centers_B_G = Column(String) #'20-HX-20003.Status_Flowline_From_Drill_Centers_B&G ( )'
    COL_20_HX_20004_Status_Flowline_From_Drill_Centers_B_G = Column(String) #'20-HX-20004.Status_Flowline_From_Drill_Centers_B&G ( )'
    COL_20_PIC_10114_PV_P2_Subsea_Flowline_Eq_Choke_Open = Column(Numeric) #'20-PIC-10114.PV_P2_Subsea_Flowline_Eq_Choke_%_Open (PSIG)'
    COL_20_PIC_10214_PV_P1_Subsea_Flowline_Eq_Choke_Open = Column(Numeric) #'20-PIC-10214.PV_P1_Subsea_Flowline_Eq_Choke_%_Open (PSIG)'
    COL_20_PT_10007_01_PV_Flowline_From_Drill_Center_C = Column(Numeric) #'20-PT-10007-01.PV_Flowline_From_Drill_Center_C (PSIG)'
    COL_20_PT_10008_01_PV_Flowline_From_Drill_Center_C = Column(Numeric) #'20-PT-10008-01.PV_Flowline_From_Drill_Center_C (PSIG)'
    COL_20_PT_20007_01_PV_Flowline_From_Drill_Centers_B_G = Column(Numeric) #'20-PT-20007-01.PV_Flowline_From_Drill_Centers_B&G (PSIG)'
    COL_20_PT_20008_01_PV_Flowline_From_Drill_Centers_B_G = Column(Numeric) #'20-PT-20008-01.PV_Flowline_From_Drill_Centers_B&G (PSIG)'
    COL_20_PT_20114_PV_Subsea_Flowline_Launcher = Column(Numeric) #'20-PT-20114.PV_Subsea_Flowline_Launcher (PSIG)'
    COL_20_PT_20214_PV_Subsea_Flowline_Receiver = Column(Numeric) #'20-PT-20214.PV_Subsea_Flowline_Receiver (PSIG)'
    COL_20_TT_10105_PV_Subsea_Flowline_To_Train_1 = Column(Numeric) #'20-TT-10105.PV_Subsea_Flowline_To_Train_1 (Deg.F)'
    COL_20_TT_10205_PV_Subsea_Flowline_Test_Sep = Column(Numeric) #'20-TT-10205.PV_Subsea_Flowline_Test_Sep (Deg.F)'
    COL_20_TT_20105_PV_Train_2_Subsea_Flowline_Launcher = Column(Numeric) #'20-TT-20105.PV_Train_2_Subsea_Flowline_Launcher (Deg.F)'
    COL_20_TT_20205_PV_Train_2_Subsea_Flowline_Receiver = Column(Numeric) #'20-TT-20205.PV_Train_2_Subsea_Flowline_Receiver (Deg.F)'
    COL_20_ZT_10104_PV_To_From_Subsea_Flowline = Column(Numeric) #'20-ZT-10104.PV_To/From_Subsea_Flowline (%)'
    COL_20_ZT_10204_PV_To_From_Subsea_Flowline = Column(Numeric) #'20-ZT-10204.PV_To/From_Subsea_Flowline (%)'
    COL_20_ZT_20104_PV_Train_2_Subsea_Flowline_Launcher = Column(Numeric) #'20-ZT-20104.PV_Train_2_Subsea_Flowline_Launcher (%)'
    COL_20_ZT_20204_PV_Train_2_Subsea_Flowline_Receiver = Column(Numeric) #'20-ZT-20204.PV_Train_2_Subsea_Flowline_Receiver (%)'

    def __init__(self, *args):
        self.timestamp,\
        self.COL_05_PT_28201_01_B2_Manifold_Pressure,\
        self.COL_05_PT_28201_03_B2_Manifold_Pressure,\
        self.COL_05_PT_29101_02_C1_Manifold_Pressure,\
        self.COL_05_PT_29101_03_C1_Manifold_Pressure,\
        self.COL_05_PT_33101_02_G1_Manifold_Pressure,\
        self.COL_05_PT_33101_03_G1_Manifold_Pressure,\
        self.COL_05_PT_34101_01_H1_Manifold_Pressure,\
        self.COL_05_PT_34101_04_H1_Manifold_Pressure,\
        self.COL_05_TT_28201_01_B2_Manifold_Temperature,\
        self.COL_05_TT_28201_03_B2_Manifold_Temperature,\
        self.COL_05_TT_29101_02_C1_Manifold_Temperature,\
        self.COL_05_TT_29101_03_C1_Manifold_Temperature,\
        self.COL_05_TT_33101_02_G1_Manifold_Temperature,\
        self.COL_05_TT_33101_03_G1_Manifold_Temperature,\
        self.COL_05_TT_34101_01_H1_Manifold_Temperature,\
        self.COL_05_TT_34101_04_H1_Manifold_Temperature,\
        self.COL_20_HX_10003_Status_Flowline_From_Drill_Center_C,\
        self.COL_20_HX_10004_Status_Flowline_From_Drill_Center_C,\
        self.COL_20_HX_20003_Status_Flowline_From_Drill_Centers_B_G,\
        self.COL_20_HX_20004_Status_Flowline_From_Drill_Centers_B_G,\
        self.COL_20_PIC_10114_PV_P2_Subsea_Flowline_Eq_Choke_Open,\
        self.COL_20_PIC_10214_PV_P1_Subsea_Flowline_Eq_Choke_Open,\
        self.COL_20_PT_10007_01_PV_Flowline_From_Drill_Center_C,\
        self.COL_20_PT_10008_01_PV_Flowline_From_Drill_Center_C,\
        self.COL_20_PT_20007_01_PV_Flowline_From_Drill_Centers_B_G,\
        self.COL_20_PT_20008_01_PV_Flowline_From_Drill_Centers_B_G,\
        self.COL_20_PT_20114_PV_Subsea_Flowline_Launcher,\
        self.COL_20_PT_20214_PV_Subsea_Flowline_Receiver,\
        self.COL_20_TT_10105_PV_Subsea_Flowline_To_Train_1,\
        self.COL_20_TT_10205_PV_Subsea_Flowline_Test_Sep,\
        self.COL_20_TT_20105_PV_Train_2_Subsea_Flowline_Launcher,\
        self.COL_20_TT_20205_PV_Train_2_Subsea_Flowline_Receiver,\
        self.COL_20_ZT_10104_PV_To_From_Subsea_Flowline,\
        self.COL_20_ZT_10204_PV_To_From_Subsea_Flowline,\
        self.COL_20_ZT_20104_PV_Train_2_Subsea_Flowline_Launcher,\
        self.COL_20_ZT_20204_PV_Train_2_Subsea_Flowline_Receiver = tuple(args)

    @orm.reconstructor
    def init_on_load(self, *args):
        self.__init__(args)

    def __repr__(self):
        return "<Flowline(timestamp ='{}',\
            COL_05_PT_28201_01_B2_Manifold_Pressure ='{}',\
            COL_05_PT_28201_03_B2_Manifold_Pressure ='{}',\
            COL_05_PT_29101_02_C1_Manifold_Pressure ='{}',\
            COL_05_PT_29101_03_C1_Manifold_Pressure ='{}',\
            COL_05_PT_33101_02_G1_Manifold_Pressure ='{}',\
            COL_05_PT_33101_03_G1_Manifold_Pressure ='{}',\
            COL_05_PT_34101_01_H1_Manifold_Pressure ='{}',\
            COL_05_PT_34101_04_H1_Manifold_Pressure ='{}',\
            COL_05_TT_28201_01_B2_Manifold_Temperature ='{}',\
            COL_05_TT_28201_03_B2_Manifold_Temperature ='{}',\
            COL_05_TT_29101_02_C1_Manifold_Temperature ='{}',\
            COL_05_TT_29101_03_C1_Manifold_Temperature ='{}',\
            COL_05_TT_33101_02_G1_Manifold_Temperature ='{}',\
            COL_05_TT_33101_03_G1_Manifold_Temperature ='{}',\
            COL_05_TT_34101_01_H1_Manifold_Temperature ='{}',\
            COL_05_TT_34101_04_H1_Manifold_Temperature ='{}',\
            COL_20_HX_10003_Status_Flowline_From_Drill_Center_C ='{}',\
            COL_20_HX_10004_Status_Flowline_From_Drill_Center_C ='{}',\
            COL_20_HX_20003_Status_Flowline_From_Drill_Centers_B_G ='{}',\
            COL_20_HX_20004_Status_Flowline_From_Drill_Centers_B_G ='{}',\
            COL_20_PIC_10114_PV_P2_Subsea_Flowline_Eq_Choke_Open ='{}',\
            COL_20_PIC_10214_PV_P1_Subsea_Flowline_Eq_Choke_Open ='{}',\
            COL_20_PT_10007_01_PV_Flowline_From_Drill_Center_C ='{}',\
            COL_20_PT_10008_01_PV_Flowline_From_Drill_Center_C ='{}',\
            COL_20_PT_20007_01_PV_Flowline_From_Drill_Centers_B_G ='{}',\
            COL_20_PT_20008_01_PV_Flowline_From_Drill_Centers_B_G ='{}',\
            COL_20_PT_20114_PV_Subsea_Flowline_Launcher ='{}',\
            COL_20_PT_20214_PV_Subsea_Flowline_Receiver ='{}',\
            COL_20_TT_10105_PV_Subsea_Flowline_To_Train_1 ='{}',\
            COL_20_TT_10205_PV_Subsea_Flowline_Test_Sep ='{}',\
            COL_20_TT_20105_PV_Train_2_Subsea_Flowline_Launcher ='{}',\
            COL_20_TT_20205_PV_Train_2_Subsea_Flowline_Receiver ='{}',\
            COL_20_ZT_10104_PV_To_From_Subsea_Flowline ='{}',\
            COL_20_ZT_10204_PV_To_From_Subsea_Flowline ='{}',\
            COL_20_ZT_20104_PV_Train_2_Subsea_Flowline_Launcher ='{}',\
            COL_20_ZT_20204_PV_Train_2_Subsea_Flowline_Receiver ='{}')>"\
            .format(self.timestamp,
            self.COL_05_PT_28201_01_B2_Manifold_Pressure ,
            self.COL_05_PT_28201_03_B2_Manifold_Pressure ,
            self.COL_05_PT_29101_02_C1_Manifold_Pressure ,
            self.COL_05_PT_29101_03_C1_Manifold_Pressure ,
            self.COL_05_PT_33101_02_G1_Manifold_Pressure ,
            self.COL_05_PT_33101_03_G1_Manifold_Pressure ,
            self.COL_05_PT_34101_01_H1_Manifold_Pressure ,
            self.COL_05_PT_34101_04_H1_Manifold_Pressure ,
            self.COL_05_TT_28201_01_B2_Manifold_Temperature ,
            self.COL_05_TT_28201_03_B2_Manifold_Temperature ,
            self.COL_05_TT_29101_02_C1_Manifold_Temperature ,
            self.COL_05_TT_29101_03_C1_Manifold_Temperature ,
            self.COL_05_TT_33101_02_G1_Manifold_Temperature ,
            self.COL_05_TT_33101_03_G1_Manifold_Temperature ,
            self.COL_05_TT_34101_01_H1_Manifold_Temperature ,
            self.COL_05_TT_34101_04_H1_Manifold_Temperature ,
            self.COL_20_HX_10003_Status_Flowline_From_Drill_Center_C ,
            self.COL_20_HX_10004_Status_Flowline_From_Drill_Center_C ,
            self.COL_20_HX_20003_Status_Flowline_From_Drill_Centers_B_G ,
            self.COL_20_HX_20004_Status_Flowline_From_Drill_Centers_B_G ,
            self.COL_20_PIC_10114_PV_P2_Subsea_Flowline_Eq_Choke_Open ,
            self.COL_20_PIC_10214_PV_P1_Subsea_Flowline_Eq_Choke_Open ,
            self.COL_20_PT_10007_01_PV_Flowline_From_Drill_Center_C ,
            self.COL_20_PT_10008_01_PV_Flowline_From_Drill_Center_C ,
            self.COL_20_PT_20007_01_PV_Flowline_From_Drill_Centers_B_G ,
            self.COL_20_PT_20008_01_PV_Flowline_From_Drill_Centers_B_G ,
            self.COL_20_PT_20114_PV_Subsea_Flowline_Launcher ,
            self.COL_20_PT_20214_PV_Subsea_Flowline_Receiver ,
            self.COL_20_TT_10105_PV_Subsea_Flowline_To_Train_1 ,
            self.COL_20_TT_10205_PV_Subsea_Flowline_Test_Sep ,
            self.COL_20_TT_20105_PV_Train_2_Subsea_Flowline_Launcher ,
            self.COL_20_TT_20205_PV_Train_2_Subsea_Flowline_Receiver ,
            self.COL_20_ZT_10104_PV_To_From_Subsea_Flowline ,
            self.COL_20_ZT_10204_PV_To_From_Subsea_Flowline ,
            self.COL_20_ZT_20104_PV_Train_2_Subsea_Flowline_Launcher ,
            self.COL_20_ZT_20204_PV_Train_2_Subsea_Flowline_Receiver
            )


