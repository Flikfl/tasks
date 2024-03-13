def get_and_process_data() -> dict[str, list[int]]:
    data: dict[str, list[int]] = {}
    
    while True:
        user_input: str = input()

        if user_input == 'СТОП':
            break

        book_name, price = user_input.strip().split('-')

        if data.get(book_name) == None:
            data[book_name] = [int(price)]
        else:
            data[book_name].append(int(price))

    return data

def get_average_price(data: dict[str, list[int]]) -> dict[str, int]:
    
    for k, v in data.items():
        total: int = 0
        for digit in v:
            total += digit
        
        avg_price = round(total/len(v))
        data[k] = avg_price
    
    return data

def get_min_price(data: dict[str, int]) -> list[str, str]:
    values = data.values()
    min_value = min(values)

    for k, v in data.items():
        if v == min_value:
            return [k, str(v)]

def main() -> None:
    data = get_and_process_data()
    data = get_average_price(data)
    book_name, avg_price =  get_min_price(data)
    print(book_name, avg_price)

if __name__ == "__main__":
    main()