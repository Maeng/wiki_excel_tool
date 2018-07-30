# wiki_excel_tool

 The tool compares two excel files in same attribute and make xlsx file including the result of compare.

 같은 어트리뷰트에 해당하는 두 엑셀 파일을 비교하고, 결과를 xlsx 파일로 출력하는 툴입니다.
 
 Codes are based on wiki_refine_tool and the point is excel_pds_tool.py
 
 코드의 베이스는 wiki_refine_tool이며 주요 부분은 excel_pds_tool 코드 부분입니다.
 
 After the work changed, The plan will include like these; compare excel file and database table, print the result of comparing several files, highlight of the difference between files, change the excel files directoroy. 
 
 업무 변경 후 추가될 것이 있다면, 데이터베이스와의 비교, 여러 파일의 비교 결과, 차이가 있는 부분에 대한 하이라이트, 파일 디렉토리 변경 등이 있겠습니다.

 The standard input and output file of this codes are CEO refined file. So, need to modify variable and paremeter as consider other attributes.
 (ex: display_name to refine_value)
 
 현재 코드는 ceo 정제 파일을 기준으로 하였기 때문에, 다른 어트리뷰트를 고려하여 변수 및 파라미터를 수정할 필요가 있습니다.

  <h2>run</h2>
 <b>search_xlsx</b> : 
 Read directory and append the file names to xlsx_list which include attribute value in file name.
 (Exclude _compare.xlsx file)
 (auto refined data in index 0)
 
  어트리뷰트 입력값을 파일명에 포함한 xlsx 포맷의 파일을 xlsx_list에 추출하여 list로 리턴합니다.
  _compare 파일은 결과 파일임으로 제외합니다.
 (index 0에는 auto refined data가 들어가도록 함)
  ```python
 def search_xlsx(attr):
    ...
    return xlsx_list
 ```

<b>Call tool</b>
```python 
ExcelPandasTool(file_name='{}_compare.xlsx'.format(attr.value)).write_compare_excel(excel_list)
```


 <h2>excel_pds_tool</h2>
 
 <b>get_dict_from_df</b> : 
 Input dataframe and output dictionary based on rows
 
 데이터프레임 입력, 디렉터리 출력 (행 기준)
 ```python
def get_dict_from_df(df):
    return df.to_dict('records')
 ```
 
 <b>write_compare_excel</b> : xlsx_list loop -> append sheets include original data from xlsx files

 ```python
def write_compare_excel(self, excel_file_list):
    ...
 ```
 Some rows skip the value in page_title, template_name, template_key, template_value.
 (Especially data refined by person)
 So need to fill entire data to compare each rows.
 
 몇 행은 page_title, template_name, template_key, template_value을 생략한 경우가 있습니다.(사람에 의해 정제된 파일)
 
 하기 for loop는 전체 데이터를 채워 각 행을 비교하기 위한 것입니다.
```python
for df in df_dropped_list[1:]: ...
```

df_final is the concat of entire read data

데이터 전체 붙인 결과 df_final
```python
df_final = pd.concat([df_dropped_list[0].set_index('page_id'), df_dropped_list[1].set_index('page_id')],
                             keys=['Auto', 'Original']).sort_values(by=['page_id', 'display_name'])
```

cp~ = copy of df_final

cp1 = remove duplicated values once(consequently, be union) and sorted by page_id, display_name

중복된 값 한번 제거(결과적으로 합집합) 및 page_id, display_name으로 소팅
```python
cp1 = cp1.drop_duplicates().sort_values(by=['page_id', 'display_name'])
```
cp2 = keep='last' return last duplicated value as TRUE(accordingly, be intersection) and sorted by page_id, display_name

keep='last' 는 중복의 마지막만 True로 리턴(결과적으로 교집합) 및 page_id, display_name으로 소팅

```python
cp2['is_duplicate'] = cp2.duplicated(keep='last')
cp2 = cp2[cp2.is_duplicate].drop(columns=['is_duplicate']).sort_values(by=['page_id', 'display_name'])
```
cp3 = keep='False' return all duplicated value as TRUE.
/ Choose only False values then, be union set of difference set.
Also, sorted by page_id, display_name

keep='False' 는 중복하는 모든 값을 True로 리턴
FALSE만 뽑아낼 시 차집합의 통합. 또한 page_id, display_name으로 소팅

```python
cp3['is_duplicate_false'] = cp3.duplicated(keep=False)
cp3 = cp3[~cp3.is_duplicate_false].drop(columns=['is_duplicate_false']).sort_values(by=['page_id', 'display_name'])
```

As Result, {}_compare.xlsx file includes 5 sheets.
 - original Auto_refined data / 자동 정제된 오리지널 데이터
 - original refined data before / 이전에 정제되었던 데이터
 - total concat of two data / 상기 두 데이터 이어붙인 데이터
 - the union of two data / 상기 두 데이터의 합집합 
 - the intersection of two data / 상기 두 데이터의 교집합 
 - the set of subtract intersection from union / 합집합 - 교집합
  
  In Excel, It's possible to check difference set (A-B, B-A) using filter function
  
  엑셀에서 마지막 시트에 필터 기능 사용시 각 데이터의 차집합 확인 가능