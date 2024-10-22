"""Defining unit tests for utils.py!"""

__author__ = "730732196"

import pytest

# Learned with the assignment
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_with_mixed_values_use_case():
    """Test only_evens with odd and even numbers."""
    input_list = [1, 2, 3, 4, 5]
    result = only_evens(input_list)
    assert result == [2, 4]


def test_only_evens_with_all_odd_use_case():
    """Test only_evens with an all odd number list."""
    input_list = [1, 3, 5, 7]
    result = only_evens(input_list)
    assert result == []


def test_only_evens_with_empty_list_edge_case():
    """Test only_evens with an empty list."""
    input_list = []
    result = only_evens(input_list)
    assert result == []


# Above 3 are for the only_evens function (Basic tests)


def test_sub_with_valid_range_use_case():
    """Test sub with a valid index range."""
    input_list = [10, 20, 30, 40, 50]
    result = sub(input_list, 1, 4)
    assert result == [20, 30, 40]


def test_sub_with_negative_start_edge_case():
    """Test sub with a negative start index."""
    input_list = [10, 20, 30, 40]
    result = sub(input_list, -1, 3)
    assert result == [10, 20, 30]


def test_sub_with_out_of_range_end_use_case():
    """Test sub with an end index larger than the list length."""
    input_list = [1, 2, 3]
    result = sub(input_list, 1, 5)
    assert result == [2, 3]


# Above 3 are for the sub function


def test_add_at_index_valid_use_case():
    """Test add_at_index by adding an element at a valid index."""
    input_list = [1, 2, 3]
    add_at_index(input_list, 4, 2)
    assert input_list == [1, 2, 4, 3]


def test_add_at_index_at_start_use_case():
    """Test add_at_index by adding an element at the start."""
    input_list = [5, 6, 7]
    add_at_index(input_list, 1, 0)
    assert input_list == [1, 5, 6, 7]


def test_add_at_index_raises_indexerror_edge_case():
    """Test that add_at_index raises an IndexError for an invalid index."""
    input_list = [10, 20, 30]
    with pytest.raises(IndexError):
        add_at_index(input_list, 15, 5)


# Above 3 are for the add_at_index function
# I had to import pytest for this to work and was stuck way too long!!!!
