# Takes a list of strings, and returns a list where all the strings have the same property:
# Excluding the first word of the input, all output strings must be composed only of letters
# greater than or equal to all the letters of the string immediately before it in the input
def check_ascending(input_list):

    if len(input_list) == 0:
        return []

    # Directly set because the first element of the input is always included
    rtn_list = [input_list[0]]
    all_greater = True

    # Loop through all inputs, excluding the first one
    for i in range(1, len(input_list)):
        all_greater = True
        prev = input_list[i-1]
        to_check = input_list[i]

        # Breaks included to prevent needless loops
        for p_char in prev:
            for t_char in to_check:
                if t_char < p_char:
                    all_greater = False
                    break
            if not all_greater:
                break

        # If the words run through the whole check and no discrepancy is found
        if all_greater:
            rtn_list.append(to_check)

    return rtn_list


# Simple functionality test
def test_one():
    input_list = ['cad', 'delk', 'deal', 'morp', 'dogie', 'tory']
    expected = ['cad', 'delk', 'morp', 'tory']
    result = check_ascending(input_list)

    c_match = False
    d_match = False
    m_match = False
    t_match = False

    for word in expected:
        for value in result:
            if (value == word) & (word == 'cad'):
                c_match = True
            if (value == word) & (word == 'delk'):
                d_match = True
            if (value == word) & (word == 'morp'):
                m_match = True
            if (value == word) & (word == 'tory'):
                t_match = True

    if c_match & d_match & m_match & t_match:
        print('PASSED')
    else:
        print('FAILED')

    return


# Testing empty list behavior
def test_two():
    input_list = []
    result = check_ascending(input_list)

    if len(result) == 0:
        print('PASSED')
    else:
        print('FAILED')
    return


# Testing how the function handles spaces
def test_three():
    input_list = ['cad', 'delk', 'deal', 'morp', ' ']
    result = check_ascending(input_list)
    expected = ['cad', 'delk', 'morp']

    c_match = False
    d_match = False
    m_match = False

    for word in expected:
        for value in result:
            if (value == word) & (word == 'cad'):
                c_match = True
            if (value == word) & (word == 'delk'):
                d_match = True
            if (value == word) & (word == 'morp'):
                m_match = True

    if c_match & d_match & m_match:
        print('PASSED')
    else:
        print('FAILED')

    return


test_one()
test_two()
test_three()
