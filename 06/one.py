
def is_marker(marker):
	s = set()
	for char in marker:
		if char in s:
			return False
		else:
			s.add(char)

	return True


def main():
	# Get input
	file = open("input")
	buffer = file.readline()
	file.close()

	marker = ""
	i = 0

	for char in buffer:
		marker += char
		i += 1

		if len(marker) == 4:
			if is_marker(marker):
				break
			else:
				marker = marker[1:]

	print(i)


if __name__ == "__main__":
	main()
