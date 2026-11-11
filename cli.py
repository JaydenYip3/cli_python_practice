import argparse 

parser = argparse.ArgumentParser(prog= "cli_db", description= "simple cli tool that writes to a simple db", epilog="testing" )


parser.add_argument("name", help="What is your name?")

args = parser.parse_args()

print(args.name)
