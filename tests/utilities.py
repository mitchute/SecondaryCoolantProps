def abs_error_passes(test_val, true_val, error_tol):
    pct_err = abs((test_val - true_val) / true_val)
    return True if pct_err <= error_tol else False
