from pathlib import Path

script_path = Path(__file__)
project_dir = script_path.parent
log_path = project_dir / "sample_log.txt"
try:
    with open(log_path, encoding="utf-8") as log_file:
        line_count = 0
        cnc_count = 0
        spindle_count = 0
        program_running_count = 0
        for log_line in log_file:
            line_count = line_count + 1
            if "CNC" in log_line:
                cnc_count = cnc_count + 1
            if "Spindle" in log_line:
                spindle_count = spindle_count + 1
            if "Program running" in log_line:
                program_running_count = program_running_count + 1
    report_text = (f"CNC событий: {cnc_count}\n"
                   f"Spindle событий: {spindle_count}\n"
                   f"Program running событий: {program_running_count}\n"
                   f"Всего строк: {line_count}")
    report_path = project_dir / "report.txt"
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_text)
    print(report_text)
except FileNotFoundError:
    print("Файл не найден")
