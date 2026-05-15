def format_inputdata(input_data):
    res_formatted = [f"{r:.6f}" for r in input_data]
    result = "-".join(res_formatted)
    return result