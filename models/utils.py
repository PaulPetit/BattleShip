def setCursorPos(x, y):
    print("\033[{};{}H".format(y, x), end="");
