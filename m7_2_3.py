def main(files: list[str]) -> None:
    int_info = 2
    bool_info = True
    text_info = "Python程序设计\n"
    file_name, open_mode, encoding_type = files[0]
    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    print(f"# .write() returned: {file_obj.write(f'Line 1, {text_info}')=}")
    print(f"# .write() returned: {file_obj.write(str(int_info))=}")
    print("# .write() returned:", file_obj.write("Line 3, string literal.\n"))
    print(f"# .write() returned: {file_obj.write(str(bool_info))=}")
    print("# .write() returned:", file_obj.write("The End.\n"))
    file_obj.close()

    file_name, open_mode, encoding_type = files[1]
    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    print(f"# .write() returned: {file_obj.write(bytes(f'Line 1, {text_info}','utf-8'))=}")
    print(f"# .write() returned: {file_obj.write(int_info.to_bytes(4,'little'))=}")
    print("# .write() returned:", file_obj.write(
        bytearray("Line 3, string literal.\n", 'utf-8')))
    print(f"# .write() returned: {file_obj.write(bytearray([bool_info]))=}")
    print("# .write() returned:", file_obj.write(bytes("The End.\n", 'utf-8')))
    file_obj.close()

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_names = [(base_name + ".data.txt", "t", 'utf-8'),
                  (base_name + ".data.bin", "b", None)]
    main(file_names)

# .write() returned: file_obj.write(f'Line 1, {text_info}')=19
# .write() returned: file_obj.write(str(int_info))=1
# .write() returned: 24
# .write() returned: file_obj.write(str(bool_info))=4
# .write() returned: 9
# .write() returned: file_obj.write(bytes(f'Line 1, {text_info}','utf-8'))=27
# .write() returned: file_obj.write(int_info.to_bytes(4,'little'))=4
# .write() returned: 24
# .write() returned: file_obj.write(bytes([bool_info]))=1
# .write() returned: 9