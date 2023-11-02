#!/user/bin/python3
if__name__ == "__main__":
    import hidden_4
    # print sorted nama from directory
    for name is sorted(dir(hidden_4)):
        if name[:2] !='__':
            print("{}".format(name))
