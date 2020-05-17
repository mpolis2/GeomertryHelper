def rectangle(length ='x', width ='x', area ='x'):
    print("This will calculate the missing variable in Length * Width = Area")
    length = input ("What is the length? (type 'x' if unknown): ")
    width = input("What is the width? (type 'x' if unknown): ")
    area = input("What is the area? (type 'x' if unknown): ")
    # returns the unknown variable as a tuple of (name, value)
    if area == 'x':
        return ("area", int(length) * int(width))
    elif width == 'x':
        return ("width", int(area) / int(length))
    elif length == 'x':
        return ("length", int(area) / int(width))

def circle(circumference = 'x', radius = 'x'):
    print("This will calculate the missing variable circumference = 2 pi radius")
    circumference = input("What is the circumference? (type 'x' if unknown): ")
    radius = input("What is the radius? (type 'x' if unknown): ")
    if circumference == 'x':
        return("circumference", 2 * 3.142 * int(radius))
    if radius == 'x':
        return("radius", circumference / (2 * 3.142))

def rectangle_list():
    rectangle = {'length': None, 'width' : None, 'area' : None, 'perimeter' : None}
    rectangle['length'] = input("what is the length? ")
    rectangle['width'] = input("what is the width? ")
    rectangle['area'] = input("what is the area? ")
    rectangle['perimeter'] = input("what is the perimeter? ")
    print(rectangle)
    rectangle_solved = {}
    if rectangle['area'] == 'x':
        rectangle_solved["area"] = int(rectangle["length"]) * int(rectangle["width"])
    if rectangle['width'] == 'x':
        rectangle_solved["width"] = int(rectangle["area"]) / int(rectangle["length"])
    if rectangle['length'] == 'x':
        rectangle_solved["length"] = int(rectangle["area"]) / int(rectangle["width"])
    if rectangle['perimeter'] == 'x':
        rectangle_solved["perimeter"] = int(rectangle["length"])*2 + int(rectangle["width"]) *2
    print(f'solved = {rectangle_solved}')

rectangle_list()

# answer = rectangle()
# print(f'the {answer[0]} is {answer[1]}')
#
# answer = circle()
# print(f'the {answer[0]} is {answer[1]}')


# to ask about try / except blocks retrying until it passes
'''
def rectangle_list():
    rectangle = {'length': None, 'width' : None, 'area' : None, 'perimeter' : None}
    while True:
        try:
            rectangle['length'] = int(input("what is the length? "))
            rectangle['width'] = int(input("what is the width? "))
            rectangle['area'] = int(input("what is the area? "))
            rectangle['perimeter'] = int(input("what is the perimeter? "))
        except(ValueError):
            print("numbers only, please")
            continue
        else:
            break
'''