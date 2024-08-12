def parse_2d_array(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            data = [line.split() for line in lines]
            return data
    except FileNotFoundError:
        print("File not found!")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def sort_2d_array(data):
    sorted_data = [sorted(row) for row in data]
    return sorted_data

def main():
    filename = input("Enter the filename containing 2D array data: ")
    array_data = parse_2d_array(filename)
    if array_data:
        print("Original 2D array:")
        for row in array_data:
            print(row)
        
        sorted_array = sort_2d_array(array_data)
        print("\nSorted 2D array:")
        for row in sorted_array:
            print(row)

if __name__ == "__main__":
    main()
