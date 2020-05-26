import requests
import xlrd
import json
import xlwt
from xlrd import open_workbook

def xlsx_open(filepath):
    book = xlrd.open_workbook(filepath)
    return book

def xlsx_getRow(sheet, row):
    object = {}
    object["method"] = sheet.cell_value(row, 2)
    object["host"] = sheet.cell_value(row, 3)
    object["path"] = sheet.cell_value(row, 4)
    object["url"] = object["host"] + object["path"]
    object["params"] = sheet.cell_value(row, 5)
    object["header"] = sheet.cell_value(row, 6)
    object["code"] = sheet.cell_value(row, 7)
    object["expected_code"] = sheet.cell_value(row, 8)
    if object["header"] == "":
        object["header"] = None
    return object

def xlsx_request(object):
    try:
        if object["method"] == "post":
            response = requests.post(object["url"], data=json.loads(object["params"]), headers=object["header"], cookies=object["cookies"])
            result = response.json()
        elif object["method"] == "get":
            response = requests.get(object["url"], object["params"], headers=object["header"], cookies=object["cookies"])
            result = response.json()
        else:
            print("Unknown method " + object["method"])
    except requests.exceptions.ConnectTimeout as e:
        result = {object["code"]: "timeout"}

    print(result)
    return result

def xlsx_set(sheet, row, col, value, red=False):
    style = "font:colour_index red;"
    if red == False:
        sheet.write(row, col, value)
    else:
        sheet.write(row, col, value, xlwt.easyxf(style))

def xlsx_save(book, filepath):
    book.save(filepath)

def dosheet(brd, bwt, sheetIndex, cookies=None):
    brd_sheet = brd.sheets()[sheetIndex]
    bwt_sheet = bwt.get_sheet(sheetIndex)
    count = brd_sheet.nrows
    for i in range(1, count):
        object = xlsx_getRow(brd_sheet, i)
        object["cookies"] = cookies
        result = xlsx_request(object)

        if result.get(object["code"]) == object["expected_code"]:
            xlsx_set(bwt_sheet, i, 9, "pass", False)
            xlsx_set(bwt_sheet, i, 10, result[object["code"]], False)
        else:
            xlsx_set(bwt_sheet, i, 9, "fail", True)
            xlsx_set(bwt_sheet, i, 10, result[object["code"]], False)

