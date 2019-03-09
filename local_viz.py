from bhp_sep import dataset_processor as dp
from bhp_sep.dataset_processor import DataProcessor

DP=DataProcessor()

def get_headings_by_text(text=None):
    return [heading for heading in dp.headings if text in heading]

# from bhp_sep.dataset_processor import DataProcessor
#
# flow_rate = [dp.COL_21_FQI_10518_01_NetRate_PV,
#              dp.COL_21_FT_40518_03_Gross_Volume_Flow_Rate,
#              dp.COL_30_FT_69521_01_PV_Flotation_Cell_Prod_Wtr_To_Ovbrd,
#              dp.COL_30_FT_19107_01_PV_2nd_Stg_Hydrocyclone_Inlet]
#
# psi = [heading for heading in dp.headings if 'Psi' in heading]
# temperature = [heading for heading in dp.headings if 'DegF' in heading]


HD_Temperature = '(DegF)'
HD_PSIG = 'PSIG'
HD_PSID = 'PSID'
HD_PERCENTAGE = '(%)'


plt = DP.visualizer(*get_headings_by_text(HD_Temperature))
plt.tight_layout()
plt.savefig('temp.png')
plt.show()
