from db import DB
import pandas as pd
import numpy as np
import math


def highlight_diff(data, color='yellow'):
    attr = 'background-color: {}'.format(color)
    other = data.xs('First', axis='columns', level=-1)
    return pd.DataFrame(np.where(data.ne(other, level=0), attr, ''),
                        index=data.index, columns=data.columns)


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
                if tp is 935:
                    print('!')
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

        #concat_df = pd.concat(df_dropped_list)
        concat_df = pd.concat([df_dropped_list[0].set_index('page_id'), df_dropped_list[1].set_index('page_id')],
                              keys=['Auto', 'Original'])
        df_final = concat_df.swaplevel()[df_dropped_list[0].columns[1:]]

        df_final.style.apply(highlight_diff, axis=None)
        df_final.to_excel(writer, sheet_name="concat", index=False)

        concat_df.drop_duplicates().sort_values(by=['page_id']).to_excel(writer, sheet_name="합집합", index=False)
        #concat_df.drop_duplicates(['display_name', 'title']).sort_values(by=['page_id']).to_excel(writer, sheet_name="합집합", index=False)

        concat_df['is_duplicate'] = concat_df.duplicated()
        #concat_df['is_duplicate'] = concat_df.duplicated(['display_name', 'title'])
        concat_df[concat_df.is_duplicate].drop(columns=['is_duplicate']).sort_values(by=['page_id']).to_excel(writer, sheet_name="교집합", index=False)

        writer.save()



