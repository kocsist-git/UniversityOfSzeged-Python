import argparse

parser=argparse.ArgumentParser()

parser.add_argument("echo", help="Próbáld ki", default="Semmi")
parser.add_argument("-alap", help="negyzetre emeles", type=int)
parser.add_argument("-kitevo", help="negyzetre emeles", type=int, default=2)

args = parser.parse_args()
print(args.echo)
print(args.alap**args.kitevo)