from bisect import bisect_left, bisect_right

class Utils:
    @staticmethod
    def bisect_range(arr, l, r, key=lambda x: x):
        """
        Bisects a sorted list of tuples based on the first element using the provided lambda key.

        Parameters:
        arr (list): A sorted list of tuples.
        l (int/float): The lower bound of the range.
        r (int/float): The upper bound of the range.
        key (function): Lambda function that defines the comparison (default compares the first element of each tuple).

        Returns:
        list: The sublist with elements in the range [l, r].
        """

        left_idx = bisect_left(arr, l, key=key)
        
        right_idx = bisect_right(arr, r, key=key)
        
        return arr[left_idx:right_idx]
