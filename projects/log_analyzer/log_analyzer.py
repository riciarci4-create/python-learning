from pathlib import Path


def analyze_log(log_path):
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
        return {
            "line_count": line_count,
            "cnc_count": cnc_count,
            "spindle_count": spindle_count,
            "program_running_count": program_running_count
        }
    except FileNotFoundError:
        return None


def main():
    script_path = Path(__file__)
    project_dir = script_path.parent
    log_path = project_dir / "sample_log.txt"
    analysis_result = analyze_log(log_path)
    if analysis_result is None:
        print("Файл не найден")
        return
    line_count = analysis_result["line_count"]
    cnc_count = analysis_result["cnc_count"]
    spindle_count = analysis_result["spindle_count"]
    program_running_count = analysis_result["program_running_count"]
    try:
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


if __name__ == "__main__":
    main()
