
def get_and_process_data() -> dict[str, int]:
    data: dict = {}
    
    while True:
        user_input: str = input()

        if user_input == 'END':
            break

        name, count = user_input.strip().split(',')

        if data.get(name) == None:
            data[name] = int(count)
        else:
            data[name] += int(count)

    return data


def get_max(data: dict) -> list[str, int]:
    max_value = max(data.values())

    for name in data:
        if data.get(name) == max_value:
            return [name, max_value]

def main() -> None:
    data: dict[str, int] = get_and_process_data()
    name, count = get_max(data)
    print(f'{name} {count}')
    

if __name__ == "__main__":
    main()

