

def get_and_process_data() -> dict[str, int]:
    data: dict[str, int] = {}
    
    while True:
        user_input: str = input()

        if user_input == 'END':
            break

        group_name, date = user_input.strip().split(', ')

        if data.get(group_name) == None:
            if date.split('.')[-1] == '2023':
                data[group_name] = 1
        else:
            data[group_name] += 1

    return data

def get_max(data: dict) -> list[str, int]:
    max_value = max(data.values())

    for group_name in data:
        if data.get(group_name) == max_value:
            return [group_name, str(max_value)]


def main() -> None:
    data = get_and_process_data()
    result = ' '.join(get_max(data))

    print(result)

if __name__ == "__main__":
    main()