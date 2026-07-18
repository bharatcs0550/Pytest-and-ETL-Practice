import csv

def load_csv(filepath):
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def test_row_count_matches():
    source = load_csv('source_data.csv')
    loaded = load_csv('loaded_data.csv')
    assert len(source) == len(loaded), f"Row count mismatch: source has {len(source)}, loaded has {len(loaded)}" 


def test_date_format_transformed_correctly():
    source = load_csv('source_data.csv')
    loaded = load_csv('loaded_data.csv')
    
    source_customer_101 = source[0]
    loaded_customer_101 = loaded[0]
    
    assert source_customer_101['customer_id'] == loaded_customer_101['customer_id']
    assert loaded_customer_101['transaction_date'] == '2026-07-15'

def test_status_code_mapped_correctly():
    source = load_csv('source_data.csv')
    loaded = load_csv('loaded_data.csv')
    
    # customer 103 has status_code 'P' in source, should be 'Pending' in loaded
    source_103 = source[2]
    loaded_103 = loaded[2]
    
    assert source_103['customer_id'] == loaded_103['customer_id']
    assert loaded_103['status_description'] == 'Pending'