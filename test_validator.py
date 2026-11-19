
import pandas as pd
import pytest

from validator import load_data, validate_data


def test_load_data():
    # YOUR TASK:
    # Load data.csv.
    # Check that the result is a DataFrame.
    pass


def test_missing_values():
    # YOUR TASK:
    # Create a small DataFrame with a missing age.
    # Verify that the validator detects it.
    pass


def test_duplicate_customer_ids():
    # YOUR TASK:
    # Create two records with the same customer_id.
    # Verify duplicate detection.
    pass


def test_invalid_age():
    # YOUR TASK:
    # Create a record with age 15.
    # Verify that it is flagged.
    pass


def test_negative_charges():
    # YOUR TASK:
    # Create a record with negative monthly_charges.
    # Verify that it is flagged.
    pass


def test_negative_tenure():
    # YOUR TASK:
    # Create a record with negative tenure_months.
    # Verify that it is flagged.
    pass
