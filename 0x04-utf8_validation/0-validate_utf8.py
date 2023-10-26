def valid_utf8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    def is_start_byte(byte):
        """
        Check if a given byte is a valid UTF-8 start byte.

        Args:
            byte (int): The byte to be checked.

        Returns:
            bool: True if the byte is a valid start byte, else False.
        """
        return (byte & 0b10000000) == 0b00000000

    def count_ones(byte):
        """
        Count the number of consecutive 1s in the leading bits of a byte.

        Args:
            byte (int): The byte to be checked.

        Returns:
            int: The count of consecutive 1s in the leading bits.
        """
        count = 0
        while (byte & 0b10000000) == 0b10000000:
            count += 1
            byte <<= 1
        return count

    i = 0
    while i < len(data):
        byte = data[i]
        if not is_start_byte(byte):
            return False

        num_bytes = count_ones(byte)
        if num_bytes == 1 or num_bytes > 4:
            return False

        if i + num_bytes > len(data):
            return False

        for j in range(i + 1, i + num_bytes):
            if not (data[j] & 0b11000000 == 0b10000000):
                return False

        i += num_bytes

    return True

