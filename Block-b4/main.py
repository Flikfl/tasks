

def great_ruler(wars: list) -> bool:

    for _, result in wars:
        match result:
            case 'поражение':
                return False
            case _:
                continue

    return True

