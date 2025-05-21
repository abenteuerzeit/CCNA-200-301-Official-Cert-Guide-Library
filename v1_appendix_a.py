def decimal_to_binary(decimal):
    """Convert decimal to 8-bit binary representation"""
    try:
        decimal = int(decimal)
        if 0 <= decimal <= 255:
            return format(decimal, '08b')
        else:
            return "Error: Decimal value must be between 0-255"
    except ValueError:
        return "Error: Invalid decimal input"

def binary_to_decimal(binary):
    """Convert 8-bit binary to decimal"""
    try:
        # Check if input is valid binary
        if all(bit in '01' for bit in binary) and len(binary) <= 8:
            return str(int(binary, 2))
        else:
            return "Error: Binary must contain only 0s and 1s (max 8 digits)"
    except ValueError:
        return "Error: Invalid binary input"

def hex_to_binary(hex_val):
    """Convert hex to 4-bit binary"""
    try:
        hex_val = hex_val.upper()
        if len(hex_val) == 1 and hex_val in "0123456789ABCDEF":
            decimal = int(hex_val, 16)
            return format(decimal, '04b')
        else:
            return "Error: Hex value must be a single digit (0-9, A-F)"
    except ValueError:
        return "Error: Invalid hex input"

def binary_to_hex(binary):
    """Convert 4-bit binary to hex"""
    try:
        if all(bit in '01' for bit in binary) and len(binary) <= 4:
            # Ensure 4 bits by padding with leading zeros
            padded_binary = binary.zfill(4)
            decimal = int(padded_binary, 2)
            return format(decimal, 'X')  # 'X' gives uppercase hex
        else:
            return "Error: Binary must contain only 0s and 1s (max 4 digits)"
    except ValueError:
        return "Error: Invalid binary input"

def power_of_2(exponent):
    """Calculate 2^exponent"""
    try:
        exponent = int(exponent)
        if 1 <= exponent <= 32:
            return f"{2**exponent:,}"
        else:
            return "Error: Exponent must be between 1-32"
    except ValueError:
        return "Error: Invalid exponent input"

def find_exponent(power):
    """Find x where 2^x equals the given power"""
    try:
        # Remove commas if present
        power_clean = power.replace(',', '')
        power_val = int(power_clean)
        
        # Check if it's a power of 2
        if power_val > 0 and (power_val & (power_val - 1) == 0):  # Bit trick to check if power of 2
            exponent = power_val.bit_length() - 1
            if 1 <= exponent <= 32:
                return str(exponent)
            else:
                return "Error: Result outside range 1-32"
        else:
            return "Error: Not a power of 2"
    except ValueError:
        return "Error: Invalid power input"

def cidr_to_mask(cidr):
    """Convert CIDR prefix to subnet mask"""
    try:
        cidr = int(cidr)
        if 0 <= cidr <= 32:
            # Calculate the mask in binary (32 bits)
            binary_mask = '1' * cidr + '0' * (32 - cidr)
            
            # Convert to dotted decimal
            oct1 = int(binary_mask[0:8], 2)
            oct2 = int(binary_mask[8:16], 2)
            oct3 = int(binary_mask[16:24], 2)
            oct4 = int(binary_mask[24:32], 2)
            
            decimal = f"{oct1}.{oct2}.{oct3}.{oct4}"
            binary_formatted = f"{binary_mask[0:8]} {binary_mask[8:16]} {binary_mask[16:24]} {binary_mask[24:32]}"
            
            return f"Decimal: {decimal}\nBinary: {binary_formatted}"
        else:
            return "Error: CIDR must be between 0-32"
    except ValueError:
        return "Error: Invalid CIDR input"

