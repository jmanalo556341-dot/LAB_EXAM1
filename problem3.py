def get_network(number):

    networks = {
        "Smart": ["13", "14", "20", "21", "28", "29", "30"],
        "TNT": ["09", "10", "11", "12", "18", "19"],
        "Sun": ["22", "23", "32", "33"],
        "Globe": ["15", "16", "17", "25", "26", "27"],
        "TM": ["03", "04", "05", "06", "07"],
        "Red": ["01", "02", "24"],
        "Dito": ["91", "92", "93", "94", "95", "96", "97", "98"]
    }


    if len(number) != 11 or not number.isdigit() or not number.startswith("09"):
        return "Invalid mobile number"


    key_digits = number[2:4]


    for network, codes in networks.items():
        if key_digits in codes:
            return f"The network of the mobile number is {network}"

    return "Unknown network"

    number = input("Enter a mobile number: ")
    print(get_network(number))
