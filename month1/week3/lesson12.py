try:
    with open("machine_log.txt", "r", encoding="utf-8") as log_file:
        line_count = 0
        cnc_count = 0
        spindle_count = 0
        program_count = 0
        for log_line in log_file:
            line_count = line_count + 1
            if "CNC" in log_line:
                cnc_count = cnc_count + 1
                print(log_line.strip())
            if "Spindle" in log_line:
                spindle_count = spindle_count + 1
            if "Program running" in log_line:
                program_count = program_count + 1
        report_text = (f"Всего записей {line_count}\n"
                       f"Записей CNC {cnc_count}\n"
                       f"Записей Spindle {spindle_count}\n"
                       f"Записей Program running {program_count}\n")
        print(report_text)
        with open("report.txt", "w", encoding="utf-8") as report_file:
            report_file.write(report_text)
except FileNotFoundError:
    print("Файл лога не найден")