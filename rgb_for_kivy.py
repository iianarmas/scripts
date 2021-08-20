def rgb_converter(value):
    rgb = ['{:.2f}'.format(float(i) / 255) for i in value]
    return f'\nred = {rgb[0]}\ngreen= {rgb[1]}\nblue = {rgb[2]}'


user = input('Enter rgb values: ').split()

convert = rgb_converter(user)

print(convert)
