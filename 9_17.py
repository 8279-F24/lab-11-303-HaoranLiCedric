def contact_lis():
    contacts = {}
    entry = input()
    entries = entry.split()
    for pair in entries:
        name,number = pair.split(",")
        contacts[name] = number


    name_s = input()
    print(contacts[name_s])
contact_lis()
        