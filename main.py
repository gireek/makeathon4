# from threading import Thread
# from server.viz_server import start
#
# Thread(target=start).start()


# from bhp_sep.dataset_processor import DataProcessor
# DataProcessor.merge_data_parts()


# from bhp_sep.dataset_processor import DataProcessor
#
# flow_rate = [dp.COL_21_FQI_10518_01_NetRate_PV,
#              dp.COL_21_FT_40518_03_Gross_Volume_Flow_Rate,
#              dp.COL_30_FT_69521_01_PV_Flotation_Cell_Prod_Wtr_To_Ovbrd,
#              dp.COL_30_FT_19107_01_PV_2nd_Stg_Hydrocyclone_Inlet]
#
# psi = [heading for heading in dp.headings if 'Psi' in heading]
# temperature = [heading for heading in dp.headings if 'DegF' in heading]
#
#





# #
#
# plt = DP.visualizer(*get_headings_by_text(HD_Temperature))
#
# plt.tight_layout()
# plt.savefig('temp.png')
# plt.show()
#
#
#
# # for heading in dp.headings:
# #     try:
# #         plt = DP.visualizer(heading)
# #         cleanString = re.sub('\W+', '_', heading)
# #         plt.savefig(cleanString+".png")
# #         plt.show()
# #     except Exception as e:
# #         print("ERROR: "+heading)
# #         print(e)
