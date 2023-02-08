class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """This is a derivative of longest contiguous subarray of consecutive X
        The primary difference is the iterative step now checks for two integers rather 
        than one. 

        High Level Approach - 
        SLIDING WINDOW 
        Iterate through the list and expand the window as long as two conditions are met
        - type in the two list of allowed types 
        - only one type has been used thus far 

        When this condition isn't met, we then increment the starting index.
        -- To take this problem from N^2 -> N, optimizing this step is key
        -- In the standard contiguous subarray question, that optimization happens when
        our logical iterative step will start from the new value.
        -- In this case, to recreate that same logic, we want to start from the last occurrence
        of least recently seen value. This way we ensure that the point we concatenate to only has
        two allowed variable types
        """
        start_index = 0
        venture_index = start_index + 1
        if len(fruits) <= 2:
            return len(fruits)
        max_picks = 2
        # Store the allowed types and their last known index
        allowed_types = {
            fruits[start_index]: start_index,
            fruits[venture_index]: venture_index,
        }
        # We want at least two items left in the list
        while start_index < (len(fruits) - 1) and venture_index < len(fruits):
            # If it's in the allowed types, move right
            # OR
            # If it's not an allowed type but we have the ability to add another type
            # Both cases will execute the same behavior
            if (fruits[venture_index] in allowed_types) or len(allowed_types) == 1:
                # Store the last time that value appeared.
                allowed_types[fruits[venture_index]] = venture_index
                venture_index+=1
            else:
                # Calculate and capture distance but don't include the current value
                max_picks = max(max_picks, (venture_index - start_index))
                # Find the value with the earliest index
                cutoff_num = min(allowed_types, key=lambda _type: allowed_types[_type])
                # Start from the index immediately after cut-off number
                start_index = allowed_types.pop(cutoff_num) + 1

        # This last pointer reference assumes that venture_index MUST be >= len(fruits)
        return max(max_picks, (venture_index - start_index))
