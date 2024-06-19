import json

def load_json(file_path):
    json_open = open(file_path,'r')
    json_data = json.load(json_open)
    return json_data

def save_json(file_path, data):
    new_json = open(file_path,'w')
    json.dump(data,new_json)
    return

def update_json(data, key, new_value):
    if key in data:
        data[key] = new_value
    else:
        print(f"キー '{key}' が見つかりません。")
    return data

def main():
    file_path = './day17/data.json'
    data = load_json(file_path)
    print("現在のJSONデータ:", data)

    key = input("更新したいキーを入力してください: ")
    new_value = input("新しい値を入力してください: ")

    updated_data = update_json(data, key, new_value)
    save_json(file_path, updated_data)
    print("更新後のJSONデータ:", updated_data)

if __name__ == "__main__":
    main()