import pandas as pd
from matplotlib import ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter

from proj_data.bhp_sep.raw import path as raw_path
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

COL_05_PT_28201_01_B2_Manifold_Pressure = '05-PT-28201-01_B2_Manifold_Pressure (Psi)'
COL_05_PT_28201_03_B2_Manifold_Pressure = '05-PT-28201-03_B2_Manifold_Pressure (Psi)'
COL_05_PT_29101_02_C1_Manifold_Pressure = '05-PT-29101-02_C1_Manifold_Pressure (Psi)'
COL_05_PT_29101_03_C1_Manifold_Pressure = '05-PT-29101-03_C1_Manifold_Pressure (Psi)'
COL_05_PT_33101_02_G1_Manifold_Pressure = '05-PT-33101-02_G1_Manifold_Pressure (Psi)'
COL_05_PT_33101_03_G1_Manifold_Pressure = '05-PT-33101-03_G1_Manifold_Pressure (Psi)'
COL_05_PT_34101_01_H1_Manifold_Pressure = '05-PT-34101-01_H1_Manifold_Pressure (Psi)'
COL_05_PT_34101_04_H1_Manifold_Pressure = '05-PT-34101-04_H1_Manifold_Pressure (Psi)'
COL_05_TT_28201_01_B2_Manifold_Temperature = '05-TT-28201-01_B2_Manifold_Temperature (DegF)'
COL_05_TT_28201_03_B2_Manifold_Temperature = '05-TT-28201-03_B2_Manifold_Temperature (DegF)'
COL_05_TT_29101_02_C1_Manifold_Temperature = '05-TT-29101-02_C1_Manifold_Temperature (DegF)'
COL_05_TT_29101_03_C1_Manifold_Temperature = '05-TT-29101-03_C1_Manifold_Temperature (DegF)'
COL_05_TT_33101_02_G1_Manifold_Temperature = '05-TT-33101-02_G1_Manifold_Temperature (DegF)'
COL_05_TT_33101_03_G1_Manifold_Temperature = '05-TT-33101-03_G1_Manifold_Temperature (DegF)'
COL_05_TT_34101_01_H1_Manifold_Temperature = '05-TT-34101-01_H1_Manifold_Temperature (DegF)'
COL_05_TT_34101_04_H1_Manifold_Temperature = '05-TT-34101-04_H1_Manifold_Temperature (DegF)'
COL_20_HX_10003_Status_Flowline_From_Drill_Center_C = '20-HX-10003.Status_Flowline_From_Drill_Center_C ( )'
COL_20_HX_10004_Status_Flowline_From_Drill_Center_C = '20-HX-10004.Status_Flowline_From_Drill_Center_C ( )'
COL_20_HX_20003_Status_Flowline_From_Drill_Centers_B_G = '20-HX-20003.Status_Flowline_From_Drill_Centers_B&G ( )'
COL_20_HX_20004_Status_Flowline_From_Drill_Centers_B_G = '20-HX-20004.Status_Flowline_From_Drill_Centers_B&G ( )'
COL_20_PIC_10114_PV_P2_Subsea_Flowline_Eq_Choke_Open = '20-PIC-10114.PV_P2_Subsea_Flowline_Eq_Choke_%_Open (PSIG)'
COL_20_PIC_10214_PV_P1_Subsea_Flowline_Eq_Choke_Open = '20-PIC-10214.PV_P1_Subsea_Flowline_Eq_Choke_%_Open (PSIG)'
COL_20_PT_10007_01_PV_Flowline_From_Drill_Center_C = '20-PT-10007-01.PV_Flowline_From_Drill_Center_C (PSIG)'
COL_20_PT_10008_01_PV_Flowline_From_Drill_Center_C = '20-PT-10008-01.PV_Flowline_From_Drill_Center_C (PSIG)'
COL_20_PT_20007_01_PV_Flowline_From_Drill_Centers_B_G = '20-PT-20007-01.PV_Flowline_From_Drill_Centers_B&G (PSIG)'
COL_20_PT_20008_01_PV_Flowline_From_Drill_Centers_B_G = '20-PT-20008-01.PV_Flowline_From_Drill_Centers_B&G (PSIG)'
COL_20_PT_20114_PV_Subsea_Flowline_Launcher = '20-PT-20114.PV_Subsea_Flowline_Launcher (PSIG)'
COL_20_PT_20214_PV_Subsea_Flowline_Receiver = '20-PT-20214.PV_Subsea_Flowline_Receiver (PSIG)'
COL_20_TT_10105_PV_Subsea_Flowline_To_Train_1 = '20-TT-10105.PV_Subsea_Flowline_To_Train_1 (Deg.F)'
COL_20_TT_10205_PV_Subsea_Flowline_Test_Sep = '20-TT-10205.PV_Subsea_Flowline_Test_Sep (Deg.F)'
COL_20_TT_20105_PV_Train_2_Subsea_Flowline_Launcher = '20-TT-20105.PV_Train_2_Subsea_Flowline_Launcher (Deg.F)'
COL_20_TT_20205_PV_Train_2_Subsea_Flowline_Receiver = '20-TT-20205.PV_Train_2_Subsea_Flowline_Receiver (Deg.F)'
COL_20_ZT_10104_PV_To_From_Subsea_Flowline = '20-ZT-10104.PV_To/From_Subsea_Flowline (%)'
COL_20_ZT_10204_PV_To_From_Subsea_Flowline = '20-ZT-10204.PV_To/From_Subsea_Flowline (%)'
COL_20_ZT_20104_PV_Train_2_Subsea_Flowline_Launcher = '20-ZT-20104.PV_Train_2_Subsea_Flowline_Launcher (%)'
COL_20_ZT_20204_PV_Train_2_Subsea_Flowline_Receiver = '20-ZT-20204.PV_Train_2_Subsea_Flowline_Receiver (%)'
COL_21_FQI_10518_01_NetRate_PV = '21-FQI-10518-01.NetRate.PV (BPD)'
COL_21_FT_40518_03_Density = '21-FT-40518-03_Density_(Coriolis) (g/cc)'
COL_21_FT_40518_03_Gross_Volume_Flow_Rate = '21-FT-40518-03_Gross_Volume_Flow_Rate_(Coriolis) (bbl/d)'
COL_21_HY_10535_OUT_Flowline_Lchr_Rcvr_To_Prod_Sep = '21-HY-10535.OUT_Flowline_Lchr/Rcvr_To_Prod_Sep (%)'
COL_21_HY_40534_OUT_Test_Separator_Inlet = '21-HY-40534.OUT_Test_Separator_Inlet (%)'
COL_21_LIC_10516_SP_Prod_Sep_Oil_Out_To_2nd_Stg_Sep = '21-LIC-10516.SP_Prod_Sep_Oil_Out_To_2nd_Stg_Sep (%)'
COL_21_LIC_10620_CV_2nd_Stg_Hydrocyclone_Wtr_Out = '21-LIC-10620.CV_2nd_Stg_Hydrocyclone_Wtr_Out (%)'
COL_21_LIC_10620_SP_2nd_Stg_Hydrocyclone_Wtr_Out = '21-LIC-10620.SP_2nd_Stg_Hydrocyclone_Wtr_Out (%)'
COL_21_LIC_40516_SP_Test_Allocation_Sep_Interface = '21-LIC-40516.SP_Test_Allocation_Sep_Interface (%)'
COL_21_LT_10515_PV_Prod_Sep_Oil_Interface_Level = '21-LT-10515.PV_Prod_Sep_Oil_Interface_Level (%)'
COL_21_LT_10516_PV_Prod_Sep_Oil_Interface_Level = '21-LT-10516.PV_Prod_Sep_Oil_Interface_Level (%)'
COL_21_LT_10618_PV_Prod_Sep_2nd_Stg_Interface = '21-LT-10618.PV_Prod_Sep_2nd_Stg_Interface (%)'
COL_21_LT_10620_PV_Prod_Sep_2nd_Stg_Interface = '21-LT-10620.PV_Prod_Sep_2nd_Stg_Interface (%)'
COL_21_LT_40515_PV_Test_Allocation_Sep_Interface = '21-LT-40515.PV_Test_Allocation_Sep_Interface (%)'
COL_21_LT_40516_PV_Test_Allocation_Sep_Interface = '21-LT-40516.PV_Test_Allocation_Sep_Interface (%)'
COL_21_LY_10516_OUT_Prod_Sep_Oil_Out_To_2nd_Stg_Sep = '21-LY-10516.OUT_Prod_Sep_Oil_Out_To_2nd_Stg_Sep (%)'
COL_21_LY_10616_OUT_Prod_Sep_2nd_Stg_Fluid_To_Exch = '21-LY-10616.OUT_Prod_Sep_2nd_Stg_Fluid_To_Exch (%)'
COL_21_LY_10620_OUT_2nd_Stg_Hydrocyclone_Wtr_Out = '21-LY-10620.OUT_2nd_Stg_Hydrocyclone_Wtr_Out (%)'
COL_21_LY_11516_OUT_Train_1_Treater_Wtr_Interface_Level = '21-LY-11516.OUT_Train_1_Treater_Wtr_Interface_Level (%)'
COL_21_LY_40516_OUT = '21-LY-40516.OUT (%)'
COL_21_PT_10505_PV_Production_Separator = '21-PT-10505.PV_Production_Separator (PSIG)'
COL_21_PT_10605_PV_Prod_Sep_2nd_Stg = '21-PT-10605.PV_Prod_Sep_2nd_Stg (PSIG)'
COL_21_PT_40505_PV_Test_Allocation_Separator = '21-PT-40505.PV_Test_Allocation_Separator (PSIG)'
COL_21_TT_10508_PV_Prod_Sep_Gas_Out_To_Flash_Clr = '21-TT-10508.PV_Prod_Sep_Gas_Out_To_Flash_Clr (Deg.F)'
COL_21_TT_10608_PV_Prod_Sep_2nd_Stg_Gas_Out = '21-TT-10608.PV_Prod_Sep_2nd_Stg_Gas_Out (Deg.F)'
COL_21_TT_11616_PV_Crude_Oil_Trim_Heat_Outlet = '21-TT-11616.PV_Crude_Oil_Trim_Heat_Outlet (Deg.F)'
COL_30_FT_19107_01_PV_2nd_Stg_Hydrocyclone_Inlet = '30-FT-19107-01.PV_2nd_Stg_Hydrocyclone_Inlet (BPD)'
COL_30_FT_19108_PV = '30-FT-19108.PV ( )'
COL_30_FT_29108_PV = '30-FT-29108.PV (BPD)'
COL_30_FT_69521_01_PV_Flotation_Cell_Prod_Wtr_To_Ovbrd = '30-FT-69521-01.PV_Flotation_Cell_Prod_Wtr_To_Ovbrd (BPD)'
COL_30_LIC_69516_CV_Flotation_Cell_Out_To_Drn = '30-LIC-69516.CV_Flotation_Cell_Out_To_Drn (%)'
COL_30_LIC_69518_CV_Flotation_Cell_Prod_Wtr_To_Ovbrd = '30-LIC-69518.CV_Flotation_Cell_Prod_Wtr_To_Ovbrd (%)'
COL_30_LT_69514_PV_Flotation_Cell = '30-LT-69514.PV_Flotation_Cell (%)'
COL_30_LT_69515_PV_Flotation_Cell = '30-LT-69515.PV_Flotation_Cell (%)'
COL_30_LT_69516_PV_Flotation_Cell = '30-LT-69516.PV_Flotation_Cell (%)'
COL_30_LT_69518_PV_Flotation_Cell = '30-LT-69518.PV_Flotation_Cell (%)'
COL_30_LY_69518_OUT_Flotation_Cell_Prod_Wtr_To_Ovbrd = '30-LY-69518.OUT_Flotation_Cell_Prod_Wtr_To_Ovbrd (%)'
COL_30_PDIC_19104_SP_2nd_Stg_Prod_Hydrocyclone_Out = '30-PDIC-19104.SP_2nd_Stg_Prod_Hydrocyclone_Out ( )'
COL_30_PDT_19104_01_PV_2nd_Stg_Hydrocyclone_Out_To_Drn = '30-PDT-19104-01.PV_2nd_Stg_Hydrocyclone_Out_To_Drn (PSID)'
COL_30_PDT_19104_02_PV_2nd_Stg_Hydrocyclone_To_Skimmer = '30-PDT-19104-02.PV_2nd_Stg_Hydrocyclone_To_Skimmer (PSID)'
COL_30_PDT_19104_PV_2nd_Stg_Hydrocyclone_Out_To_Drn_Diff_Press_Ratio = '30-PDT-19104.PV_2nd_Stg_Hydrocyclone_Out_To_Drn_Diff_Press_Ratio (PSID)'
COL_30_PDY_19104_OUT_2nd_Stg_Prod_Hydrocyclone_Out = '30-PDY-19104.OUT_2nd_Stg_Prod_Hydrocyclone_Out (%)'
COL_30_PT_69503_PV_Flotation_Cell = '30-PT-69503.PV_Flotation_Cell (PSIG)'
COL_30_PT_69512_PV = '30-PT-69512.PV (psig)'
COL_30_PY_69503_OUT_Flotation_Cell_Out_To_LP_Flare = '30-PY-69503.OUT_Flotation_Cell_Out_To_LP_Flare (%)'
COL_37_PT_62301_PV_Closed_Smp_Tk_Pmp_Disch_To_Sep = '37-PT-62301.PV_Closed_Smp_Tk_Pmp_Disch_To_Sep (PSIG)'

