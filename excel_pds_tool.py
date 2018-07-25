from db import DB
import pandas as pd
import math


class ExcelPandasTool:

    def __init__(self, file_name=None):
        self.file_name = file_name

    @staticmethod
    def get_excel(file_name):
        result_list = pd.read_excel(file_name)
        return result_list

    # @staticmethod
    # def get_excel(file_name, sheet_name):
    #     result_list = pd.read_excel(file_name, sheet_name)
    #     return result_list

    #data = { 'sheet1' : [ {'column_name' : [ cell1, cell2, cell3.. ],
                        # 'column_name' : [ 0, 1, 2.. ] } ],
            # 'sheet2' : [ {''} ] ...}
    # def write_excel(self, data):
    #     for key in data:
    #         df = pd.DataFrame(data[key])
    #         writer = pd.ExcelWriter('', engine='xlsxwriter')
    #         df.to_excel(writer, sheet_name=key)
    #         writer.save()

    # def write_excel(self, data, sheet_name):
    #     df = pd.DataFrame(data)
    #     writer = pd.ExcelWriter(self.file_name, engine='xlsxwriter', options={'strings_to_urls': False})
    #     df.to_excel(writer, sheet_name=sheet_name, index=False)
    #     writer.save()

    def write_compare_excel(self, excel_file_list):
        writer = pd.ExcelWriter(self.file_name, engine='xlsxwriter', options={'strings_to_urls': False})

        dic_list = list()
        for file in excel_file_list:
            data = self.get_excel(file)
            df = pd.DataFrame(data)
            dic_list.append(df.to_dict(orient='records'))
            df.to_excel(writer, sheet_name="original_" + file, index=False)

        formerdict = dic_list[1][0]
        for dic in dic_list[1][1:]:
            if dic['page_id'] == formerdict['page_id']:
                print(dic)
                if type(dic['page_title']) is float and math.isnan(dic['page_title']) :
                        dic['page_title'] = formerdict['page_title']
                if type(dic['template_name']) is float and math.isnan(dic['template_name']):
                    dic['template_name'] = formerdict['template_name']
                if type(dic['template_key']) is float and math.isnan(dic['template_key']):
                    dic['template_key'] = formerdict['template_key']
                if type(dic['template_value']) is float and math.isnan(dic['template_value']):
                    dic['template_value'] = formerdict['template_value']
            else:
                formerdict = dic


        list1 = dic_list[0]
        #if not set(value.values()).issubset(set(sum([list(x.values()) for x in list(dic.values())], []))):
        #set1 = frozenset(list1.items())
        #set2 = set(dic_list[1])
        #header_list = dic_list[0].keys()

        writer.save()


def get_set_data(data_list):
    result_set = set()
    for r in data_list:
        if r['date'] is not None:
            if r['date'] is not None:
                if type(r['date']) is str:
                    result_set.add((r['page_id'], r['page_title'].replace('_', ' ') if r['page_title'] is not None else 'None', r['date']))
                else:
                    result_set.add((r['page_id'], r['page_title'].replace('_', ' ') if r['page_title'] is not None else 'None', r['date'].strftime('%Y-%m-%d')))
            else:
                result_set.add((r['page_id'], r['page_title'].replace('_', ' ') if r['page_title'] is not None else 'None', 'None'))
    return result_set

if __name__ == '__main__':
    excel_pds_tool = ExcelPandasTool()
    #db_set = get_set_data(DB().select('select * FROM temp_' + attr))

    # original
    excel1 = get_set_data(excel_pds_tool.get_excel('ceo_0704.xlsx', 'refined'))
    # auto refined
    excel2 = get_set_data(excel_pds_tool.get_excel('ceo.xlsx'))

    excel_set = excel1.union(excel2)

    intersection_set = excel1.intersection(excel2)
    #dif_db = db_set.difference(excel_set)
    dif_excel = excel1.difference(excel2)
    cnt = len(intersection_set)

    #TODO create cnt_set from other sets

    excel_tool.write_excel(intersection_set, 'intersection')
    #excel_tool.write_excel(dif_db, 'dif_db')
    excel_tool.write_excel(dif_excel, 'dif_excel')
    #excel_tool.write_excel(cnt_set, 'count')
    excel_tool.write_excel(excel1, 'original_1')
    excel_tool.write_excel(excel2, 'original_1')
