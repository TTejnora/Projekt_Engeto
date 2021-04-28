import requests
import os
import csv
import sys
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor

def check_output_file (sysargv : str) -> bool:
    # raise error if the argument doesnt contain '.' + csv format
    assert '.' in sysargv , 'Given output file has not .csv type. Program terminated.'
    name = sysargv.split('.').pop()
    assert name == 'csv', 'Given output file has not csv type. Program terminated.'
    return

def process_sysargv () :
    # check sys.argv and returns list with district link and output file
    sysargv = sys.argv[1:]
    assert len(sysargv) == 2 , 'Exactly 2 arguments to be entered. Program terminated.'
    output_file = sysargv[1]
    check_output_file(output_file) # checking if the output file has proper format
    first_arg = sysargv[0].strip("'")
    return first_arg,output_file

def stahni_html(starting_url):
    #download the html from given URL, if not accessible, raise the Error
    r = requests.get(starting_url)
    if r.status_code != 200:
        raise RuntimeError("The reference %s returned status %d. Data not donwloaded. Program stops" %
                           (starting_url, r.status_code))
    html = r.text
    return html

def najdi_odkazy_level2(starting_url, link_selektor) -> list : # returns list of lists
    # function searching given location to obtain all district codes and their links to summary
    html = stahni_html(starting_url)
    soup = BeautifulSoup(html, "html.parser")
    odkazy = []
    #structure of page is that every 1st line contains the info we need.
    for index,a_elem in enumerate(soup.find_all(link_selektor),start = 1):
        if index % 3 == 1 and not ('-' in a_elem.contents[0]):
            # the reference is only particular and needs to be join with the basic page reference.
            # We cannot use the inserted link
            odkazy.append([a_elem.text,BASIC+a_elem.contents[0]['href']])
    return odkazy

def extract_table (href : str  ) -> list:
    # from given reference download all the tables = class .table and put them in the list, which is returned
    def get_name(html_local):  # the only way found to get the location name
        soup_local = BeautifulSoup(html_local, "html.parser") # I didnt know how to transfer the BeautifulSoup object in
        vse = soup_local.find_all('h3')
        for item in vse:
            a = item.text.split(':')
            if 'Obec' in a[0]:
                obec = a[1].strip(' "\n"')
        return obec
    # from given reference download all the tables = class .table and put them in the list, which is returned
    html = stahni_html(href)
    district_name = get_name(html)
    soup = BeautifulSoup(html, "html.parser")
    tables = []
    #using Extractor to get tables from the html code
    for a_elem in soup.select('.table'):
        extractor = Extractor(a_elem)
        extractor.parse()
        tables.append(extractor.return_list())
    return tables,district_name

def get_result(district_code :  str, href : str ):
    # downloading the tables from the given reference and returning requested values
    # in list to be saved in the output file
    tables,target = extract_table(href) # getting the tables and district name
    strany = []
    output_list = [district_code, target]
    for index, line in enumerate(tables):
        if index == 0: # the first part of searched values
            output_list.append(''.join(line[2][3].split()))
            output_list.append(''.join(line[2][4].split()))
            output_list.append(''.join(line[2][7].split()))
        else:
            for section in line:    # extracting the parties into the list from tables left
                if section[0].isdigit():
                    strany.append(section[1])
    strany.pop(0) # removing the first line with digit, which is not referring to a party
    output_list.extend(strany) # adding parties
    return output_list

def write_result(data_list : list , output_path : str):
    #writing into the csv file
    print(f'Saving results to {output_path}')
    with open(output_path, 'w', newline='', encoding="utf-8") as file:
        f_writer = csv.writer(file)
        f_writer.writerows(data_list)
    return

def main():
# checking if the output file has csv format
    url,output_file = process_sysargv()
# the verification of link reference will be when trying to donwload the data
# searching the first level of page for the district and collecting found districts and their href into the level 2
    level2 = najdi_odkazy_level2(url, 'td')
    print(f"Downloaded data from from {url}")
#header for csv file
    to_csv = [['kód obce','název obce',"voliči v seznamu","vydané obálky","platné hlasy","kandidující strany"]]
    for item in level2 :
        vloz = get_result(*item)
        to_csv.append(vloz)
    write_result(to_csv,output_file)
    print("Completed.")

# globální proměnná pro skládání s linkem v odkazech
BASIC = 'https://volby.cz/pls/ps2017nss/'
if __name__ == "__main__":
    main()