headings = (
    '05-PT-28201-01_B2_Manifold_Pressure (Psi)',
    '05-PT-28201-03_B2_Manifold_Pressure (Psi)',
    '05-PT-29101-02_C1_Manifold_Pressure (Psi)',
    '05-PT-29101-03_C1_Manifold_Pressure (Psi)',
    '05-PT-33101-02_G1_Manifold_Pressure (Psi)',
    '05-PT-33101-03_G1_Manifold_Pressure (Psi)',
    '05-PT-34101-01_H1_Manifold_Pressure (Psi)',
    '05-PT-34101-04_H1_Manifold_Pressure (Psi)',
    '05-TT-28201-01_B2_Manifold_Temperature (DegF)',
    '05-TT-28201-03_B2_Manifold_Temperature (DegF)',
    '05-TT-29101-02_C1_Manifold_Temperature (DegF)',
    '05-TT-29101-03_C1_Manifold_Temperature (DegF)',
    '05-TT-33101-02_G1_Manifold_Temperature (DegF)',
    '05-TT-33101-03_G1_Manifold_Temperature (DegF)',
    '05-TT-34101-01_H1_Manifold_Temperature (DegF)',
    '05-TT-34101-04_H1_Manifold_Temperature (DegF)',
    '20-HX-10003.Status_Flowline_From_Drill_Center_C ( )',
    '20-HX-10004.Status_Flowline_From_Drill_Center_C ( )',
    '20-HX-20003.Status_Flowline_From_Drill_Centers_B&G ( )',
    '20-HX-20004.Status_Flowline_From_Drill_Centers_B&G ( )',
    '20-PIC-10114.PV_P2_Subsea_Flowline_Eq_Choke_%_Open (PSIG)',
    '20-PIC-10214.PV_P1_Subsea_Flowline_Eq_Choke_%_Open (PSIG)',
    '20-PT-10007-01.PV_Flowline_From_Drill_Center_C (PSIG)',
    '20-PT-10008-01.PV_Flowline_From_Drill_Center_C (PSIG)',
    '20-PT-20007-01.PV_Flowline_From_Drill_Centers_B&G (PSIG)',
    '20-PT-20008-01.PV_Flowline_From_Drill_Centers_B&G (PSIG)',
    '20-PT-20114.PV_Subsea_Flowline_Launcher (PSIG)',
    '20-PT-20214.PV_Subsea_Flowline_Receiver (PSIG)',
    '20-TT-10105.PV_Subsea_Flowline_To_Train_1 (Deg.F)',
    '20-TT-10205.PV_Subsea_Flowline_Test_Sep (Deg.F)',
    '20-TT-20105.PV_Train_2_Subsea_Flowline_Launcher (Deg.F)',
    '20-TT-20205.PV_Train_2_Subsea_Flowline_Receiver (Deg.F)',
    '20-ZT-10104.PV_To/From_Subsea_Flowline (%)',
    '20-ZT-10204.PV_To/From_Subsea_Flowline (%)',
    '20-ZT-20104.PV_Train_2_Subsea_Flowline_Launcher (%)',
    '20-ZT-20204.PV_Train_2_Subsea_Flowline_Receiver (%)',
    '21-FQI-10518-01.NetRate.PV (BPD)',
    '21-FT-40518-03_Density_(Coriolis) (g/cc)',
    '21-FT-40518-03_Gross_Volume_Flow_Rate_(Coriolis) (bbl/d)',
    '21-HY-10535.OUT_Flowline_Lchr/Rcvr_To_Prod_Sep (%)',
    '21-HY-40534.OUT_Test_Separator_Inlet (%)',
    '21-LIC-10516.SP_Prod_Sep_Oil_Out_To_2nd_Stg_Sep (%)',
    '21-LIC-10620.CV_2nd_Stg_Hydrocyclone_Wtr_Out (%)',
    '21-LIC-10620.SP_2nd_Stg_Hydrocyclone_Wtr_Out (%)',
    '21-LIC-40516.SP_Test_Allocation_Sep_Interface (%)',
    '21-LT-10515.PV_Prod_Sep_Oil_Interface_Level (%)',
    '21-LT-10516.PV_Prod_Sep_Oil_Interface_Level (%)',
    '21-LT-10618.PV_Prod_Sep_2nd_Stg_Interface (%)',
    '21-LT-10620.PV_Prod_Sep_2nd_Stg_Interface (%)',
    '21-LT-40515.PV_Test_Allocation_Sep_Interface (%)',
    '21-LT-40516.PV_Test_Allocation_Sep_Interface (%)',
    '21-LY-10516.OUT_Prod_Sep_Oil_Out_To_2nd_Stg_Sep (%)',
    '21-LY-10616.OUT_Prod_Sep_2nd_Stg_Fluid_To_Exch (%)',
    '21-LY-10620.OUT_2nd_Stg_Hydrocyclone_Wtr_Out (%)',
    '21-LY-11516.OUT_Train_1_Treater_Wtr_Interface_Level (%)',
    '21-LY-40516.OUT (%)',
    '21-PT-10505.PV_Production_Separator (PSIG)',
    '21-PT-10605.PV_Prod_Sep_2nd_Stg (PSIG)',
    '21-PT-40505.PV_Test_Allocation_Separator (PSIG)',
    '21-TT-10508.PV_Prod_Sep_Gas_Out_To_Flash_Clr (Deg.F)',
    '21-TT-10608.PV_Prod_Sep_2nd_Stg_Gas_Out (Deg.F)',
    '21-TT-11616.PV_Crude_Oil_Trim_Heat_Outlet (Deg.F)',
    '30-FT-19107-01.PV_2nd_Stg_Hydrocyclone_Inlet (BPD)',
    '30-FT-19108.PV ( )',
    '30-FT-29108.PV (BPD)',
    '30-FT-69521-01.PV_Flotation_Cell_Prod_Wtr_To_Ovbrd (BPD)',
    '30-LIC-69516.CV_Flotation_Cell_Out_To_Drn (%)',
    '30-LIC-69518.CV_Flotation_Cell_Prod_Wtr_To_Ovbrd (%)',
    '30-LT-69514.PV_Flotation_Cell (%)',
    '30-LT-69515.PV_Flotation_Cell (%)',
    '30-LT-69516.PV_Flotation_Cell (%)',
    '30-LT-69518.PV_Flotation_Cell (%)',
    '30-LY-69518.OUT_Flotation_Cell_Prod_Wtr_To_Ovbrd (%)',
    '30-PDIC-19104.SP_2nd_Stg_Prod_Hydrocyclone_Out ( )',
    '30-PDT-19104-01.PV_2nd_Stg_Hydrocyclone_Out_To_Drn (PSID)',
    '30-PDT-19104-02.PV_2nd_Stg_Hydrocyclone_To_Skimmer (PSID)',
    '30-PDT-19104.PV_2nd_Stg_Hydrocyclone_Out_To_Drn_Diff_Press_Ratio (PSID)',
    '30-PDY-19104.OUT_2nd_Stg_Prod_Hydrocyclone_Out (%)',
    '30-PT-69503.PV_Flotation_Cell (PSIG)',
    '30-PT-69512.PV (psig)',
    '30-PY-69503.OUT_Flotation_Cell_Out_To_LP_Flare (%)',
    '37-PT-62301.PV_Closed_Smp_Tk_Pmp_Disch_To_Sep (PSIG)'
)

