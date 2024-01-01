func compress(chars []byte) int {
    if len(chars) == 1 {
		return 1
	}

	writeIndex := 0
	readIndex := 0

	for readIndex < len(chars) {
		currentChar := chars[readIndex]
		count := 0

		for readIndex < len(chars) && chars[readIndex] == currentChar {
			readIndex++
			count++
		}

		chars[writeIndex] = currentChar
		writeIndex++

		if count > 1 {
			countStr := strconv.Itoa(count)
			for _, digit := range countStr {
				chars[writeIndex] = byte(digit)
				writeIndex++
			}
		}
	}

	return writeIndex
}
