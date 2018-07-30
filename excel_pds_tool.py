from db import DB
import pandas as pd
import math

def highlight_cells():
    # provide your criteria for highlighting the cells here
    return ['background-color: yellow']

class ExcelPandasTool:

    def __init__(self, file_name=None):
        self.file_name = file_name

    @staticmethod
    def get_excel(file_name):
        result_list = pd.read_excel(file_name)
        return result_list

    @staticmethod
    def get_dict_from_df(df):
        return df.to_dict('records')

    def write_compare_excel(self, excel_file_list):
        writer = pd.ExcelWriter(self.file_name, engine='xlsxwriter', options={'strings_to_urls': False})

        df_list = list()
        df_dropped_list = list()

        for file in excel_file_list:
            data = self.get_excel(file)
            df = pd.DataFrame(data)
            df_list.append(df)
            df.to_excel(writer, sheet_name="original_" + file, index=False)
            df_dropped = df.drop(columns=['wiki_id', 'detail_info'])
            df_dropped_list.append(df_dropped)

        for df in df_dropped_list[1:]:
            first_series = df.iloc[0]
            for tp, series_in_df in df.iterrows():
                if series_in_df['page_id'] == first_series['page_id']:
                    if type(series_in_df['page_title']) is float and math.isnan(series_in_df['page_title']):
                        series_in_df['page_title'] = first_series['page_title']
                    if type(series_in_df['template_name']) is float and math.isnan(series_in_df['template_name']):
                        series_in_df['template_name'] = first_series['template_name']
                    if type(series_in_df['template_key']) is float and math.isnan(series_in_df['template_key']):
                        series_in_df['template_key'] = first_series['template_key']
                    if type(series_in_df['template_value']) is float and math.isnan(series_in_df['template_value']):
                        series_in_df['template_value'] = first_series['template_value']

                    df.loc[tp] = series_in_df
                else:
                    first_series = series_in_df

        df_final = pd.concat([df_dropped_list[0].set_index('page_id'), df_dropped_list[1].set_index('page_id')],
                             keys=['Auto', 'Original']).sort_values(by=['page_id', 'display_name'])
        df_final.to_excel(writer, sheet_name="총집합")

        cp1 = df_final.copy()
        cp2 = df_final.copy()
        cp3 = df_final.copy()

        cp1 = cp1.drop_duplicates().sort_values(by=['page_id', 'display_name'])
        cp1.to_excel(writer, sheet_name="합집합")

        cp2['is_duplicate'] = cp2.duplicated(keep='last')
        cp2 = cp2[cp2.is_duplicate].drop(columns=['is_duplicate']).sort_values(by=['page_id', 'display_name'])
        cp2.to_excel(writer, sheet_name="교집합")

        cp3['is_duplicate_false'] = cp3.duplicated(keep=False)
        cp3 = cp3[~cp3.is_duplicate_false].drop(columns=['is_duplicate_false']).sort_values(by=['page_id', 'display_name'])
        cp3.to_excel(writer, sheet_name="중복 전부 제거")

        print(len(cp1), len(cp2), len(cp3))
        writer.save()



