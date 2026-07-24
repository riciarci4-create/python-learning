"""Analyze machine log lines for the Month 1 exam."""


def analyze_lines(log_lines):
    line_count = 0
    cnc_count = 0
    error_count = 0
    for log_line in log_lines:
        log_line_upper = log_line.upper()
        line_count = line_count + 1
        if "CNC" in log_line_upper:
            cnc_count = cnc_count + 1
        if "ERROR" in log_line_upper:
            error_count = error_count + 1
    return {"Всего строк": line_count,
            "CNC": cnc_count,
            "ERROR": error_count}


log_lines = ["CNC started",
             "Temperature OK",
             "ERROR spindle stopped",
             "Cnc stopped",
             "cnc process",
             "error",
             "ErrOr"]
print(analyze_lines(log_lines))
