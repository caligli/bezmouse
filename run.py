import mouse
import argparse

# deviation:
# 0 means straight line
# > 0 means curve (example: 20)

# speed:
# 1 for fastest
# > 1 for slow movement (example: 500)


# FLAG CONTROL EXAMPLE:

# parser = argparse.ArgumentParser()
# parser.add_argument('indir', type=str, help='Input dir for videos')
# parser.add_argument('-w', action='store_true')
# parser.add_argument(
#     '--my_optional',
#     type=int,
#     default=2,
#     help='provide an integer (default: 2)'
# )
# my_namespace = parser.parse_args()
# print(my_namespace.my_optional)

parser = argparse.ArgumentParser()
parser.add_argument('window', type=str, help='window data for xdotool')
parser.add_argument('x', type=int, help='x axis coordinate')
parser.add_argument('y', type=int, help='y axis coordinate')
parser.add_argument('width', type=int, help='width from upleft corner')
parser.add_argument('height', type=int, help='height from upleft corner')
parser.add_argument('deviation', type=int, help='0 <> 100')
parser.add_argument('speed', type=int, help='1 <> INF')
args = parser.parse_args()

mouse.move_to_area(args.x, args.y, args.width, args.height, args.deviation, args.speed)