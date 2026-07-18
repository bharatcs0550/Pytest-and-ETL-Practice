def find_errors_in_bug(filepath):
    errors = []
    with open(filepath, mode ='r') as file:
        for line in file:
            if 'ERROR' in line:
                errors.append(line.strip())
    return errors

def test_no_unpexpected_errors_in_logs():
    errors = find_errors_in_bug('system_log.txt')
    assert len(errors) == 0, f"found {len(errors)} error(s) in logs"