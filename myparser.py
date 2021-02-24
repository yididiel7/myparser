import argparse

if __name__ == '__main__':  # TODO Ctrl+Shift+F12 closes the file view.
	# Initialize the parser
	parser = argparse.ArgumentParser(
		description="my math script"
	)

	# Add the parameters positional/optional
	parser.add_argument('-n', '--num1', help="Number 1", type=float)
	parser.add_argument('-i', '--num2', help="Number 2", type=float)
	parser.add_argument('-o', '--operation', help="provide operator", default='+')

	# Parser the arguments
	args = parser.parse_args()
	print(args)
	result = None
	if args.operation == '+':
		result = args.num1 + args.num2
	if args.operation == '-':
		result = args.num1 - args.num2
	if args.operation == '*':
		result = args.num1 * args.num2
	if args.operation == 'pow':
		result = pow(args.num1,  args.num2)

	print("Result : ", result)