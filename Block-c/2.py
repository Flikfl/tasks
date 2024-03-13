def get_data() -> list[list, int]:
    data: dict = {}
    politicians: list[list[str, int]] = []
    
    while True:
        user_input = input()

        if user_input == 'END':
            break

        name, income = user_input.strip().split(',')

        if data.get(name) == None:
            data[name] = int(income)
        else:
            data[name] += int(income)
        
    max_income = int(input())

    for name, income in data.items():
        politicians.append([name, income])
    
    return [politicians, max_income]

def proccess_data(politicians: list, max_income: int) -> list[str]:
    violators: list[str] = []

    for politician, income in politicians:
        if income > max_income:
            violators.append(politician)

    return violators


def main() -> None:
    politicians, max_income = get_data()
    violators = proccess_data(politicians, max_income)
    
    result = ', '.join(violators)
    print(result)

if __name__ == "__main__":
    main()