error_dates = (
    '2016-10-26',
    '2016-11-11',
    '2016-11-16',
    '2016-11-27',
    '2017-01-28',
    '2017-03-12'
)


class DataProcessor:

    def __init__(self):
        self.df = pd.read_csv(raw_path.get("Hackathon_DataSet_OctApr.txt"), sep='\t')

    @staticmethod
    def merge_data_parts():
        part_1 = pd.read_csv(raw_path.get("Hackathon_DataSet_OctApr_Part1.txt"), sep='\t').drop('Id', 1).drop(
            'hackathon4',
            1).drop(
            'PIIntTSTicks', 1).drop('PIIntShapeID', 1)
        part_2 = pd.read_csv(raw_path.get("Hackathon_DataSet_OctApr_Part2.txt"), sep='\t').drop('Id', 1).drop(
            'hackathon4',
            1).drop(
            'PIIntTSTicks', 1).drop('PIIntShapeID', 1)
        part_2 = part_2.dropna(axis=1)
        merged = part_1.merge(part_2, on='TimeStamp', how='inner')
        merged['TimeStamp'] = pd.to_datetime(merged['TimeStamp'])
        merged.to_csv(raw_path.get() + "Hackathon_DataSet_OctApr.txt", index=False, sep='\t')

    def add_days_to_timestamp(timestamp, days=1, format='%Y-%m-%d %H:%M:%S'):
        timestamp_dt = datetime.strptime(timestamp, format)
        timestamp_dt += timedelta(days=days)
        return timestamp_dt.strftime(format)

    def visualizer(self, *cols):
        cols = list(cols)
        df = self.df.copy()
        df = df[['TimeStamp'] + list(cols)]

        window = 24 * 120 + 1
        for col in list(cols):
            try:
                df[col] = df[col].rolling(window).mean()
            except:
                pass

        # df = df.dropna()

        print(df)

        fig, ax = plt.subplots()
        df.plot(kind='line', x='TimeStamp', y=cols, figsize=(40, 10), ax=ax, x_compat=True, linewidth=1)

        df = df.dropna(axis=1)
        ax.set_axisbelow(True)

        def format_func(value, tick_number):
            return df.TimeStamp[value]

        for error_date in error_dates:
            try:
                value = df.query('TimeStamp.str.contains("{}")'.format(error_date)).head(1).index.item()
                # value = df[df['TimeStamp']==error_date].index.item()
                plt.axvspan(value, value + 2 * 60 * 24, facecolor='#2ca02c', alpha=0.5)
            except:
                pass

        majorLocator = MultipleLocator(4)
        majorFormatter = FuncFormatter(format_func)
        minorLocator = MultipleLocator(1)

        ax.xaxis.set_major_locator(majorLocator)
        ax.xaxis.set_major_formatter(majorFormatter)
        ax.xaxis.set_minor_locator(minorLocator)

        major_ticks = np.arange(0, len(df), 2 * 60 * 24)
        minor_ticks = np.arange(0, len(df), 120 * 6)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        # ax.set_yticks(major_ticks)
        # ax.set_yticks(minor_ticks, minor=True)

        plt.xticks(rotation=90)
        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        return plt

    def visualizer2(self, *cols):
        cols = list(cols)
        df = self.df.copy()
        df = df[['TimeStamp'] + list(cols)]

        window = 2 * 120 + 1
        for col in list(cols):
            try:
                df[col] = df[col].rolling(window).mean()
            except:
                pass

        # df = df.dropna()
        sdeviation = df.std()
        avg = df.mean(numeric_only=True)
        cols = list(df.select_dtypes(include=['float64', 'int64']))
        fifth = df.copy()
        for i in cols:
            print(i)

            fifth[i] = abs(abs(fifth[i] - avg[i]) % sdeviation[i])
        df = fifth
        print(df)

        fig, ax = plt.subplots()
        df.plot(kind='line', x='TimeStamp', y=cols, figsize=(40, 10), ax=ax, x_compat=True, linewidth=1)

        df = df.dropna(axis=1)
        ax.set_axisbelow(True)

        def format_func(value, tick_number):
            return df.TimeStamp[value]

        for error_date in error_dates:
            try:
                value = df.query('TimeStamp.str.contains("{}")'.format(error_date)).head(1).index.item()
                # value = df[df['TimeStamp']==error_date].index.item()
                plt.axvspan(value, value + 2 * 60 * 24, facecolor='#2ca02c', alpha=0.5)
            except:
                pass

        majorLocator = MultipleLocator(4)
        majorFormatter = FuncFormatter(format_func)
        minorLocator = MultipleLocator(1)

        ax.xaxis.set_major_locator(majorLocator)
        ax.xaxis.set_major_formatter(majorFormatter)
        ax.xaxis.set_minor_locator(minorLocator)

        major_ticks = np.arange(0, len(df), 2 * 60 * 24)
        minor_ticks = np.arange(0, len(df), 120 * 6)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        # ax.set_yticks(major_ticks)
        # ax.set_yticks(minor_ticks, minor=True)

        plt.xticks(rotation=90)
        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        return plt

    def visualizer_sum(self, *cols):
        cols = list(cols)
        df = self.df.copy()

        df = df.assign(**{'sum': 0})

        window = 2 * 120 + 1
        for col in list(cols):
            pass
        try:
            # print(type(df[col]))
            # df[sum] = df[col] + df[sum]
            df['sum'] = df.sum(axis=0)
        except:
            pass

        # df = df.dropna()
        cols = ['sum']
        df = df[['TimeStamp'] + list(['sum'])]
        print(df)

        fig, ax = plt.subplots()
        df.plot(kind='line', x='TimeStamp', y=cols, figsize=(40, 10), ax=ax, x_compat=True, linewidth=1)

        df = df.dropna(axis=1)
        ax.set_axisbelow(True)

        def format_func(value, tick_number):
            return df.TimeStamp[value]

        for error_date in error_dates:
            try:
                value = df.query('TimeStamp.str.contains("{}")'.format(error_date)).head(1).index.item()
                # value = df[df['TimeStamp']==error_date].index.item()
                plt.axvspan(value, value + 2 * 60 * 24, facecolor='#2ca02c', alpha=0.5)
            except:
                pass

        majorLocator = MultipleLocator(4)
        majorFormatter = FuncFormatter(format_func)
        minorLocator = MultipleLocator(1)

        ax.xaxis.set_major_locator(majorLocator)
        ax.xaxis.set_major_formatter(majorFormatter)
        ax.xaxis.set_minor_locator(minorLocator)

        major_ticks = np.arange(0, len(df), 2 * 60 * 24)
        minor_ticks = np.arange(0, len(df), 120 * 6)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        # ax.set_yticks(major_ticks)
        # ax.set_yticks(minor_ticks, minor=True)

        plt.xticks(rotation=90)
        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        return plt
