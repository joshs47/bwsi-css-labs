from labs.lab_1.lab_1c import max_subarray_sum

def test_example_case():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert max_subarray_sum(nums) == 6