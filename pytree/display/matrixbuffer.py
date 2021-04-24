class MatrixBuffer:
    '''
    Matrix buffer which stores an ASCII image.
    '''
    #
    #
    def __init__(self, width: int, height: int):
        if type(width) is not int or width < 1:
            raise ValueError('width must be a positive integer')

        if type(height) is not int or height < 1:
            raise ValueError('height must be a positive integer')

        self.__width = width
        self.__height = height

        self.__a = [[' '] * width for _ in range(height)]

        self.__y_bottom = -1

    #
    #
    def width(self):
        return self.__width

    #
    #
    def height(self):
        return self.__height

    #
    #
    def fill_str(self, x: int, y: int, value: str):
        if type(value) is not str:
            raise ValueError('Invalid argument: value must be a string')

        self.__check_arg_x(x, 'x')
        self.__check_arg_y(y, 'y')

        a = self.__a
        x_start = x
        len_value = len(value)

        for i in range(len_value):
            x = x_start + i

            if x >= self.__width:
                break

            a[y][x] = value[i]

        self.__update_y_bottom(y)

    #
    #
    def fill_hori_line(self, character: str, y: int, x_start: int, x_end: int):
        self.__check_arg_y(y, 'y')
        self.__check_arg_x(x_start, 'x_start')
        self.__check_arg_x(x_end, 'x_end')

        for x in range(x_start, x_end + 1):
            self.__a[y][x] = character

        self.__update_y_bottom(y)

    #
    #
    def fill_vert_line(self, character: str, x: int, y_start: int, y_end: int):
        self.__check_arg_x(x, 'x')
        self.__check_arg_y(y_start, 'y_start')
        self.__check_arg_y(y_end, 'y_end')

        for y in range(y_start, y_end + 1):
            self.__a[y][x] = character

        self.__update_y_bottom(y_end)

    #
    #
    def __check_arg_x(self, value: int, name_arg: str):
        if value < 0 or value >= self.__width:
            raise ValueError('Invalid argument:', name_arg)

    #
    #
    def __check_arg_y(self, value: int, name_arg: str):
        if value < 0 or value >= self.__height:
            raise ValueError('Invalid argument:', name_arg)

    #
    #
    def __update_y_bottom(self, value: int):
        self.__y_bottom = max(self.__y_bottom, value)

    #
    #
    def get_str(self) -> str:
        lst_rows = self.get_lst_rows()
        res = '\n'.join(lst_rows)
        return res

    #
    #
    def get_lst_rows(self) -> list:
        lst_rows = [''.join(row) for row in self.__a]

        # optimization: remove unnecessary ending row
        del lst_rows[self.__y_bottom + 1:]

        return lst_rows
