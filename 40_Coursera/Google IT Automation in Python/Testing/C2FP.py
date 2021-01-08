#!/usr/bin/env python3

import csv
import re
import operator


def extract_regex_syslog(syslog):

    """This function read a syslog file then uses regex to group and match the INFO logs and ERROR
    logs, it stores them in two lists and returns the two lists"""
    # Var Init
    line_info = []
    line_error = []

    with open(syslog, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'.*(INFO).*[\w ]*.*\(([\w .]*)\)', line) is not None:
                line_info.append(re.search(r'.*(INFO).*[\w ]*.*\(([\w .]*)\)', line))
            if re.search(r'.*(ERROR)(.+[\w].*)\(([\w .]*)\)', line) is not None:
                line_error.append(re.search(r'.*(ERROR)(.+[\w].*)\(([\w .]*)\)', line))
            else:
                continue
    f.close()
    return line_error, line_info


def create_dictionary(line_error, line_info):
    """This function takes two lists of regex objects as inputs, then process
    them to convert to dictionaries to count the unique occurences of ERROR and
    ERROR for each user (STAT), as well the top errors, and then tranforms them to list
    to dict in roder to add the desired Keys"""

    # Init variables
    dict_error = {}
    dict_error_csv = {}
    dict_stat = {}
    dict_stat_csv = {}
    list_error = []
    list_stat = []
    KEYS_ERROR = ["Error", "Count"]
    KEYS_STAT = ["Username", "INFO", "ERROR"]

    # Lists of Regex objects are transformed into Dictionaries
    # Error list to Dict_Error
    for line in line_error:
        # Form dictionary for errors
        if line.group(2).strip() not in dict_error.keys():
            dict_error[line.group(2).strip()] = 1
        elif line.group(2).strip() in dict_error.keys():
            dict_error[line.group(2).strip()] += 1
        else:
            pass
        # Form dictionary stat with ERRORS
        if line.group(3).strip() not in dict_stat.keys() and dict_stat.values() is None:
            dict_stat[line.group(3)] = [0, 1]
        elif line.group(3).strip() not in dict_stat.keys() and dict_stat.values() is not None:
            dict_stat[line.group(3)] = [0, 1]
        elif line.group(3).strip() in dict_stat.keys() and dict_stat.values() is not None:
            dict_stat[line.group(3)][1] += 1
        else:
            pass


    # Update dictionary stat with INFO
    for line in line_info:
        if line.group(2).strip() not in dict_stat.keys() and dict_stat.values() is None:
            dict_stat[line.group(2).strip()] = [1, 0]
        elif line.group(2).strip() not in dict_stat.keys() and dict_stat.values() is not None:
            dict_stat[line.group(2).strip()] = [1, 0]
        elif line.group(2).strip() in dict_stat.keys() and dict_stat.values() is not None:
            dict_stat[line.group(2).strip()][0] += 1
        else:
            continue


    # Sort Dictionaries is transformed into List
    list_error = sorted(dict_error.items(), key=operator.itemgetter(1), reverse=True)
    list_stat = sorted(dict_stat.items(), key=operator.itemgetter(0))

    # Iterate on KEYS_ERROR and list of error to transform into dict
    dict_error_csv = dict.fromkeys(KEYS_ERROR)
    for key in dict_error_csv.keys():
        for error, count in list_error:
            if key == "Error":
                if error not in dict_error_csv.values() and dict_error_csv[key] is None:
                    dict_error_csv[key] = [error]
                elif error not in dict_error_csv.values() and dict_error_csv[key] is not None:
                    dict_error_csv[key].append(error)
                else:
                    continue
            if key == "Count":
                if dict_error_csv[key] is None:
                    dict_error_csv[key] = [count]
                elif dict_error_csv[key] is not None:
                    dict_error_csv[key].append(count)
                else:
                    continue

    # Iterate on KEYS_STAT and list of stat to transform into dict stat
    dict_stat_csv = dict.fromkeys(KEYS_STAT)
    for key in dict_stat_csv.keys():
        for user, count in list_stat:
            if key == "Username":
                if dict_stat_csv[key] is None:
                    dict_stat_csv[key] = [user]
                elif dict_stat_csv[key] is not None:
                    dict_stat_csv[key].append(user)
                else:
                    continue
            if key == "ERROR":
                if dict_stat_csv[key] is None:
                    dict_stat_csv[key] = [count[1]]
                elif dict_stat_csv[key] is not None:
                    dict_stat_csv[key].append(count[1])
                else:
                    pass
            if key == "INFO":
                if dict_stat_csv[key] is None:
                    dict_stat_csv[key] = [count[0]]
                elif dict_stat_csv[key] is not None:
                    dict_stat_csv[key].append(count[0])
                else:
                    pass
    ld_error = [dict(zip(dict_error_csv, t)) for t in zip(*dict_error_csv.values())]
    ld_stat = [dict(zip(dict_stat_csv, t)) for t in zip(*dict_stat_csv.values())]
    return ld_error, ld_stat


def create_csv_files(dict_error_csv, dict_stat_csv):
    with open("error_message.csv", mode='w+') as f:
        fieldnames = ['Error', 'Count']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dict_error_csv)
    f.close()
    with open("user_statistics.csv", mode='w+') as f:
        fieldnames = ['Username', 'INFO', 'ERROR']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dict_stat_csv)
    f.close()
    return None


if __name__ == "__main__":
    line_error, line_info = extract_regex_syslog("syslog.log")
    dict_error, dict_stat = create_dictionary(line_error, line_info)
    create_csv_files(dict_error, dict_stat)
