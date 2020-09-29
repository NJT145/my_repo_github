import http.client, urllib.request, urllib.parse, urllib.error, base64
from openpyxl.workbook import Workbook
from timeit import default_timer as timer


Ocp_Apim_Subscription_Key = ''

def NoAuth_GetCounties(countryId):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('urgentcargus.azure-api.net')
        conn.request("GET",
                     "/api/NoAuth/GetCounties?countryId="+str(countryId)+"&%s" % params,
                     "{body}",
                     headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data.decode('utf8').replace("'", '"')
    except Exception as e:
        return "Error: {0}".format(e)


def NoAuth_GetLocalities(countryId, countyId):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key,
    }
    params = urllib.parse.urlencode({
    })
    try:

        conn = http.client.HTTPSConnection('urgentcargus.azure-api.net')
        conn.request("GET",
                     "/api/NoAuth/GetLocalities?countryId=" + str(countryId) + "&countyId=" + str(countyId) + "&%s" % params,
                     "{body}",
                     headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data.decode('utf8').replace("'", '"')
    except Exception as e:
        return "Error: {0}".format(repr(e))

def add_row(sheet, row_no, row_list):
    for col in range(1, len(row_list) + 1):
        sheet.cell(row=row_no, column=col, value=row_list[col - 1])

def country_report(countryId):
    wb = Workbook()
    dest_filename = "countryId_"+str(int(countryId))+"_report.xlsx"
    sheet = wb.active
    sheet.title = "County-Locality-countryId_1"
    title_row = ["CountryId",
                 "CountyId", "County_Name", "County_Abbreviation",
                 "LocalityId", "Locality_Name", "Locality_ParentId", "Locality_ParentName",
                 "Locality_ExtraKm", "Locality_InNetwork", "Locality_PostalCode", "Locality_MaxHour"]
    column_count = len(title_row)
    add_row(sheet, 1, title_row)
    row_index = 2

    allCounties = eval(NoAuth_GetCounties(countryId).replace("null,", "None,"))
    for County in allCounties:
        CountyId = County["CountyId"]
        County_Name = County["Name"]
        County_Abbreviation = County["Abbreviation"]
        allLocalities= eval(NoAuth_GetLocalities(countryId,CountyId).replace("null,", "None,"))
        for Locality in allLocalities:
            row_list = [countryId, CountyId, County_Name, County_Abbreviation]
            row_list.append(Locality["LocalityId"])
            row_list.append(Locality["Name"])
            row_list.append(Locality["ParentId"])
            row_list.append(Locality["ParentName"])
            row_list.append(Locality["ExtraKm"])
            row_list.append(Locality["InNetwork"])
            row_list.append(Locality["PostalCode"])
            row_list.append(Locality["MaxHour"])
            add_row(sheet,row_index, row_list)
            row_index += 1
    wb.save(filename=dest_filename)

start = timer()
country_report(1)
end = timer()
print("all done at %.2f seconds" % (end-start))
file_path1 = r"C:\Users\nejat.gunaydin\Desktop\Gls-UrgentCargo (002).xlsx"
file_path2 = r"C:\Users\nejat.gunaydin\Documents\GitHub\private\PyCharm_Projects\countryId_1_report.xlsx"