def mask_to_cidr(mask):
    """Convert subnet mask to CIDR prefix"""
    try:
        # Check if in proper format (x.x.x.x)
        octets = mask.split('.')
        if len(octets) != 4:
            return "Error: Mask must be in format x.x.x.x"
            
        # Convert to binary
        binary = ''
        for octet in octets:
            octet_val = int(octet)
            if 0 <= octet_val <= 255:
                binary += format(octet_val, '08b')
            else:
                return "Error: Each octet must be 0-255"
        
        # Count consecutive 1s from the start
        count = 0
        for bit in binary:
            if bit == '1':
                count += 1
            else:
                break
                
        # Check if valid mask (all 1s followed by all 0s)
        if '01' in binary:
            return "Error: Invalid subnet mask format (must be consecutive 1s followed by 0s)"
            
        return f"CIDR: /{count}"
    except ValueError:
        return "Error: Invalid mask input"

def display_full_table(table_choice):
    """Display the full table based on user choice"""
    if table_choice == '1':
        generate_decimal_binary_table()
    elif table_choice == '2':
        generate_hex_binary_table()
    elif table_choice == '3':
        generate_powers_of_2()
    elif table_choice == '4':
        generate_subnet_masks()

def generate_decimal_binary_table():
    """Generate Table A-1: Decimal-Binary Cross Reference for values 0-255"""
    print("\nTable A-1: Decimal-Binary Cross Reference, Decimal Values 0-255\n")
    
    print("| Decimal Value | Binary Value | Decimal Value | Binary Value | Decimal Value | Binary Value | Decimal Value | Binary Value |")
    print("| ------------- | ------------ | ------------- | ------------ | ------------- | ------------ | ------------- | ------------ |")
    
    # Generate rows for values 0-127
    for i in range(32):
        row = []
        for j in range(4):  # 4 columns
            decimal = i + j * 32  # Calculate decimal value
            binary = format(decimal, '08b')  # Convert to 8-bit binary
            row.extend([str(decimal).ljust(3), binary])
        
        print(f"| {row[0]:13} | {row[1]:12} | {row[2]:13} | {row[3]:12} | {row[4]:13} | {row[5]:12} | {row[6]:13} | {row[7]:12} |")
    
    # Generate rows for values 128-255
    for i in range(32):
        row = []
        for j in range(4):  # 4 columns
            decimal = i + j * 32 + 128  # Calculate decimal value (starting from 128)
            binary = format(decimal, '08b')  # Convert to 8-bit binary
            row.extend([str(decimal).ljust(3), binary])
        
        print(f"| {row[0]:13} | {row[1]:12} | {row[2]:13} | {row[3]:12} | {row[4]:13} | {row[5]:12} | {row[6]:13} | {row[7]:12} |")

def generate_hex_binary_table():
    """Generate Table A-2: Hex-Binary Cross Reference"""
    print("\nTable A-2: Hex-Binary Cross Reference\n")
    
    print("| Hex | 4-Bit Binary |")
    print("| --- | ------------ |")
    
    hex_chars = "0123456789ABCDEF"
    for char in hex_chars:
        decimal = int(char, 16)  # Convert hex to decimal
        binary = format(decimal, '04b')  # Convert to 4-bit binary
        print(f"| {char:3} | {binary:12} |")

def generate_powers_of_2():
    """Generate Table A-3: Powers of 2, from 2^1 through 2^32"""
    print("\nTable A-3: Powers of 2\n")
    
    # Calculate all powers to determine max width
    powers = [(i, 2**i) for i in range(1, 33)]
    max_power_width = max(len(f"{p[1]:,}") for p in powers)
    
    print("| X  | 2^X" + " " * (max_power_width-3) + " | X  | 2^X" + " " * (max_power_width-3) + " |")
    print("| -- | " + "-" * max_power_width + " | -- | " + "-" * max_power_width + " |")
    
    # Generate two columns (1-16 and 17-32)
    for i in range(1, 17):
        power1 = 2 ** i
        power2 = 2 ** (i + 16)
        
        power1_str = f"{power1:,}".ljust(max_power_width)
        power2_str = f"{power2:,}".ljust(max_power_width)
        
        print(f"| {i:2} | {power1_str} | {i+16:2} | {power2_str} |")

