from db import DB
from excel_pds_tool import ExcelPandasTool
import os
from refine_type.attribute_enum import AttributeEnum


def search_xlsx(attr):

    xlsx_list = list()
    file_names = os.listdir()
    auto_refined_file = attr.value + ".xlsx"

    for filename in file_names :
        if "_compare" not in filename:
            if filename.endswith(".xlsx") and filename.startswith(attr.value):
                if filename == auto_refined_file:
                    xlsx_list.insert(0, filename)
                else:
                    xlsx_list.append(filename)
    return xlsx_list


def get_data():

    result = list()
    # for r in DB().get_procedure(sql=procedure_dict['sql'], argv=procedure_dict['argv']):
    #     if attribute_type in [AttributeEnum.CEO]:
    #         data = PersonType(unrefined_value=r['template_value'], attribute_type=attribute_type).get()
    #         if data is not None:
    #             row = r
    #             for idx in range(len(data[0])) :
    #                 row.update(display_name=data[0][idx])
    #                 row.update(title=data[1][idx])
    #                 result.append(row.copy())
    return result


if __name__ == '__main__':

    # for attribute names
    for attr in AttributeEnum:
        excel_list = search_xlsx(attr)

        if type(excel_list) is list and len(excel_list) > 0:
            ExcelPandasTool(file_name='{}_compare.xlsx'.format(attr.value)).write_compare_excel(excel_list)
            #ExcelPandasTool(file_name='{}_compare.xlsx'.format(attr.value)).write_compare_excel(excel_list, get_data())



