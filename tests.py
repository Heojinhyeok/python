import json

def load_json_key(data, key):
    # input: json(data), key(dict['key'])
    # output: dict['key']
    # function:
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e

    except Exception as ex:
        print("에러발생 : %s" % ex)
    else:
        return result_dict[key]

def main():
    file = 'file.json'
    jsondata = open(file).read()
    searchkey = 'array'

    searchvalue = load_json_key(jsondata, searchkey)
    print(searchvalue)

if __name__ == '__main__':
    main()
