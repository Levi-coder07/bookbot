def sort_on(dict):
    return dict["num"]
def sum(strings):
    dictionary = {}
    for i in strings:
        i = i.lower()
        if (i in dictionary):
            dictionary[i] = dictionary[i] + 1 
        else:
            dictionary[i] = 1
    list1 = []
    dicts = {"name": 0 ,"num":0}
    for key in dictionary.keys():
        dicts = {"name": 0 ,"num":0}
        dicts["name"] = key
        dicts["num"] = dictionary[key]

        list1.append(dicts)
    
    list1.sort(reverse=True, key=sort_on)
    print(list1)
    for key in list1:
        if key["name"].isalpha():
            print(f"The '{key['name']}' character was found {key['num']} times")
def main():
    with open("books/frankenstein.txt") as f:
        
        file_contents = f.read()
        
    sum(file_contents)
if __name__ == "__main__":
    main()