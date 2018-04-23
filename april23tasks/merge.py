file_one = "HDFC_companies.csv"
file_two = "icici_final.csv"
file_three = open("companies_final.csv", 'w')
entries_file_one = {}
entries_list = []

file_one_cursor = open(file_one)
file_two_cursor = open(file_two)

for line in file_one_cursor:
    line_to_lower = line.lower();
    line_from_split = line_to_lower.split(",");
    company_name = line_from_split[0]
    if company_name not in entries_file_one:
        entries_file_one[company_name] = line_from_split
    #print(entries_file_one[company_name][0])

    for line2 in file_two_cursor:
        line_to_lower2 = line2.lower();
        line_from_split2 = line_to_lower2.split(",")
        company_name2 = line_from_split2[0]
        #print(company_name2)

        if company_name2 in entries_file_one[company_name]:
            if len(entries_file_one[company_name]):
                print "hi"
                entries_file_one[company_name].extend(line_from_split2)
            entries_list = entries_file_one[company_name]
            print entries_list
            file_three.write("%s\t" % entries_list[0])
            file_three.write("%s\t" % entries_list[1])
            file_three.write("%s\t" % entries_list[2])
            file_three.write("%s\t" % entries_list[3])
            break
        break








