try:
    with open("machine_log.txt", "r", encoding="utf-8") as log_file:
        line_count = 0
        cnc_count = 0
        for log_line in log_file:
            line_count = line_count + 1
            if "CNC" in log_line:
                cnc_count = cnc_count + 1
    print(f"Всего значений {line_count}")
    print(f"Значений CNC {cnc_count}")
except FileNotFoundError:
    print("Нет файла лога")


