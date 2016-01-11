def uniqueify(listing):
    new_data = []
    urls = []
    for ind,elem in enumerate(listing):
        if not elem in urls:
            urls.append(elem)
            new_data.append(elem)
    return new_data

def dict_uniqueify(listing):
    new_data = []
    urls = []
    for ind,datum in listing:
        if not datum["url"] in urls:
            urls.append(datum["url"])
            new_data.append(datum)
    return new_data

if __name__ == '__main__':
    simple = [1,1,2,3]
    intermediate = ["https://www.vets.gov","https://www.vets.gov","https://www.vets.gov/benefits","https://www.vets.gov"]
    advanced = [
        {"url":"https://www.vets.gov"},
        {"url":"https://www.vets.gov"},
        {"url":"https://www.vets.gov"},
        {"url":"https://www.vets.gov/benefits"},
        {"url":"https://www.vets.gov"}
    ]
    if uniqueify(simple) == [1,2,3]:
        print "works on simple"
    if uniqueify(intermediate) == ["https://www.vets.gov","https://www.vets.gov/benefits"]:
        print "works on intermediate"
    print uniqueify(advanced)
