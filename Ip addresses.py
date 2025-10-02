def is_valid_part(part):
    try:
        #Setting number as a int
        number = int(part)
    except ValueError:
        #returns any non ints
        return False
#Only lets number above 0 and number that do not go above 255
    if number < 0 or number > 255:
        return False
    #removes leading zero's
    if len(part) > 1 and part[0] == '0':
        return False

    return True
print("is valid part")
print(is_valid_part("255"))
print(is_valid_part("256"))
print(is_valid_part("01"))
print(is_valid_part("0"))
def is_valid_ip(ip):
    #ip split
    parts = ip.split('.')
#if there are not 4 sections, return false
    if len(parts) != 4:
        return False
    for part in parts:
        #Loops through each section and checks it using is_valid_parts
        if not is_valid_part(part):
            return False

    return True
print("is valid ip")
print(is_valid_ip("192.168.1.1"))
print(is_valid_ip("192.168.256.1"))
print(is_valid_ip("192.168.1"))
print(is_valid_ip("192.168.01.1"))
def decimal_to_binary(n):
    if n == 0:
        return "0"
    else:
        result = decimal_to_binary(n // 2) + str(n % 2)
        return result.lstrip("0")
print("decimal to binary")
print(decimal_to_binary(10))
print(decimal_to_binary(255))
print(decimal_to_binary(1))
def binary_to_decimal(b):
    if b == '':
        return 0
    else:
        leftmost_bit = int(b[0])
        return leftmost_bit * (2 ** (len(b) - 1)) + binary_to_decimal(b[1:])
print("Binary to Decimal:")
print(binary_to_decimal("1010"))
print(binary_to_decimal("11111111"))
print(binary_to_decimal("1"))