def generate_subnet_masks():
    """Generate Table A-4: All 33 possible subnet masks"""
    print("\nTable A-4: All Subnet Masks\n")
    
    print("| Decimal            | Prefix | Binary                                  |")
    print("| ------------------ | ------ | --------------------------------------- |")
    
    for cidr in range(33):
        # Calculate the mask in binary (32 bits)
        binary_mask = '1' * cidr + '0' * (32 - cidr)
        
        # Convert to dotted decimal
        oct1 = int(binary_mask[0:8], 2)
        oct2 = int(binary_mask[8:16], 2)
        oct3 = int(binary_mask[16:24], 2)
        oct4 = int(binary_mask[24:32], 2)
        
        decimal = f"{oct1}.{oct2}.{oct3}.{oct4}"
        prefix = f"/{cidr}"
        binary_formatted = f"{binary_mask[0:8]} {binary_mask[8:16]} {binary_mask[16:24]} {binary_mask[24:32]}"
        
        print(f"| {decimal:18} | {prefix:6} | {binary_formatted:39} |")

def main():
    while True:
        print("\n===== NUMERIC REFERENCE LOOKUP TOOL =====")
        print("1. Decimal-Binary Conversion")
        print("2. Hex-Binary Conversion")
        print("3. Powers of 2")
        print("4. Subnet Masks")
        print("5. Display Full Table")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            print("\n--- Decimal-Binary Conversion ---")
            print("a. Decimal to Binary")
            print("b. Binary to Decimal")
            sub_choice = input("Enter your choice (a/b): ").lower()
            
            if sub_choice == 'a':
                decimal = input("Enter decimal value (0-255): ")
                result = decimal_to_binary(decimal)
                print(f"Result: {result}")
            elif sub_choice == 'b':
                binary = input("Enter binary value (up to 8 bits): ")
                result = binary_to_decimal(binary)
                print(f"Result: {result}")
            else:
                print("Invalid choice")
                
        elif choice == '2':
            print("\n--- Hex-Binary Conversion ---")
            print("a. Hex to Binary")
            print("b. Binary to Hex")
            sub_choice = input("Enter your choice (a/b): ").lower()
            
            if sub_choice == 'a':
                hex_val = input("Enter hex digit (0-9, A-F): ")
                result = hex_to_binary(hex_val)
                print(f"Result: {result}")
            elif sub_choice == 'b':
                binary = input("Enter binary value (up to 4 bits): ")
                result = binary_to_hex(binary)
                print(f"Result: {result}")
            else:
                print("Invalid choice")
                
        elif choice == '3':
            print("\n--- Powers of 2 ---")
            print("a. Find 2^x")
            print("b. Find x in 2^x = n")
            sub_choice = input("Enter your choice (a/b): ").lower()
            
            if sub_choice == 'a':
                exponent = input("Enter exponent (1-32): ")
                result = power_of_2(exponent)
                print(f"Result: {result}")
            elif sub_choice == 'b':
                power = input("Enter a power of 2: ")
                result = find_exponent(power)
                print(f"Result: {result}")
            else:
                print("Invalid choice")
                
        elif choice == '4':
            print("\n--- Subnet Masks ---")
            print("a. CIDR to Subnet Mask")
            print("b. Subnet Mask to CIDR")
            sub_choice = input("Enter your choice (a/b): ").lower()
            
            if sub_choice == 'a':
                cidr = input("Enter CIDR prefix (0-32): ")
                result = cidr_to_mask(cidr)
                print(f"Result:\n{result}")
            elif sub_choice == 'b':
                mask = input("Enter subnet mask (e.g., 255.255.255.0): ")
                result = mask_to_cidr(mask)
                print(f"Result: {result}")
            else:
                print("Invalid choice")
                
        elif choice == '5':
            print("\n--- Display Full Table ---")
            print("1. Decimal-Binary Cross Reference")
            print("2. Hex-Binary Cross Reference")
            print("3. Powers of 2")
            print("4. Subnet Masks")
            table_choice = input("Enter table to display (1-4): ")
            display_full_table(table_choice)
            
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()