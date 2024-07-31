def main():
    with open('file2.txt', 'r') as file2:
        content_file2 = file2.read()

    with open('file1.txt', 'r') as file1:
        content_file1 = file1.read()
        
    with open('file1.txt', 'w') as file1:
        file1.write(content_file2 + content_file1)

if __name__ == '__main__':
    main()