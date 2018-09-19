
if __name__ == "__main__":
    # with open('try.txt') as f:
    #     print(f.readline())

    # try:
    #     f = open('try1.txt', 'r')
    #     f.write('hello\n')
    # except IOError as e:
    #     raise e
    # finally:
    #     f.close()
    # try:
    #     a = 5/0
    # except ZeroDivisionError as e:
    #     print('zero devision error', e)
    # finally:
    #     print('this is something!')
    import  sys
    try:
        f = open('abc.txt', 'rb')
    except IOError:
        print("Could not read file:", 'abc.txt')
        sys.exit()


    # for root, dirs, files in os.walk('.'):
    #   for name in files:
    #      if name.endswith('.jpg') or name.endswith('.JPG'):
    #         os.remove(os.path.join(name, root))
